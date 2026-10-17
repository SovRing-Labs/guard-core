#!/usr/bin/env python3
import json, os, pathlib, subprocess, tempfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as td:
 p=pathlib.Path(td); root=p/'owned'; (root/'bin').mkdir(parents=True); (root/'projects').mkdir()
 home=p/'home'; home.mkdir()
 env=dict(os.environ, HOME=str(home), GUARD_ROOT=str(root), GUARD_DB=str(p/'baseline.db'))
 def run(*args):
  return subprocess.check_output(['python3',str(ROOT/'bin/guard-core'),*args],env=env,text=True)
 def git(*args):
  subprocess.run(['git','-C',str(root),*args],check=True,capture_output=True)
 def commit():
  git('add','.'); git('-c','user.name=Fixture','-c','user.email=fixture@example.com','commit','-qm','receipt')
 f=root/'bin/tool'; f.write_text('original')
 git('init','-q'); commit()
 stats=json.loads(run('baseline','--stats')); assert stats['files']==1
 assert len(json.loads(run('check','--json'))['1'])==1
 f.write_text('modified'); assert len(json.loads(run('check','--json'))['-1'])==1
 commit(); assert len(json.loads(run('check','--json'))['1'])==1
 (root/'bin/new').write_text('new'); assert len(json.loads(run('check','--json'))['0'])==1
 f.unlink(); assert len(json.loads(run('check','--json'))['-1'])==1
 print(json.dumps({'pass':True,'baseline_files':stats['files'],'checks':['unchanged','dirty','committed','new','removed'],'lookup_us_mean':stats['lookup_us_mean']}))

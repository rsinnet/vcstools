from vcstools import GitClient
from vcstools.vcs_base import VcsError

        subprocess.check_call("git init", shell=True, cwd=self.remote_path)
        subprocess.check_call("touch fixed.txt", shell=True, cwd=self.remote_path)
        subprocess.check_call("git add *", shell=True, cwd=self.remote_path)
        subprocess.check_call("git commit -m initial", shell=True, cwd=self.remote_path)
        subprocess.check_call("git tag test_tag", shell=True, cwd=self.remote_path)
        subprocess.check_call("git branch test_branch", shell=True, cwd=self.remote_path)
        po = subprocess.Popen("git log -n 1 --pretty=format:\"%H\"", shell=True, cwd=self.remote_path, stdout=subprocess.PIPE)
        subprocess.check_call("touch modified.txt", shell=True, cwd=self.remote_path)
        subprocess.check_call("touch modified-fs.txt", shell=True, cwd=self.remote_path)
        subprocess.check_call("git add *", shell=True, cwd=self.remote_path)
        subprocess.check_call("git commit -m initial", shell=True, cwd=self.remote_path)
        po = subprocess.Popen("git log -n 1 --pretty=format:\"%H\"", shell=True, cwd=self.remote_path, stdout=subprocess.PIPE)
        subprocess.check_call("touch deleted.txt", shell=True, cwd=self.remote_path)
        subprocess.check_call("touch deleted-fs.txt", shell=True, cwd=self.remote_path)
        subprocess.check_call("git add *", shell=True, cwd=self.remote_path)
        subprocess.check_call("git commit -m modified", shell=True, cwd=self.remote_path)
        po = subprocess.Popen("git log -n 1 --pretty=format:\"%H\"", shell=True, cwd=self.remote_path, stdout=subprocess.PIPE)
        subprocess.check_call("git tag last_tag", shell=True, cwd=self.remote_path)
        subprocess.check_call("git reset --hard test_tag", shell=True, cwd=self.local_path)
        subprocess.check_call("git reset --hard test_tag", shell=True, cwd=self.local_path)
        subprocess.check_call("git config --replace-all branch.master.merge master", shell=True, cwd=self.local_path)
           
        subprocess.check_call("git checkout test_tag -b localbranch", shell=True, cwd=self.local_path)
        subprocess.check_call("touch local.txt", shell=True, cwd=self.local_path)
        subprocess.check_call("git add *", shell=True, cwd=self.local_path)
        subprocess.check_call("git commit -m my_branch", shell=True, cwd=self.local_path)
        subprocess.check_call("git tag my_branch_tag", shell=True, cwd=self.local_path)
        po = subprocess.Popen("git log -n 1 --pretty=format:\"%H\"", shell=True, cwd=self.local_path, stdout=subprocess.PIPE)
        subprocess.check_call("git checkout test_tag", shell=True, cwd=self.local_path)
        subprocess.check_call("touch tagged.txt", shell=True, cwd=self.local_path)
        subprocess.check_call("git add *", shell=True, cwd=self.local_path)
        subprocess.check_call("git commit -m no_branch", shell=True, cwd=self.local_path)
        subprocess.check_call("git tag no_br_tag", shell=True, cwd=self.local_path)
        subprocess.check_call("touch dangling.txt", shell=True, cwd=self.local_path)
        subprocess.check_call("git add *", shell=True, cwd=self.local_path)
        subprocess.check_call("git commit -m dangling", shell=True, cwd=self.local_path)
        po = subprocess.Popen("git log -n 1 --pretty=format:\"%H\"", shell=True, cwd=self.local_path, stdout=subprocess.PIPE)
        subprocess.check_call("git checkout master", shell=True, cwd=self.local_path)
    def test_inject_protection(self):
        client = GitClient(self.local_path)
        try:
            client.is_tag('foo"; bar"', fetch = False)
            self.fail("expected Exception")
        except VcsError: pass
        try:
            client.rev_list_contains('foo"; echo bar"', "foo", fetch = False)
            self.fail("expected Exception")
        except VcsError: pass
        try:
            client.rev_list_contains('foo', 'foo"; echo bar"', fetch = False)
            self.fail("expected Exception")
        except VcsError: pass
        try:
            client.get_version('foo"; echo bar"', fetch = False)
            self.fail("expected Exception")
        except VcsError: pass
        
        subprocess.check_call("rm deleted-fs.txt", shell=True, cwd=self.local_path)
        subprocess.check_call("git rm deleted.txt", shell=True, cwd=self.local_path)
        subprocess.check_call("git add modified.txt", shell=True, cwd=self.local_path)
        subprocess.check_call("git add added.txt", shell=True, cwd=self.local_path)
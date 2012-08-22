from __future__ import unicode_literals


        self.root_directory = tempfile.mkdtemp()
        self.directories = dict(setUp=self.root_directory)
        self.remote_path = os.path.join(self.root_directory, "remote")

        self.local_version_init = po.stdout.read().decode('UTF-8').rstrip("'").lstrip("'")
        self.local_version_second = po.stdout.read().decode('UTF-8').rstrip("'").lstrip("'")

        self.local_version = po.stdout.read().decode('UTF-8').rstrip("'").lstrip("'")
        self.local_path = os.path.join(self.root_directory, "local")


    # test for #3497
    def test_checkout_into_subdir_without_existing_parent(self):


        self.assertEquals('', client.get_status())

        f.write('0123456789abcdef')
        f.write('0123456789abcdef')
        f.write('0123456789abcdef')
        f.write('0123456789abcdef')



class HGExportRepositoryClientTest(HGClientTestSetups):

    @classmethod
    def setUpClass(self):
        HGClientTestSetups.setUpClass()
        url = self.local_url
        client = HgClient(self.local_path)
        client.checkout(url)

        self.basepath_export = os.path.join(self.root_directory, 'export')

    def tearDown(self):
        pass

    def test_export_repository(self):
        client = HgClient(self.local_path)
        self.assertTrue(
          client.export_repository(self.local_version, self.basepath_export)
        )

        self.assertTrue(os.path.exists(self.basepath_export + '.tar.gz'))
        self.assertFalse(os.path.exists(self.basepath_export + '.tar'))
        self.assertFalse(os.path.exists(self.basepath_export))
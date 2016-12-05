from pip._vendor.six.moves.urllib import parse as urllib_parse
import os
import urllib
 
class Index(object):
    def __init__(self, url):
        self.url = url
        self.netloc = urllib_parse.urlsplit(url).netloc
        self.simple_url = self.url_to_path('simple')
        self.pypi_url = self.url_to_path('pypi')
        self.pip_json_url = self.url_to_path('pypi/pip/json')

    def url_to_path(self, path):
        return urllib_parse.urljoin(self.url, path)

## TUF INTEGRATION
class TUFConfigClass(object):
    def __init__(self, repo_path, repo_mirrors):
        self.repo_path = repo_path
        self.repo_mirrors =  repo_mirrors
        self.check_root_metadata(repo_path)
        
    def check_root_metadata(self, repo_path):
        current = os.path.join(repo_path,'metadata/current')
        previous = os.path.join(repo_path,'metadata/previous')
        filename = os.path.join(current,'root.json')
        
        if not os.path.isfile(filename):
            print 'Pip does not have TUF metadata. Downloading..'
            tuf_root_metadata = os.path.join(self.repo_mirrors['mirror1']['url_prefix'],self.repo_mirrors['mirror1']['metadata_path'],'root.json')
            downloaded_root_metadata = urllib.urlretrieve (tuf_root_metadata, "root.json")
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(current)
                    os.makedirs(previous)
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise
                    
            os.rename(downloaded_root_metadata[0], filename)
            print 'Root metadata downloaded from '+tuf_root_metadata


here = os.path.abspath(os.path.dirname(__file__))
tuf_dir = os.path.join(here, '../tuf/client')

PyPI = Index('https://pypi.python.org/')
TUFConfig = TUFConfigClass(
    tuf_dir,
    {
        'mirror1':
        {
            'url_prefix': 'http://128.238.63.6/repository',
            'metadata_path': 'metadata',
            'targets_path': 'targets',
            'confined_target_dirs': ['']
        }
    })

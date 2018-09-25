import os
import requests
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_existing_post():
    r = requests.get('http://localhost:8000/?rest_route=/wp/v2/posts')
    assert r.status_code == 200
    json = r.json()
    content = "<p>Welcome to WordPress. This is your first post." \
        " Edit or delete it, then start writing!</p>\n"
    assert content in json[0]['content']['rendered']

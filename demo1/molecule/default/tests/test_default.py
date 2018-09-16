import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_apache_user_exists(host):
    apache = host.user("apache")
    assert apache.exists


def test_httpd_package_installed(host):
    httpd = host.package("httpd")
    assert httpd.is_installed


def test_httpd_service_started_and_enabled(host):
    httpd = host.service("httpd")
    assert httpd.is_running
    assert httpd.is_enabled

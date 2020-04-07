import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_trivy_package_installed(host):
    assert host.package("trivy").is_installed


def test_trivy_binary_exists(host):
    assert host.file('/usr/local/bin/trivy').exists


def test_trivy_binary_file(host):
    assert host.file('/usr/local/bin/trivy').is_file


def test_trivy_repo_exists(host):
    assert host.file('/etc/apt/sources.list.d/trivy.list').exists or \
      host.file('/etc/yum.repos.d/trivy.repo').exists


def test_trivy_repo_file(host):
    assert host.file('/etc/apt/sources.list.d/trivy.list').is_file or \
      host.file('/etc/yum.repos.d/trivy.repo').is_file


def test_trivy_binary_which(host):
    assert host.check_output('which trivy') == '/usr/local/bin/trivy'

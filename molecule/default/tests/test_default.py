import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'trivy'
PACKAGE_BINARY = '/usr/bin/trivy'
DEBIAN_REPO_FILE = '/etc/apt/sources.list.d/trivy.list'
EL_REPO_FILE = '/etc/yum.repos.d/trivy.repo'


def test_trivy_package_installed(host):
    """
    Tests if trivy is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_trivy_binary_exists(host):
    """
    Tests if trivy binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_trivy_binary_file(host):
    """
    Tests if trivy binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_trivy_binary_which(host):
    """
    Tests the output to confirm trivy's binary location.
    """
    assert host.check_output('which trivy') == PACKAGE_BINARY


def test_trivy_repo_exists(host):
    """
    Tests if trivy's DEBIAN/EL repo file exists.
    """
    assert host.file(DEBIAN_REPO_FILE).exists or \
        host.file(EL_REPO_FILE).exists


def test_trivy_repo_file(host):
    """
    Tests if trivy's DEBIAN/EL repo file is file type.
    """
    assert host.file(DEBIAN_REPO_FILE).is_file or \
        host.file(EL_REPO_FILE).is_file

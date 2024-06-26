[![build-test](https://github.com/darkwizard242/ansible-role-trivy/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-trivy/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-trivy/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-trivy/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/trivy) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-trivy&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-trivy) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-trivy&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-trivy) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-trivy&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-trivy) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-trivy?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-trivy?color=orange&style=flat-square)

# Ansible Role: trivy

Role to install (_by default_) [trivy](https://github.com/aquasecurity/trivy) package or uninstall (_if passed as var_) on Debian based systems and EL based systems. Trivy is a comprehensive and easy to use vulnerability scanner for containers.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
trivy_app: trivy
trivy_app_desired_state: present
trivy_debian_pre_reqs:
  - apt-transport-https
  - gnupg
trivy_debian_pre_reqs_desired_state: present
trivy_repo_debian_gpg_key: https://aquasecurity.github.io/trivy-repo/deb/public.key
trivy_repo_debian: "deb https://aquasecurity.github.io/trivy-repo/deb {{ ansible_lsb['codename'] }} main"
trivy_repo_debian_filename: "{{ trivy_app }}"
trivy_repo_debian_desired_state: present
trivy_repo_el: https://aquasecurity.github.io/trivy-repo/rpm/releases/$releasever/$basearch/
trivy_repo_el_name: trivy
trivy_repo_el_description: Trivy repository
trivy_repo_el_gpgcheck: no
trivy_repo_el_enabled: yes
trivy_repo_el_filename: trivy
trivy_repo_el_desired_state: present
```

### Variables table:

Variable                            | Description
----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
trivy_app                           | Name of trivy application package require to be installed i.e. `trivy`
trivy_app_desired_state             | State of the trivy_app package. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
trivy_debian_pre_reqs               | Trivy recommends the installation of both these packages on Debian family systems and as such, they are considered pre-requisites.
trivy_debian_pre_reqs_desired_state | Desired state for Trivy pre-requisite apps on Debian family systems.
trivy_repo_debian_gpg_key           | Trivy GPG key required on Debian family systems
trivy_repo_debian                   | Trivy repo URL for Debain family systems. Utilized facts such as `ansible_lsb['codename']`.
trivy_repo_debain_filename          | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
trivy_repo_debian_desired_state     | `present` indicates creating the repository file if it doesn't exist on Debian based systems. Alternative is `absent` (not recommended as it will prevent from installation of **trivy** package).
trivy_repo_el                       | Repository `baseurl` for Trivy on EL based systems.
trivy_repo_el_name                  | Repository name for Trivy on EL based systems.
trivy_repo_el_description           | Description to be added in EL based repository file for Trivy.
trivy_repo_el_gpgcheck              | Boolean for whether to perform gpg check against Trivy on EL based systems.
trivy_repo_el_enabled               | Boolean to set so that Trivy repository is enabled on EL based systems.
trivy_repo_el_filename              | Name of the repository file that will be stored at `/yum/sources.list.d/trivy.repo` on EL based systems.
trivy_repo_el_desired_state         | `present` indicates creating the repository file if it doesn't exist on EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **trivy** package).

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **trivy** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.trivy
```

For customizing behavior of role (i.e. installing latest verion of **trivy**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.trivy
  vars:
    trivy_apps_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **trivy** packages) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.trivy
  vars:
    trivy_apps_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-trivy/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).

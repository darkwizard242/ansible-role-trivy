[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-trivy.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-trivy) ![Ansible Role](https://img.shields.io/ansible/role/47706?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47706?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47706?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-trivy&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-trivy) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-trivy?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-trivy?color=orange&style=flat-square)

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

Variable                            | Value (default)                                                                          | Description
----------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
trivy_app                           | trivy                                                                                    | Name of trivy application package require to be installed i.e. `trivy`
trivy_app_desired_state             | present                                                                                  | State of the trivy_app package. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
trivy_debian_pre_reqs               | apt-transport-https, gnupg                                                               | Trivy recommends the installation of both these packages on Debian family systems and as such, they are considered pre-requisites.
trivy_debian_pre_reqs_desired_state | present                                                                                  | Desired state for Trivy pre-requisite apps on Debian family systems.
trivy_repo_debian_gpg_key           | <https://aquasecurity.github.io/trivy-repo/deb/public.key>                               | Trivy GPG key required on Debian family systems
trivy_repo_debian                   | "deb <https://aquasecurity.github.io/trivy-repo/deb> {{ ansible_lsb['codename'] }} main" | Trivy repo URL for Debain family systems. Utilized facts such as `ansible_lsb['codename']`.
trivy_repo_debain_filename          | trivy                                                                                    | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
trivy_repo_debian_desired_state     | present                                                                                  | `present` indicates creating the repository file if it doesn't exist on Debian based systems. Alternative is `absent` (not recommended as it will prevent from installation of **trivy** package).
trivy_repo_el                       | <https://aquasecurity.github.io/trivy-repo/rpm/releases/$releasever/$basearch/>          | Repository `baseurl` for Trivy on EL based systems.
trivy_repo_el_name                  | trivy                                                                                    | Repository name for Trivy on EL based systems.
trivy_repo_el_description           | Trivy repository                                                                         | Description to be added in EL based repository file for Trivy.
trivy_repo_el_gpgcheck              | no                                                                                       | Boolean for whether to perform gpg check against Trivy on EL based systems.
trivy_repo_el_enabled               | yes                                                                                      | Boolean to set so that Trivy repository is enabled on EL based systems.
trivy_repo_el_filename              | trivy                                                                                    | Name of the repository file that will be stored at `/yum/sources.list.d/trivy.repo` on EL based systems.
trivy_repo_el_desired_state         | present                                                                                  | `present` indicates creating the repository file if it doesn't exist on EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **trivy** package).

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).

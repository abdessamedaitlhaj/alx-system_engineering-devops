#!/usr/bin/env bash
# SSH confiiguration file
file_line {'no pass':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentification no'
}

file_line {'using specific identity':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school'
}

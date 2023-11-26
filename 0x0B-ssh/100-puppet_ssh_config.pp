# SSH confiiguration file
file_line {'ssh config'
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => ['PasswordAuthentification no', 'IdentityFile ~/.ssh/school'],
  replace => 'true'
}

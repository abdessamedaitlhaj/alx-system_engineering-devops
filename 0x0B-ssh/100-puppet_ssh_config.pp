# SSH confiiguration file
file {'ssh config'
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => ['PasswordAuthentification no', 'IdentityFile ~/.ssh/school']
}

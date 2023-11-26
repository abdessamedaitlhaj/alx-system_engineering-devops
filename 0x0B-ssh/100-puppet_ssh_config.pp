# SSH confiiguration file
file {'ssh config'
  path    => '/etc/ssh/ssh_config'
  line    => ['PasswordAuthentification no', 'IdentityFile ~/.ssh/school']
}

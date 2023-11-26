# SSH confiiguration file
file {'ssh config'
  path    => './ssh_config'
  content => 'Passwordauthentification no\nIdentityFile ~/.ssh/school'
}

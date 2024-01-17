# replace the 'pphp' with valid file extention 'php'
exec { 'fix_extention':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

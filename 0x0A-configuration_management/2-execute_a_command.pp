# Kill the process `killmenow`

exec { 'kill_killmenow':
  command => '/usr/bin/pkill killmenow'
}

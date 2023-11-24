
# Ensure pip is installed
package { 'pip3':
  ensure => 'installed'
}

# Install Flask using pip
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

# The script that creates a puppet file at /tmp
file { '/tmp/school':
    ensure  => 'file',
    mode    => '0744',
    group   => 'www-data',
    owner   => 'www-data',
    content => 'I love Puppet',
}

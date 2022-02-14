# -*- mode: ruby -*-
# vi: set ft=ruby :

# Define environment variables
$set_environment_variables = <<SCRIPT
tee "/etc/profile.d/myvars.sh" > "/dev/null" <<EOF
# weatherapi environment variables
export POSTGRES_PASSWORD=#{ENV['POSTGRES_PASSWORD']}
export WEATHER_API_KEY=#{ENV['WEATHER_API_KEY']}
EOF
SCRIPT


Vagrant.configure("2") do |config|
  config.vm.box = "devalone/ubuntu-20.04-server-x64-puppet"
  config.vm.box_version = "1.0.0"
  # Set up environment variables 
  config.vm.provision "shell", inline: $set_environment_variables, run: "always"

  config.vm.provision :shell do |shell|
    shell.inline = "mkdir -p /etc/puppet/modules;
                    puppet module install puppetlabs-docker;
                    "
  end
  # Idempotently install docker compose 
  config.vm.provision :shell do |shell|
    shell.inline = "
                    if [[ ! -f docker-compose-linux-x86_64 ]]
                    then
                    mkdir -p /usr/local/lib/docker/cli-plugins;
                    wget https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64;
                    cp docker-compose-linux-x86_64 /usr/local/lib/docker/cli-plugins/docker-compose;
                    chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
                    fi
                    "
  end
  # Move docker-compose file to vagrant box
  config.vm.provision "file", source: "./docker-compose.yml", destination: "docker-compose.yml"

  # Install docker and add vagrant user to docker group via Puppet
  config.vm.provision "puppet"

  # Bring up app stack with docker-compose 
  config.vm.provision :shell do |shell|
    shell.inline = "docker compose up -d"
  end
  
  config.vm.network "forwarded_port", guest: 80, host: 8080


end

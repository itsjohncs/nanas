Vagrant.configure("2") do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "legion-image"

  config.vm.network "private_network", ip: "10.10.0.2"

  # Provision the VM with our Ansible playbook.
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "vagrant/playbook.yml"
    ansible.sudo = true
  end
end

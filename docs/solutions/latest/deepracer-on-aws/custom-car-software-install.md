---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/custom-car-software-install.html
---

# Install the AWS DeepRacer community software
<a name="custom-car-software-install"></a>

The [AWS DeepRacer Community custom car repository](https://github.com/aws-deepracer-community/deepracer-custom-car) provides installation scripts that replicate the DeepRacer on AWS software stack on Raspberry Pi hardware.

1. Clone the repository:

   ```
   git clone https://github.com/aws-deepracer-community/deepracer-custom-car.git
   cd deepracer-custom-car
   ```

1. Run the prerequisites installation script and reboot:

   ```
   sudo ./install_prerequisites.sh
   sudo reboot
   ```

1. After the reboot, run the main installation script:

   ```
   cd deepracer-custom-car
   sudo ./install_deepracer.sh
   ```

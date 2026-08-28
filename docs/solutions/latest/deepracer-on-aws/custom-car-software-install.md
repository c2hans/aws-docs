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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

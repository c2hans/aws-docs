---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/custom-car-software-boot.html
---

# First boot and updates
<a name="custom-car-software-boot"></a>

1. Insert the SD card into the Raspberry Pi 5 and power on the vehicle.

1. Allow the first-run cloud-init process to complete. This might take several minutes.

1. Connect to the Raspberry Pi via SSH and wait for any automatic OS updates to finish before proceeding.

```
ssh deepracer@deepracer.local
sudo apt-get update && sudo apt-get upgrade -y
sudo reboot
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

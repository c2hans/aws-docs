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

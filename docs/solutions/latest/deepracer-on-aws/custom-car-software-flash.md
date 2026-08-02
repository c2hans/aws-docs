---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/custom-car-software-flash.html
---

# Flash the SD card
<a name="custom-car-software-flash"></a>

1. Download and install [Raspberry Pi Imager](https://www.raspberrypi.com/software/) from the Raspberry Pi website on your computer.

1. Insert a 128 GB micro SD card into your computer.

1. In Raspberry Pi Imager, select **Ubuntu Server 24.04 LTS (64-bit)** as the operating system.

1. Before writing, open **OS Customization** and set:
   + Hostname: `deepracer`
   + Username: `deepracer`
   + Enable SSH with password authentication.

1. Write the image to the SD card.

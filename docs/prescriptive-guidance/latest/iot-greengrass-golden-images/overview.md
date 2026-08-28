---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iot-greengrass-golden-images/overview.html
---

# What is a golden image?
<a name="overview"></a>

A golden image is a snapshot of software used to flash or provision many devices. Here are some examples of golden images in other domains that you might already be familiar with:
+ **Raspberry Pi**: The [Raspberry Pi OS ISO files](https://www.raspberrypi.com/software/operating-systems/) that you can download and use to flash the Raspberry Pi SD card.
+ **Amazon Elastic Compute Cloud (Amazon EC2)**: The [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) you use to launch an [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instance.
+ **Docker**: The Docker images you download from registries such as [Docker Hub](https://hub.docker.com/) and use to launch Docker containers.
+ **Micro-controllers**: For highly-constrained micro-controllers, it's common to combine the bootloader, the application, and data sections into a single Motorola S-record file, Intel HEX file, or binary file for flashing-by-wire in the factory.

## Extracting a golden image from a golden device
<a name="extraction"></a>

A golden image can be composed, or it can be created by taking a snapshot of a golden device whose image represents the desired state. In the case of AWS IoT Greengrass, using a snapshot of a golden device is the recommended approach.

As shown in the following illustration, a golden device is created, its file system is read to create the golden image, and this image is then written to many devices, at scale.

![Creating and using a golden image to provision devices.](http://docs.aws.amazon.com/prescriptive-guidance/latest/iot-greengrass-golden-images/images/guide-img/ca526734-1212-4b56-a092-9b8dbbd2ef52/images/cdd5a6a1-8472-4a2f-bacf-340617b7cc05.png)

## Unique configuration
<a name="configuration"></a>

Although the same golden image is written to every device, a small amount of unique configuration or personalization (for example, unique serial numbers, unique device names, and unique credentials) is typically also needed for each device. In the Raspberry Pi example, the `raspi-config` utility is used to create the unique configuration after flashing. In the case of AWS IoT Greengrass, a core device requires at least a unique thing name, a unique device certificate, and a unique private key.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

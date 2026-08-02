---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iot-greengrass-golden-images/introduction.html
---

# Manufacturing devices at scale with AWS IoT Greengrass golden images
<a name="introduction"></a>

*Greg Breen, Amazon Web Services*

[AWS IoT Greengrass](https://aws.amazon.com/greengrass/) is an edge runtime and cloud service that helps you compose, deploy, and manage Internet of Things (IoT) device software at scale. By convention, an AWS IoT Greengrass [deployment](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-deployments.html) distributes your application's software [components](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-components.html) from the cloud to your devices. If you're a device maker who manufactures at scale, it's unlikely that you'd want to perform an AWS IoT Greengrass deployment from the cloud to each device that comes off the manufacturing line in your factory. Instead, you would likely want to bundle your entire software stack into a single image, and flash each device by wire. This guide outlines approaches you can take to bundling the AWS IoT Greengrass edge runtime, and your application components and configuration, into a *golden image*. This helps to facilitate efficient and scalable factory-line programming of your devices. These approaches help increase the productivity of your device manufacturing operations and reduce your per-unit manufacturing costs.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for architects, technical leads, and engineers who are responsible for designing and developing the manufacturing stations on the production line of an IoT device or product that uses AWS IoT Greengrass.

## Applicability
<a name="applicability"></a>

AWS IoT Greengrass offers two edge runtime options: [nucleus ](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html) and [nucleus lite](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html). This guidance is specifically written for the nucleus option.

## Assumed knowledge
<a name="assumed-knowledge"></a>

This guide assumes that you're familiar with:
+ The AWS IoT Greengrass service and features such as components, deployments, recipes, and artifacts. For information, see the [AWS IoT Greengrass documentation](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html).
+ The Linux operating system.
+ Device manufacturing lines and processes.

## Attachments
<a name="attachments-ca526734-1212-4b56-a092-9b8dbbd2ef52"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

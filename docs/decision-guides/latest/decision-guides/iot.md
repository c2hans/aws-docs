---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/iot.html
---

# Choosing an AWS IoT service
<a name="iot"></a>

**Understand the differences and pick the one that's right for you**

<table>
<tbody>
  <tr><td><b>Purpose</b></td><td colspan="2">Help determine which AWS IoT services are the best fit for your organization.</td></tr>
  <tr><td><b>Last updated</b></td><td colspan="2">June 28, 2024</td></tr>
  <tr><td><b>Covered services</b></td><td><b>Foundational services</b></td><td><b>Use case or industry-specific services</b></td></tr>
  <tr><td></td><td><i>Device and design</i><ul><li> <a href="https://docs.aws.amazon.com/freertos/latest/userguide/what-is-freertos.html">FreeRTOS</a> </li><li> <a href="https://docs.aws.amazon.com/iot-expresslink/">AWS IoT ExpressLink</a> </li><li> <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html">AWS IoT Greengrass</a> </li><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html">AWS IoT Device SDKs</a> </li></ul><br /><i>Connect, manage and monitor</i><ul><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html">AWS IoT Core</a> </li><li> <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html">Amazon Kinesis Video Streams</a> </li><li> <a href="https://docs.aws.amazon.com/iot-device-defender/latest/devguide/what-is-device-defender.html">AWS IoT Device Defender</a> </li><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html">AWS IoT Device Management</a> </li></ul><br /><i>Analyze and act</i><ul><li> <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html">AWS IoT Events</a> </li></ul><br /><i>Design and validate</i><ul><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor.html">AWS IoT Core Device Advisor</a> </li><li> <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/device-tester-for-greengrass-ug.html">AWS IoT Device Tester</a> </li><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html">AWS IoT Device Client</a> </li></ul></td><td><i>Smart manufacturing</i><ul><li> <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html">AWS IoT SiteWise</a> </li><li> <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv2.html">AWS IoT SiteWise Edge</a> </li><li> <a href="https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-gs.html">AWS IoT TwinMaker</a> </li></ul><br /><i>Connected vehicles</i><ul><li> <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/getting-started-console-tutorial.html">AWS IoT FleetWise</a> </li></ul><br /><i>Public infrastructure</i><ul><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-sidewalk.html">AWS IoT Core for Amazon Sidewalk</a> </li><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html">AWS IoT Core for LoRaWAN</a> </li></ul></td></tr>
</tbody>
</table>

## Introduction
<a name="introduction"></a>

Internet of Things (IoT) technologies have become a transformative force in the business world. They offer a wide range of opportunities for innovation, efficiency, and customer-centric strategies. IoT provides the foundation for smart devices, smart homes, smart buildings, next-generation vehicles, smart manufacturing, and public infrastructure. Businesses can use IoT technologies to increase efficiency with automation, gain visibility into their supply chains, get insights from their data, and offer smart connected experiences for their customers.

AWS offers a variety of purpose-built IoT services. The foundational services help you to design and simplify complex IoT tasks. These services provide device-to-cloud connectivity, secure data ingestion, data processing, analytics, and the ability to run machine learning (ML) inferences on the edge. In addition, AWS offers IoT services that are designed for particular industries or use cases, including smart manufacturing, connected vehicles, and public infrastructure.

This decision guide will help you ask the right questions, evaluate your criteria, and determine which IoT services are the best fit for your needs.

[![AWS Videos](http://img.youtube.com/vi/o4Rr_lDFWfA?si=D-ZdUEJx0FOE6az0/0.jpg)](http://www.youtube.com/watch?v=o4Rr_lDFWfA?si=D-ZdUEJx0FOE6az0)

## Understand
<a name="understand"></a>

IoT is sometimes described as a bridge between the physical and digital worlds.

It is a network of connected devices and sensors that communicate with each other and the cloud. These devices and sensors (sometimes called things) collect data from a very broad range of sources.

![Diagram showing an introduction to Internet of Things (IoT).](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/what-is-iot.jpg)

The devices collect data from sources that are connected to home appliances, buildings, machines, vehicles, hardware, factory production lines, pipelines, and connected people (for example, people wearing smart, connected devices for monitoring their health and fitness).

IoT services are designed to help you:
+ Securely connect your IoT devices to the cloud.
+ Process the data locally on the devices.
+ Securely capture and ingest data in the cloud for additional processing or for added intelligence.
+ Manage structured and unstructured data, such as video streams.
+ Analyze that data and enrich it further using analytics and machine learning services to generate actionable insights.
+ Develop plans that you can act on (such as exercise recommendations for individuals, or predictive machine maintenance strategies for industrial assets or fleets of vehicles).
+ Perform remote over-the-air updates to keep your devices and systems up to date.
+ Scale your operations from an initial set of devices up to billions globally, while achieving higher reliability, quality of service, and availability.
+ Monitor your organization’s security posture across your entire device fleet.

![Diagram showing the AWS IoT stack.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/IoT-stack.png)

When asking how AWS IoT services can be useful to your organization, it's important to think about how these services are organized.

If you think about these services as a stack, as shown in the previous image, the foundational AWS Cloud services you need are at the base. These include services that provide compute, storage, database, containers, system management, networking management, and security. These services can also provide the analytics, ML, and artificial intelligence (AI) capabilities required to make the most of the insights you get from your IoT data.

Moving up the stack, you see a range of purpose-built IoT services (including industry-specific services) and IoT solutions from both AWS and AWS Partners.

### Generative AI and IoT
<a name="understand-genAI"></a>

While IoT-specific generative AI is still evolving, we see two broad categories of use cases:
+ Use cases that help IoT solution developers build more capable solutions faster and with higher quality.
+ Use cases that help end users naturally interact with IoT devices to generate recommendations and insights from their data.

There are a wide range of possibilities when you connect a vast amount of IoT data with generative AI technology. Your initial focus, however, is likely to be on tangible use cases where you can find value today.

![Diagram showing a comprehensive set of AWS IoT services.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/iot-services.png)

For example, developers can provide a description of the application function with details about an IoT circuit board and sensors. Then, a generative AI-powered function can produce prototype code with associated infrastructure as code (IaC) and installation steps. It can also provide generic prototype code for one type of board and automatically convert it to working code for another.

Consider also [this sample app](https://aws.amazon.com//blogs/iot/building-an-ai-assistant-for-smart-manufacturing-with-aws-iot-twinmaker-and-amazon-bedrock/) for using AWS IoT TwinMaker with Amazon Bedrock in manufacturing as an example of what you can accomplish when combining AI and IoT.

Further, generative AI models can create infrastructure code (such as CloudFormation templates) that define asset models in AWS IoT SiteWise, device metadata in AWS IoT Device Management, and other associated AWS infrastructure.

This can reduce proof of concept (PoC) development time and lower the barrier of entry to create customized AWS solutions. You can then use generative AI models to audit environments and provide recommendations to save on costs and improve your organization's security posture.

Finally, you can synthetically create realistic and unidentifiable user data to comprehensively test IoT applications with a small sample of data and description of user behavior. This can help you to test unforeseen edge cases. This testing results in better products, accelerated release cycles, and fewer production issues.

## Consider
<a name="consider"></a>

Here are some of the key criteria to consider when you’re choosing which IoT services are the best fit for your organization.

------
#### [ Business outcome ]

 ![Business applications icon](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch-Category_Business-Applications_48.png)

**Business outcome**

 Start by articulating the problem that you want to solve, along with the desired business outcome that will result from solving that problem. AWS offers a number of purpose-built services that are specific in what they can provide to help you get to the business outcome you want.

For example, you might run a logistics company and use robots in your warehouses to automate the movement of packages within the facility. To reduce downtime, it’s important to be able to quickly get reports of a malfunction and react right away. It’s even better to reliably get data that signals a potential upcoming malfunction. An AWS monitoring service such as [AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html) is designed specifically with that kind of scenario in mind. Similarly, [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) is designed to help you analyze and get value from the vast amount of data coming in from your connected sites (where you might be receiving data from industrial sites and equipment).

------
#### [ Scale, reliability, and quality of service ]

 ![Auto scaling icon](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Res_Amazon-EC2_Auto-Scaling_48.png)

**Scale, reliability, and quality of service**

To properly consider the issues of scale, reliability, and quality of service in AWS IoT, it's important to know that the AWS global infrastructure is built around AWS Regions and Availability Zones.

AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

To ensure availability in the event of a disruption, AWS IoT operates across multiple Availability Zones. In terms of the scale, reliability, and quality of service attributes of specific AWS services, here are some useful things to know:
+ [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html) provides fully managed [MQTT (Message Queuing Telemetry Transport)](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) -based messaging features. You can use these features to help you build adaptive IoT architectures. It also provides native support for a managed MQTT broker that supports persistent, always-on connections and advanced message retention policies. The broker also handles millions of devices and topics simultaneously. AWS IoT and the AWS IoT Device SDKs support the MQTT Quality of Service (QoS) levels 0 and 1.
+ [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/getting-started.html) provides support for data resiliency and backup with features that allow devices to communicate over the local network, even after losing internet connectivity. This allows the core to receive messages that are sent while the core is offline. Stream manager processes data locally until the connection is restored, and sends data to the cloud or local storage.
+ With [AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html), you can update devices in the field while using Amazon Amazon S3 versioning for all firmware and software, and update manifests for devices.
+ With [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), you can document your IoT infrastructure as code and provision cloud resources using a CloudFormation template.

------
#### [ Lifecycle management ]

 ![Lifecycle management icon](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Res_AWS-Systems-Manager_Change-Manager_48.png)

**Lifecycle management**

From initial deployment to eventual retirement, your IoT devices have a finite lifespan. You need to manage them effectively, reliably, and securely during that lifespan to achieve your business goals. How you address IoT product lifecycle management (PLM) is important in considering the AWS IoT services that you’ll need. Services such as [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html), [AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html), and [AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html) all provide important pieces of lifecycle management ([as described in this blog post](https://aws.amazon.com/blogs/iot/navigating-iot-product-lifecycle-management-with-aws-iot/)).

------
#### [ Edge support ]

 ![Edge support icon](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Res_Amazon-CloudFront_Edge-Location_48.png)

**Edge support**

In many IoT scenarios, you're working with devices that might rely on an [edge computing model](https://aws.amazon.com//what-is/edge-computing/) — and you need services that support running workloads at the edge.

A great example of this is [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html). It’s an open source IoT edge runtime and cloud service that helps you build, deploy, and manage IoT applications on your devices.

You can use it to build software that enables your devices to act locally on the data that they generate, run predictions based on ML models, and filter and aggregate device data. It enables your devices to collect and analyze data closer to where that data is generated, react autonomously to local events, and communicate securely with other devices on the local network.

Similarly, [AWS IoT ExpressLink](https://docs.aws.amazon.com/iot-expresslink/) powers a range of connectivity modules that are developed and offered by AWS Partners. These modules include software that implements AWS mandated security requirements. This makes it faster and easier for you to securely connect devices to the cloud, and to seamlessly integrate with a range of AWS services.

[AWS IoT SiteWise Edge](https://aws.amazon.com/iot-sitewise/sitewise-edge/) brings features of AWS IoT SiteWise in the cloud to the factory premises. Specifically, you can use asset models that are defined in the cloud service to process data in the SiteWise Edge gateway locally. You can also visualize equipment data by using local SiteWise Monitor dashboards that are served from the SiteWise Edge gateway.

[AWS IoT Device SDKs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html) are also a great resource for edge support. They include open source libraries, developer guides with samples, and porting guides.

Finally, the [AWS IoT Lens for the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/edge-layer.html) offers further guidance about the edge layer in IoT systems and what you need to support it.

------
#### [ Digital twin capabilities ]

 ![Digital twin capabilities icon](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch_AWS-IoT-TwinMaker_48.png)

**Digital twin capabilities**

A digital twin is a live digital representation of a system and all of its physical and digital components. It is dynamically updated with data to mimic the true structure, state, and behavior of the system.

The AWS IoT service that provides digital twin capabilities is [AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/what-is-twinmaker.html). You can use it to build operational digital twins of physical and digital systems.

With AWS IoT TwinMaker, you can create digital visualizations to help you keep track of your physical factory, building, or industrial plant. The visualizations use measurements and analyses from a variety of real-world sensors, cameras, and enterprise applications. You can use this real-world data to monitor operations, diagnose and correct errors, and optimize operations.

------
#### [ Development time ]

 ![Development time icon](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Dev-Tools_48.png)

**Development time**

To develop an IoT solution, you will likely need to structure your work into multiple phases, from proof of concept (PoC) to production and scale. You start getting benefits from IoT sooner if you use the right tools to prepare for your PoC, and prove the value of what you’re developing to get the support needed for broader implementation. The AWS tools that you can use for this include:
+ [AWS IoT Core Device Advisor](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor.html) — This tool provides a cloud-based, fully managed test capability for validating IoT devices during device software development. It includes pre- built tests that you can use to validate IoT devices for reliable and secure connectivity with AWS IoT Core, before deploying devices to production.
+ [AWS IoT Device SDKs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html) — The SDKs include open source libraries, developer guides with samples, and porting guides. You can use these to build IoT products or solutions on your choice of hardware platforms.
+ [AWS IoT Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-tutorials.html) — This tool provides code to help your device connect to AWS IoT, perform fleet provisioning tasks, support device security policies, connect using secure tunneling, and process jobs on your device.
+ [AWS IoT Sensors](https://apps.apple.com/us/app/aws-iot-sensors/id6447531633) (IOS app) — You can use this tool to visualize sensor data from your device with 1-click.

------
#### [ Video streaming support ]

 ![Video streaming support icon](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch_Amazon-Kinesis-Video-Streams_48.png)

**Video streaming support**

IoT implementations increasingly have video as a key data source. Those sources can include everything from smartphones, security cameras, and webcams to drones and cameras embedded in cars. In industrial settings, video inputs have become a critical component for automating defect detection sequences on the production line. Here are a couple of the AWS IoT services that you might consider to manage and make effective use of video inputs:
+ [Amazon Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html) — You can use this fully managed AWS service to stream live video from devices to the AWS Cloud, or to build applications for real-time video processing or batch-oriented video analytics. You can also use it to capture massive amounts of live video data from millions of sources. These sources include smartphones, security cameras, webcams, cameras embedded in cars, and drones.

  In addition, you can use Kinesis Video Streams to send non-video, time series data such as audio data, thermal imagery, depth data, and radar data. Using live video streams from these sources into a Kinesis video stream, you can build applications to access the data, frame-by-frame, in real time for low-latency processing.
+ [AWS IoT FleetWise](https://aws.amazon.com/blogs/iot/announcing-aws-iot-fleetwise-vision-system-data-preview/) vision system data — Announced in preview at re:Invent 2023, AWS IoT FleetWise supports vision system data collection for vehicles. With this feature, you can collect metadata, object list and detection data, and images or videos from camera, lidar, radar, and other vision subsystems.

------
#### [ Security ]

 ![Security icon](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch-Category_Security-Identity-Compliance_48.png)

**Security**

Security is a vital component of any IoT implementation. It's important for any IoT service to ensure that all elements of an IoT connection are encrypted and incorporate security best practices—whether it’s handling data at the edge or in transit to the cloud.

All traffic to and from [AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/security.html), for example, is sent securely over Transport Layer Security (TLS). AWS cloud security mechanisms protect data as it moves between AWS IoT and other AWS services. AWS IoT services address every layer of your application and device security.

You can safeguard your device data with preventative mechanisms, like encryption and access control, and consistently audit and monitor your configurations with [AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/dd-tutorials.html). You can use AWS IoT Device Defender to proactively assess the cloud configuration of your IoT device fleet, provide ongoing monitoring of device activities through rule-based and ML-based capabilities, and trigger alarms when an audit violation or behavior anomaly is identified.

------

## Choose
<a name="choose"></a>

Now that you know the criteria that you’ll use to evaluate your IoT service options, you're ready to choose which services might be a good fit.

Use the following table to help determine the services that are the best fit for your organization and use case.

------
#### [ Foundational services ]

These services are foundational to the implementation of Internet of Things (IoT) solutions on AWS.

|  **What is it optimized for?**  |  **Service**  |
| --- | --- |
| **Device and design**<br />AWS IoT device software services are optimized to:+  Build and manage IoT applications at the edge <br />+  Quickly transform any embedded device into an IoT-connected device  | [FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/what-is-freertos.html) <br />[AWS IoT ExpressLink](https://docs.aws.amazon.com/iot-expresslink/) <br />[AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) <br />[AWS IoT Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html) <br />[AWS IoT Device SDKs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html)  |
| **Connect, manage, and monitor**<br />AWS connectivity, control, and monitoring services are optimized to:+  Connect IoT devices to AWS <br />+  Audit IoT configurations <br />+  Secure IoT devices <br />+  Easily monitor and remotely manage IoT devices  | [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html) <br />[Amazon Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html) <br />[AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/dd-tutorials.html) <br />[AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) |
| **Analyze and act**<br />AWS IoT Events services are optimized to:+  Detect and respond to events from IoT sensors  | [AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html)  |
| **Validate**<br />These tools help you validate your designs. | [AWS IoT Device Tester](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-tester-for-greengrass-ug.html) <br />[AWS IoT Core Device Advisor](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor.html)  |

------
#### [ Use case or industry-specific services ]

These services are designed to meet the needs of specific industries or use cases.

|  **What is it optimized for?**  |  **Service**  |
| --- | --- |
| **Smart manufacturing**<br />These services are optimized for combining machine data from a single line, a factory, or a network of sites (such as manufacturing plants, assembly facilities, and refineries) to proactively improve performance. | [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/getting-started.html) <br />[AWS IoT SiteWise Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv2.html) <br />[AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-gs.html)  |
| **Connected vehicles**<br />This service is optimized for providing applications that analyze vehicle fleet health, which can help you to more quickly identify potential maintenance issues or make in-vehicle infotainment systems more capable. | [AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/getting-started-console-tutorial.html)  |
| **Public infrastructure**<br />These services are used in smart cities and transportation systems to:+  Support the use of smart metering technologies <br />+  Improve operations and logistics <br />+  Support the tactical edge <br />+  Manage traffic and public safety  | [AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html) <br />[AWS IoT Core for Amazon Sidewalk](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sidewalk.html)  |

------

## Use
<a name="use"></a>

To get started with the AWS IoT services, we have provided a pathway to explore each service. The following sections provide links to in-depth documentation, hands-on tutorials, and resources.

The first section provides links to resources for the key foundational IoT services: FreeRTOS, AWS IoT Greengrass, AWS IoT ExpressLink, AWS IoT Core, AWS IoT Device Defender, AWS IoT Device Management, AWS IoT Events, Amazon Kinesis Video Streams, and AWS IoT Analytics.

------
#### [ FreeRTOS ]
+ **What is FreeRTOS?**

  Learn about the microcontroller operating system that makes small, low-powered edge devices easy to program, deploy, secure, and maintain.

  [Explore the guide](https://docs.aws.amazon.com/freertos/latest/userguide/what-is-freertos.html)

+ **AWS IoT Device Tester for FreeRTOS**

  Use AWS IoT Device Tester for FreeRTOS to qualify data throughput rate with the FreeRTOS operating system.

  [Explore the guide](https://docs.aws.amazon.com/freertos/latest/userguide/device-tester-for-freertos-ug.html)

+ **FreeRTOS Porting Guide**

  Port FreeRTOS to a microcontroller platform.

  [Explore the guide](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-guide.html)

------
#### [ AWS IoT Greengrass ]
+ **What is AWS IoT Greengrass**

  Set up AWS IoT Greengrass and integrate it with other services.

  [Explore the guide](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)

+ **AWS IoT Greengrass V2 workshop**

  Build a virtual environment and an edge gateway that runs AWS IoT Greengrass Core software V2.

  [Use the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/5ecc2416-f956-4273-b729-d0d30556013f/en-US/chapter1-introduction/10-what-you-are-going-to-build)

+ **AWS IoT Greengrass API Reference**

  Learn about all the API operations for AWS IoT Greengrass V2 in detail. Read sample requests, responses, and errors for the supported web services protocols.

  [Explore the API reference](https://docs.aws.amazon.com/greengrass/v2/APIReference/Welcome.html)

------
#### [ AWS IoT ExpressLink ]
+ **What is AWS IoT ExpressLink?**

  Learn how ExpressLink hardware modules are preprogrammed to connect to AWS IoT services and are preloaded with security credentials.

  [Explore the guide](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-overview.html)

+ **AWS IoT ExpressLink Onboarding-by-Claim Customer/OEM Guide**

  Learn about an onboarding-by-claim mechanism that was specifically created to make the most of an AWS IoT ExpressLink module's capabilities.

  [Explore the guide](https://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/oemog.html)

+ **Start working with AWS IoT ExpressLink**

  Explore the AWS IoT ExpressLink development kit and resources to help you start using it.

  [Explore the guide](https://docs.aws.amazon.com/iot-expresslink/latest/gettingstartedguide/elgsg.html)

------
#### [ AWS IoT Core ]
+ **Get started with AWS IoT Core**

  Learn about AWS IoT concepts and terms that will help you start using AWS IoT.

  [Explore the guide](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html)

+ **AWS IoT Core API Reference**

  Explore the API operations for AWS IoT Core, including the data plane, jobs, and secure tunneling. It also provides sample requests, responses, and errors.

  [Explore the API reference](https://docs.aws.amazon.com/iot/latest/apireference/index.html)

+ **AWS IoT Core tutorials**

  Discover AWS IoT tutorials and choose the best learning path for your goal.

  [Get started with the tutorials](https://docs.aws.amazon.com/iot/latest/developerguide/iot-tutorials.html)

------
#### [ AWS IoT Device Defender ]
+ **What is AWS IoT Device Defender?**

  Learn about AWS IoT Device Defender, a security and monitoring service you can use to audit the configuration of your devices, monitor connected devices, and mitigate security risks.

  [Explore the guide](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/what-is-device-defender.html)

+ **Use the disconnected duration metric in AWS IoT Device Defender**

  The disconnected duration metric in AWS IoT Device Defender provides AWS IoT Device Defender Detect customers the ability to monitor Internet of Things (IoT) device connectivity status and duration of disconnection. This blog explains how to use it.

  [Read the blog](https://aws.amazon.com/blogs/iot/how-to-get-started-with-the-new-disconnected-duration-metric-in-aws-iot-device-defender/)

+ **AWS IoT Device Defender pricing guide**

  Learn how the pricing elements of the service work.

  [Explore the pricing guide](https://aws.amazon.com/iot-device-defender/pricing/)

------
#### [ AWS IoT Device Management ]
+ **Get started with AWS IoT Device Management**

  Start managing devices (also known as "things") and see an example of how information about things is stored in your registry as JSON data.

  [Explore the guide](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html)

+ **AWS IoT Device Management FAQs**

  Learn about where, how, when, and why you might use AWS IoT Device Management.

  [Explore the FAQs](https://aws.amazon.com/iot-device-management/faq/)

+ **Secure Internet of Things (IoT) with AWS**

  Get a detailed look at how you can use AWS security services to secure your IoT workloads in consumer and industrial environments.

  [Explore the whitepaper](https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/securing-iot-with-aws.html)

------
#### [ AWS IoT Events ]
+ **What is AWS IoT Events?**

  Use AWS IoT Events to monitor your equipment or device fleets for failures or changes in operation, and to initiate actions when such events occur.

  [Explore the guide](https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html)

+ **AWS IoT Events pricing guide**

  Learn how AWS IoT Events pricing works.

  [Explore the pricing guide](https://aws.amazon.com/iot-events/pricing/)

+ **AWS IoT Events FAQs**

  Learn about where, how, when and why you might use AWS IoT Events.

  [Explore the FAQs](https://aws.amazon.com/iot-events/faqs/)

------
#### [ Amazon Kinesis Video Streams ]
+ **What is Amazon Kinesis Video Streams?**

  Use Kinesis Video Streams to stream live video from devices to the AWS Cloud, or to build applications for real-time video processing or batch-oriented video analytics.

  [Explore the guide](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html)

+ **Amazon Kinesis Video Streams pricing**

  Learn how Kinesis Video Streams pricing works.

  [Explore the pricing guide](https://aws.amazon.com/kinesis/video-streams/pricing/)

+ **Amazon Kinesis Video Streams with WebRTC Developer Guide**

  Use Kinesis Video Streams with WebRTC to build applications for live peer-to-peer media streaming, or for real-time audio or video interactivity between camera IoT devices, web browsers, and mobile devices.

  [Explore the guide](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/what-is-kvswebrtc.html)

------

This section links to resources about use case or industry-specific AWS IoT services, including AWS IoT SiteWise, AWS IoT TwinMaker, and AWS IoT FleetWise.

------
#### [ AWS IoT SiteWise ]
+ **What is AWS IoT SiteWise?**

  Use AWS IoT SiteWise to collect, model, analyze, and visualize data from industrial equipment at scale.

  [Explore the guide](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html)

+ **AWS IoT SiteWise pricing guide**

  Learn how AWS IoT SiteWise pricing works—with separate charges for usage of Messaging, Data Processing, Data Storage, Data Export, AWS IoT SiteWise Monitor, AWS IoT SiteWise Edge, and Alarms.

  [Explore the pricing guide](https://aws.amazon.com/iot-sitewise/pricing/)

+ **AWS IoT SiteWise FAQs**

  Learn about where, how, when and why you might use AWS IoT SiteWise.

  [Explore the FAQs](https://aws.amazon.com/iot-sitewise/faqs/)

------
#### [ AWS IoT TwinMaker ]
+ **What is AWS IoT TwinMaker?**

  Use AWS IoT TwinMaker to build operational digital twins of physical and digital systems.

  [Explore the guide](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/what-is-twinmaker.html)

+ **AWS IoT TwinMaker pricing guide**

  Learn how AWS IoT TwinMaker pricing works. You can choose between the basic, standard, and tiered bundle pricing plans, depending upon the size and unique characteristics of your workloads.

  [Explore the pricing guide](https://aws.amazon.com/iot-twinmaker/pricing/)

+ **AWS IoT TwinMaker FAQs**

  Learn about where, how, when and why you might use AWS IoT TwinMaker.

  [Explore the FAQs](https://aws.amazon.com/iot-twinmaker/faqs/)

------
#### [ AWS IoT FleetWise ]
+ **What is AWS IoT FleetWise?**

  Use AWS IoT FleetWise to collect, transform, and transfer vehicle data to the cloud in near real time.

  [Explore the guide](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)

+ **AWS IoT FleetWise pricing guide**

  Learn how pricing works for AWS IoT FleetWise. It describes how it works on two dimensions: by number of vehicles and by number of messages.

  [Explore the pricing guide](https://aws.amazon.com/iot-fleetwise/pricing/)

+ **AWS IoT FleetWise FAQs**

  Learn about where, how, when and why you might use AWS IoT FleetWise.

  [Explore the FAQs](https://aws.amazon.com/iot-fleetwise/faqs/)

------

## Explore
<a name="explore"></a>
+ **Architecture diagrams**

  Explore reference architecture diagrams to help you develop your IoT solutions on AWS.

  [Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23iot&awsf.industries=*all&awsf.business-category=*all)

+ **Whitepapers**

  Explore whitepapers to help you get started, learn best practices, and understand your IoT options.

  [Explore whitepapers](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23iot&awsf.industries=*all&awsf.business-category=*all)

+ **AWS videos**

  Explore videos that will help you better use and understand the available AWS IoT services.

  [Watch the videos](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23video&awsf.methodology=*all&awsf.tech-category=tech-category%23iot&awsf.industries=*all&awsf.business-category=*all)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Decision Guides. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query decision-guides` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

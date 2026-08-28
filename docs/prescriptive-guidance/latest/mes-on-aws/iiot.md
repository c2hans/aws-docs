---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/iiot.html
---

# Industrial Internet of Things (IIoT)
<a name="iiot"></a>

Typical manufacturing facilities have thousands of sensors and devices that generate a lot of data. Most of this data goes unused. MES can contextualize this data and make it usable with the help of cloud-native services. MES can also connect with machines and devices, collect information automatically—for example, from process parameters and test results—and use it to respond in real time to events, save time, and eliminate the possibility of error due to manual entry. For example, you could collect results from testing machines, determine the product quality, and create non-conformance records or secondary inspection workflows in an automated manner without any manual data entry. Over time, cloud-native IoT services can help find specific patterns and root causes for defects, and you can prevent the defects from occurring by modifying the manufacturing process.

AWSoffers a broad and deep range of solutions for unlocking your IoT data and accelerating business results. These solutions include [AWS Partner solutions](https://aws.amazon.com/iot/partner-solutions/) and [AWS services](https://aws.amazon.com/iot/), which are the building blocks for the architecture based on customers' unique needs. The AWS IoT services that you can include in your architecture as building blocks include the following:
+ [AWS IoT Greengrass](https://aws.amazon.com/greengrass/) is an IoT open-source edge runtime and cloud service that helps you build, deploy, and manage device software. The edge runtime or client software runs on premises and is compatible with various hardware. It enables local processing, messaging, data management, and ML inference, and offers pre-built components to accelerate application development. AWS IoT Greengrass can exchange data with the edge component of MES for latency-sensitive use cases.
+ [AWS IoT Core](https://aws.amazon.com/iot-core/) is a managed cloud platform that lets connected devices interact with cloud applications and other devices easily and securely. AWS IoT Core can support billions of devices and trillions of messages reliably and securely, and can process and route those messages to AWS endpoints and other devices. When you use AWS IoT Core, your applications can keep track of, and communicate with, all your devices all the time, even when they aren't connected.
+ [AWS IoT SiteWise](https://aws.amazon.com/iot-sitewise/) is a managed service that enables industrial enterprises to collect, store, organize, and visualize thousands of sensor data streams across multiple industrial facilities. AWS IoT SiteWise includes software that runs on a gateway device that sits on site in a facility, continuously collects the data from historians or specialized industrial services, and sends it to the cloud. You can further analyze this collected data in the cloud and use it for dashboarding or feed it to MES for responses to results and trends.

## Architecture
<a name="iiot-architeccture"></a>

A typical IoT data ingestion and processing architecture can take many shapes based on unique environmental factors. The most common use case is to collect data from machines on the local network and securely send this data to the cloud. Here is the sample architecture for this use case.

![MES architecture for IIoT use cases](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/e8b88c3d-f05c-419f-aabc-48d635664177.png)

1. Machine or data source: These could be smart machines that are connected to the network and can share the data on their own, or other data sources such as PLCs and historians. The data coming from these sources can be in different protocols, such as MQTT and OPC-UA.

1. AWS IoT Greengrass is installed on a Greengrass core device with components that collect data from data sources and send it to the cloud.

1. Data in the MQTT protocol goes to AWS IoT Core. AWS IoT Core further redirects this data based on the rules that are configured.

1. Data in the OPC-UA protocol goes to AWS IoT SiteWise. Organizations can visualize this data by using the AWS IoT SiteWise portal. The data is fed to AWS IoT Core and eventually to a data lake for contextualization and to combine it with data from other systems.

1. Amazon Kinesis streams the data from AWS IoT Core to store it. AWS IoT Core has a feature [rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) that gives it the ability to interact with other AWS services.

1. An Amazon Timestream database stores the data. This is just an example—you can use any other type of database depending on the nature of the data.

1. Amazon EKS manages the availability and scalability of the Kubernetes control plane nodes within the microservice.

1. You can feed the data that's ingested from machines and other operational technology (OT) data sources to a data lake.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

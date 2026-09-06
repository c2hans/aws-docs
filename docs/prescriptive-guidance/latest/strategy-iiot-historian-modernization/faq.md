---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-historian-modernization/faq.html
---

# FAQ
<a name="faq"></a>

## What is manufacturing historian modernization?
<a name="faq-1"></a>

*Manufacturing historian modernization* is the process of integrating plant data, data contextualization, and analytics with current and emerging technologies, such as supervisory control and data acquisition (SCADA) systems, on-premises historians, and industrial IoT solutions.

## What are the benefits of historian modernization?
<a name="faq-2"></a>

Historian modernization provides enhanced visibility into system performance and operations by collecting, storing, and analyzing real-time and historical data from across the organization's production ecosystem. You can use this data to improve efficiency and productivity, minimize downtime, and enable long-term data analysis, resulting in improved decision-making from a business perspective. For more information, see [Use cases for historian modernization](use-cases.md) in this guide.

## What technologies are used in historian modernization?
<a name="faq-3"></a>

The technologies typically include SCADA systems, data historians, and industrial IoT solutions, such as edge computing and digital twins. These technologies provide comprehensive data and insights into production systems. There are number of AWS services that can help you gather the data. The following are a few key services to consider when building a solution to analyze industrial data:
+ [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) is an open source IoT edge runtime and cloud service that helps you build, deploy, and manage device software. You can use AWS IoT Greengrass for the IoT applications on millions of devices in homes, factories, vehicles, and businesses.
+ [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) is a managed service that helps you collect, store, organize, and visualize thousands of sensor data streams across multiple industrial facilities.
+ [AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/what-is-twinmaker.html) is a service that helps you create digital twins of real-world systems. You can use the digital twin to monitor operations, diagnose and correct errors, and optimize operations.
+ [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html) is a fast, scalable, and serverless time-series database service for IoT and operational applications. It can store and analyze trillions of time-series data points per day.

## What steps are involved in historian modernization?
<a name="faq-4"></a>

The historian modernization process typically involves the following steps:

1. Aligning OT data and analytics to business objectives

1. Collecting, aggregating, and normalizing data from sources, such as IIoT devices and historians

1. Storing data securely and consistently

1. Analyzing and evaluating the data for insights that can grow your business

For more information, see [Historian modernization approaches](approaches.md) in this guide.

## What challenges should be considered when modernizing a historian?
<a name="faq-5"></a>

Challenges to consider when modernizing a historian include ensuring secure and consistent data storage, ensuring quality and accuracy of data, preventing data loss, connecting to legacy systems, and addressing data privacy and security concerns. Additionally, modernizing a historian requires careful planning and implementation to ensure a successful outcome.

## How can a cloud-based historian access data with low latency at the edge?
<a name="faq-6"></a>

Every modernized cloud-based historian should have access to data at the edge. The data is cached at the edge for few days for local consumption at the site or for running any ML inference. This data also helps support any KPIs and production metrics if the local or edge networks are disconnected from the cloud network.

## Can I use a cloud-based historian if I have already invested in an on-premises setup with multi-year license?
<a name="faq-7"></a>

There are number of ways you can push data from existing historians, such as [AVEVA PI System](https://www.aveva.com/en/products/aveva-pi-system/), to create multi-site visibility or support advanced use cases, such as digital twins.

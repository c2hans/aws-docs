---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/differentiators-for-automotive-platforms-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Differentiators for automotive platforms on AWS
<a name="differentiators-for-automotive-platforms-on-aws"></a>

 As the overall trends in the automotive industry tend to be moving away from on-premises infrastructure, we are also seeing a trend away from provisioned infrastructure running an open-source software handling ingest to adopting more cloud managed services.

 Data ingestion and processing of vehicle telemetry data at scale requires a very heavy lift for the OEMs, especially handling peak processing for a short period of time. For the newer connected vehicles, 100 data sensors in the vehicle can [generate 25 gigabytes of data per hour](https://www.statista.com/chart/8018/connected-car-data-generation/), with only a fraction of that being published to the connected car platform. If an OEM produces [one million vehicles a year](https://www.statista.com/outlook/mmo/passenger-cars/worldwide#technical-specifications), and the peak usage is 60% of these vehicles on the road at the same time, the OEM will need to scale their platform to ingest a significant amount of data per vehicle, and that will grow as the use cases increase. AWS IoT Core, delivered as a distributed and managed platform, scales automatically as your vehicle fleet grows, and will scale as the vehicle data ingest increases as well.

 There are other additional benefits to the automotive use case the managed services of AWS IoT Core:
+  **Scalability** – Proper resource allocation specific to the OEMs workloads along with elastic infrastructure allows the OEM to not worry about a capacity planning effort as their fleet or customer use cases change over time - the operator can scale from zero to millions of vehicles automatically.
+  **Global Availability** – AWS IoT Core is a global service, available in 21 regions throughout the world, allowing for global architectures and enabling the operator to comply with local data storage and privacy requirements providing customers the flexibility to choose which region their content is stored based on their requirements. In addition to regulatory compliance, having global endpoints allows the broker to be as close as possible to the vehicle, decreasing latency and increasing end user satisfaction.
+  **Cost savings** – Using AWS IoT as the message broker within a connected vehicle platform reduces operational overhead as the OEM does not need to worry about provisioning infrastructure, cluster management, right-sizing compute, or administrative functions when building on a fully managed message broker
+  **Reliability** – With millions of daily connected devices, and trillions of messages processed monthly and 99.9% uptime service-level agreement (SLA), end customers have discovered the reliability of AWS IoT Core for other workloads across industries.
+  **Observability** – With many integrated services like CloudWatch, FleetHub and AWS IoT Device Management AWS IoT Core provides the ability to monitor your fleet with unified service metrics and dashboards across your fleet of vehicles and provides the ability to automate the detection and mitigation of problems.

 In addition to the managed services of AWS IoT Core, there are several other advantages for automotive OEMs to select AWS IoT Core as its managed message broker for its connected vehicle platform.

 **Security of the AWS Cloud:** Cloud security at AWS is the highest priority. The OEM benefits from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations. In the cloud, you don't have to manage physical servers or storage devices. Instead, you use software-based security tools to monitor and protect the flow of information into and out of your cloud resources. Security is a [shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) between AWS and the customer. AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud.

 AWS also provides you with services that you can use securely. Customers should carefully consider the services they choose as their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations. Each connected device or client must establish trust by authenticating using principals such as X.509 certificates, which should not be shared between devices. All traffic to and from AWS IoT is sent securely most commonly using Mutual Transport Layer Security (mTLS) or other authentication mechanisms. Data moving between services is authenticated and authorized by Identity and Access Management. In addition, AWS IoT provides security services like AWS IoT Device Defender which allows you to automatically detect, generate & rotate expiring certificates on your devices

 Securing connectivity platforms using AWS services and features:

 **Provisioning vehicle identities using AWS IoT Core:** AWS provides several different ways to provision your vehicle's connectivity devices to IoT Core and to enable the device manufacturer to install unique X.509 certificates on the device. This flexibility allows OEMs to pick the best method for their specific use cases, whether the certificate is installed on the device before they are delivered or installing the certificate later on in the manufacturing process such as the first time the device tries to connect. This topic will be covered in more detail later in the document.

 **OTA and the edge:** The AWS IoT Jobs service allows the OEM to securely update the vehicle software over the air (OTA). The binaries are signed in the cloud using AWS Signer which is to ensure integrity in transit to the vehicle such that the device agent can verify the signature against a known code-signing certificate. The agent on the vehicle connects to the Jobs service via MQTT or HTTPs each boot to check if there is a software update scheduled. The job execution state is updated by the device agent to ensure the installation is successful.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

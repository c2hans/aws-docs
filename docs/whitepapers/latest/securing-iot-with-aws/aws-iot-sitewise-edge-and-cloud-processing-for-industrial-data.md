---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/aws-iot-sitewise-edge-and-cloud-processing-for-industrial-data.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS IoT SiteWise – Edge and Cloud processing for industrial data
<a name="aws-iot-sitewise-edge-and-cloud-processing-for-industrial-data"></a>

 [AWS IoT SiteWise](https://aws.amazon.com/iot-sitewise/) is a managed service that allows industrial enterprises to collect, store, organize, and visualize thousands of sensor data streams across multiple industrial facilities. AWS IoT SiteWise includes software that runs on a gateway device that resides onsite in a facility, continuously collects the data from a historian or a specialized industrial server, and sends it to the AWS Cloud. Industrial companies can use AWS IoT SiteWise to monitor and improve processes in a single industrial site or across multiple facilities, understand and resolve equipment issues efficiently, and visualize operational data of devices and equipment with the SiteWise Monitor feature.

## Security capabilities
<a name="cap-6"></a>

 AWS IoT SiteWise gateway supports connectivity over the OPC-UA, Modbus TCP, or Ethernet/IP (EIP) protocols. AWS IoT SiteWise offers additional security when supported in the protocols, such as using encryption and server authentication secrets to authenticate between OPC-UA data sources securing your industrial data as it moves from your servers to the gateway. If your gateway has a hardware security module, you can configure AWS IoT Greengrass to secure your gateway. For AWS IoT SiteWise Monitor, customers can follow the principle of least privilege by using the minimum set of access policy permissions for their portal users and implement a healthy password rotation policy by configuring an appropriate expiration for passwords.

 Additionally, AWS IoT SiteWise Edge now offers many of these capabilities on-premises in support of low latency and network fault intolerant applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

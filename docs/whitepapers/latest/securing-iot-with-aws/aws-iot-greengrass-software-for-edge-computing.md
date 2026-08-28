---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/aws-iot-greengrass-software-for-edge-computing.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS IoT Greengrass – Software for edge computing
<a name="aws-iot-greengrass-software-for-edge-computing"></a>

 [AWS IoT Greengrass](https://aws.amazon.com/greengrass/) is software that lets customers run local compute, messaging, data caching, sync, and ML inference capabilities for connected devices, allowing connected devices to operate even with intermittent connectivity to the cloud. After the device reconnects, AWS IoT Greengrass synchronizes the data on the device with AWS IoT Core, providing constant functionality regardless of connectivity. AWS IoT Greengrass seamlessly extends AWS to devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage.

## Security capabilities
<a name="cap-2"></a>

 AWS IoT Greengrass authenticates and encrypts device data for both local and cloud communications, and data is never exchanged between devices and the cloud without proven identity. The service uses security and access management similar to what customers are familiar with in AWS IoT Core, with mutual device authentication and authorization, and secure connectivity to the cloud.

 More specifically, AWS IoT Greengrass uses X.509 certificates, managed subscriptions, AWS IoT policies, and AWS Identity and Access Management (IAM) policies and roles to ensure that AWS IoT Greengrass applications are secure. AWS IoT devices require an AWS IoT thing, a device certificate, and an AWS IoT policy to connect to the AWS IoT Greengrass service. This allows AWS IoT Greengrass core devices to securely connect to the AWS IoT cloud service. It also allows the AWS IoT Greengrass cloud service to deploy configuration information, AWS Lambda functions, and managed subscriptions to AWS IoT Greengrass core devices. In addition, AWS IoT Greengrass provides hardware root of trust private key storage for edge devices.

 Other important security capabilities of AWS IoT Greengrass are monitoring and logging. For example, core software in the service can write logs to Amazon CloudWatch (which also functions for AWS IoT Core) and to the local file system of customers' core devices. Logging is configured at the group level and all AWS IoT Greengrass log entries include a time stamp, log level, and information about the event. AWS IoT Greengrass is integrated with AWS CloudTrail—a service that provides a record of actions taken by a user, role, or an AWS service in AWS IoT Greengrass—and if activated by the customer, it captures application programming interface (API) calls for AWS IoT Greengrass as events. This includes calls from the AWS IoT Greengrass console and code calls to the AWS IoT Greengrass API operations. For example, customers can create a trail and calls can enable continuous delivery of AWS CloudTrail events to an Amazon Simple Storage Service (Amazon S3) bucket, including events for AWS IoT Greengrass. If customers don’t want to create a trail, they can view the most recent events in the AWS CloudTrail console in event history. This information can be used to do a number of things, such as determining when a request was made to AWS IoT Greengrass and the IP address from which the request was made.

 Best practice options are available to secure customers’ data on the device and should be utilized whenever possible. For AWS IoT Greengrass, all IoT AWS IoT Greengrass devices should enable full disk encryption and follow key management best practices. Customers can utilize full disk encryption, using AES 256-bit keys based on NIST FIPS 140-2 validated algorithms and follow key management best practices. For low-power devices such as those using FreeRTOS, customers can follow NIST 8114 lightweight cryptography recommendations.

 The previous sections covered microcontrollers and edge use cases. The following sections will focus on IoT services that operate in the cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

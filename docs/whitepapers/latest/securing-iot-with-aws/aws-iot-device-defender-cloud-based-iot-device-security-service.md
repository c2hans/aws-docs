---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/aws-iot-device-defender-cloud-based-iot-device-security-service.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS IoT Device Defender – Cloud-based IoT device security service
<a name="aws-iot-device-defender-cloud-based-iot-device-security-service"></a>

 [AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/) is a fully managed service that helps customers secure their fleet of devices. The service continuously audits IoT configurations to ensure that configurations aren’t deviating from security best practices—such as ensuring device identity, authenticating and authorizing devices, and encrypting device data. The service can send an alert if there are any gaps in a customer's IoT configuration that might create a security risk, such as identity certificates being shared across multiple devices or a device with a revoked identity certificate trying to connect to AWS IoT Core.

 AWS IoT Device Defender also lets customers continuously monitor security metrics from devices and AWS IoT Core for deviations from the expected behaviors for each device. Customers can define the appropriate behavior for their devices or use ML to model the regular device behavior based on historical data. If something doesn’t look right according to defined behaviors or ML models, AWS IoT Device Defender pushes an alarm so customers can act to mitigate the issue. For example, spikes in outbound traffic might indicate that a device is participating in a distributed denial of service (DDoS) attack. Additionally, AWS IoT Greengrass and FreeRTOS automatically integrate with AWS IoT Device Defender to provide security metrics from the devices for evaluation.

## Security capabilities
<a name="cap-5"></a>

 AWS IoT Device Defender audits IoT configurations associated with customers’ devices against a set of defined IoT security best practices so customers know exactly where they have security gaps. Customers can run audits on a continuous or one-time basis. AWS IoT Device Defender comes with security best practices that customers can select and run as part of the audit. For example, customer can create an audit to check for identity certificates that are inactive, revoked, expiring, or pending transfer in less than seven days. Audits make it possible for customer to receive alerts while their IoT configuration is updated.

 AWS IoT Device Defender detects anomalies in device behavior that may indicate a compromised device by monitoring high-value security metrics from the cloud and AWS IoT Core and comparing them against expected device behavior that customers define. For example, AWS IoT Device Defender lets customers define how many ports are open on the device, who the device can talk to, where it is connecting from, and how much data it sends or receives. AWS IoT Device Defender also allows customers to use ML models to set device normal behavior (for example, the number of times customers’ devices connect with AWS IoT cloud every five minutes). Then, it monitors the device communication and traffic and alerts customers if something looks wrong according to defined behaviors or ML models (such as traffic from devices to a known malicious IP or a spike in connection attempts).

 AWS IoT Device Defender publishes security alarms to the AWS IoT console, Amazon CloudWatch, and Amazon Simple Notification Service when an audit fails or when behavior anomalies are detected so customers can investigate and determine the root cause. For example, AWS IoT Device Defender can alert customers when device identities are accessing sensitive APIs. AWS IoT Device Defender also provides built-in mitigation actions customers can take to minimize the impact of security issues such as adding a thing to a thing group (for example, quarantine), updating a device certificate, replacing default policy version, and enabling IoT logging.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

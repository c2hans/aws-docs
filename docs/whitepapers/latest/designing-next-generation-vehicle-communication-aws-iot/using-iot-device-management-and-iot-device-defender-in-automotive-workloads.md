---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/using-iot-device-management-and-iot-device-defender-in-automotive-workloads.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Using IoT Device Management and IoT Device Defender in automotive workloads
<a name="using-iot-device-management-and-iot-device-defender-in-automotive-workloads"></a>

 One key function of a connected vehicle platform is to ensure the operationalization of the fleet of vehicles. Whether the ask is to organize and group vehicle fleets into flexible hierarchies to streamline maintenance by make/model/year or to ensure the in-vehicle firmware is up-to-date, AWS IoT Core Device Management offers capabilities to ensure long-standing operations of a fleet of vehicles is handled with ease. From securing and monitoring device fleet health status and enablers to analyze trends, observability and push updates at scale.

 When a vehicle is onboarded to AWS IoT Core, all other services within the AWS IoT ecosystem are available to implement if the customer can derive value from those services. These services are not required to be used as part of a connected vehicle platform, but add differentiators to the long-term operationalization of the fleet of vehicles.

## AWS IoT Jobs
<a name="iot-jobs"></a>

 One key aspect of the software defined vehicle, is the capability of perform device software updates, over-the-air (OTA). With AWS IoT Jobs, it provides a framework to send a set of remote operations over MQTT to be run on remote devices connected to AWS IoT. For example, a customer can define an IoT Job that instructs a set of ECUs to download and install an application, run a firmware update, reboot the ECU or TCU, rotate certificates and perform operational steps such as remote troubleshooting session. AWS IoT Jobs is a simple framework to enable job documents and will still require an edge implementation to listen to job topics for remote commands and job documents.

## Lifecycle events
<a name="lifecycle-events"></a>

 Ensuring the current status of each vehicle is key for workflows such as remote commands. With AWS IoT Core, lifecycle events help enable storing the presence of the vehicle, either connected to AWS IoT Core or in a disconnected state. Each time a device connects or disconnects a payload is sent to a topic (`$aws/events/presence/connected/clientId`) which can then be used to create workflows aligned to these events. An example payload is as follows:

```
{
    "clientId": "186b5",
    "timestamp": 1573002230757,
    "eventType": "connected",
    "sessionIdentifier": "a4666d2a7d844ae4ac5d7b38c9cb7967",
    "principalIdentifier": "12345678901234567890123456789012",
    "ipAddress": "192.0.2.0",
    "versionNumber": 0
}
```

 Most design patterns around lifecycle events store the connection status in DynamoDB or some even use the AWS IoT Device Shadow service to persist the current connection state.

## Vehicle security monitoring and response
<a name="vehicle-security-monitoring-and-response-omar-to-add-monitoring-here"></a>

 **Monitoring and responding to vehicle events**

Regulations such as the UNECE Regulation 155 and standards such as ISO 21434 require that vehicles are monitored throughout the lifecycle. Monitoring vehicle threats goes beyond technology and requires organizational strategy, people, and processes to do so successfully. AWS can help provide services that provide insights from data collected from the vehicle and vehicle ecosystem (for example, charging stations, and companion applications).

Customers can use AWS IoT Core to analyze relevant security data in the cloud. Customers can send data to services that can analyze data for security purposes using AWS IoT Rules. For example, you can send telemetry data, CAN data, or other types of data via an AWS IoT Rule to Amazon OpenSearch Service. From OpenSearch Service you can configure rules that you want to alert on for anomalous behavior coming from your ECUs. This can be telemetry data that is anomalous like successive door openings, or ECU related logs that may indicate an ECU has an issue.

AWS IoT Device Defender is a downstream service of AWS IoT Core which provides additional security services that allows the customer to audit the configuration of vehicles, monitor connected vehicles to detect abnormal behavior, and mitigate security risks. This can be fed to AWS Security Hub CSPM and to your vehicle security operation center which can provide detection, runbooks, and remediation mechanisms across the fleet using AWS services. For more information on a detect and response architecture and example, see the [connected vehicle security reference architecture](https://aws.amazon.com/blogs/iot/securing-modern-connected-vehicle-platforms-with-aws-iot/).

OEMs need to configure their ECUs for least privilege behaviors. Not every ECU will not the same permissions to the same resources. Without a policy engine, it is difficult to implement least privilege. AWS IoT Device Defender addresses these challenges by providing tools to identify security issues and deviations from best practices. AWS IoT Device Defender can audit device fleets to ensure they adhere to security best practices such as overly permissive devices and detect abnormal behavior on devices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/publisher-supported-components.html
---

# Publisher-supported components
<a name="publisher-supported-components"></a>

|  |
| --- |
| Publisher-supported components are in a preview release for AWS IoT Greengrass and are subject to change. These components are not supported by AWS. You must contact the Publisher for any issues with each of the components. |

The Greengrass Publisher-supported components are developed, offered, and serviced by third-party component vendors. Third-party component vendors are either from the AWS Partner Device Catalog, AWS Heroes, or community vendors. You can purchase the components in this catalog by contacting the third-party component vendor directly.

The Greengrass Publisher-supported components include the following:

**Topics**
+ [AIShield.Edge](#publisher-supported-components-AIShield.Edge)
+ [AI EdgeLabs Sensor](#publisher-supported-components-AIEdgeLabs)
+ [Greengrass S3 Ingestor](#publisher-supported-components-S3Ingestor)

## AIShield.Edge
<a name="publisher-supported-components-AIShield.Edge"></a>

This component was developed and is supported by AIShield, powered by Bosch. Boost your AI security with AIShield.Edge. This component is designed to seamlessly deploy threat-informed, tailored defenses to edge devices, which safeguardes your devices against AI attacks.

This component offers the following benefits:
+ Seamlessly transition from vulnerability analysis with AIShield AI Security to fortified edge defenses within AWS
+ Deploy tailored defenses across multiple edge devices with ease
+ Broad protection tailored to diverse AI setups which supports various model types and frameworks
+ Stay updated with seamless integration into Amazon SageMaker AI and Greengrass workflows
+ Gain immediate insights into potential threats, with data relayed directly to AWS IoT Core
+ A cohesive AI security pathway for defense deployment on the edge from AIShield AI Security on the AWS Marketplace

This component must run on the following platform:
+ os: linux

If you are interested in purchasing this component, contact Bosch Software and Digital Solutions: AIShield.Contact@bosch.com.

## AI EdgeLabs Sensor
<a name="publisher-supported-components-AIEdgeLabs"></a>

This component was developed and is supported by AI EdgeLabs. AI EdgeLabs Sensor is a container-based application that contains AI-based threat detection and prevention capabilities. AI Sensor is wrapped into a Greengrass component and deployed as a standalone container on the core device alongside other Greengrass components.

This current component is a container-based agent that continuously verifies network communication, looks for threat patterns in software running on the Edge Host or IoT gateway. This component uses eBPF, behavioral verification of processes bandwidth, and the host-based configuration. The main functionality of this component is based on NDR/IPS and EDR functions.

This component offers the following benefits:
+ AI-based threat detection against network attacks and malware (EDR/NDR)
+ Automated AI-based Incident response (IPS)
+ Host-local threat intelligence with minimal data-transfer outside
+ Lightweight deployment with Docker and Greengrass

This component must run on one of the following platforms:
+ os: linux

If you are interested in purchasing this component, contact AI EdgeLabs: contact@edgelabs.ai.

## Greengrass S3 Ingestor
<a name="publisher-supported-components-S3Ingestor"></a>

This component was developed and is supported by Nathan Glover. The Greengrass S3 Ingestor component is designed to be used with the [stream manager component](https://docs.aws.amazon.com/greengrass/v2/developerguide/stream-manager-component.html). This component takes a line-delimited stream of JSON messages from stream manager and batches them into a GZIP file. This component enables efficient ingestion of data into Amazon S3 for further processing or for storage. This component doesn’t support sending data to the AWS Cloud in realtime.

This component must run on one of the following platforms:
+ os: linux
+ os: Windows

If you are interested in purchasing this component, contact Nathan Glover: nathan@glovers.id.au.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

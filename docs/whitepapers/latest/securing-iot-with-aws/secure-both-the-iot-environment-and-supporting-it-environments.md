---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/secure-both-the-iot-environment-and-supporting-it-environments.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 7. Secure both the IoT environment and supporting IT environments to the same level of criticality
<a name="secure-both-the-iot-environment-and-supporting-it-environments"></a>

Secure both the IoT environment and supporting IT environments to the same level of criticality following a well-documented standard. This is especially true for gateways that serve as boundaries between systems.

 Often, IoT systems still have a dependency on traditional IT systems to operate. Whether that’s for identity and authorization, billing, monitoring and remediation, or maintenance, having these systems become unavailable to the IoT system can cause cascading failures. Therefore, you should use the risk assessment and asset inventory to document these critical dependencies and architect all relevant systems to the same level of resiliency and security. Some ways to do this include:
+  Plan and manage security lifecycle of devices.
+  Consistently harden internet-connected network resources such as edge gateways.
+  Avoid hardcoding or storing credentials and secrets locally on devices.
+  Use device certificates and temporary credentials instead of long-term credentials to access AWS cloud services.
+  Limit the number of listening ports on IoT devices, and ensure access only from authorized systems.
+  Create allow lists for access with a management mechanism similar to that of software updates.
+  Disable unused sensors, actuators, services, or software on the IoT device.
+  Establish secure connections to cloud services, and monitor these connections.

## Supporting AWS resources
<a name="resources-7"></a>

 AWS provides the following assets, capabilities, and services to help secure cloud connected network resources and securely manage on-premises computing resources:
+  [NIST Guide to General Server Security](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-123.pdf) – For general guidance on security devices (such as edge gateways).
+  [AWS IoT Greengrass hardware security](https://docs.aws.amazon.com/greengrass/v1/developerguide/hardware-security.html#optional-provisioning)
+  [Working with secrets](https://docs.aws.amazon.com/greengrass/v1/developerguide/secrets-using.html) at the Edge.
+  [AWS IoT SiteWise Gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-gateway.html) – Securely configuring edge gateways.
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) – Provides you with a centralized and consistent way to gather operational insights and carry out routine management tasks.
+  [AWS IoT Device Management](https://aws.amazon.com/iot-device-management/) – A service that allows you to securely register, organize, monitor, and remotely manage IIoT devices at scale throughout their lifecycle.
+  [AWS IoT secure tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html) – Accesses IIoT devices behind restricted firewalls at remote sites for troubleshooting, configuration updates, and other operational tasks.
+  [Plant network to Amazon Virtual Private Cloud connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html)
+  [AWS IoT Greengrass - Connect on port 443 or through a network proxy](https://docs.aws.amazon.com/greengrass/v1/developerguide/gg-core.html#alpn-network-proxy)
+  [Security Pillar of AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [IoT Lens](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html)

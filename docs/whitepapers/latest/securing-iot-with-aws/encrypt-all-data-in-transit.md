---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/encrypt-all-data-in-transit.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 6. Encrypt all data in transit
<a name="encrypt-all-data-in-transit"></a>

Encrypt all data in transit, including sensor and device data, administration, provisioning, and deployments.

 Nearly all modern IoT devices have the power to perform encryption of network traffic, so take advantage of that and protect both the data plane and control plane communications. This not only ensures confidentiality of the data, but also the integrity of monitoring signals. For protocols that can’t be encrypted, consider if a second device closer to the IoT asset can accept the communication and convert it to something more secure to then send outside the local perimeter. Some additional considerations include:
+  Protect the confidentiality and integrity of inbound and outbound network communication channels that you use for data transfers, monitoring, administration, provisioning, and deployments by selecting modern internet native cryptographic network protocols.
+  If possible, limit the number of protocols implemented within a given environment and disable default network services that are unused.
+  If over-the-air updates are implemented, network-related vulnerabilities that affect the integrity of the over-the-air process should be addressed first.
+  If possible, implement mechanisms to identify when an insecure network environment is being used. For example, if the certificate used for TLS encryption doesn’t match a known certificate on the device such as in a man-in-the-middle event.

## Supporting AWS resources
<a name="resources-6"></a>

 AWS provides the following assets, capabilities, and services to help you encrypt your networks:
+  [AWS IoT SDKs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html) – Help you securely and quickly connect your devices to AWS IoT.
+  [FreeRTOS libraries](https://docs.aws.amazon.com/freertos/latest/userguide/dev-guide-freertos-libraries.html) – Provide additional functionality to the FreeRTOS kernel and its internal libraries.
+  [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) Private Certificate Authority – Provision your own certificates.
+  [Security best practices for AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security-best-practices.html)
+  [Security Pillar of AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [IoT Lens](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

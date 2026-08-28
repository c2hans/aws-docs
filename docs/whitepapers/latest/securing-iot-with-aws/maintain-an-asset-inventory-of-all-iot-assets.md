---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/maintain-an-asset-inventory-of-all-iot-assets.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 2. Maintain an asset inventory of all IoT assets
<a name="maintain-an-asset-inventory-of-all-iot-assets"></a>

Maintain an asset inventory of all IoT assets, including IT assets required to maintain IoT operations. Categorize them by safety, criticality, ability to patch, and other actionable criteria.

 A critical aspect of a good security program is having visibility into your system. It’s also important that you create visibility with actionable outcomes in mind, so you can automate operations and maintenance of these devices after deployment.
+  Create and maintain an asset inventory for all IoT assets along with their major characteristics that you may want to action upon. This includes things such as deployed certificates and software or hardware versions.
+  Segment devices into categories or apply appropriate tags to be able to manage them programmatically. Focus on actionable data such criticality of the devices, location, whether the device can or should be updated, or important contact and owner information.

## Supporting AWS resources
<a name="resources-2"></a>

 AWS provides the following services to help you create and maintain a connected asset inventory:
+  [AWS IoT Device Management](https://aws.amazon.com/iot-device-management/features/) – For devices connected to AWS IoT.
+  [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) – For cloud and on-premises computers.
+  [Security Pillar of AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [IoT Lens](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

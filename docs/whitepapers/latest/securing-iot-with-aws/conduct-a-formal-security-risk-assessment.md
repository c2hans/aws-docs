---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/conduct-a-formal-security-risk-assessment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 1. Conduct a formal security risk assessment using a common framework
<a name="conduct-a-formal-security-risk-assessment"></a>

Conduct a formal security risk assessment using a common framework (such as [MITRE ATT&CK](https://attack.mitre.org/)). Use this to inform system design.

 Whether you’re deploying consumer devices, industrial workloads, or operational technologies, it is important to first evaluate the risks and threats associated with your deployment. For example, one common threat to IoT devices listed in the MITRE ATT&CK framework is a [Network Denial of Service (T1498)](https://attack.mitre.org/techniques/T1498/). A denial-of-service (DoS) attack against an IoT device can be defined as disallowing status or command and control communication to and from an IoT device and its controllers. In the case of a consumer IoT device, such as a smart bulb, not having the ability to communicate status or receive updates from a central control place could create problems, but would likely not necessarily have dramatic consequences. However, in an OT system managing a water treatment facility, losing the ability to receive commands to open or shut key valves could create a larger impact to people and the environment. So, it’s important to look at the impact of various common threats, how they apply to different IoT use cases, and ways to mitigate them. Key steps include:
+  Identify, manage, and track gaps and vulnerabilities. Create and maintain an up-to-date threat model that can be monitored against.
+  Segment systems based on their risk assessment. Some IoT and IT systems may share the same risks, so use a predefined zoning model with appropriate controls between them.
+  Follow a micro segmentation approach to isolate the impact of an event.
+  Use appropriate security mechanisms to control information flow between network segments.
+  Regularly identify and review security event minimization opportunities as your IoT system evolves.

## Supporting AWS resources
<a name="resources-1"></a>

 When building your environment inside of AWS, foundational services such as Amazon Virtual Private Cloud (VPC), VPC security groups (SGs), and network access control lists (network ACLs) should be used to implement the micro segmentation. AWS recommends using multiple accounts, which helps to isolate IoT applications, data, and business processes across your environment and use AWS Organizations for better manageability and centralized insight. Additional information can be found in the [Security Pillar of AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [Organizing Your AWS Environment Using Multiple Accounts whitepaper](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html).

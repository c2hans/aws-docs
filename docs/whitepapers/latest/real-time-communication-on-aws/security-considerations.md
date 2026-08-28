---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/security-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security considerations
<a name="security-considerations"></a>

 RTC application components typically run directly on internet facing Amazon EC2 instances. In addition to TCP, flows use protocols like UDP and SIP. In these cases, AWS Shield Standard protects Amazon EC2 instances from common infrastructure layer (Layer 3 and 4) DDoS attacks, such as UDP reflection attacks, DNS reflection, NTP reflection, SSDP reflection, and so on. AWS Shield Standard uses various techniques like priority-based traffic shaping that are automatically engaged when a well-defined DDoS attack signature is detected.

 AWS also provides advanced protection against large and sophisticated DDoS attacks for these applications by enabling AWS Shield Advanced on Elastic IP addresses. AWS Shield Advanced provides enhanced DDoS detection that automatically detects the type of AWS resource and size of EC2 instance and applies appropriate predefined mitigations with protections against SYN or UDP floods. With AWS Shield Advanced, customers can also create their own custom mitigation profiles by engaging the 24x7 AWS DDoS Response Team (DRT). AWS Shield Advanced also ensures that during a DDoS attack, all of your Amazon VPC Network Access Control Lists (ACLs) are automatically enforced at the border of the AWS network providing you with access to additional bandwidth and scrubbing capacity to mitigate large volumetric DDoS attacks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

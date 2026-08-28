---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/metering-policy-middlebox.html
---

# Manage AWS Transit Gateway metering policy middlebox attachments
<a name="metering-policy-middlebox"></a>

transit gateway metering policies support Middlebox attachments allowing you to flexibly allocate data processing charges for network traffic routed via middlebox appliances such as network firewalls and load balancers. Examples of middlebox attachments are Network Function attachment to AWS Network Firewall or VPC attachments that route traffic to third-party security appliances in a VPC. Traffic between source and destination transit gateway attachments traverses via these middlebox attachments for typical security inspection use-cases. You can define metering policies to flexibly allocated data processing usage on middlebox attachments to the original source attachment, final destination attachment or transit gateway account owner. For Network Function attachments, the AWS Network Firewall data processing charges are also allocated to the metered account.

Designated transit gateway attachments that route traffic through network appliances for security inspection, load balancing, or other network functions. Data usage for the traffic traversing middlebox attachments is metered to the account owner specified in the metering policy. You can specify a maximum of 10 middlebox attachments. Supported middlebox attachment types are Network Function (AWS Network Firewall), VPC and VPN attachments.

**Topics**
+ [Add middlebox attachments](create-middlebox-attachment.md)
+ [Remove middlebox attachments](edit-middlebox-attachment.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

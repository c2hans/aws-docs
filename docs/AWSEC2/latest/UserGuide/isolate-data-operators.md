---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/isolate-data-operators.html
---

# Isolate data from your own operators
<a name="isolate-data-operators"></a>

The AWS Nitro System has [ zero operator access](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/no-aws-operator-access.html). There is no mechanism for any AWS system or person to log in to Amazon EC2 Nitro hosts, access the memory of EC2 instances, or access any customer data stored on local encrypted instance storage or remote encrypted Amazon EBS volumes.

When processing highly sensitive data, you might consider restricting access to that data by preventing even your own operators from accessing the EC2 instance.

You can create custom Attestable AMIs that are configured to provide an isolated compute environment. The AMI configuration depends on your workload and application requirements. Consider these best practices when building your AMI to create an isolated compute environment.
+ **Remove all interactive access** to prevent your operators or users access to the instance.
+ **Ensure that only trusted software and code** is included in the AMI.
+ **Configure a network firewall** within the instance to block access.
+ **Ensure read-only and immutable states** for all storage and file systems.
+ **Restrict instance access** to authenticated, authorized, and logged API calls.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

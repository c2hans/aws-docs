---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-isolated-amis.html
---

# Updating Attestable AMIs that have no interactive access
<a name="working-with-isolated-amis"></a>

After you launch an instance using an isolated compute environment AMI, there is no way for any user or operator to connect to the instance. This means that there is no way to install or update any software on the instance after launch.

If new software or a software update is required, you must create a new Attestable AMI that includes the required software or software updates. Then, use that AMI to launch a new instance, or to perform a root volume replacement on the original instance. Any software changes made to the AMI will result in a new hash being generated.

The following actions will result in a change to the reference measurements in the NitroTPM Attestation Document:
+ Stopping and starting an instance launched with an Attestable AMI
+ Performing a root volume replacement with a different AMI

If you perform any of these actions, you must then update your attestation service with the new reference measurements. For example, you must update your KMS key policy to the new reference measurements if you are using AWS KMS for attestation.

An instance retains its NitroTPM key material for the entire instance lifecycle, and persists through stop/starts and root volume replacement operations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

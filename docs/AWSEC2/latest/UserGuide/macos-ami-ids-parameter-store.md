---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-ids-parameter-store.html
---

# Retrieve macOS AMI IDs using AWS Systems Manager Parameter Store API
<a name="macos-ami-ids-parameter-store"></a>

You must specify an AMI when you launch an instance. An AMI is specific to an AWS Region, operating system, and processor architecture. You can view all of the macOS AMIs in an AWS Region and retrieve the latest macOS AMI by querying the AWS Systems Manager Parameter Store API. Using these public parameters, you don't need to manually look up macOS AMI IDs. Public parameters are available for both x86 and ARM64 macOS AMIs, and can be integrated with your existing AWS CloudFormation templates.

**Required permissions**
To perform this action, the [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts) must have permissions to call the `ssm:GetParameter` API action.

**To view a list of all macOS AMIs in the current AWS Region using the AWS CLI**
Use the following [get-parameters-by-path](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters-by-path.html) command to view a list of all macOS AMIs in the current Region.

```
aws ssm get-parameters-by-path --path /aws/service/ec2-macos --recursive --query "Parameters[].Name"
```

**To retrieve the AMI ID of the latest major macOS AMI using the AWS CLI**
Use the following [get-parameter](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameter.html) command with the sub-parameter `image_id`. In the following example, replace `sonoma` with a macOS supported major version, `x86_64_mac` with the processor, and `region-code` with a supported AWS Region for which you want the latest macOS AMI ID.

```
aws ssm get-parameter --name /aws/service/ec2-macos/{{sonoma}}/{{x86_64_mac}}/latest/image_id --region {{region-code}}
```

For more information, see [Calling AMI public parameters for macOS](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-ami.html#public-parameters-ami-macos) in the *AWS Systems Manager User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

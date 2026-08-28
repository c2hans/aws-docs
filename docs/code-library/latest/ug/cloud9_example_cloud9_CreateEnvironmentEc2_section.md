---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloud9_example_cloud9_CreateEnvironmentEc2_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateEnvironmentEc2` with a CLI
<a name="cloud9_example_cloud9_CreateEnvironmentEc2_section"></a>

The following code examples show how to use `CreateEnvironmentEc2`.

------
#### [ CLI ]

**AWS CLI**
**To create an AWS Cloud9 EC2 development environment**
This following `create-environment-ec2` example creates an AWS Cloud9 development environment with the specified settings, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.

```
aws cloud9 create-environment-ec2 \
    --name {{my-demo-env}} \
    --description {{"My demonstration development environment."}} \
    --instance-type {{t2.micro}} --image-id {{amazonlinux-2023-x86_64}} \
    --subnet-id {{subnet-1fab8aEX}} \
    --automatic-stop-time-minutes {{60}} \
    --owner-arn {{arn:aws:iam::123456789012:user/MyDemoUser}}
```
Output:

```
{
    "environmentId": "8a34f51ce1e04a08882f1e811bd706EX"
}
```
For more information, see [Creating an EC2 Environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html) in the *AWS Cloud9 User Guide*.
+  For API details, see [CreateEnvironmentEc2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-ec2.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates an AWS Cloud9 development environment with the specified settings, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.**

```
New-C9EnvironmentEC2 -Name my-demo-env -AutomaticStopTimeMinutes 60 -Description "My demonstration development environment." -InstanceType t2.micro -OwnerArn arn:aws:iam::123456789012:user/MyDemoUser -SubnetId subnet-d43a46EX
```
**Output:**

```
ffd88420d4824eeeaeaa8a04bfde8cEX
```
+  For API details, see [CreateEnvironmentEc2](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates an AWS Cloud9 development environment with the specified settings, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.**

```
New-C9EnvironmentEC2 -Name my-demo-env -AutomaticStopTimeMinutes 60 -Description "My demonstration development environment." -InstanceType t2.micro -OwnerArn arn:aws:iam::123456789012:user/MyDemoUser -SubnetId subnet-d43a46EX
```
**Output:**

```
ffd88420d4824eeeaeaa8a04bfde8cEX
```
+  For API details, see [CreateEnvironmentEc2](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_ec2-instance-connect_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon EC2 Instance Connect examples using AWS CLI
<a name="cli_2_ec2-instance-connect_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon EC2 Instance Connect.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `send-ssh-public-key`
<a name="ec2-instance-connect_SendSshPublicKey_cli_2_topic"></a>

The following code example shows how to use `send-ssh-public-key`.

**AWS CLI**
**To send a an SSH public key to an instance**
The following `send-ssh-public-key` example sends the specified SSH public key to the specified instance. The key is used to authenticate the specified user.

```
aws ec2-instance-connect send-ssh-public-key \
    --instance-id {{i-1234567890abcdef0}} \
    --instance-os-user {{ec2-user}} \
    --availability-zone {{us-east-2b}} \
    --ssh-public-key {{file://path/my-rsa-key.pub}}
```
This command produces no output.
+  For API details, see [SendSshPublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2-instance-connect/send-ssh-public-key.html) in *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

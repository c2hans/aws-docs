---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/console-managed-iam-roles-edit.html
---

# Edit IAM role from console
<a name="console-managed-iam-roles-edit"></a>

When you edit a Firehose stream, Firehose updates the corresponding permission policy accordingly to reflect the configuration and permission changes.

For example, when you edit the Firehose stream and enable **Transform source records with AWS Lambda** feature using the latest version of Lambda function as `exampleLambdaFunction`, you get the following policy statement in the permission policy.

```
{
  "Sid": "lambdaProcessing",
  "Effect": "Allow",
  "Action": [
    "lambda:InvokeFunction",
    "lambda:GetFunctionConfiguration"
  ],
  "Resource": "{{arn:aws:}}lambda:{{us-east-1}}:{{123456789012}}:function:exampleLambdaFunction:$LATEST"
}
```

**Important**
A console-managed IAM role is designed to be autonomous. We don't recommend that you modify the permission policy or trust policy outside of the console.

## Steps to edit IAM role from console
<a name="console-manage-iam-roles-edit-stream"></a>

1. Open the Firehose console at [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/).

1. Choose **Firehose streams** and choose the name of a Firehose stream you want to update.

1. On the **Configuration** tab, in the **Server access** section, choose **Edit**.

1. Update the IAM role option.
**Note**
By default, the console always updates an IAM role with the pattern *service-role* in its ARN. When you choose the existing IAM role option, make sure to select an IAM role without the *service-role* string in its ARN so that console doesn’t make any changes to it.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

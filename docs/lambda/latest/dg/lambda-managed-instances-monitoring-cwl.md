---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-monitoring-cwl.html
---

# Sending capacity provider system logs to CloudWatch Logs
<a name="lambda-managed-instances-monitoring-cwl"></a>

By default, Lambda automatically captures system logs for your capacity provider and sends them to CloudWatch Logs, provided your capacity provider's [operator role](lambda-managed-instances-operator-role.md) has the necessary permissions. These logs are stored in a log group named `/aws/lambda/capacity-provider/{{<capacity-provider-name>}}`. If needed, you can configure your capacity provider to send logs to a different log group using the Lambda console, AWS CLI, or Lambda API. For more information, see [Configuring CloudWatch log groups](lambda-managed-instances-cwl-configure.md).

You can view logs for your capacity provider using the Lambda console, the CloudWatch console, the AWS Command Line Interface (AWS CLI), or the CloudWatch API. For more information, see [Viewing CloudWatch logs for capacity providers](lambda-managed-instances-cwl-view-logs.md).

## Required IAM permissions
<a name="lambda-managed-instances-cwl-permissions"></a>

Your capacity provider's [operator role](lambda-managed-instances-operator-role.md) needs the following permissions to upload logs to CloudWatch Logs:
+ `logs:CreateLogGroup`
+ `logs:CreateLogStream`
+ `logs:PutLogEvents`

To learn more, see [Using identity-based policies (IAM policies) for CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.html) in the *Amazon CloudWatch User Guide*.

You can add these CloudWatch Logs permissions using the `AWSLambdaManagedEC2ResourceOperator` AWS managed policy provided by Lambda. To add this policy to your role, run the following command:

```
aws iam attach-role-policy --role-name {{your-role}} --policy-arn arn:aws:iam::aws:policy/AWSLambdaManagedEC2ResourceOperator
```

For more information, see [Lambda operator role for Lambda Managed Instances](lambda-managed-instances-operator-role.md).

**Important**
If the operator role doesn't have the required permissions, Lambda does not deliver system logs and does not return an error. Make sure that your operator role has the correct permissions to avoid silent log delivery failures.

## Pricing
<a name="lambda-managed-instances-cwl-pricing"></a>

There is no additional charge for using capacity provider system logs; however, standard CloudWatch Logs charges apply. For more information, see [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

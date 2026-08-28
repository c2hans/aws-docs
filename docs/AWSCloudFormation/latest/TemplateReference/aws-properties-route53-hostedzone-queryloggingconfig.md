---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-hostedzone-queryloggingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HostedZone QueryLoggingConfig
<a name="aws-properties-route53-hostedzone-queryloggingconfig"></a>

A complex type that contains information about a configuration for DNS query logging.

## Syntax
<a name="aws-properties-route53-hostedzone-queryloggingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-hostedzone-queryloggingconfig-syntax.json"></a>

```
{
  "[CloudWatchLogsLogGroupArn](#cfn-route53-hostedzone-queryloggingconfig-cloudwatchlogsloggrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-hostedzone-queryloggingconfig-syntax.yaml"></a>

```
  [CloudWatchLogsLogGroupArn](#cfn-route53-hostedzone-queryloggingconfig-cloudwatchlogsloggrouparn): {{String}}
```

## Properties
<a name="aws-properties-route53-hostedzone-queryloggingconfig-properties"></a>

`CloudWatchLogsLogGroupArn`  <a name="cfn-route53-hostedzone-queryloggingconfig-cloudwatchlogsloggrouparn"></a>
The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-route53-hostedzone-queryloggingconfig--seealso"></a>
+ [Return values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#aws-resource-route53-hostedzone-return-values) in the topic [AWS::Route53::HostedZone](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html)
+ [QueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_QueryLoggingConfig.html) in the *Amazon Route 53 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

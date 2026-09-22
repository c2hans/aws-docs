---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-queryloggingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::QueryLoggingConfig
<a name="aws-resource-route53-queryloggingconfig"></a>

A complex type that contains information about a configuration for DNS query logging.

## Syntax
<a name="aws-resource-route53-queryloggingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53-queryloggingconfig-syntax.json"></a>

```
{
  "Type" : "AWS::Route53::QueryLoggingConfig",
  "Properties" : {
      "[CloudWatchLogsLogGroupArn](#cfn-route53-queryloggingconfig-cloudwatchlogsloggrouparn)" : {{String}},
      "[HostedZoneId](#cfn-route53-queryloggingconfig-hostedzoneid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-route53-queryloggingconfig-syntax.yaml"></a>

```
Type: AWS::Route53::QueryLoggingConfig
Properties:
  [CloudWatchLogsLogGroupArn](#cfn-route53-queryloggingconfig-cloudwatchlogsloggrouparn): {{String}}
  [HostedZoneId](#cfn-route53-queryloggingconfig-hostedzoneid): {{String}}
```

## Properties
<a name="aws-resource-route53-queryloggingconfig-properties"></a>

`CloudWatchLogsLogGroupArn`  <a name="cfn-route53-queryloggingconfig-cloudwatchlogsloggrouparn"></a>
The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostedZoneId`  <a name="cfn-route53-queryloggingconfig-hostedzoneid"></a>
The ID of the hosted zone that CloudWatch Logs is logging queries for.
*Required*: Yes
*Type*: String
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-route53-queryloggingconfig-return-values"></a>

### Ref
<a name="aws-resource-route53-queryloggingconfig-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53-queryloggingconfig-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53-queryloggingconfig-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
The ID for a configuration for DNS query logging.

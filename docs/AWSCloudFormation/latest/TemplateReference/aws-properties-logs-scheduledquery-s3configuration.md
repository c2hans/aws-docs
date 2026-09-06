---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-scheduledquery-s3configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::ScheduledQuery S3Configuration
<a name="aws-properties-logs-scheduledquery-s3configuration"></a>

Configuration for Amazon S3 destination where scheduled query results are delivered.

## Syntax
<a name="aws-properties-logs-scheduledquery-s3configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-scheduledquery-s3configuration-syntax.json"></a>

```
{
  "[DestinationIdentifier](#cfn-logs-scheduledquery-s3configuration-destinationidentifier)" : {{String}},
  "[RoleArn](#cfn-logs-scheduledquery-s3configuration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-scheduledquery-s3configuration-syntax.yaml"></a>

```
  [DestinationIdentifier](#cfn-logs-scheduledquery-s3configuration-destinationidentifier): {{String}}
  [RoleArn](#cfn-logs-scheduledquery-s3configuration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-logs-scheduledquery-s3configuration-properties"></a>

`DestinationIdentifier`  <a name="cfn-logs-scheduledquery-s3configuration-destinationidentifier"></a>
The Amazon S3 URI where query results are delivered. Must be a valid S3 URI format.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-logs-scheduledquery-s3configuration-rolearn"></a>
The ARN of the IAM role that grants permissions to write query results to the specified Amazon S3 destination.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

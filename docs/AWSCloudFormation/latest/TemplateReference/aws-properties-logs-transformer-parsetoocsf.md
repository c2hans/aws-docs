---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-parsetoocsf.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer ParseToOCSF
<a name="aws-properties-logs-transformer-parsetoocsf"></a>

This processor converts logs into [Open Cybersecurity Schema Framework (OCSF)](https://ocsf.io) events.

For more information about this processor including examples, see [parseToOCSF](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseToOCSF) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-parsetoocsf-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-parsetoocsf-syntax.json"></a>

```
{
  "[EventSource](#cfn-logs-transformer-parsetoocsf-eventsource)" : {{String}},
  "[MappingVersion](#cfn-logs-transformer-parsetoocsf-mappingversion)" : {{String}},
  "[OcsfVersion](#cfn-logs-transformer-parsetoocsf-ocsfversion)" : {{String}},
  "[Source](#cfn-logs-transformer-parsetoocsf-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-parsetoocsf-syntax.yaml"></a>

```
  [EventSource](#cfn-logs-transformer-parsetoocsf-eventsource): {{String}}
  [MappingVersion](#cfn-logs-transformer-parsetoocsf-mappingversion): {{String}}
  [OcsfVersion](#cfn-logs-transformer-parsetoocsf-ocsfversion): {{String}}
  [Source](#cfn-logs-transformer-parsetoocsf-source): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-parsetoocsf-properties"></a>

`EventSource`  <a name="cfn-logs-transformer-parsetoocsf-eventsource"></a>
Specify the service or process that produces the log events that will be converted with this processor.
*Required*: Yes
*Type*: String
*Allowed values*: `CloudTrail | Route53Resolver | VPCFlow | EKSAudit | AWSWAF`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MappingVersion`  <a name="cfn-logs-transformer-parsetoocsf-mappingversion"></a>
The version of the OCSF mapping to use for parsing log data.
*Required*: No
*Type*: String
*Pattern*: `^v\d+\.\d+(\.\d+)?$`
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OcsfVersion`  <a name="cfn-logs-transformer-parsetoocsf-ocsfversion"></a>
Specify which version of the OCSF schema to use for the transformed log events.
*Required*: Yes
*Type*: String
*Allowed values*: `V1.1 | V1.5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-parsetoocsf-source"></a>
The path to the field in the log event that you want to parse. If you omit this value, the whole log message is parsed.
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

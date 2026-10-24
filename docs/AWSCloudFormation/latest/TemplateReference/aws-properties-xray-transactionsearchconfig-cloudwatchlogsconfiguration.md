---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-xray-transactionsearchconfig-cloudwatchlogsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::XRay::TransactionSearchConfig CloudWatchLogsConfiguration
<a name="aws-properties-xray-transactionsearchconfig-cloudwatchlogsconfiguration"></a>

<a name="aws-properties-xray-transactionsearchconfig-cloudwatchlogsconfiguration-description"></a>The `CloudWatchLogsConfiguration` property type specifies Property description not available. for an [AWS::XRay::TransactionSearchConfig](aws-resource-xray-transactionsearchconfig.md).

## Syntax
<a name="aws-properties-xray-transactionsearchconfig-cloudwatchlogsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-xray-transactionsearchconfig-cloudwatchlogsconfiguration-syntax.json"></a>

```
{
  "[SpansLogGroupKmsKeyId](#cfn-xray-transactionsearchconfig-cloudwatchlogsconfiguration-spansloggroupkmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-xray-transactionsearchconfig-cloudwatchlogsconfiguration-syntax.yaml"></a>

```
  [SpansLogGroupKmsKeyId](#cfn-xray-transactionsearchconfig-cloudwatchlogsconfiguration-spansloggroupkmskeyid): {{String}}
```

## Properties
<a name="aws-properties-xray-transactionsearchconfig-cloudwatchlogsconfiguration-properties"></a>

`SpansLogGroupKmsKeyId`  <a name="cfn-xray-transactionsearchconfig-cloudwatchlogsconfiguration-spansloggroupkmskeyid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]*:kms:[a-z0-9-]+:\d{12}:key/[a-zA-Z0-9-]+$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

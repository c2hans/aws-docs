---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-function-awsservicerequestconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Function AwsServiceRequestConfiguration
<a name="aws-properties-mediatailor-function-awsservicerequestconfiguration"></a>

<a name="aws-properties-mediatailor-function-awsservicerequestconfiguration-description"></a>The `AwsServiceRequestConfiguration` property type specifies Property description not available. for an [AWS::MediaTailor::Function](aws-resource-mediatailor-function.md).

## Syntax
<a name="aws-properties-mediatailor-function-awsservicerequestconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-function-awsservicerequestconfiguration-syntax.json"></a>

```
{
  "[Body](#cfn-mediatailor-function-awsservicerequestconfiguration-body)" : {{String}},
  "[Headers](#cfn-mediatailor-function-awsservicerequestconfiguration-headers)" : {{{{{Key}}: {{Value}}, ...}}},
  "[MethodType](#cfn-mediatailor-function-awsservicerequestconfiguration-methodtype)" : {{String}},
  "[Output](#cfn-mediatailor-function-awsservicerequestconfiguration-output)" : {{{{{Key}}: {{Value}}, ...}}},
  "[RequestTimeoutMilliseconds](#cfn-mediatailor-function-awsservicerequestconfiguration-requesttimeoutmilliseconds)" : {{Integer}},
  "[Runtime](#cfn-mediatailor-function-awsservicerequestconfiguration-runtime)" : {{String}},
  "[TargetRegion](#cfn-mediatailor-function-awsservicerequestconfiguration-targetregion)" : {{String}},
  "[TargetService](#cfn-mediatailor-function-awsservicerequestconfiguration-targetservice)" : {{String}},
  "[Url](#cfn-mediatailor-function-awsservicerequestconfiguration-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-function-awsservicerequestconfiguration-syntax.yaml"></a>

```
  [Body](#cfn-mediatailor-function-awsservicerequestconfiguration-body): {{String}}
  [Headers](#cfn-mediatailor-function-awsservicerequestconfiguration-headers): {{
    {{Key}}: {{Value}}}}
  [MethodType](#cfn-mediatailor-function-awsservicerequestconfiguration-methodtype): {{String}}
  [Output](#cfn-mediatailor-function-awsservicerequestconfiguration-output): {{
    {{Key}}: {{Value}}}}
  [RequestTimeoutMilliseconds](#cfn-mediatailor-function-awsservicerequestconfiguration-requesttimeoutmilliseconds): {{Integer}}
  [Runtime](#cfn-mediatailor-function-awsservicerequestconfiguration-runtime): {{String}}
  [TargetRegion](#cfn-mediatailor-function-awsservicerequestconfiguration-targetregion): {{String}}
  [TargetService](#cfn-mediatailor-function-awsservicerequestconfiguration-targetservice): {{String}}
  [Url](#cfn-mediatailor-function-awsservicerequestconfiguration-url): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-function-awsservicerequestconfiguration-properties"></a>

`Body`  <a name="cfn-mediatailor-function-awsservicerequestconfiguration-body"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Headers`  <a name="cfn-mediatailor-function-awsservicerequestconfiguration-headers"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MethodType`  <a name="cfn-mediatailor-function-awsservicerequestconfiguration-methodtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `GET | POST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Output`  <a name="cfn-mediatailor-function-awsservicerequestconfiguration-output"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequestTimeoutMilliseconds`  <a name="cfn-mediatailor-function-awsservicerequestconfiguration-requesttimeoutmilliseconds"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `100`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-mediatailor-function-awsservicerequestconfiguration-runtime"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `JSONATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRegion`  <a name="cfn-mediatailor-function-awsservicerequestconfiguration-targetregion"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetService`  <a name="cfn-mediatailor-function-awsservicerequestconfiguration-targetservice"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z0-9-]+`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-mediatailor-function-awsservicerequestconfiguration-url"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

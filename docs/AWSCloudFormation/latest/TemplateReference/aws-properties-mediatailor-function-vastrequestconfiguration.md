---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-function-vastrequestconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Function VastRequestConfiguration
<a name="aws-properties-mediatailor-function-vastrequestconfiguration"></a>

<a name="aws-properties-mediatailor-function-vastrequestconfiguration-description"></a>The `VastRequestConfiguration` property type specifies Property description not available. for an [AWS::MediaTailor::Function](aws-resource-mediatailor-function.md).

## Syntax
<a name="aws-properties-mediatailor-function-vastrequestconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-function-vastrequestconfiguration-syntax.json"></a>

```
{
  "[Body](#cfn-mediatailor-function-vastrequestconfiguration-body)" : {{String}},
  "[Headers](#cfn-mediatailor-function-vastrequestconfiguration-headers)" : {{{{{Key}}: {{Value}}, ...}}},
  "[MethodType](#cfn-mediatailor-function-vastrequestconfiguration-methodtype)" : {{String}},
  "[Output](#cfn-mediatailor-function-vastrequestconfiguration-output)" : {{{{{Key}}: {{Value}}, ...}}},
  "[RequestTimeoutMilliseconds](#cfn-mediatailor-function-vastrequestconfiguration-requesttimeoutmilliseconds)" : {{Integer}},
  "[Runtime](#cfn-mediatailor-function-vastrequestconfiguration-runtime)" : {{String}},
  "[Url](#cfn-mediatailor-function-vastrequestconfiguration-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-function-vastrequestconfiguration-syntax.yaml"></a>

```
  [Body](#cfn-mediatailor-function-vastrequestconfiguration-body): {{String}}
  [Headers](#cfn-mediatailor-function-vastrequestconfiguration-headers): {{
    {{Key}}: {{Value}}}}
  [MethodType](#cfn-mediatailor-function-vastrequestconfiguration-methodtype): {{String}}
  [Output](#cfn-mediatailor-function-vastrequestconfiguration-output): {{
    {{Key}}: {{Value}}}}
  [RequestTimeoutMilliseconds](#cfn-mediatailor-function-vastrequestconfiguration-requesttimeoutmilliseconds): {{Integer}}
  [Runtime](#cfn-mediatailor-function-vastrequestconfiguration-runtime): {{String}}
  [Url](#cfn-mediatailor-function-vastrequestconfiguration-url): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-function-vastrequestconfiguration-properties"></a>

`Body`  <a name="cfn-mediatailor-function-vastrequestconfiguration-body"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Headers`  <a name="cfn-mediatailor-function-vastrequestconfiguration-headers"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MethodType`  <a name="cfn-mediatailor-function-vastrequestconfiguration-methodtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `GET | POST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Output`  <a name="cfn-mediatailor-function-vastrequestconfiguration-output"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequestTimeoutMilliseconds`  <a name="cfn-mediatailor-function-vastrequestconfiguration-requesttimeoutmilliseconds"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `100`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-mediatailor-function-vastrequestconfiguration-runtime"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `JSONATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-mediatailor-function-vastrequestconfiguration-url"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

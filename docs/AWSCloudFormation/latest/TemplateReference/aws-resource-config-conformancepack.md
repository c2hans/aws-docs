---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-conformancepack.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConformancePack

A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed in an account and a region. ConformancePack creates a service linked role in your account. The service linked role is created only when the role does not exist in your account.

## Syntax
<a name="aws-resource-config-conformancepack-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-config-conformancepack-syntax.json"></a>

```json
{
  "Type" : "AWS::Config::ConformancePack",
  "Properties" : {
      "[ConformancePackInputParameters](#cfn-config-conformancepack-conformancepackinputparameters)" : {{[ ConformancePackInputParameter, ... ]}},
      "[ConformancePackName](#cfn-config-conformancepack-conformancepackname)" : {{String}},
      "[DeliveryS3Bucket](#cfn-config-conformancepack-deliverys3bucket)" : {{String}},
      "[DeliveryS3KeyPrefix](#cfn-config-conformancepack-deliverys3keyprefix)" : {{String}},
      "[Scope](#cfn-config-conformancepack-scope)" : {{Scope}},
      "[Source](#cfn-config-conformancepack-source)" : {{Source}},
      "[Tags](#cfn-config-conformancepack-tags)" : {{[ Tag, ... ]}},
      "[TemplateBody](#cfn-config-conformancepack-templatebody)" : {{String}},
      "[TemplateS3Uri](#cfn-config-conformancepack-templates3uri)" : {{String}},
      "[TemplateSSMDocumentDetails](#cfn-config-conformancepack-templatessmdocumentdetails)" : {{TemplateSSMDocumentDetails}}
    }
}
```

### YAML
<a name="aws-resource-config-conformancepack-syntax.yaml"></a>

```yaml
Type: AWS::Config::ConformancePack
Properties:
  [ConformancePackInputParameters](#cfn-config-conformancepack-conformancepackinputparameters): {{
    - ConformancePackInputParameter}}
  [ConformancePackName](#cfn-config-conformancepack-conformancepackname): {{String}}
  [DeliveryS3Bucket](#cfn-config-conformancepack-deliverys3bucket): {{String}}
  [DeliveryS3KeyPrefix](#cfn-config-conformancepack-deliverys3keyprefix): {{String}}
  [Scope](#cfn-config-conformancepack-scope): {{
    Scope}}
  [Source](#cfn-config-conformancepack-source): {{
    Source}}
  [Tags](#cfn-config-conformancepack-tags): {{
    - Tag}}
  [TemplateBody](#cfn-config-conformancepack-templatebody): {{String}}
  [TemplateS3Uri](#cfn-config-conformancepack-templates3uri): {{String}}
  [TemplateSSMDocumentDetails](#cfn-config-conformancepack-templatessmdocumentdetails): {{
    TemplateSSMDocumentDetails}}
```

## Properties
<a name="aws-resource-config-conformancepack-properties"></a>

`ConformancePackInputParameters`  <a name="cfn-config-conformancepack-conformancepackinputparameters"></a>
A list of ConformancePackInputParameter objects.
*Required*: No
*Type*: Array of [ConformancePackInputParameter](aws-properties-config-conformancepack-conformancepackinputparameter.md)
*Minimum*: `0`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConformancePackName`  <a name="cfn-config-conformancepack-conformancepackname"></a>
Name of the conformance pack you want to create.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z][-a-zA-Z0-9]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeliveryS3Bucket`  <a name="cfn-config-conformancepack-deliverys3bucket"></a>
The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeliveryS3KeyPrefix`  <a name="cfn-config-conformancepack-deliverys3keyprefix"></a>
The prefix for the Amazon S3 bucket.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-config-conformancepack-scope"></a>
An object of type `ConformancePackScope`, which contains the tag key and optional tag value that defines which resources trigger an evaluation for the AWS Config rules in the managed conformance pack.
Managed conformance packs with a scope populate this field. Custom conformance packs leave it empty.
*Required*: No
*Type*: [Scope](aws-properties-config-conformancepack-scope.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-config-conformancepack-source"></a>
Contains the identifier of the managed conformance pack that AWS Config deploys in your account.
This field applies only to managed conformance packs. Custom conformance packs leave it empty.
*Required*: No
*Type*: [Source](aws-properties-config-conformancepack-source.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-config-conformancepack-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-config-conformancepack-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateBody`  <a name="cfn-config-conformancepack-templatebody"></a>
A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
You can only use a YAML template with two resource types: config rule (`AWS::Config::ConfigRule`) and a remediation action (`AWS::Config::RemediationConfiguration`).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateS3Uri`  <a name="cfn-config-conformancepack-templates3uri"></a>
Location of file containing the template body (s3://bucketname/prefix). The uri must point to the conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket.
You must have access to read Amazon S3 bucket.
*Required*: No
*Type*: String
*Pattern*: `s3://.*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateSSMDocumentDetails`  <a name="cfn-config-conformancepack-templatessmdocumentdetails"></a>
An object that contains the name or Amazon Resource Name (ARN) of the AWS Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.
*Required*: No
*Type*: [TemplateSSMDocumentDetails](aws-properties-config-conformancepack-templatessmdocumentdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-config-conformancepack-return-values"></a>

### Ref
<a name="aws-resource-config-conformancepack-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the conformance pack.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-config-conformancepack-return-values-fn--getatt"></a>

####
<a name="aws-resource-config-conformancepack-return-values-fn--getatt-fn--getatt"></a>

`ConformancePackArn`  <a name="ConformancePackArn-fn::getatt"></a>
Amazon Resource Name (ARN) of the conformance pack.

`Type`  <a name="Type-fn::getatt"></a>
The type of the conformance pack. Valid values:
+ `CUSTOM` – A custom conformance pack.
+ `MANAGED` – A managed conformance pack.

## Examples
<a name="aws-resource-config-conformancepack--examples"></a>

### Conformance Pack
<a name="aws-resource-config-conformancepack--examples--Conformance_Pack"></a>

The following example creates a conformance pack.

#### JSON
<a name="aws-resource-config-conformancepack--examples--Conformance_Pack--json"></a>

```json
{
    "Resources": {
        "ConformancePack": {
            "Type": "AWS::Config::ConformancePack",
            "Properties": {
                "ConformancePackName": "ConformancePackName",
                "DeliveryS3Bucket": "DeliveryS3Bucket",
                "TemplateS3Uri": "s3://bucketname/prefix"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-config-conformancepack--examples--Conformance_Pack--yaml"></a>

```yaml
---
AWSTemplateFormatVersion: 2010-09-09
Resources:
    CloudFormationCanaryPack:
        Type: AWS::Config::ConformancePack
        Properties:
          ConformancePackName: ConformancePackName
          DeliveryS3Bucket: DeliveryS3Bucket
          TemplateS3Uri: s3://bucketname/prefix
```

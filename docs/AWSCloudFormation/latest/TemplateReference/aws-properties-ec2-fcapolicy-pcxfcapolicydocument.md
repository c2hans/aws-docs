---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-fcapolicy-pcxfcapolicydocument.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FcaPolicy PcxFcaPolicyDocument
<a name="aws-properties-ec2-fcapolicy-pcxfcapolicydocument"></a>

<a name="aws-properties-ec2-fcapolicy-pcxfcapolicydocument-description"></a>The `PcxFcaPolicyDocument` property type specifies Property description not available. for an [AWS::EC2::FcaPolicy](aws-resource-ec2-fcapolicy.md).

## Syntax
<a name="aws-properties-ec2-fcapolicy-pcxfcapolicydocument-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-fcapolicy-pcxfcapolicydocument-syntax.json"></a>

```
{
  "[CidrRangeSpecifications](#cfn-ec2-fcapolicy-pcxfcapolicydocument-cidrrangespecifications)" : {{CidrRangeSpecifications}},
  "[Dimensions](#cfn-ec2-fcapolicy-pcxfcapolicydocument-dimensions)" : {{[ String, ... ]}},
  "[ReportingGranularity](#cfn-ec2-fcapolicy-pcxfcapolicydocument-reportinggranularity)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-fcapolicy-pcxfcapolicydocument-syntax.yaml"></a>

```
  [CidrRangeSpecifications](#cfn-ec2-fcapolicy-pcxfcapolicydocument-cidrrangespecifications): {{
    CidrRangeSpecifications}}
  [Dimensions](#cfn-ec2-fcapolicy-pcxfcapolicydocument-dimensions): {{
    - String}}
  [ReportingGranularity](#cfn-ec2-fcapolicy-pcxfcapolicydocument-reportinggranularity): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-fcapolicy-pcxfcapolicydocument-properties"></a>

`CidrRangeSpecifications`  <a name="cfn-ec2-fcapolicy-pcxfcapolicydocument-cidrrangespecifications"></a>
Property description not available.
*Required*: No
*Type*: [CidrRangeSpecifications](aws-properties-ec2-fcapolicy-cidrrangespecifications.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dimensions`  <a name="cfn-ec2-fcapolicy-pcxfcapolicydocument-dimensions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `data-transfer | data-processing`
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReportingGranularity`  <a name="cfn-ec2-fcapolicy-pcxfcapolicydocument-reportinggranularity"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `eni | ec2 | subnet | vpc | account | peering-id | cidr`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

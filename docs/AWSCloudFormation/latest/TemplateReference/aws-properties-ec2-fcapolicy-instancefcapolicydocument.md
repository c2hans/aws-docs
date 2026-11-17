---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-fcapolicy-instancefcapolicydocument.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FcaPolicy InstanceFcaPolicyDocument
<a name="aws-properties-ec2-fcapolicy-instancefcapolicydocument"></a>

Specifies how shared network costs are allocated and reported for an EC2 instance.

## Syntax
<a name="aws-properties-ec2-fcapolicy-instancefcapolicydocument-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-fcapolicy-instancefcapolicydocument-syntax.json"></a>

```
{
  "[CidrRangeSpecifications](#cfn-ec2-fcapolicy-instancefcapolicydocument-cidrrangespecifications)" : {{CidrRangeSpecifications}},
  "[Dimensions](#cfn-ec2-fcapolicy-instancefcapolicydocument-dimensions)" : {{[ String, ... ]}},
  "[ReportingGranularity](#cfn-ec2-fcapolicy-instancefcapolicydocument-reportinggranularity)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-fcapolicy-instancefcapolicydocument-syntax.yaml"></a>

```
  [CidrRangeSpecifications](#cfn-ec2-fcapolicy-instancefcapolicydocument-cidrrangespecifications): {{
    CidrRangeSpecifications}}
  [Dimensions](#cfn-ec2-fcapolicy-instancefcapolicydocument-dimensions): {{
    - String}}
  [ReportingGranularity](#cfn-ec2-fcapolicy-instancefcapolicydocument-reportinggranularity): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-fcapolicy-instancefcapolicydocument-properties"></a>

`CidrRangeSpecifications`  <a name="cfn-ec2-fcapolicy-instancefcapolicydocument-cidrrangespecifications"></a>
The CIDR range specifications. Specify this property when `ReportingGranularity` is `cidr`.
*Required*: No
*Type*: [CidrRangeSpecifications](aws-properties-ec2-fcapolicy-cidrrangespecifications.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dimensions`  <a name="cfn-ec2-fcapolicy-instancefcapolicydocument-dimensions"></a>
The cost dimensions to allocate. You can specify one or both values.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `data-transfer | data-processing`
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReportingGranularity`  <a name="cfn-ec2-fcapolicy-instancefcapolicydocument-reportinggranularity"></a>
The granularity at which costs are reported. This list contains exactly one value.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `eni | ec2 | subnet | vpc | account | peering-id | cidr`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

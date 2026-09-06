---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fms-policy-icmptypecode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::Policy IcmpTypeCode
<a name="aws-properties-fms-policy-icmptypecode"></a>

ICMP protocol: The ICMP type and code.

## Syntax
<a name="aws-properties-fms-policy-icmptypecode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fms-policy-icmptypecode-syntax.json"></a>

```
{
  "[Code](#cfn-fms-policy-icmptypecode-code)" : {{Integer}},
  "[Type](#cfn-fms-policy-icmptypecode-type)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-fms-policy-icmptypecode-syntax.yaml"></a>

```
  [Code](#cfn-fms-policy-icmptypecode-code): {{Integer}}
  [Type](#cfn-fms-policy-icmptypecode-type): {{Integer}}
```

## Properties
<a name="aws-properties-fms-policy-icmptypecode-properties"></a>

`Code`  <a name="cfn-fms-policy-icmptypecode-code"></a>
ICMP code.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-fms-policy-icmptypecode-type"></a>
ICMP type.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

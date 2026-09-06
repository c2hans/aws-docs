---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-legalhold-daterange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::LegalHold DateRange
<a name="aws-properties-backup-legalhold-daterange"></a>

This is a resource filter containing FromDate: DateTime and ToDate: DateTime. Both values are required. Future DateTime values are not permitted.

The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds ((milliseconds are optional). For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

## Syntax
<a name="aws-properties-backup-legalhold-daterange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-legalhold-daterange-syntax.json"></a>

```
{
  "[FromDate](#cfn-backup-legalhold-daterange-fromdate)" : {{String}},
  "[ToDate](#cfn-backup-legalhold-daterange-todate)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-legalhold-daterange-syntax.yaml"></a>

```
  [FromDate](#cfn-backup-legalhold-daterange-fromdate): {{String}}
  [ToDate](#cfn-backup-legalhold-daterange-todate): {{String}}
```

## Properties
<a name="aws-properties-backup-legalhold-daterange-properties"></a>

`FromDate`  <a name="cfn-backup-legalhold-daterange-fromdate"></a>
This value is the beginning date, inclusive.
The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds (milliseconds are optional).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ToDate`  <a name="cfn-backup-legalhold-daterange-todate"></a>
This value is the end date, inclusive.
The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds (milliseconds are optional).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

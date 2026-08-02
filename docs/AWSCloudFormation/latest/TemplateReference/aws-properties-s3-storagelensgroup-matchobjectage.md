---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelensgroup-matchobjectage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLensGroup MatchObjectAge
<a name="aws-properties-s3-storagelensgroup-matchobjectage"></a>

This resource contains `DaysGreaterThan` and `DaysLessThan` to define the object age range (minimum and maximum number of days).

## Syntax
<a name="aws-properties-s3-storagelensgroup-matchobjectage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelensgroup-matchobjectage-syntax.json"></a>

```
{
  "[DaysGreaterThan](#cfn-s3-storagelensgroup-matchobjectage-daysgreaterthan)" : {{Integer}},
  "[DaysLessThan](#cfn-s3-storagelensgroup-matchobjectage-dayslessthan)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3-storagelensgroup-matchobjectage-syntax.yaml"></a>

```
  [DaysGreaterThan](#cfn-s3-storagelensgroup-matchobjectage-daysgreaterthan): {{Integer}}
  [DaysLessThan](#cfn-s3-storagelensgroup-matchobjectage-dayslessthan): {{Integer}}
```

## Properties
<a name="aws-properties-s3-storagelensgroup-matchobjectage-properties"></a>

`DaysGreaterThan`  <a name="cfn-s3-storagelensgroup-matchobjectage-daysgreaterthan"></a>
This property indicates the minimum object age in days.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DaysLessThan`  <a name="cfn-s3-storagelensgroup-matchobjectage-dayslessthan"></a>
This property indicates the maximum object age in days.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

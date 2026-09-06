---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelensgroup-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLensGroup Filter
<a name="aws-properties-s3-storagelensgroup-filter"></a>

This resource sets the criteria for the Storage Lens group data that is displayed. For multiple filter conditions, the `AND` or `OR` logical operator is used.

## Syntax
<a name="aws-properties-s3-storagelensgroup-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelensgroup-filter-syntax.json"></a>

```
{
  "[And](#cfn-s3-storagelensgroup-filter-and)" : {{And}},
  "[MatchAnyPrefix](#cfn-s3-storagelensgroup-filter-matchanyprefix)" : {{[ String, ... ]}},
  "[MatchAnySuffix](#cfn-s3-storagelensgroup-filter-matchanysuffix)" : {{[ String, ... ]}},
  "[MatchAnyTag](#cfn-s3-storagelensgroup-filter-matchanytag)" : {{[ Tag, ... ]}},
  "[MatchObjectAge](#cfn-s3-storagelensgroup-filter-matchobjectage)" : {{MatchObjectAge}},
  "[MatchObjectSize](#cfn-s3-storagelensgroup-filter-matchobjectsize)" : {{MatchObjectSize}},
  "[Or](#cfn-s3-storagelensgroup-filter-or)" : {{Or}}
}
```

### YAML
<a name="aws-properties-s3-storagelensgroup-filter-syntax.yaml"></a>

```
  [And](#cfn-s3-storagelensgroup-filter-and): {{
    And}}
  [MatchAnyPrefix](#cfn-s3-storagelensgroup-filter-matchanyprefix): {{
    - String}}
  [MatchAnySuffix](#cfn-s3-storagelensgroup-filter-matchanysuffix): {{
    - String}}
  [MatchAnyTag](#cfn-s3-storagelensgroup-filter-matchanytag): {{
    - Tag}}
  [MatchObjectAge](#cfn-s3-storagelensgroup-filter-matchobjectage): {{
    MatchObjectAge}}
  [MatchObjectSize](#cfn-s3-storagelensgroup-filter-matchobjectsize): {{
    MatchObjectSize}}
  [Or](#cfn-s3-storagelensgroup-filter-or): {{
    Or}}
```

## Properties
<a name="aws-properties-s3-storagelensgroup-filter-properties"></a>

`And`  <a name="cfn-s3-storagelensgroup-filter-and"></a>
This property contains the `And` logical operator, which allows multiple filter conditions to be joined for more complex comparisons of Storage Lens group data. Objects must match all of the listed filter conditions that are joined by the `And` logical operator. Only one of each filter condition is allowed.
*Required*: No
*Type*: [And](aws-properties-s3-storagelensgroup-and.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchAnyPrefix`  <a name="cfn-s3-storagelensgroup-filter-matchanyprefix"></a>
This property contains a list of prefixes. At least one prefix must be specified. Up to 10 prefixes are allowed.
*Required*: No
*Type*: Array of String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchAnySuffix`  <a name="cfn-s3-storagelensgroup-filter-matchanysuffix"></a>
This property contains a list of suffixes. At least one suffix must be specified. Up to 10 suffixes are allowed.
*Required*: No
*Type*: Array of String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchAnyTag`  <a name="cfn-s3-storagelensgroup-filter-matchanytag"></a>
This property contains the list of S3 object tags. At least one object tag must be specified. Up to 10 object tags are allowed.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3-storagelensgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchObjectAge`  <a name="cfn-s3-storagelensgroup-filter-matchobjectage"></a>
This property contains `DaysGreaterThan` and `DaysLessThan` to define the object age range (minimum and maximum number of days).
*Required*: No
*Type*: [MatchObjectAge](aws-properties-s3-storagelensgroup-matchobjectage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchObjectSize`  <a name="cfn-s3-storagelensgroup-filter-matchobjectsize"></a>
This property contains `BytesGreaterThan` and `BytesLessThan` to define the object size range (minimum and maximum number of Bytes).
*Required*: No
*Type*: [MatchObjectSize](aws-properties-s3-storagelensgroup-matchobjectsize.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Or`  <a name="cfn-s3-storagelensgroup-filter-or"></a>
This property contains the `Or` logical operator, which allows multiple filter conditions to be joined. Objects can match any of the listed filter conditions, which are joined by the `Or` logical operator. Only one of each filter condition is allowed.
*Required*: No
*Type*: [Or](aws-properties-s3-storagelensgroup-or.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

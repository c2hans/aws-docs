---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelensgroup-and.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLensGroup And
<a name="aws-properties-s3-storagelensgroup-and"></a>

This resource is a logical operator that allows multiple filter conditions to be joined for more complex comparisons of Storage Lens group data. Objects must match all of the listed filter conditions that are joined by the `And` logical operator. Only one of each filter condition is allowed.

## Syntax
<a name="aws-properties-s3-storagelensgroup-and-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelensgroup-and-syntax.json"></a>

```
{
  "[MatchAnyPrefix](#cfn-s3-storagelensgroup-and-matchanyprefix)" : {{[ String, ... ]}},
  "[MatchAnySuffix](#cfn-s3-storagelensgroup-and-matchanysuffix)" : {{[ String, ... ]}},
  "[MatchAnyTag](#cfn-s3-storagelensgroup-and-matchanytag)" : {{[ Tag, ... ]}},
  "[MatchObjectAge](#cfn-s3-storagelensgroup-and-matchobjectage)" : {{MatchObjectAge}},
  "[MatchObjectSize](#cfn-s3-storagelensgroup-and-matchobjectsize)" : {{MatchObjectSize}}
}
```

### YAML
<a name="aws-properties-s3-storagelensgroup-and-syntax.yaml"></a>

```
  [MatchAnyPrefix](#cfn-s3-storagelensgroup-and-matchanyprefix): {{
    - String}}
  [MatchAnySuffix](#cfn-s3-storagelensgroup-and-matchanysuffix): {{
    - String}}
  [MatchAnyTag](#cfn-s3-storagelensgroup-and-matchanytag): {{
    - Tag}}
  [MatchObjectAge](#cfn-s3-storagelensgroup-and-matchobjectage): {{
    MatchObjectAge}}
  [MatchObjectSize](#cfn-s3-storagelensgroup-and-matchobjectsize): {{
    MatchObjectSize}}
```

## Properties
<a name="aws-properties-s3-storagelensgroup-and-properties"></a>

`MatchAnyPrefix`  <a name="cfn-s3-storagelensgroup-and-matchanyprefix"></a>
This property contains a list of prefixes. At least one prefix must be specified. Up to 10 prefixes are allowed.
*Required*: No
*Type*: Array of String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchAnySuffix`  <a name="cfn-s3-storagelensgroup-and-matchanysuffix"></a>
This property contains a list of suffixes. At least one suffix must be specified. Up to 10 suffixes are allowed.
*Required*: No
*Type*: Array of String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchAnyTag`  <a name="cfn-s3-storagelensgroup-and-matchanytag"></a>
This property contains the list of object tags. At least one object tag must be specified. Up to 10 object tags are allowed.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3-storagelensgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchObjectAge`  <a name="cfn-s3-storagelensgroup-and-matchobjectage"></a>
This property contains `DaysGreaterThan` and `DaysLessThan` properties to define the object age range (minimum and maximum number of days).
*Required*: No
*Type*: [MatchObjectAge](aws-properties-s3-storagelensgroup-matchobjectage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchObjectSize`  <a name="cfn-s3-storagelensgroup-and-matchobjectsize"></a>
This property contains `BytesGreaterThan` and `BytesLessThan` to define the object size range (minimum and maximum number of Bytes).
*Required*: No
*Type*: [MatchObjectSize](aws-properties-s3-storagelensgroup-matchobjectsize.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelensgroup-or.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLensGroup Or
<a name="aws-properties-s3-storagelensgroup-or"></a>

This resource contains the `Or` logical operator, which allows multiple filter conditions to be joined for more complex comparisons of Storage Lens group data. Objects can match any of the listed filter conditions that are joined by the `Or` logical operator. Only one of each filter condition is allowed.

## Syntax
<a name="aws-properties-s3-storagelensgroup-or-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelensgroup-or-syntax.json"></a>

```
{
  "[MatchAnyPrefix](#cfn-s3-storagelensgroup-or-matchanyprefix)" : {{[ String, ... ]}},
  "[MatchAnySuffix](#cfn-s3-storagelensgroup-or-matchanysuffix)" : {{[ String, ... ]}},
  "[MatchAnyTag](#cfn-s3-storagelensgroup-or-matchanytag)" : {{[ Tag, ... ]}},
  "[MatchObjectAge](#cfn-s3-storagelensgroup-or-matchobjectage)" : {{MatchObjectAge}},
  "[MatchObjectSize](#cfn-s3-storagelensgroup-or-matchobjectsize)" : {{MatchObjectSize}}
}
```

### YAML
<a name="aws-properties-s3-storagelensgroup-or-syntax.yaml"></a>

```
  [MatchAnyPrefix](#cfn-s3-storagelensgroup-or-matchanyprefix): {{
    - String}}
  [MatchAnySuffix](#cfn-s3-storagelensgroup-or-matchanysuffix): {{
    - String}}
  [MatchAnyTag](#cfn-s3-storagelensgroup-or-matchanytag): {{
    - Tag}}
  [MatchObjectAge](#cfn-s3-storagelensgroup-or-matchobjectage): {{
    MatchObjectAge}}
  [MatchObjectSize](#cfn-s3-storagelensgroup-or-matchobjectsize): {{
    MatchObjectSize}}
```

## Properties
<a name="aws-properties-s3-storagelensgroup-or-properties"></a>

`MatchAnyPrefix`  <a name="cfn-s3-storagelensgroup-or-matchanyprefix"></a>
This property contains a list of prefixes. At least one prefix must be specified. Up to 10 prefixes are allowed.
*Required*: No
*Type*: Array of String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchAnySuffix`  <a name="cfn-s3-storagelensgroup-or-matchanysuffix"></a>
This property contains the list of suffixes. At least one suffix must be specified. Up to 10 suffixes are allowed.
*Required*: No
*Type*: Array of String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchAnyTag`  <a name="cfn-s3-storagelensgroup-or-matchanytag"></a>
This property contains the list of S3 object tags. At least one object tag must be specified. Up to 10 object tags are allowed.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3-storagelensgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchObjectAge`  <a name="cfn-s3-storagelensgroup-or-matchobjectage"></a>
This property filters objects that match the specified object age range.
*Required*: No
*Type*: [MatchObjectAge](aws-properties-s3-storagelensgroup-matchobjectage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchObjectSize`  <a name="cfn-s3-storagelensgroup-or-matchobjectsize"></a>
This property contains the `BytesGreaterThan` and `BytesLessThan` values to define the object size range (minimum and maximum number of Bytes).
*Required*: No
*Type*: [MatchObjectSize](aws-properties-s3-storagelensgroup-matchobjectsize.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

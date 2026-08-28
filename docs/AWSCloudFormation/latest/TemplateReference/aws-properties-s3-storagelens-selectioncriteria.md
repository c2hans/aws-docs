---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-selectioncriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens SelectionCriteria
<a name="aws-properties-s3-storagelens-selectioncriteria"></a>

This resource contains the details of the Amazon S3 Storage Lens selection criteria.

## Syntax
<a name="aws-properties-s3-storagelens-selectioncriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-selectioncriteria-syntax.json"></a>

```
{
  "[Delimiter](#cfn-s3-storagelens-selectioncriteria-delimiter)" : {{String}},
  "[MaxDepth](#cfn-s3-storagelens-selectioncriteria-maxdepth)" : {{Integer}},
  "[MinStorageBytesPercentage](#cfn-s3-storagelens-selectioncriteria-minstoragebytespercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-selectioncriteria-syntax.yaml"></a>

```
  [Delimiter](#cfn-s3-storagelens-selectioncriteria-delimiter): {{String}}
  [MaxDepth](#cfn-s3-storagelens-selectioncriteria-maxdepth): {{Integer}}
  [MinStorageBytesPercentage](#cfn-s3-storagelens-selectioncriteria-minstoragebytespercentage): {{Number}}
```

## Properties
<a name="aws-properties-s3-storagelens-selectioncriteria-properties"></a>

`Delimiter`  <a name="cfn-s3-storagelens-selectioncriteria-delimiter"></a>
This property contains the details of the S3 Storage Lens delimiter being used.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxDepth`  <a name="cfn-s3-storagelens-selectioncriteria-maxdepth"></a>
This property contains the details of the max depth that S3 Storage Lens will collect metrics up to.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinStorageBytesPercentage`  <a name="cfn-s3-storagelens-selectioncriteria-minstoragebytespercentage"></a>
This property contains the details of the minimum storage bytes percentage threshold that S3 Storage Lens will collect metrics up to.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

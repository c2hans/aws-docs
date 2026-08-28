---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kendra-querysuggestionsblocklist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::QuerySuggestionsBlockList
<a name="aws-resource-kendra-querysuggestionsblocklist"></a>

**Note**
Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

Creates a block list to exlcude certain queries from suggestions.

Any query that contains words or phrases specified in the block list is blocked or filtered out from being shown as a suggestion.

You need to provide the file location of your block list text file in your S3 bucket. In your text file, enter each block word or phrase on a separate line.

For information on the current quota limits for block lists, see [Quotas for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html).

`CreateQuerySuggestionsBlockList` is currently not supported in the AWS GovCloud (US-West) region.

For an example of creating a block list for query suggestions using the Python SDK, see [Query suggestions block list](https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions.html#query-suggestions-blocklist).

## Syntax
<a name="aws-resource-kendra-querysuggestionsblocklist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kendra-querysuggestionsblocklist-syntax.json"></a>

```
{
  "Type" : "AWS::Kendra::QuerySuggestionsBlockList",
  "Properties" : {
      "[Description](#cfn-kendra-querysuggestionsblocklist-description)" : {{String}},
      "[IndexId](#cfn-kendra-querysuggestionsblocklist-indexid)" : {{String}},
      "[Name](#cfn-kendra-querysuggestionsblocklist-name)" : {{String}},
      "[RoleArn](#cfn-kendra-querysuggestionsblocklist-rolearn)" : {{String}},
      "[SourceS3Path](#cfn-kendra-querysuggestionsblocklist-sources3path)" : {{S3Path}},
      "[Tags](#cfn-kendra-querysuggestionsblocklist-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kendra-querysuggestionsblocklist-syntax.yaml"></a>

```
Type: AWS::Kendra::QuerySuggestionsBlockList
Properties:
  [Description](#cfn-kendra-querysuggestionsblocklist-description): {{String}}
  [IndexId](#cfn-kendra-querysuggestionsblocklist-indexid): {{String}}
  [Name](#cfn-kendra-querysuggestionsblocklist-name): {{String}}
  [RoleArn](#cfn-kendra-querysuggestionsblocklist-rolearn): {{String}}
  [SourceS3Path](#cfn-kendra-querysuggestionsblocklist-sources3path): {{
    S3Path}}
  [Tags](#cfn-kendra-querysuggestionsblocklist-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kendra-querysuggestionsblocklist-properties"></a>

`Description`  <a name="cfn-kendra-querysuggestionsblocklist-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^\P{C}*$`
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexId`  <a name="cfn-kendra-querysuggestionsblocklist-indexid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]*$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-kendra-querysuggestionsblocklist-name"></a>
The name of the block list.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-kendra-querysuggestionsblocklist-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceS3Path`  <a name="cfn-kendra-querysuggestionsblocklist-sources3path"></a>
Information required to find a specific file in an Amazon S3 bucket.
*Required*: Yes
*Type*: [S3Path](aws-properties-kendra-querysuggestionsblocklist-s3path.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-kendra-querysuggestionsblocklist-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-kendra-querysuggestionsblocklist-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kendra-querysuggestionsblocklist-return-values"></a>

### Ref
<a name="aws-resource-kendra-querysuggestionsblocklist-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-kendra-querysuggestionsblocklist-return-values-fn--getatt"></a>

####
<a name="aws-resource-kendra-querysuggestionsblocklist-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
The identifier of a block list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-function-functionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Function FunctionConfig
<a name="aws-properties-cloudfront-function-functionconfig"></a>

Contains configuration information about a CloudFront function.

## Syntax
<a name="aws-properties-cloudfront-function-functionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-function-functionconfig-syntax.json"></a>

```
{
  "[Comment](#cfn-cloudfront-function-functionconfig-comment)" : {{String}},
  "[KeyValueStoreAssociations](#cfn-cloudfront-function-functionconfig-keyvaluestoreassociations)" : {{[ KeyValueStoreAssociation, ... ]}},
  "[Runtime](#cfn-cloudfront-function-functionconfig-runtime)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-function-functionconfig-syntax.yaml"></a>

```
  [Comment](#cfn-cloudfront-function-functionconfig-comment): {{String}}
  [KeyValueStoreAssociations](#cfn-cloudfront-function-functionconfig-keyvaluestoreassociations): {{
    - KeyValueStoreAssociation}}
  [Runtime](#cfn-cloudfront-function-functionconfig-runtime): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-function-functionconfig-properties"></a>

`Comment`  <a name="cfn-cloudfront-function-functionconfig-comment"></a>
A comment to describe the function. The comment cannot be longer than 128 characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyValueStoreAssociations`  <a name="cfn-cloudfront-function-functionconfig-keyvaluestoreassociations"></a>
The configuration for the key value store associations.
*Required*: No
*Type*: Array of [KeyValueStoreAssociation](aws-properties-cloudfront-function-keyvaluestoreassociation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-cloudfront-function-functionconfig-runtime"></a>
The function's runtime environment version.
*Required*: Yes
*Type*: String
*Allowed values*: `cloudfront-js-1.0 | cloudfront-js-2.0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

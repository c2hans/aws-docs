---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-crawler-lakeformationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Crawler LakeFormationConfiguration
<a name="aws-properties-glue-crawler-lakeformationconfiguration"></a>

Specifies AWS Lake Formation configuration settings for the crawler.

## Syntax
<a name="aws-properties-glue-crawler-lakeformationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-crawler-lakeformationconfiguration-syntax.json"></a>

```
{
  "[AccountId](#cfn-glue-crawler-lakeformationconfiguration-accountid)" : {{String}},
  "[UseLakeFormationCredentials](#cfn-glue-crawler-lakeformationconfiguration-uselakeformationcredentials)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-glue-crawler-lakeformationconfiguration-syntax.yaml"></a>

```
  [AccountId](#cfn-glue-crawler-lakeformationconfiguration-accountid): {{String}}
  [UseLakeFormationCredentials](#cfn-glue-crawler-lakeformationconfiguration-uselakeformationcredentials): {{Boolean}}
```

## Properties
<a name="aws-properties-glue-crawler-lakeformationconfiguration-properties"></a>

`AccountId`  <a name="cfn-glue-crawler-lakeformationconfiguration-accountid"></a>
Required for cross account crawls. For same account crawls as the target data, this can be left as null.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseLakeFormationCredentials`  <a name="cfn-glue-crawler-lakeformationconfiguration-uselakeformationcredentials"></a>
Specifies whether to use AWS Lake Formation credentials for the crawler instead of the IAM role credentials.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-resolver-appsyncruntime.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Resolver AppSyncRuntime
<a name="aws-properties-appsync-resolver-appsyncruntime"></a>

Describes a runtime used by an AWS AppSync resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.

## Syntax
<a name="aws-properties-appsync-resolver-appsyncruntime-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-resolver-appsyncruntime-syntax.json"></a>

```
{
  "[Name](#cfn-appsync-resolver-appsyncruntime-name)" : {{String}},
  "[RuntimeVersion](#cfn-appsync-resolver-appsyncruntime-runtimeversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-resolver-appsyncruntime-syntax.yaml"></a>

```
  [Name](#cfn-appsync-resolver-appsyncruntime-name): {{String}}
  [RuntimeVersion](#cfn-appsync-resolver-appsyncruntime-runtimeversion): {{String}}
```

## Properties
<a name="aws-properties-appsync-resolver-appsyncruntime-properties"></a>

`Name`  <a name="cfn-appsync-resolver-appsyncruntime-name"></a>
The `name` of the runtime to use. Currently, the only allowed value is `APPSYNC_JS`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeVersion`  <a name="cfn-appsync-resolver-appsyncruntime-runtimeversion"></a>
The `version` of the runtime to use. Currently, the only allowed version is `1.0.0`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

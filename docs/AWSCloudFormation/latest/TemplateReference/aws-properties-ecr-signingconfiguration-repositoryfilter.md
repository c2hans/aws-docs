---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-signingconfiguration-repositoryfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::SigningConfiguration RepositoryFilter
<a name="aws-properties-ecr-signingconfiguration-repositoryfilter"></a>

A repository filter used to determine which repositories have their images automatically signed on push. Each filter consists of a filter type and filter value.

## Syntax
<a name="aws-properties-ecr-signingconfiguration-repositoryfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-signingconfiguration-repositoryfilter-syntax.json"></a>

```
{
  "[Filter](#cfn-ecr-signingconfiguration-repositoryfilter-filter)" : {{String}},
  "[FilterType](#cfn-ecr-signingconfiguration-repositoryfilter-filtertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecr-signingconfiguration-repositoryfilter-syntax.yaml"></a>

```
  [Filter](#cfn-ecr-signingconfiguration-repositoryfilter-filter): {{String}}
  [FilterType](#cfn-ecr-signingconfiguration-repositoryfilter-filtertype): {{String}}
```

## Properties
<a name="aws-properties-ecr-signingconfiguration-repositoryfilter-properties"></a>

`Filter`  <a name="cfn-ecr-signingconfiguration-repositoryfilter-filter"></a>
The filter value used to match repository names. When using `WILDCARD_MATCH`, the `*` character matches any sequence of characters.
Examples:
+ `myapp/*` - Matches all repositories starting with `myapp/`
+ `*/production` - Matches all repositories ending with `/production`
+ `*prod*` - Matches all repositories containing `prod`
*Required*: Yes
*Type*: String
*Pattern*: `^(?:[a-z0-9*]+(?:[._-][a-z0-9*]+)*/)*[a-z0-9*]+(?:[._-][a-z0-9*]+)*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterType`  <a name="cfn-ecr-signingconfiguration-repositoryfilter-filtertype"></a>
The type of filter to apply. Currently, only `WILDCARD_MATCH` is supported, which uses wildcard patterns to match repository names.
*Required*: Yes
*Type*: String
*Allowed values*: `WILDCARD_MATCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

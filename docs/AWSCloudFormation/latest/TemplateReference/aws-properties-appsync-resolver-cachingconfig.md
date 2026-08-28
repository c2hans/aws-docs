---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-resolver-cachingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Resolver CachingConfig
<a name="aws-properties-appsync-resolver-cachingconfig"></a>

The caching configuration for a resolver that has caching activated.

## Syntax
<a name="aws-properties-appsync-resolver-cachingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-resolver-cachingconfig-syntax.json"></a>

```
{
  "[CachingKeys](#cfn-appsync-resolver-cachingconfig-cachingkeys)" : {{[ String, ... ]}},
  "[Ttl](#cfn-appsync-resolver-cachingconfig-ttl)" : {{Number}}
}
```

### YAML
<a name="aws-properties-appsync-resolver-cachingconfig-syntax.yaml"></a>

```
  [CachingKeys](#cfn-appsync-resolver-cachingconfig-cachingkeys): {{
    - String}}
  [Ttl](#cfn-appsync-resolver-cachingconfig-ttl): {{Number}}
```

## Properties
<a name="aws-properties-appsync-resolver-cachingconfig-properties"></a>

`CachingKeys`  <a name="cfn-appsync-resolver-cachingconfig-cachingkeys"></a>
The caching keys for a resolver that has caching activated.
Valid values are entries from the `$context.arguments`, `$context.source`, and `$context.identity` maps.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ttl`  <a name="cfn-appsync-resolver-cachingconfig-ttl"></a>
The TTL in seconds for a resolver that has caching activated.
Valid values are 1–3,600 seconds.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

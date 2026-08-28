---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-app-cacheconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::App CacheConfig
<a name="aws-properties-amplify-app-cacheconfig"></a>

Describes the cache configuration for an Amplify app.

For more information about how Amplify applies an optimal cache configuration for your app based on the type of content that is being served, see [Managing cache configuration](https://docs.aws.amazon.com/amplify/latest/userguide/managing-cache-configuration) in the *Amplify User guide*.

## Syntax
<a name="aws-properties-amplify-app-cacheconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-app-cacheconfig-syntax.json"></a>

```
{
  "[Type](#cfn-amplify-app-cacheconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-app-cacheconfig-syntax.yaml"></a>

```
  [Type](#cfn-amplify-app-cacheconfig-type): {{String}}
```

## Properties
<a name="aws-properties-amplify-app-cacheconfig-properties"></a>

`Type`  <a name="cfn-amplify-app-cacheconfig-type"></a>
The type of cache configuration to use for an Amplify app.
The `AMPLIFY_MANAGED` cache configuration automatically applies an optimized cache configuration for your app based on its platform, routing rules, and rewrite rules.
The `AMPLIFY_MANAGED_NO_COOKIES` cache configuration type is the same as `AMPLIFY_MANAGED`, except that it excludes all cookies from the cache key. This is the default setting.
*Required*: No
*Type*: String
*Allowed values*: `AMPLIFY_MANAGED | AMPLIFY_MANAGED_NO_COOKIES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

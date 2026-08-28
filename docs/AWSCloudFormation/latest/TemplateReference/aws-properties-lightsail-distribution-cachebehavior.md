---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-distribution-cachebehavior.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Distribution CacheBehavior
<a name="aws-properties-lightsail-distribution-cachebehavior"></a>

`CacheBehavior` is a property of the [AWS::Lightsail::Distribution](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html) resource. It describes the default cache behavior of an Amazon Lightsail content delivery network (CDN) distribution.

## Syntax
<a name="aws-properties-lightsail-distribution-cachebehavior-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-distribution-cachebehavior-syntax.json"></a>

```
{
  "[Behavior](#cfn-lightsail-distribution-cachebehavior-behavior)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-distribution-cachebehavior-syntax.yaml"></a>

```
  [Behavior](#cfn-lightsail-distribution-cachebehavior-behavior): {{String}}
```

## Properties
<a name="aws-properties-lightsail-distribution-cachebehavior-properties"></a>

`Behavior`  <a name="cfn-lightsail-distribution-cachebehavior-behavior"></a>
The cache behavior of the distribution.
The following cache behaviors can be specified:
+ ** `cache` ** - This option is best for static sites. When specified, your distribution caches and serves your entire website as static content. This behavior is ideal for websites with static content that doesn't change depending on who views it, or for websites that don't use cookies, headers, or query strings to personalize content.
+ ** `dont-cache` ** - This option is best for sites that serve a mix of static and dynamic content. When specified, your distribution caches and serves only the content that is specified in the distribution’s `CacheBehaviorPerPath` parameter. This behavior is ideal for websites or web applications that use cookies, headers, and query strings to personalize content for individual users.
*Required*: No
*Type*: String
*Allowed values*: `dont-cache | cache`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-healthchecksource-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HealthCheckSource Tag

A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.

## Syntax
<a name="aws-properties-route53-healthchecksource-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-healthchecksource-tag-syntax.json"></a>

```
{
  "[Key](#cfn-route53-healthchecksource-tag-key)" : {{String}},
  "[Value](#cfn-route53-healthchecksource-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-healthchecksource-tag-syntax.yaml"></a>

```
  [Key](#cfn-route53-healthchecksource-tag-key): {{String}}
  [Value](#cfn-route53-healthchecksource-tag-value): {{String}}
```

## Properties
<a name="aws-properties-route53-healthchecksource-tag-properties"></a>

`Key`  <a name="cfn-route53-healthchecksource-tag-key"></a>
The value of `Key` depends on the operation that you want to perform:
+ **Add a tag to a health check or hosted zone**: `Key` is the name that you want to give the new tag.
+ **Edit a tag**: `Key` is the name of the tag that you want to change the `Value` for.
+ ** Delete a key**: `Key` is the name of the tag you want to remove.
+ **Give a name to a health check**: Edit the default `Name` tag. In the Amazon Route 53 console, the list of your health checks includes a **Name** column that lets you see the name that you've given to each health check.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-route53-healthchecksource-tag-value"></a>
The value of `Value` depends on the operation that you want to perform:
+ **Add a tag to a health check or hosted zone**: `Value` is the value that you want to give the new tag.
+ **Edit a tag**: `Value` is the new value that you want to assign the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

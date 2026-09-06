---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-totallocalstoragegbrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider TotalLocalStorageGBRequest
<a name="aws-properties-ecs-capacityprovider-totallocalstoragegbrequest"></a>

The minimum and maximum total local storage in gigabytes (GB) for instance types with local storage. This is useful for workloads that require local storage for temporary data or caching.

## Syntax
<a name="aws-properties-ecs-capacityprovider-totallocalstoragegbrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-totallocalstoragegbrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ecs-capacityprovider-totallocalstoragegbrequest-max)" : {{Number}},
  "[Min](#cfn-ecs-capacityprovider-totallocalstoragegbrequest-min)" : {{Number}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-totallocalstoragegbrequest-syntax.yaml"></a>

```
  [Max](#cfn-ecs-capacityprovider-totallocalstoragegbrequest-max): {{Number}}
  [Min](#cfn-ecs-capacityprovider-totallocalstoragegbrequest-min): {{Number}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-totallocalstoragegbrequest-properties"></a>

`Max`  <a name="cfn-ecs-capacityprovider-totallocalstoragegbrequest-max"></a>
The maximum total local storage in GB. Instance types with more local storage are excluded from selection.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ecs-capacityprovider-totallocalstoragegbrequest-min"></a>
The minimum total local storage in GB. Instance types with less local storage are excluded from selection.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

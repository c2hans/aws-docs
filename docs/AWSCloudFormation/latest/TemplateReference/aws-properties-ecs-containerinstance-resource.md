---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-containerinstance-resource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ContainerInstance Resource
<a name="aws-properties-ecs-containerinstance-resource"></a>

Describes the resources available for a container instance.

## Syntax
<a name="aws-properties-ecs-containerinstance-resource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-containerinstance-resource-syntax.json"></a>

```
{
  "[DoubleValue](#cfn-ecs-containerinstance-resource-doublevalue)" : {{Number}},
  "[IntegerValue](#cfn-ecs-containerinstance-resource-integervalue)" : {{Integer}},
  "[LongValue](#cfn-ecs-containerinstance-resource-longvalue)" : {{Number}},
  "[Name](#cfn-ecs-containerinstance-resource-name)" : {{String}},
  "[StringSetValue](#cfn-ecs-containerinstance-resource-stringsetvalue)" : {{[ String, ... ]}},
  "[Type](#cfn-ecs-containerinstance-resource-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-containerinstance-resource-syntax.yaml"></a>

```
  [DoubleValue](#cfn-ecs-containerinstance-resource-doublevalue): {{Number}}
  [IntegerValue](#cfn-ecs-containerinstance-resource-integervalue): {{
    Integer}}
  [LongValue](#cfn-ecs-containerinstance-resource-longvalue): {{Number}}
  [Name](#cfn-ecs-containerinstance-resource-name): {{String}}
  [StringSetValue](#cfn-ecs-containerinstance-resource-stringsetvalue): {{
    - String}}
  [Type](#cfn-ecs-containerinstance-resource-type): {{String}}
```

## Properties
<a name="aws-properties-ecs-containerinstance-resource-properties"></a>

`DoubleValue`  <a name="cfn-ecs-containerinstance-resource-doublevalue"></a>
When the `doubleValue` type is set, the value of the resource must be a double precision floating-point type.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegerValue`  <a name="cfn-ecs-containerinstance-resource-integervalue"></a>
When the `integerValue` type is set, the value of the resource must be an integer.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LongValue`  <a name="cfn-ecs-containerinstance-resource-longvalue"></a>
When the `longValue` type is set, the value of the resource must be an extended precision floating-point type.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ecs-containerinstance-resource-name"></a>
The name of the resource, such as `CPU`, `MEMORY`, `PORTS`, `PORTS_UDP`, or a user-defined resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringSetValue`  <a name="cfn-ecs-containerinstance-resource-stringsetvalue"></a>
When the `stringSetValue` type is set, the value of the resource must be a string type.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-ecs-containerinstance-resource-type"></a>
The type of the resource. Valid values: `INTEGER`, `DOUBLE`, `LONG`, or `STRINGSET`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

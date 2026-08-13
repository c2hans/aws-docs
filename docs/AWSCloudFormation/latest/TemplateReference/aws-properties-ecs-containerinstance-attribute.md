---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-containerinstance-attribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ContainerInstance Attribute
<a name="aws-properties-ecs-containerinstance-attribute"></a>

An attribute is a name-value pair that's associated with an Amazon ECS object. Use attributes to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see [Attributes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-containerinstance-attribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-containerinstance-attribute-syntax.json"></a>

```
{
  "[Name](#cfn-ecs-containerinstance-attribute-name)" : {{String}},
  "[Value](#cfn-ecs-containerinstance-attribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-containerinstance-attribute-syntax.yaml"></a>

```
  [Name](#cfn-ecs-containerinstance-attribute-name): {{String}}
  [Value](#cfn-ecs-containerinstance-attribute-value): {{String}}
```

## Properties
<a name="aws-properties-ecs-containerinstance-attribute-properties"></a>

`Name`  <a name="cfn-ecs-containerinstance-attribute-name"></a>
The name of the attribute. The `name` must contain between 1 and 128 characters. The name may contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (\_), forward slashes (/), back slashes (\\), or periods (.).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ecs-containerinstance-attribute-value"></a>
The value of the attribute. The `value` must contain between 1 and 128 characters. It can contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (\_), periods (.), at signs (@), forward slashes (/), back slashes (\\), colons (:), or spaces. The value can't start or end with a space.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

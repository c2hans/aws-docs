---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-ebstagspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service EBSTagSpecification
<a name="aws-properties-ecs-service-ebstagspecification"></a>

The tag specifications of an Amazon EBS volume.

## Syntax
<a name="aws-properties-ecs-service-ebstagspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-ebstagspecification-syntax.json"></a>

```
{
  "[PropagateTags](#cfn-ecs-service-ebstagspecification-propagatetags)" : {{String}},
  "[ResourceType](#cfn-ecs-service-ebstagspecification-resourcetype)" : {{String}},
  "[Tags](#cfn-ecs-service-ebstagspecification-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-service-ebstagspecification-syntax.yaml"></a>

```
  [PropagateTags](#cfn-ecs-service-ebstagspecification-propagatetags): {{String}}
  [ResourceType](#cfn-ecs-service-ebstagspecification-resourcetype): {{String}}
  [Tags](#cfn-ecs-service-ebstagspecification-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-ecs-service-ebstagspecification-properties"></a>

`PropagateTags`  <a name="cfn-ecs-service-ebstagspecification-propagatetags"></a>
Determines whether to propagate the tags from the task definition to the Amazon EBS volume. Tags can only propagate to a `SERVICE` specified in `ServiceVolumeConfiguration`. If no value is specified, the tags aren't propagated.
*Required*: No
*Type*: String
*Allowed values*: `SERVICE | TASK_DEFINITION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-ecs-service-ebstagspecification-resourcetype"></a>
The type of volume resource.
*Required*: Yes
*Type*: String
*Allowed values*: `volume`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ecs-service-ebstagspecification-tags"></a>
The tags applied to this Amazon EBS volume. `AmazonECSCreated` and `AmazonECSManaged` are reserved tags that can't be used.
*Required*: No
*Type*: Array of [Tag](aws-properties-ecs-service-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

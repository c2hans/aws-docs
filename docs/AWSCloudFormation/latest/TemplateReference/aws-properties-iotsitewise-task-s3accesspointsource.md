---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-task-s3accesspointsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Task S3AccessPointSource
<a name="aws-properties-iotsitewise-task-s3accesspointsource"></a>

<a name="aws-properties-iotsitewise-task-s3accesspointsource-description"></a>The `S3AccessPointSource` property type specifies Property description not available. for an [AWS::IoTSiteWise::Task](aws-resource-iotsitewise-task.md).

## Syntax
<a name="aws-properties-iotsitewise-task-s3accesspointsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-task-s3accesspointsource-syntax.json"></a>

```
{
  "[AccessPointArn](#cfn-iotsitewise-task-s3accesspointsource-accesspointarn)" : {{String}},
  "[Prefix](#cfn-iotsitewise-task-s3accesspointsource-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-task-s3accesspointsource-syntax.yaml"></a>

```
  [AccessPointArn](#cfn-iotsitewise-task-s3accesspointsource-accesspointarn): {{String}}
  [Prefix](#cfn-iotsitewise-task-s3accesspointsource-prefix): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-task-s3accesspointsource-properties"></a>

`AccessPointArn`  <a name="cfn-iotsitewise-task-s3accesspointsource-accesspointarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov)?:s3:[a-z0-9-]*:\d{12}:accesspoint[/:][a-zA-Z0-9._-]+$`
*Minimum*: `4`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-iotsitewise-task-s3accesspointsource-prefix"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

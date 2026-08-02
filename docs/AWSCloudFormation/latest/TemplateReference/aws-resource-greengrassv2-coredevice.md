---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-greengrassv2-coredevice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::CoreDevice
<a name="aws-resource-greengrassv2-coredevice"></a>

<a name="aws-resource-greengrassv2-coredevice-description"></a>The `AWS::GreengrassV2::CoreDevice` resource Property description not available. for GreengrassV2.

## Syntax
<a name="aws-resource-greengrassv2-coredevice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-greengrassv2-coredevice-syntax.json"></a>

```
{
  "Type" : "AWS::GreengrassV2::CoreDevice",
  "Properties" : {
      "[CoreDeviceThingName](#cfn-greengrassv2-coredevice-coredevicethingname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-greengrassv2-coredevice-syntax.yaml"></a>

```
Type: AWS::GreengrassV2::CoreDevice
Properties:
  [CoreDeviceThingName](#cfn-greengrassv2-coredevice-coredevicethingname): {{String}}
```

## Properties
<a name="aws-resource-greengrassv2-coredevice-properties"></a>

`CoreDeviceThingName`  <a name="cfn-greengrassv2-coredevice-coredevicethingname"></a>
The name of the core device. This is also the name of the AWS IoT thing.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-greengrassv2-coredevice-return-values"></a>

### Ref
<a name="aws-resource-greengrassv2-coredevice-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-greengrassv2-coredevice-return-values-fn--getatt"></a>

####
<a name="aws-resource-greengrassv2-coredevice-return-values-fn--getatt-fn--getatt"></a>

`Architecture`  <a name="Architecture-fn::getatt"></a>
The computer architecture of the core device.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CoreVersion`  <a name="CoreVersion-fn::getatt"></a>
Property description not available.

`LastStatusUpdateTimestamp`  <a name="LastStatusUpdateTimestamp-fn::getatt"></a>
The time at which the core device's status last updated, expressed in ISO 8601 format.

`Platform`  <a name="Platform-fn::getatt"></a>
The operating system platform that the core device runs.

`Runtime`  <a name="Runtime-fn::getatt"></a>
The runtime for the core device. The runtime can be:
+  `aws_nucleus_classic`
+  `aws_nucleus_lite`

`Status`  <a name="Status-fn::getatt"></a>
The status of the core device. Core devices can have the following statuses:
+ `HEALTHY` – The AWS IoT Greengrass Core software and all components run on the core device without issue.
+ `UNHEALTHY` – The AWS IoT Greengrass Core software or a component is in a failed state on the core device.

`Tags`  <a name="Tags-fn::getatt"></a>
Property description not available.

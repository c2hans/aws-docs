---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-gateway-siemensie.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Gateway SiemensIE
<a name="aws-properties-iotsitewise-gateway-siemensie"></a>

Contains details for a AWS IoT SiteWise Edge gateway that runs on a Siemens Industrial Edge Device.

## Syntax
<a name="aws-properties-iotsitewise-gateway-siemensie-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-gateway-siemensie-syntax.json"></a>

```
{
  "[IotCoreThingName](#cfn-iotsitewise-gateway-siemensie-iotcorethingname)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-gateway-siemensie-syntax.yaml"></a>

```
  [IotCoreThingName](#cfn-iotsitewise-gateway-siemensie-iotcorethingname): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-gateway-siemensie-properties"></a>

`IotCoreThingName`  <a name="cfn-iotsitewise-gateway-siemensie-iotcorethingname"></a>
The name of the AWS IoT Thing for your AWS IoT SiteWise Edge gateway.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

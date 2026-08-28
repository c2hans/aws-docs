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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

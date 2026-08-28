---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-storagemaximumsize.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign StorageMaximumSize
<a name="aws-properties-iotfleetwise-campaign-storagemaximumsize"></a>

The maximum storage size for the data partition.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-campaign-storagemaximumsize-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-storagemaximumsize-syntax.json"></a>

```
{
  "[Unit](#cfn-iotfleetwise-campaign-storagemaximumsize-unit)" : {{String}},
  "[Value](#cfn-iotfleetwise-campaign-storagemaximumsize-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-storagemaximumsize-syntax.yaml"></a>

```
  [Unit](#cfn-iotfleetwise-campaign-storagemaximumsize-unit): {{String}}
  [Value](#cfn-iotfleetwise-campaign-storagemaximumsize-value): {{Integer}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-storagemaximumsize-properties"></a>

`Unit`  <a name="cfn-iotfleetwise-campaign-storagemaximumsize-unit"></a>
The data type of the data to store.
*Required*: Yes
*Type*: String
*Allowed values*: `MB | GB | TB`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-iotfleetwise-campaign-storagemaximumsize-value"></a>
The maximum amount of time to store data.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1073741824`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

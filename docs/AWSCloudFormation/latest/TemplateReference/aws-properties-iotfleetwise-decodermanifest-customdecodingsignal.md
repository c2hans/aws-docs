---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-decodermanifest-customdecodingsignal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest CustomDecodingSignal
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingsignal"></a>

Information about signals using a custom decoding protocol as defined by the customer.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingsignal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingsignal-syntax.json"></a>

```
{
  "[Id](#cfn-iotfleetwise-decodermanifest-customdecodingsignal-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingsignal-syntax.yaml"></a>

```
  [Id](#cfn-iotfleetwise-decodermanifest-customdecodingsignal-id): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingsignal-properties"></a>

`Id`  <a name="cfn-iotfleetwise-decodermanifest-customdecodingsignal-id"></a>
The ID of the signal.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!.*\.\.)[a-zA-Z0-9_\-#:.]+$`
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

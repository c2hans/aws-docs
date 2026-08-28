---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-provisioningtemplate-provisioninghook.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::ProvisioningTemplate ProvisioningHook
<a name="aws-properties-iot-provisioningtemplate-provisioninghook"></a>

Structure that contains payloadVersion and targetArn. Provisioning hooks can be used when fleet provisioning to validate device parameters before allowing the device to be provisioned.

## Syntax
<a name="aws-properties-iot-provisioningtemplate-provisioninghook-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-provisioningtemplate-provisioninghook-syntax.json"></a>

```
{
  "[PayloadVersion](#cfn-iot-provisioningtemplate-provisioninghook-payloadversion)" : {{String}},
  "[TargetArn](#cfn-iot-provisioningtemplate-provisioninghook-targetarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-provisioningtemplate-provisioninghook-syntax.yaml"></a>

```
  [PayloadVersion](#cfn-iot-provisioningtemplate-provisioninghook-payloadversion): {{String}}
  [TargetArn](#cfn-iot-provisioningtemplate-provisioninghook-targetarn): {{String}}
```

## Properties
<a name="aws-properties-iot-provisioningtemplate-provisioninghook-properties"></a>

`PayloadVersion`  <a name="cfn-iot-provisioningtemplate-provisioninghook-payloadversion"></a>
The payload that was sent to the target function. The valid payload is `"2020-04-01"`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArn`  <a name="cfn-iot-provisioningtemplate-provisioninghook-targetarn"></a>
The ARN of the target function.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

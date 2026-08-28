---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::Deployment DeploymentConfigurationValidationPolicy
<a name="aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy"></a>

Contains information about how long a component on a core device can validate its configuration updates before it times out. Components can use the [SubscribeToValidateConfigurationUpdates](https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-subscribetovalidateconfigurationupdates) IPC operation to receive notifications when a deployment specifies a configuration update. Then, components can respond with the [SendConfigurationValidityReport](https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-sendconfigurationvalidityreport) IPC operation. For more information, see the [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) in the *AWS IoT Greengrass V2 Developer Guide*.

## Syntax
<a name="aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy-syntax.json"></a>

```
{
  "[TimeoutInSeconds](#cfn-greengrassv2-deployment-deploymentconfigurationvalidationpolicy-timeoutinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy-syntax.yaml"></a>

```
  [TimeoutInSeconds](#cfn-greengrassv2-deployment-deploymentconfigurationvalidationpolicy-timeoutinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy-properties"></a>

`TimeoutInSeconds`  <a name="cfn-greengrassv2-deployment-deploymentconfigurationvalidationpolicy-timeoutinseconds"></a>
The amount of time in seconds that a component can validate its configuration updates. If the validation time exceeds this timeout, then the deployment proceeds for the device.
Default: `30`
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

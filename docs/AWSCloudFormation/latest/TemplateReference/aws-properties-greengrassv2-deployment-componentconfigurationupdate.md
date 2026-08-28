---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-deployment-componentconfigurationupdate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::Deployment ComponentConfigurationUpdate
<a name="aws-properties-greengrassv2-deployment-componentconfigurationupdate"></a>

Contains information about a deployment's update to a component's configuration on AWS IoT Greengrass core devices. For more information, see [Update component configurations](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html) in the *AWS IoT Greengrass V2 Developer Guide*.

## Syntax
<a name="aws-properties-greengrassv2-deployment-componentconfigurationupdate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-deployment-componentconfigurationupdate-syntax.json"></a>

```
{
  "[Merge](#cfn-greengrassv2-deployment-componentconfigurationupdate-merge)" : {{String}},
  "[Reset](#cfn-greengrassv2-deployment-componentconfigurationupdate-reset)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-greengrassv2-deployment-componentconfigurationupdate-syntax.yaml"></a>

```
  [Merge](#cfn-greengrassv2-deployment-componentconfigurationupdate-merge): {{String}}
  [Reset](#cfn-greengrassv2-deployment-componentconfigurationupdate-reset): {{
    - String}}
```

## Properties
<a name="aws-properties-greengrassv2-deployment-componentconfigurationupdate-properties"></a>

`Merge`  <a name="cfn-greengrassv2-deployment-componentconfigurationupdate-merge"></a>
A serialized JSON string that contains the configuration object to merge to target devices. The core device merges this configuration with the component's existing configuration. If this is the first time a component deploys on a device, the core device merges this configuration with the component's default configuration. This means that the core device keeps it's existing configuration for keys and values that you don't specify in this object. For more information, see [Merge configuration updates](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#merge-configuration-update) in the *AWS IoT Greengrass V2 Developer Guide*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `10485760`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Reset`  <a name="cfn-greengrassv2-deployment-componentconfigurationupdate-reset"></a>
The list of configuration nodes to reset to default values on target devices. Use JSON pointers to specify each node to reset. JSON pointers start with a forward slash (`/`) and use forward slashes to separate the key for each level in the object. For more information, see the [JSON pointer specification](https://tools.ietf.org/html/rfc6901) and [Reset configuration updates](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#reset-configuration-update) in the *AWS IoT Greengrass V2 Developer Guide*.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

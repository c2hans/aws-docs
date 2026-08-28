---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-coredefinitionversion-core.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::CoreDefinitionVersion Core
<a name="aws-properties-greengrass-coredefinitionversion-core"></a>

<a name="aws-properties-greengrass-coredefinitionversion-core-description"></a> A core is an AWS IoT device that runs the AWS IoT Greengrass core software and manages local processes for a Greengrass group. For more information, see [What Is AWS IoT Greengrass?](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html) in the * AWS IoT Greengrass Version 1 Developer Guide *.

<a name="aws-properties-greengrass-coredefinitionversion-core-inheritance"></a> In an CloudFormation template, the `Cores` property of the [`AWS::Greengrass::CoreDefinitionVersion`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html) resource contains a list of `Core` property types. Currently, the list can contain only one core.

## Syntax
<a name="aws-properties-greengrass-coredefinitionversion-core-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-coredefinitionversion-core-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-greengrass-coredefinitionversion-core-certificatearn)" : {{String}},
  "[Id](#cfn-greengrass-coredefinitionversion-core-id)" : {{String}},
  "[SyncShadow](#cfn-greengrass-coredefinitionversion-core-syncshadow)" : {{Boolean}},
  "[ThingArn](#cfn-greengrass-coredefinitionversion-core-thingarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrass-coredefinitionversion-core-syntax.yaml"></a>

```
  [CertificateArn](#cfn-greengrass-coredefinitionversion-core-certificatearn): {{String}}
  [Id](#cfn-greengrass-coredefinitionversion-core-id): {{String}}
  [SyncShadow](#cfn-greengrass-coredefinitionversion-core-syncshadow): {{Boolean}}
  [ThingArn](#cfn-greengrass-coredefinitionversion-core-thingarn): {{String}}
```

## Properties
<a name="aws-properties-greengrass-coredefinitionversion-core-properties"></a>

`CertificateArn`  <a name="cfn-greengrass-coredefinitionversion-core-certificatearn"></a>
The ARN of the device certificate for the core. This X.509 certificate is used to authenticate the core with AWS IoT and AWS IoT Greengrass services.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Id`  <a name="cfn-greengrass-coredefinitionversion-core-id"></a>
A descriptive or arbitrary ID for the core. This value must be unique within the core definition version. Maximum length is 128 characters with pattern `[a-zA-Z0-9:_-]+`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SyncShadow`  <a name="cfn-greengrass-coredefinitionversion-core-syncshadow"></a>
Indicates whether the core's local shadow is synced with the cloud automatically. The default is false.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ThingArn`  <a name="cfn-greengrass-coredefinitionversion-core-thingarn"></a>
The Amazon Resource Name (ARN) of the core, which is an AWS IoT device (thing).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-coredefinitionversion-core--seealso"></a>
+ [Core](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-core.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

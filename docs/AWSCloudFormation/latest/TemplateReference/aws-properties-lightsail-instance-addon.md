---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-instance-addon.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Instance AddOn
<a name="aws-properties-lightsail-instance-addon"></a>

`AddOn` is a property of the [AWS::Lightsail::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html) resource. It describes the add-ons for an instance.

## Syntax
<a name="aws-properties-lightsail-instance-addon-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-instance-addon-syntax.json"></a>

```
{
  "[AddOnType](#cfn-lightsail-instance-addon-addontype)" : {{String}},
  "[AutoSnapshotAddOnRequest](#cfn-lightsail-instance-addon-autosnapshotaddonrequest)" : {{AutoSnapshotAddOn}},
  "[Status](#cfn-lightsail-instance-addon-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-instance-addon-syntax.yaml"></a>

```
  [AddOnType](#cfn-lightsail-instance-addon-addontype): {{String}}
  [AutoSnapshotAddOnRequest](#cfn-lightsail-instance-addon-autosnapshotaddonrequest): {{
    AutoSnapshotAddOn}}
  [Status](#cfn-lightsail-instance-addon-status): {{String}}
```

## Properties
<a name="aws-properties-lightsail-instance-addon-properties"></a>

`AddOnType`  <a name="cfn-lightsail-instance-addon-addontype"></a>
The add-on type (for example, `AutoSnapshot`).
`AutoSnapshot` is the only add-on that can be enabled for an instance.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoSnapshotAddOnRequest`  <a name="cfn-lightsail-instance-addon-autosnapshotaddonrequest"></a>
The parameters for the automatic snapshot add-on, such as the daily time when an automatic snapshot will be created.
*Required*: No
*Type*: [AutoSnapshotAddOn](aws-properties-lightsail-instance-autosnapshotaddon.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-lightsail-instance-addon-status"></a>
The status of the add-on.
Valid Values: `Enabled` \| `Disabled`
*Required*: No
*Type*: String
*Allowed values*: `Enabling | Disabling | Enabled | Terminating | Terminated | Disabled | Failed`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

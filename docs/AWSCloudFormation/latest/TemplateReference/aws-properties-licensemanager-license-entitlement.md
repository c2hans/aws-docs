---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-license-entitlement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::License Entitlement
<a name="aws-properties-licensemanager-license-entitlement"></a>

Describes a resource entitled for use with a license.

## Syntax
<a name="aws-properties-licensemanager-license-entitlement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-license-entitlement-syntax.json"></a>

```
{
  "[AllowCheckIn](#cfn-licensemanager-license-entitlement-allowcheckin)" : {{Boolean}},
  "[MaxCount](#cfn-licensemanager-license-entitlement-maxcount)" : {{Integer}},
  "[Name](#cfn-licensemanager-license-entitlement-name)" : {{String}},
  "[Overage](#cfn-licensemanager-license-entitlement-overage)" : {{Boolean}},
  "[Unit](#cfn-licensemanager-license-entitlement-unit)" : {{String}},
  "[Value](#cfn-licensemanager-license-entitlement-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-licensemanager-license-entitlement-syntax.yaml"></a>

```
  [AllowCheckIn](#cfn-licensemanager-license-entitlement-allowcheckin): {{Boolean}}
  [MaxCount](#cfn-licensemanager-license-entitlement-maxcount): {{Integer}}
  [Name](#cfn-licensemanager-license-entitlement-name): {{String}}
  [Overage](#cfn-licensemanager-license-entitlement-overage): {{Boolean}}
  [Unit](#cfn-licensemanager-license-entitlement-unit): {{String}}
  [Value](#cfn-licensemanager-license-entitlement-value): {{String}}
```

## Properties
<a name="aws-properties-licensemanager-license-entitlement-properties"></a>

`AllowCheckIn`  <a name="cfn-licensemanager-license-entitlement-allowcheckin"></a>
Indicates whether check-ins are allowed.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxCount`  <a name="cfn-licensemanager-license-entitlement-maxcount"></a>
Maximum entitlement count. Use if the unit is not None.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-licensemanager-license-entitlement-name"></a>
Entitlement name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Overage`  <a name="cfn-licensemanager-license-entitlement-overage"></a>
Indicates whether overages are allowed.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-licensemanager-license-entitlement-unit"></a>
Entitlement unit.
*Required*: Yes
*Type*: String
*Allowed values*: `Count | None | Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-licensemanager-license-entitlement-value"></a>
Entitlement resource. Use only if the unit is None.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

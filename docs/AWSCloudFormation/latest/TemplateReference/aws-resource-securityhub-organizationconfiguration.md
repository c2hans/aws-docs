---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-organizationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::OrganizationConfiguration
<a name="aws-resource-securityhub-organizationconfiguration"></a>

 The `AWS::SecurityHub::OrganizationConfiguration` resource specifies the way that your AWS organization is configured in AWS Security Hub CSPM. Specifically, you can use this resource to specify the configuration type for your organization and whether to automatically Security Hub CSPM and security standards in new member accounts. For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html) in the *AWS Security Hub CSPM User Guide*.

## Syntax
<a name="aws-resource-securityhub-organizationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-organizationconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::OrganizationConfiguration",
  "Properties" : {
      "[AutoEnable](#cfn-securityhub-organizationconfiguration-autoenable)" : {{Boolean}},
      "[AutoEnableStandards](#cfn-securityhub-organizationconfiguration-autoenablestandards)" : {{String}},
      "[ConfigurationType](#cfn-securityhub-organizationconfiguration-configurationtype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-organizationconfiguration-syntax.yaml"></a>

```
Type: AWS::SecurityHub::OrganizationConfiguration
Properties:
  [AutoEnable](#cfn-securityhub-organizationconfiguration-autoenable): {{Boolean}}
  [AutoEnableStandards](#cfn-securityhub-organizationconfiguration-autoenablestandards): {{String}}
  [ConfigurationType](#cfn-securityhub-organizationconfiguration-configurationtype): {{String}}
```

## Properties
<a name="aws-resource-securityhub-organizationconfiguration-properties"></a>

`AutoEnable`  <a name="cfn-securityhub-organizationconfiguration-autoenable"></a>
Whether to automatically enable Security Hub CSPM in new member accounts when they join the organization.
If set to `true`, then Security Hub CSPM is automatically enabled in new accounts. If set to `false`, then Security Hub CSPM isn't enabled in new accounts automatically. The default value is `false`.
If the `ConfigurationType` of your organization is set to `CENTRAL`, then this field is set to `false` and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which Security Hub CSPM is enabled and associate the policy with new organization accounts.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoEnableStandards`  <a name="cfn-securityhub-organizationconfiguration-autoenablestandards"></a>
Whether to automatically enable Security Hub CSPM [default standards](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html) in new member accounts when they join the organization.
The default value of this parameter is equal to `DEFAULT`.
If equal to `DEFAULT`, then Security Hub CSPM default standards are automatically enabled for new member accounts. If equal to `NONE`, then default standards are not automatically enabled for new member accounts.
If the `ConfigurationType` of your organization is set to `CENTRAL`, then this field is set to `NONE` and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which specific security standards are enabled and associate the policy with new organization accounts.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigurationType`  <a name="cfn-securityhub-organizationconfiguration-configurationtype"></a>
 Indicates whether the organization uses local or central configuration.
If you use local configuration, the Security Hub CSPM delegated administrator can set `AutoEnable` to `true` and `AutoEnableStandards` to `DEFAULT`. This automatically enables Security Hub CSPM and default security standards in new organization accounts. These new account settings must be set separately in each AWS Region, and settings may be different in each Region.
 If you use central configuration, the delegated administrator can create configuration policies. Configuration policies can be used to configure Security Hub CSPM, security standards, and security controls in multiple accounts and Regions. If you want new organization accounts to use a specific configuration, you can create a configuration policy and associate it with the root or specific organizational units (OUs). New accounts will inherit the policy from the root or their assigned OU.
*Required*: No
*Type*: String
*Allowed values*: `CENTRAL | LOCAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-organizationconfiguration-return-values"></a>

### Ref
<a name="aws-resource-securityhub-organizationconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the organization configuration identifier, formatted as `AccountId/Region/securityhub-organization-configuration`. For example, `123456789012/us-east-1/securityhub-organization-configuration`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-organizationconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-organizationconfiguration-return-values-fn--getatt-fn--getatt"></a>

`MemberAccountLimitReached`  <a name="MemberAccountLimitReached-fn::getatt"></a>
Whether the maximum number of allowed member accounts are already associated with the Security Hub CSPM administrator account.

`OrganizationConfigurationIdentifier`  <a name="OrganizationConfigurationIdentifier-fn::getatt"></a>
The organization configuration identifier, formatted as `AccountId/Region/securityhub-organization-configuration`. For example, `123456789012/us-east-1/securityhub-organization-configuration`.

`Status`  <a name="Status-fn::getatt"></a>
 Describes whether central configuration could be enabled as the `ConfigurationType` for the organization. If your `ConfigurationType` is local configuration, then the value of `Status` is always `ENABLED`.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
 Provides an explanation if the value of `Status` is equal to `FAILED` when `ConfigurationType` is equal to `CENTRAL`.

## Examples
<a name="aws-resource-securityhub-organizationconfiguration--examples"></a>

### Configuring your organization in Security Hub CSPM
<a name="aws-resource-securityhub-organizationconfiguration--examples--Configuring_your_organization_in"></a>

The following example configures organization settings in Security Hub CSPM.

#### JSON
<a name="aws-resource-securityhub-organizationconfiguration--examples--Configuring_your_organization_in--json"></a>

```
{
	"Description": "Example template to configure an organization in Security Hub",
	"Resources": {
		"SecurityHubOrganizationConfiguration": {
			"Type": "AWS::SecurityHub::OrganizationConfiguration",
			"Properties": {
				"AutoEnable": false,
				"AutoEnableStandards": "NONE",
				"ConfigurationType": "CENTRAL"
			}
		}
	}
}
```

#### YAML
<a name="aws-resource-securityhub-organizationconfiguration--examples--Configuring_your_organization_in--yaml"></a>

```
Description: Example template to configure an organization in Security Hub
Resources:
  SecurityHubOrganizationConfiguration:
    Type: 'AWS::SecurityHub::OrganizationConfiguration'
    Properties:
      AutoEnable: false
      AutoEnableStandards: "NONE"
      ConfigurationType: "CENTRAL"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-policyassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::PolicyAssociation
<a name="aws-resource-securityhub-policyassociation"></a>

The `AWS::SecurityHub::PolicyAssociation` resource specifies associations for a configuration policy or a self-managed configuration. You can associate a AWS Security Hub CSPM configuration policy or self-managed configuration with the organization root, organizational units (OUs), or AWS accounts. After a successful association, the configuration policy takes effect in the specified targets. For more information, see [Creating and associating Security Hub CSPM configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/create-associate-policy.html) in the *AWS Security Hub CSPM User Guide*.

## Syntax
<a name="aws-resource-securityhub-policyassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-policyassociation-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::PolicyAssociation",
  "Properties" : {
      "[ConfigurationPolicyId](#cfn-securityhub-policyassociation-configurationpolicyid)" : {{String}},
      "[TargetId](#cfn-securityhub-policyassociation-targetid)" : {{String}},
      "[TargetType](#cfn-securityhub-policyassociation-targettype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-policyassociation-syntax.yaml"></a>

```
Type: AWS::SecurityHub::PolicyAssociation
Properties:
  [ConfigurationPolicyId](#cfn-securityhub-policyassociation-configurationpolicyid): {{String}}
  [TargetId](#cfn-securityhub-policyassociation-targetid): {{String}}
  [TargetType](#cfn-securityhub-policyassociation-targettype): {{String}}
```

## Properties
<a name="aws-resource-securityhub-policyassociation-properties"></a>

`ConfigurationPolicyId`  <a name="cfn-securityhub-policyassociation-configurationpolicyid"></a>
 The universally unique identifier (UUID) of the configuration policy. A self-managed configuration has no UUID. The identifier of a self-managed configuration is `SELF_MANAGED_SECURITY_HUB`.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^SELF_MANAGED_SECURITY_HUB$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetId`  <a name="cfn-securityhub-policyassociation-targetid"></a>
 The identifier of the target account, organizational unit, or the root.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetType`  <a name="cfn-securityhub-policyassociation-targettype"></a>
 Specifies whether the target is an AWS account, organizational unit, or the root.
*Required*: Yes
*Type*: String
*Allowed values*: `ACCOUNT | ORGANIZATIONAL_UNIT | ROOT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-securityhub-policyassociation-return-values"></a>

### Ref
<a name="aws-resource-securityhub-policyassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the association identifier, formatted as `TargetType/TargetId`. For example, `ACCOUNT/123456789012`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-policyassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-policyassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociationIdentifier`  <a name="AssociationIdentifier-fn::getatt"></a>
The association identifier, formatted as `TargetType/TargetId`. For example, `ACCOUNT/123456789012`.

`AssociationStatus`  <a name="AssociationStatus-fn::getatt"></a>
 The current status of the association between the specified target and the configuration.

`AssociationStatusMessage`  <a name="AssociationStatusMessage-fn::getatt"></a>
 The explanation for a `FAILED` value for `AssociationStatus`.

`AssociationType`  <a name="AssociationType-fn::getatt"></a>
 Indicates whether the association between the specified target and the configuration was directly applied by the AWS Security Hub CSPM delegated administrator or inherited from a parent.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
 The date and time, in UTC and ISO 8601 format, that the configuration policy association was last updated.

## Examples
<a name="aws-resource-securityhub-policyassociation--examples"></a>

### Association a configuration policy or self-managed configuration
<a name="aws-resource-securityhub-policyassociation--examples--Association_a_configuration_policy_or_self-managed_configuration"></a>

The following example associates the specified Security Hub CSPM configuration policy with the specified account.

#### JSON
<a name="aws-resource-securityhub-policyassociation--examples--Association_a_configuration_policy_or_self-managed_configuration--json"></a>

```
{
	"Description": "Example template to associate a Security Hub configuration policy or self-managed configuration",
	"Resources": {
		"SecurityHubPolicyAssociation": {
			"Type": "AWS::SecurityHub::PolicyAssociation",
			"Properties": {
				"TargetType": "ACCOUNT",
				"TargetId": "123456789012",
				"ConfigurationPolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
			}
		}
	}
}
```

#### YAML
<a name="aws-resource-securityhub-policyassociation--examples--Association_a_configuration_policy_or_self-managed_configuration--yaml"></a>

```
Description: Example template to associate a SecurityHub configuration policy or self-managed configuration
Resources:
  SecurityHubPolicyAssociation:
    Type: "AWS::SecurityHub::PolicyAssociation"
    Properties:
      TargetType: "ACCOUNT"
      TargetId: "123456789012"
      ConfigurationPolicyId: "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
```

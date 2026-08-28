---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-configurationpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConfigurationPolicy
<a name="aws-resource-securityhub-configurationpolicy"></a>

 The `AWS::SecurityHub::ConfigurationPolicy` resource creates a central configuration policy with the defined settings. Only the AWS Security Hub CSPM delegated administrator can create this resource in the home Region. For more information, see [Central configuration in Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/central-configuration-intro.html) in the *AWS Security Hub CSPM User Guide*.

## Syntax
<a name="aws-resource-securityhub-configurationpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-configurationpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::ConfigurationPolicy",
  "Properties" : {
      "[ConfigurationPolicy](#cfn-securityhub-configurationpolicy-configurationpolicy)" : {{Policy}},
      "[Description](#cfn-securityhub-configurationpolicy-description)" : {{String}},
      "[Name](#cfn-securityhub-configurationpolicy-name)" : {{String}},
      "[Tags](#cfn-securityhub-configurationpolicy-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-configurationpolicy-syntax.yaml"></a>

```
Type: AWS::SecurityHub::ConfigurationPolicy
Properties:
  [ConfigurationPolicy](#cfn-securityhub-configurationpolicy-configurationpolicy): {{
    Policy}}
  [Description](#cfn-securityhub-configurationpolicy-description): {{String}}
  [Name](#cfn-securityhub-configurationpolicy-name): {{String}}
  [Tags](#cfn-securityhub-configurationpolicy-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-securityhub-configurationpolicy-properties"></a>

`ConfigurationPolicy`  <a name="cfn-securityhub-configurationpolicy-configurationpolicy"></a>
 An object that defines how AWS Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls).
*Required*: Yes
*Type*: [Policy](aws-properties-securityhub-configurationpolicy-policy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-securityhub-configurationpolicy-description"></a>
 The description of the configuration policy.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-securityhub-configurationpolicy-name"></a>
 The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: `-, ., !, *, /`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securityhub-configurationpolicy-tags"></a>
 User-defined tags associated with a configuration policy. For more information, see [Tagging AWS Security Hub CSPM resources](https://docs.aws.amazon.com/securityhub/latest/userguide/tagging-resources.html) in the *Security Hub CSPM user guide*.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]{1,128}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-configurationpolicy-return-values"></a>

### Ref
<a name="aws-resource-securityhub-configurationpolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the configuration policy. For example, `arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

### Fn::GetAtt
<a name="aws-resource-securityhub-configurationpolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-configurationpolicy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The ARN of the configuration policy.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
 The universally unique identifier (UUID) of the configuration policy. A self-managed configuration has no UUID. The identifier of a self-managed configuration is `SELF_MANAGED_SECURITY_HUB`.

`ServiceEnabled`  <a name="ServiceEnabled-fn::getatt"></a>
 Indicates whether the service that the configuration policy applies to is enabled in the policy.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
 The date and time, in UTC and ISO 8601 format, that the configuration policy was last updated.

## Examples
<a name="aws-resource-securityhub-configurationpolicy--examples"></a>

### Creating a Security Hub CSPM central configuration policy
<a name="aws-resource-securityhub-configurationpolicy--examples--Creating_a_central_configuration_policy"></a>

The following example creates a configuration policy with the specified settings. Only the delegated Security Hub CSPM administrator can create a configuration policy from the home Region.

#### JSON
<a name="aws-resource-securityhub-configurationpolicy--examples--Creating_a_central_configuration_policy--json"></a>

```
{
	"Description": "Example template to create a SecurityHub configuration policy",
	"Resources": {
		"SecurityHubConfigurationPolicy": {
			"Type": "AWS::SecurityHub::ConfigurationPolicy",
			"Properties": {
				"Tags": {
					"key1": "value1"
				},
				"Name": "SecurityHubConfigurationPolicyExample",
				"Description": "Example template to create SecurityHub Configuration Policy",
				"ConfigurationPolicy" : {
      				"SecurityHub": {
        				"ServiceEnabled": true,
        				"EnabledStandardIdentifiers": [
        					"arn:aws:securityhub:us-west-2::standards/aws-foundational-security-best-practices/v/1.0.0"
        				],
        				"SecurityControlsConfiguration": {
          					"EnabledSecurityControlIdentifiers": [
          						"APIGateway.1",
          						"IAM.7",
          						"RDS.14",
          						"CloudFront.5",
          						"EC2.18","S3.11",
          						"CloudFront.6"
          					],
          					"SecurityControlCustomParameters": [
            					{
				              		"SecurityControlId": "APIGateway.1",
				              		"Parameters": {
				                		"loggingLevel": {
				                			"ValueType": "CUSTOM",
				                			"Value": {
				                				"Enum": "ERROR"
				                			}
				                		}
              				  		}
              					}
          					]
        				}
      				}
				}
			}
		}
	}
}
```

#### YAML
<a name="aws-resource-securityhub-configurationpolicy--examples--Creating_a_central_configuration_policy--yaml"></a>

```
Description: Example template to create a Security Hub configuration policy
Resources:
  SecurityHubConfigurationPolicy:
    Type: "AWS::SecurityHub::ConfigurationPolicy"
    Properties:
      Tags:
        key1: value1
      Name: "SecurityHubConfigurationPolicyExample"
      Description: "Example template to create SecurityHub Configuration Policy"
      ConfigurationPolicy:
        SecurityHub:
          ServiceEnabled: true
          EnabledStandardIdentifiers:
            - !Sub "arn:${AWS::Partition}:securityhub:${AWS::Region}::standards/aws-foundational-security-best-practices/v/1.0.0"
          SecurityControlsConfiguration:
            EnabledSecurityControlIdentifiers:
              - "APIGateway.1"
              - "IAM.7"
              - "RDS.14"
              - "CloudFront.5"
              - "EC2.18"
              - "S3.11"
              - "CloudFront.6"
            SecurityControlCustomParameters:
              - SecurityControlId: "APIGateway.1"
                Parameters:
                  loggingLevel:
                    ValueType: "CUSTOM"
                    Value:
                      Enum: "ERROR"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

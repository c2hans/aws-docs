---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule TagPropagationConfiguration
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration"></a>

Specifies configuration for propagating resource tags from source log groups to centralized destination log groups. The service uses a customer-managed IAM role in the destination account to add, update, and remove tags on destination log groups.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration-syntax.json"></a>

```
{
  "[DestinationRoleArn](#cfn-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration-destinationrolearn)" : {{String}},
  "[TagConflictResolutionStrategy](#cfn-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration-tagconflictresolutionstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration-syntax.yaml"></a>

```
  [DestinationRoleArn](#cfn-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration-destinationrolearn): {{String}}
  [TagConflictResolutionStrategy](#cfn-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration-tagconflictresolutionstrategy): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration-properties"></a>

`DestinationRoleArn`  <a name="cfn-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration-destinationrolearn"></a>
The ARN of a customer-managed IAM role in the destination account. The service assumes this role to propagate tags to destination log groups. You must have `iam:PassRole` permission on this role.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:iam::\d{12}:role/[\w+=,.@/-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagConflictResolutionStrategy`  <a name="cfn-observabilityadmin-organizationcentralizationrule-tagpropagationconfiguration-tagconflictresolutionstrategy"></a>
The strategy for resolving conflicts when a tag key exists on both the source and destination log groups. If not specified, defaults to `UPDATE_SYNC`.
+ `ADD_ONLY` – Only adds new tags from the source without modifying existing destination tags.
+ `UPDATE_SYNC` – Adds new tags and updates existing tags from the source. Does not remove destination tags that are absent from the source.
+ `IN_SYNC` – Keeps destination tags fully synchronized with source tags, including removing destination tags that do not exist on the source.
*Required*: No
*Type*: String
*Allowed values*: `IN_SYNC | ADD_ONLY | UPDATE_SYNC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

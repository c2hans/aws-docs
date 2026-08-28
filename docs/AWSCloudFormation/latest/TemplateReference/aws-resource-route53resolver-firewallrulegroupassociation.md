---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53resolver-firewallrulegroupassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::FirewallRuleGroupAssociation
<a name="aws-resource-route53resolver-firewallrulegroupassociation"></a>

An association between a firewall rule group and a VPC, which enables DNS filtering for the VPC.

## Syntax
<a name="aws-resource-route53resolver-firewallrulegroupassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53resolver-firewallrulegroupassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Route53Resolver::FirewallRuleGroupAssociation",
  "Properties" : {
      "[FirewallRuleGroupId](#cfn-route53resolver-firewallrulegroupassociation-firewallrulegroupid)" : {{String}},
      "[MutationProtection](#cfn-route53resolver-firewallrulegroupassociation-mutationprotection)" : {{String}},
      "[Name](#cfn-route53resolver-firewallrulegroupassociation-name)" : {{String}},
      "[Priority](#cfn-route53resolver-firewallrulegroupassociation-priority)" : {{Integer}},
      "[Tags](#cfn-route53resolver-firewallrulegroupassociation-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-route53resolver-firewallrulegroupassociation-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-route53resolver-firewallrulegroupassociation-syntax.yaml"></a>

```
Type: AWS::Route53Resolver::FirewallRuleGroupAssociation
Properties:
  [FirewallRuleGroupId](#cfn-route53resolver-firewallrulegroupassociation-firewallrulegroupid): {{String}}
  [MutationProtection](#cfn-route53resolver-firewallrulegroupassociation-mutationprotection): {{String}}
  [Name](#cfn-route53resolver-firewallrulegroupassociation-name): {{String}}
  [Priority](#cfn-route53resolver-firewallrulegroupassociation-priority): {{Integer}}
  [Tags](#cfn-route53resolver-firewallrulegroupassociation-tags): {{
    - Tag}}
  [VpcId](#cfn-route53resolver-firewallrulegroupassociation-vpcid): {{String}}
```

## Properties
<a name="aws-resource-route53resolver-firewallrulegroupassociation-properties"></a>

`FirewallRuleGroupId`  <a name="cfn-route53resolver-firewallrulegroupassociation-firewallrulegroupid"></a>
The unique identifier of the firewall rule group.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MutationProtection`  <a name="cfn-route53resolver-firewallrulegroupassociation-mutationprotection"></a>
If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-route53resolver-firewallrulegroupassociation-name"></a>
The name of the association.
*Required*: No
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-route53resolver-firewallrulegroupassociation-priority"></a>
The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting.
You must specify a unique priority for each rule group that you associate with a single VPC. To make it easier to insert rule groups later, leave space between the numbers, for example, use 101, 200, and so on. You can change the priority setting for a rule group association after you create it.
The allowed values for `Priority` are between 100 and 9900 (excluding 100 and 9900).
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-route53resolver-firewallrulegroupassociation-tags"></a>
A list of the tag keys and values that you want to associate with the rule group.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53resolver-firewallrulegroupassociation-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-route53resolver-firewallrulegroupassociation-vpcid"></a>
The unique identifier of the VPC that is associated with the rule group.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-route53resolver-firewallrulegroupassociation-return-values"></a>

### Ref
<a name="aws-resource-route53resolver-firewallrulegroupassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `FirewallRuleGroupAssociation` ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53resolver-firewallrulegroupassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53resolver-firewallrulegroupassociation-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the firewall rule group association.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The date and time that the association was created, in Unix time format and Coordinated Universal Time (UTC).

`CreatorRequestId`  <a name="CreatorRequestId-fn::getatt"></a>
A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.

`Id`  <a name="Id-fn::getatt"></a>
The identifier for the association.

`ManagedOwnerName`  <a name="ManagedOwnerName-fn::getatt"></a>
The owner of the association, used only for associations that are not managed by you. If you use AWS Firewall Manager to manage your firewallls from DNS Firewall, then this reports Firewall Manager as the managed owner.

`ModificationTime`  <a name="ModificationTime-fn::getatt"></a>
The date and time that the association was last modified, in Unix time format and Coordinated Universal Time (UTC).

`Status`  <a name="Status-fn::getatt"></a>
The current status of the association.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
Additional information about the status of the response, if available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

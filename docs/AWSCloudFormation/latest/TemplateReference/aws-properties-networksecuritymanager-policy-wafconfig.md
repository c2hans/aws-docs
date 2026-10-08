---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-policy-wafconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Policy WafConfig
<a name="aws-properties-networksecuritymanager-policy-wafconfig"></a>

AWS WAF-specific policy configuration settings. Specify this property only for policies whose `FirewallType` is `WAF`.

## Syntax
<a name="aws-properties-networksecuritymanager-policy-wafconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-policy-wafconfig-syntax.json"></a>

```
{
  "[ConflictResolution](#cfn-networksecuritymanager-policy-wafconfig-conflictresolution)" : {{String}},
  "[ExistingCustomerWebACLResolution](#cfn-networksecuritymanager-policy-wafconfig-existingcustomerwebaclresolution)" : {{String}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-policy-wafconfig-syntax.yaml"></a>

```
  [ConflictResolution](#cfn-networksecuritymanager-policy-wafconfig-conflictresolution): {{String}}
  [ExistingCustomerWebACLResolution](#cfn-networksecuritymanager-policy-wafconfig-existingcustomerwebaclresolution): {{String}}
```

## Properties
<a name="aws-properties-networksecuritymanager-policy-wafconfig-properties"></a>

`ConflictResolution`  <a name="cfn-networksecuritymanager-policy-wafconfig-conflictresolution"></a>
How Network Security Manager combines this policy's settings with the settings of other policies that apply to the same resource.
`MERGE_WHERE_APPLICABLE` combines the rule groups of every applicable policy into one configuration. Settings that can hold only a single value, such as the default action, are taken from the highest-priority policy. `MERGE_WHERE_APPLICABLE` is currently the only supported value.
This property is required when `FirewallType` is `WAF`.
*Allowed Values*: `MERGE_WHERE_APPLICABLE`
*Required*: Conditional
*Type*: String
*Allowed values*: `MERGE_WHERE_APPLICABLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExistingCustomerWebACLResolution`  <a name="cfn-networksecuritymanager-policy-wafconfig-existingcustomerwebaclresolution"></a>
Determines what Network Security Manager does when a resource in scope is already associated with a web ACL that you created yourself.
This setting applies only to resources that already have your own web ACL. A resource with no web ACL always receives a web ACL that Network Security Manager creates and manages, whatever you set here.
When more than one policy applies to the same resource, Network Security Manager uses the value from the highest-priority policy. Values from lower-priority policies are ignored.
 `RETROFIT`
Network Security Manager adds the policy's rule groups to your existing web ACL. You keep the web ACL and it stays associated with the resource, and the rules you defined in it are preserved. Policy-wide settings, including the default action and the visibility configuration, are replaced with the policy's values.
If your web ACL is also associated with resources that this policy doesn't apply to, Network Security Manager doesn't modify it. The resource is reported as out of sync, with an issue explaining that the web ACL is shared.
When the policy stops applying to the resource, Network Security Manager stops managing your web ACL but doesn't remove the rule groups it added. To remove them, edit the web ACL yourself.
 `OVERRIDE_ASSOCIATION`
Network Security Manager associates a web ACL that it manages with the resource, replacing your association. Your web ACL is detached but is never deleted, and its own configuration is unchanged.
Network Security Manager doesn't record which web ACL it displaced and doesn't restore it. When the policy stops applying to the resource, the managed web ACL is removed and the resource is left with no web ACL. To restore your own web ACL, associate it with the resource again.
 `NO_REMEDIATION`
Network Security Manager leaves the resource and your web ACL unchanged, and doesn't create a managed web ACL for the resource. The policy's rule groups are not applied, so the resource isn't protected by this policy.
The resource is reported as out of sync for as long as this value is in effect, with an issue that names this setting as the reason and suggests changing it to `RETROFIT` or `OVERRIDE_ASSOCIATION`.
This property is required when `FirewallType` is `WAF`.
*Allowed Values*: `RETROFIT` \| `OVERRIDE_ASSOCIATION` \| `NO_REMEDIATION`
*Required*: Conditional
*Type*: String
*Allowed values*: `RETROFIT | OVERRIDE_ASSOCIATION | NO_REMEDIATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

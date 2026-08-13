---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53resolver-firewallconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::FirewallConfig
<a name="aws-resource-route53resolver-firewallconfig"></a>

Configuration of the firewall behavior provided by DNS Firewall for a single VPC from Amazon Virtual Private Cloud (Amazon VPC).

## Syntax
<a name="aws-resource-route53resolver-firewallconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53resolver-firewallconfig-syntax.json"></a>

```
{
  "Type" : "AWS::Route53Resolver::FirewallConfig",
  "Properties" : {
      "[FirewallFailOpen](#cfn-route53resolver-firewallconfig-firewallfailopen)" : {{String}},
      "[ResourceId](#cfn-route53resolver-firewallconfig-resourceid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-route53resolver-firewallconfig-syntax.yaml"></a>

```
Type: AWS::Route53Resolver::FirewallConfig
Properties:
  [FirewallFailOpen](#cfn-route53resolver-firewallconfig-firewallfailopen): {{String}}
  [ResourceId](#cfn-route53resolver-firewallconfig-resourceid): {{String}}
```

## Properties
<a name="aws-resource-route53resolver-firewallconfig-properties"></a>

`FirewallFailOpen`  <a name="cfn-route53resolver-firewallconfig-firewallfailopen"></a>
Determines how DNS Firewall operates during failures, for example when all traffic that is sent to DNS Firewall fails to receive a reply.
+ By default, fail open is disabled, which means the failure mode is closed. This approach favors security over availability. DNS Firewall returns a failure error when it is unable to properly evaluate a query.
+ If you enable this option, the failure mode is open. This approach favors availability over security. DNS Firewall allows queries to proceed if it is unable to properly evaluate them.
This behavior is only enforced for VPCs that have at least one DNS Firewall rule group association.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED | USE_LOCAL_RESOURCE_SETTING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceId`  <a name="cfn-route53resolver-firewallconfig-resourceid"></a>
The ID of the VPC that this firewall configuration applies to.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-route53resolver-firewallconfig-return-values"></a>

### Ref
<a name="aws-resource-route53resolver-firewallconfig-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53resolver-firewallconfig-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53resolver-firewallconfig-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the firewall configuration.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The AWS account ID of the owner of the VPC that this firewall configuration applies to.

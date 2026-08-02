---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53globalresolver-firewalldomainlist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53GlobalResolver::FirewallDomainList
<a name="aws-resource-route53globalresolver-firewalldomainlist"></a>

Creates a firewall domain list. Domain lists are reusable sets of domain specifications that you use in DNS firewall rules to allow, block, or alert on DNS queries to specific domains.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Syntax
<a name="aws-resource-route53globalresolver-firewalldomainlist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53globalresolver-firewalldomainlist-syntax.json"></a>

```
{
  "Type" : "AWS::Route53GlobalResolver::FirewallDomainList",
  "Properties" : {
      "[ClientToken](#cfn-route53globalresolver-firewalldomainlist-clienttoken)" : {{String}},
      "[Description](#cfn-route53globalresolver-firewalldomainlist-description)" : {{String}},
      "[DomainFileUrl](#cfn-route53globalresolver-firewalldomainlist-domainfileurl)" : {{String}},
      "[Domains](#cfn-route53globalresolver-firewalldomainlist-domains)" : {{[ String, ... ]}},
      "[GlobalResolverId](#cfn-route53globalresolver-firewalldomainlist-globalresolverid)" : {{String}},
      "[Name](#cfn-route53globalresolver-firewalldomainlist-name)" : {{String}},
      "[Tags](#cfn-route53globalresolver-firewalldomainlist-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53globalresolver-firewalldomainlist-syntax.yaml"></a>

```
Type: AWS::Route53GlobalResolver::FirewallDomainList
Properties:
  [ClientToken](#cfn-route53globalresolver-firewalldomainlist-clienttoken): {{String}}
  [Description](#cfn-route53globalresolver-firewalldomainlist-description): {{String}}
  [DomainFileUrl](#cfn-route53globalresolver-firewalldomainlist-domainfileurl): {{String}}
  [Domains](#cfn-route53globalresolver-firewalldomainlist-domains): {{
    - String}}
  [GlobalResolverId](#cfn-route53globalresolver-firewalldomainlist-globalresolverid): {{String}}
  [Name](#cfn-route53globalresolver-firewalldomainlist-name): {{String}}
  [Tags](#cfn-route53globalresolver-firewalldomainlist-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53globalresolver-firewalldomainlist-properties"></a>

`ClientToken`  <a name="cfn-route53globalresolver-firewalldomainlist-clienttoken"></a>
A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same `clientToken` has the same result every time.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-route53globalresolver-firewalldomainlist-description"></a>
A description of the firewall domain list.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainFileUrl`  <a name="cfn-route53globalresolver-firewalldomainlist-domainfileurl"></a>
The fully qualified URL of the file in Amazon S3 that contains the list of domains to import. The file should contain one domain per line.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domains`  <a name="cfn-route53globalresolver-firewalldomainlist-domains"></a>
A list of the domains. You can add up to 1000 domains per request.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalResolverId`  <a name="cfn-route53globalresolver-firewalldomainlist-globalresolverid"></a>
The ID of the global resolver that the firewall domain list is associated with.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-route53globalresolver-firewalldomainlist-name"></a>
The name of the firewall domain list.
*Required*: Yes
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9-_' ']+)`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-route53globalresolver-firewalldomainlist-tags"></a>
An array of user-defined keys and optional values. These tags can be used for categorization and organization.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53globalresolver-firewalldomainlist-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53globalresolver-firewalldomainlist-return-values"></a>

### Ref
<a name="aws-resource-route53globalresolver-firewalldomainlist-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53globalresolver-firewalldomainlist-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53globalresolver-firewalldomainlist-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the firewall domain list.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the firewall domain list was created.

`DomainCount`  <a name="DomainCount-fn::getatt"></a>
Number of domains in the domain list.

`FirewallDomainListId`  <a name="FirewallDomainListId-fn::getatt"></a>
ID of the domain list.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the firewall domain list.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
Additional information about the status of the domain list.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the firewall domain list was last updated.

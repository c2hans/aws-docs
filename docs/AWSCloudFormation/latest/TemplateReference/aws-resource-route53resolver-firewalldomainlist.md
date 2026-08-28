---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53resolver-firewalldomainlist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::FirewallDomainList
<a name="aws-resource-route53resolver-firewalldomainlist"></a>

High-level information about a list of firewall domains for use in a [AWS::Route53Resolver::FirewallRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-rule.html). This is returned by [GetFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallDomainList.html).

To retrieve the domains that are defined for this domain list, call [ListFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallDomains.html).

## Syntax
<a name="aws-resource-route53resolver-firewalldomainlist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53resolver-firewalldomainlist-syntax.json"></a>

```
{
  "Type" : "AWS::Route53Resolver::FirewallDomainList",
  "Properties" : {
      "[DomainFileUrl](#cfn-route53resolver-firewalldomainlist-domainfileurl)" : {{String}},
      "[Domains](#cfn-route53resolver-firewalldomainlist-domains)" : {{[ String, ... ]}},
      "[Name](#cfn-route53resolver-firewalldomainlist-name)" : {{String}},
      "[Tags](#cfn-route53resolver-firewalldomainlist-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53resolver-firewalldomainlist-syntax.yaml"></a>

```
Type: AWS::Route53Resolver::FirewallDomainList
Properties:
  [DomainFileUrl](#cfn-route53resolver-firewalldomainlist-domainfileurl): {{String}}
  [Domains](#cfn-route53resolver-firewalldomainlist-domains): {{
    - String}}
  [Name](#cfn-route53resolver-firewalldomainlist-name): {{String}}
  [Tags](#cfn-route53resolver-firewalldomainlist-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53resolver-firewalldomainlist-properties"></a>

`DomainFileUrl`  <a name="cfn-route53resolver-firewalldomainlist-domainfileurl"></a>
The fully qualified URL or URI of the file stored in Amazon Simple Storage Service (Amazon S3) that contains the list of domains to import.
The file must be in an S3 bucket that's in the same Region as your DNS Firewall. The file must be a text file and must contain a single domain per line.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domains`  <a name="cfn-route53resolver-firewalldomainlist-domains"></a>
A list of the domain lists that you have defined.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-route53resolver-firewalldomainlist-name"></a>
The name of the domain list.
*Required*: No
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-route53resolver-firewalldomainlist-tags"></a>
A list of the tag keys and values that you want to associate with the domain list.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53resolver-firewalldomainlist-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53resolver-firewalldomainlist-return-values"></a>

### Ref
<a name="aws-resource-route53resolver-firewalldomainlist-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `FirewallDomainList` object.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53resolver-firewalldomainlist-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53resolver-firewalldomainlist-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the firewall domain list.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The date and time that the domain list was created, in Unix time format and Coordinated Universal Time (UTC).

`CreatorRequestId`  <a name="CreatorRequestId-fn::getatt"></a>
A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.

`DomainCount`  <a name="DomainCount-fn::getatt"></a>
The number of domain names that are specified in the domain list.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the domain list.

`ManagedOwnerName`  <a name="ManagedOwnerName-fn::getatt"></a>
The owner of the list, used only for lists that are not managed by you. For example, the managed domain list `AWSManagedDomainsMalwareDomainList` has the managed owner name `Route 53 Resolver DNS Firewall`.

`ModificationTime`  <a name="ModificationTime-fn::getatt"></a>
The date and time that the domain list was last modified, in Unix time format and Coordinated Universal Time (UTC).

`Status`  <a name="Status-fn::getatt"></a>
The status of the domain list.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
Additional information about the status of the list, if available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-connectpeer-bgpoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::ConnectPeer BgpOptions
<a name="aws-properties-networkmanager-connectpeer-bgpoptions"></a>

Describes the BGP options.

## Syntax
<a name="aws-properties-networkmanager-connectpeer-bgpoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-connectpeer-bgpoptions-syntax.json"></a>

```
{
  "[PeerAsn](#cfn-networkmanager-connectpeer-bgpoptions-peerasn)" : {{Number}}
}
```

### YAML
<a name="aws-properties-networkmanager-connectpeer-bgpoptions-syntax.yaml"></a>

```
  [PeerAsn](#cfn-networkmanager-connectpeer-bgpoptions-peerasn): {{Number}}
```

## Properties
<a name="aws-properties-networkmanager-connectpeer-bgpoptions-properties"></a>

`PeerAsn`  <a name="cfn-networkmanager-connectpeer-bgpoptions-peerasn"></a>
The Peer ASN of the BGP.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-connectattachment-connectattachmentoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::ConnectAttachment ConnectAttachmentOptions
<a name="aws-properties-networkmanager-connectattachment-connectattachmentoptions"></a>

Describes a core network Connect attachment options.

## Syntax
<a name="aws-properties-networkmanager-connectattachment-connectattachmentoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-connectattachment-connectattachmentoptions-syntax.json"></a>

```
{
  "[Protocol](#cfn-networkmanager-connectattachment-connectattachmentoptions-protocol)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkmanager-connectattachment-connectattachmentoptions-syntax.yaml"></a>

```
  [Protocol](#cfn-networkmanager-connectattachment-connectattachmentoptions-protocol): {{String}}
```

## Properties
<a name="aws-properties-networkmanager-connectattachment-connectattachmentoptions-properties"></a>

`Protocol`  <a name="cfn-networkmanager-connectattachment-connectattachmentoptions-protocol"></a>
The protocol used for the attachment connection.
*Required*: No
*Type*: String
*Allowed values*: `GRE | NO_ENCAP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

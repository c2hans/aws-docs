---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcaconnectorad-template-keyusagepropertyflags.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorAD::Template KeyUsagePropertyFlags
<a name="aws-properties-pcaconnectorad-template-keyusagepropertyflags"></a>

Specifies key usage.

## Syntax
<a name="aws-properties-pcaconnectorad-template-keyusagepropertyflags-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcaconnectorad-template-keyusagepropertyflags-syntax.json"></a>

```
{
  "[Decrypt](#cfn-pcaconnectorad-template-keyusagepropertyflags-decrypt)" : {{Boolean}},
  "[KeyAgreement](#cfn-pcaconnectorad-template-keyusagepropertyflags-keyagreement)" : {{Boolean}},
  "[Sign](#cfn-pcaconnectorad-template-keyusagepropertyflags-sign)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-pcaconnectorad-template-keyusagepropertyflags-syntax.yaml"></a>

```
  [Decrypt](#cfn-pcaconnectorad-template-keyusagepropertyflags-decrypt): {{Boolean}}
  [KeyAgreement](#cfn-pcaconnectorad-template-keyusagepropertyflags-keyagreement): {{Boolean}}
  [Sign](#cfn-pcaconnectorad-template-keyusagepropertyflags-sign): {{Boolean}}
```

## Properties
<a name="aws-properties-pcaconnectorad-template-keyusagepropertyflags-properties"></a>

`Decrypt`  <a name="cfn-pcaconnectorad-template-keyusagepropertyflags-decrypt"></a>
Allows key for encryption and decryption.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyAgreement`  <a name="cfn-pcaconnectorad-template-keyusagepropertyflags-keyagreement"></a>
Allows key exchange without encryption.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sign`  <a name="cfn-pcaconnectorad-template-keyusagepropertyflags-sign"></a>
Allow key use for digital signature.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcaconnectorad-template-privatekeyattributesv2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorAD::Template PrivateKeyAttributesV2
<a name="aws-properties-pcaconnectorad-template-privatekeyattributesv2"></a>

Defines the attributes of the private key.

## Syntax
<a name="aws-properties-pcaconnectorad-template-privatekeyattributesv2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcaconnectorad-template-privatekeyattributesv2-syntax.json"></a>

```
{
  "[CryptoProviders](#cfn-pcaconnectorad-template-privatekeyattributesv2-cryptoproviders)" : {{[ String, ... ]}},
  "[KeySpec](#cfn-pcaconnectorad-template-privatekeyattributesv2-keyspec)" : {{String}},
  "[MinimalKeyLength](#cfn-pcaconnectorad-template-privatekeyattributesv2-minimalkeylength)" : {{Number}}
}
```

### YAML
<a name="aws-properties-pcaconnectorad-template-privatekeyattributesv2-syntax.yaml"></a>

```
  [CryptoProviders](#cfn-pcaconnectorad-template-privatekeyattributesv2-cryptoproviders): {{
    - String}}
  [KeySpec](#cfn-pcaconnectorad-template-privatekeyattributesv2-keyspec): {{String}}
  [MinimalKeyLength](#cfn-pcaconnectorad-template-privatekeyattributesv2-minimalkeylength): {{Number}}
```

## Properties
<a name="aws-properties-pcaconnectorad-template-privatekeyattributesv2-properties"></a>

`CryptoProviders`  <a name="cfn-pcaconnectorad-template-privatekeyattributesv2-cryptoproviders"></a>
Defines the cryptographic providers used to generate the private key.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `100 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeySpec`  <a name="cfn-pcaconnectorad-template-privatekeyattributesv2-keyspec"></a>
Defines the purpose of the private key. Set it to "KEY\_EXCHANGE" or "SIGNATURE" value.
*Required*: Yes
*Type*: String
*Allowed values*: `KEY_EXCHANGE | SIGNATURE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimalKeyLength`  <a name="cfn-pcaconnectorad-template-privatekeyattributesv2-minimalkeylength"></a>
Set the minimum key length of the private key.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iam-samlprovider-samlprivatekey.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IAM::SAMLProvider SAMLPrivateKey
<a name="aws-properties-iam-samlprovider-samlprivatekey"></a>

Contains the private keys for the SAML provider.

This data type is used as a response element in the [GetSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSAMLProvider.html) operation.

## Syntax
<a name="aws-properties-iam-samlprovider-samlprivatekey-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iam-samlprovider-samlprivatekey-syntax.json"></a>

```
{
  "[KeyId](#cfn-iam-samlprovider-samlprivatekey-keyid)" : {{String}},
  "[Timestamp](#cfn-iam-samlprovider-samlprivatekey-timestamp)" : {{String}}
}
```

### YAML
<a name="aws-properties-iam-samlprovider-samlprivatekey-syntax.yaml"></a>

```
  [KeyId](#cfn-iam-samlprovider-samlprivatekey-keyid): {{String}}
  [Timestamp](#cfn-iam-samlprovider-samlprivatekey-timestamp): {{String}}
```

## Properties
<a name="aws-properties-iam-samlprovider-samlprivatekey-properties"></a>

`KeyId`  <a name="cfn-iam-samlprovider-samlprivatekey-keyid"></a>
The unique identifier for the SAML private key.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Z0-9]+`
*Minimum*: `22`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timestamp`  <a name="cfn-iam-samlprovider-samlprivatekey-timestamp"></a>
The date and time, in [ISO 8601 date-time ](http://www.iso.org/iso/iso8601) format, when the private key was uploaded.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

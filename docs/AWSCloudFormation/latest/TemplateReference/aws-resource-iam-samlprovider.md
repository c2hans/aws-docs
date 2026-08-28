---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-samlprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IAM::SAMLProvider
<a name="aws-resource-iam-samlprovider"></a>

Creates an IAM resource that describes an identity provider (IdP) that supports SAML 2.0.

The SAML provider resource that you create with this operation can be used as a principal in an IAM role's trust policy. Such a policy can enable federated users who sign in using the SAML IdP to assume the role. You can create an IAM role that supports Web-based single sign-on (SSO) to the AWS Management Console or one that supports API access to AWS.

When you create the SAML provider resource, you upload a SAML metadata document that you get from your IdP. That document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that the IdP sends. You must generate the metadata document using the identity management software that is used as your organization's IdP.

**Note**
 This operation requires [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

 For more information, see [Enabling SAML 2.0 federated users to access the AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html) and [About SAML 2.0-based federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html) in the *IAM User Guide*.

## Syntax
<a name="aws-resource-iam-samlprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iam-samlprovider-syntax.json"></a>

```
{
  "Type" : "AWS::IAM::SAMLProvider",
  "Properties" : {
      "[AddPrivateKey](#cfn-iam-samlprovider-addprivatekey)" : {{String}},
      "[AssertionEncryptionMode](#cfn-iam-samlprovider-assertionencryptionmode)" : {{String}},
      "[Name](#cfn-iam-samlprovider-name)" : {{String}},
      "[PrivateKeyList](#cfn-iam-samlprovider-privatekeylist)" : {{[ SAMLPrivateKey, ... ]}},
      "[RemovePrivateKey](#cfn-iam-samlprovider-removeprivatekey)" : {{String}},
      "[SamlMetadataDocument](#cfn-iam-samlprovider-samlmetadatadocument)" : {{String}},
      "[Tags](#cfn-iam-samlprovider-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iam-samlprovider-syntax.yaml"></a>

```
Type: AWS::IAM::SAMLProvider
Properties:
  [AddPrivateKey](#cfn-iam-samlprovider-addprivatekey): {{String}}
  [AssertionEncryptionMode](#cfn-iam-samlprovider-assertionencryptionmode): {{String}}
  [Name](#cfn-iam-samlprovider-name): {{String}}
  [PrivateKeyList](#cfn-iam-samlprovider-privatekeylist): {{
    - SAMLPrivateKey}}
  [RemovePrivateKey](#cfn-iam-samlprovider-removeprivatekey): {{String}}
  [SamlMetadataDocument](#cfn-iam-samlprovider-samlmetadatadocument): {{String}}
  [Tags](#cfn-iam-samlprovider-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iam-samlprovider-properties"></a>

`AddPrivateKey`  <a name="cfn-iam-samlprovider-addprivatekey"></a>
Specifies the new private key from your external identity provider. The private key must be a .pem file that uses AES-GCM or AES-CBC encryption algorithm to decrypt SAML assertions.
*Required*: No
*Type*: String
*Pattern*: `[\u0009\u000A\u000D\u0020-\u00FF]+`
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AssertionEncryptionMode`  <a name="cfn-iam-samlprovider-assertionencryptionmode"></a>
Specifies the encryption setting for the SAML provider.
*Required*: No
*Type*: String
*Allowed values*: `Allowed | Required`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iam-samlprovider-name"></a>
The name of the provider to create.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
*Required*: No
*Type*: String
*Pattern*: `[\w._-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateKeyList`  <a name="cfn-iam-samlprovider-privatekeylist"></a>
The private key metadata for the SAML provider.
*Required*: No
*Type*: Array of [SAMLPrivateKey](aws-properties-iam-samlprovider-samlprivatekey.md)
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemovePrivateKey`  <a name="cfn-iam-samlprovider-removeprivatekey"></a>
The Key ID of the private key to remove.
*Required*: No
*Type*: String
*Pattern*: `[A-Z0-9]+`
*Minimum*: `22`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SamlMetadataDocument`  <a name="cfn-iam-samlprovider-samlmetadatadocument"></a>
An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP.
For more information, see [About SAML 2.0-based federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html) in the *IAM User Guide*
*Required*: No
*Type*: String
*Minimum*: `1000`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iam-samlprovider-tags"></a>
A list of tags that you want to attach to the new IAM SAML provider. Each tag consists of a key name and an associated value. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.
*Required*: No
*Type*: Array of [Tag](aws-properties-iam-samlprovider-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iam-samlprovider-return-values"></a>

### Ref
<a name="aws-resource-iam-samlprovider-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iam-samlprovider-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iam-samlprovider-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) for the specified `AWS::IAM::SAMLProvider` resource.

`SamlProviderUUID`  <a name="SamlProviderUUID-fn::getatt"></a>
The unique identifier assigned to the SAML provider.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

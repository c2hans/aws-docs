---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-finspace-environment-federationparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FinSpace::Environment FederationParameters
<a name="aws-properties-finspace-environment-federationparameters"></a>

Configuration information when authentication mode is FEDERATED.

## Syntax
<a name="aws-properties-finspace-environment-federationparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-finspace-environment-federationparameters-syntax.json"></a>

```
{
  "[ApplicationCallBackURL](#cfn-finspace-environment-federationparameters-applicationcallbackurl)" : {{String}},
  "[AttributeMap](#cfn-finspace-environment-federationparameters-attributemap)" : {{[ AttributeMapItems, ... ]}},
  "[FederationProviderName](#cfn-finspace-environment-federationparameters-federationprovidername)" : {{String}},
  "[FederationURN](#cfn-finspace-environment-federationparameters-federationurn)" : {{String}},
  "[SamlMetadataDocument](#cfn-finspace-environment-federationparameters-samlmetadatadocument)" : {{String}},
  "[SamlMetadataURL](#cfn-finspace-environment-federationparameters-samlmetadataurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-finspace-environment-federationparameters-syntax.yaml"></a>

```
  [ApplicationCallBackURL](#cfn-finspace-environment-federationparameters-applicationcallbackurl): {{String}}
  [AttributeMap](#cfn-finspace-environment-federationparameters-attributemap): {{
    - AttributeMapItems}}
  [FederationProviderName](#cfn-finspace-environment-federationparameters-federationprovidername): {{String}}
  [FederationURN](#cfn-finspace-environment-federationparameters-federationurn): {{String}}
  [SamlMetadataDocument](#cfn-finspace-environment-federationparameters-samlmetadatadocument): {{String}}
  [SamlMetadataURL](#cfn-finspace-environment-federationparameters-samlmetadataurl): {{String}}
```

## Properties
<a name="aws-properties-finspace-environment-federationparameters-properties"></a>

`ApplicationCallBackURL`  <a name="cfn-finspace-environment-federationparameters-applicationcallbackurl"></a>
The redirect or sign-in URL that should be entered into the SAML 2.0 compliant identity provider configuration (IdP).
*Required*: No
*Type*: String
*Pattern*: `^https?://[-a-zA-Z0-9+&amp;@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&amp;@#/%=~_|]{1,1000}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AttributeMap`  <a name="cfn-finspace-environment-federationparameters-attributemap"></a>
SAML attribute name and value. The name must always be `Email` and the value should be set to the attribute definition in which user email is set. For example, name would be `Email` and value `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`. Please check your SAML 2.0 compliant identity provider (IdP) documentation for details.
*Required*: No
*Type*: Array of [AttributeMapItems](aws-properties-finspace-environment-attributemapitems.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FederationProviderName`  <a name="cfn-finspace-environment-federationparameters-federationprovidername"></a>
Name of the identity provider (IdP).
*Required*: No
*Type*: String
*Pattern*: `[^_\p{Z}][\p{L}\p{M}\p{S}\p{N}\p{P}][^_\p{Z}]+`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FederationURN`  <a name="cfn-finspace-environment-federationparameters-federationurn"></a>
The Uniform Resource Name (URN). Also referred as Service Provider URN or Audience URI or Service Provider Entity ID.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9._\-:\/#\+]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SamlMetadataDocument`  <a name="cfn-finspace-environment-federationparameters-samlmetadatadocument"></a>
SAML 2.0 Metadata document from identity provider (IdP).
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1000`
*Maximum*: `10000000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SamlMetadataURL`  <a name="cfn-finspace-environment-federationparameters-samlmetadataurl"></a>
Provide the metadata URL from your SAML 2.0 compliant identity provider (IdP).
*Required*: No
*Type*: String
*Pattern*: `^https?://[-a-zA-Z0-9+&amp;@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&amp;@#/%=~_|]{1,1000}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

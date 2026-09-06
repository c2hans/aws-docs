---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspacesweb-identityprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::IdentityProvider
<a name="aws-resource-workspacesweb-identityprovider"></a>

This resource specifies an identity provider that is then associated with a web portal. This resource is not required if your portal's `AuthenticationType` is IAM Identity Center.

## Syntax
<a name="aws-resource-workspacesweb-identityprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspacesweb-identityprovider-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpacesWeb::IdentityProvider",
  "Properties" : {
      "[IdentityProviderDetails](#cfn-workspacesweb-identityprovider-identityproviderdetails)" : {{{{{Key}}: {{Value}}, ...}}},
      "[IdentityProviderName](#cfn-workspacesweb-identityprovider-identityprovidername)" : {{String}},
      "[IdentityProviderType](#cfn-workspacesweb-identityprovider-identityprovidertype)" : {{String}},
      "[PortalArn](#cfn-workspacesweb-identityprovider-portalarn)" : {{String}},
      "[Tags](#cfn-workspacesweb-identityprovider-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-workspacesweb-identityprovider-syntax.yaml"></a>

```
Type: AWS::WorkSpacesWeb::IdentityProvider
Properties:
  [IdentityProviderDetails](#cfn-workspacesweb-identityprovider-identityproviderdetails): {{
    {{Key}}: {{Value}}}}
  [IdentityProviderName](#cfn-workspacesweb-identityprovider-identityprovidername): {{String}}
  [IdentityProviderType](#cfn-workspacesweb-identityprovider-identityprovidertype): {{String}}
  [PortalArn](#cfn-workspacesweb-identityprovider-portalarn): {{String}}
  [Tags](#cfn-workspacesweb-identityprovider-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-workspacesweb-identityprovider-properties"></a>

`IdentityProviderDetails`  <a name="cfn-workspacesweb-identityprovider-identityproviderdetails"></a>
The identity provider details. The following list describes the provider detail keys for each identity provider type.
+ For Google and Login with Amazon:
  +  `client_id`
  +  `client_secret`
  +  `authorize_scopes`
+ For Facebook:
  +  `client_id`
  +  `client_secret`
  +  `authorize_scopes`
  +  `api_version`
+ For Sign in with Apple:
  +  `client_id`
  +  `team_id`
  +  `key_id`
  +  `private_key`
  +  `authorize_scopes`
+ For OIDC providers:
  +  `client_id`
  +  `client_secret`
  +  `attributes_request_method`
  +  `oidc_issuer`
  +  `authorize_scopes`
  +  `authorize_url` *if not available from discovery URL specified by oidc\_issuer key*
  +  `token_url` *if not available from discovery URL specified by oidc\_issuer key*
  +  `attributes_url` *if not available from discovery URL specified by oidc\_issuer key*
  +  `jwks_uri` *if not available from discovery URL specified by oidc\_issuer key*
+ For SAML providers:
  + `MetadataFile` OR `MetadataURL`
  + `IDPSignout` (boolean) *optional*
  + `IDPInit` (boolean) *optional*
  + `RequestSigningAlgorithm` (string) *optional* - Only accepts `rsa-sha256`
  + `EncryptedResponses` (boolean) *optional*
*Required*: Yes
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviderName`  <a name="cfn-workspacesweb-identityprovider-identityprovidername"></a>
The identity provider name.
*Required*: Yes
*Type*: String
*Pattern*: `^[^_][\p{L}\p{M}\p{S}\p{N}\p{P}][^_]+$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviderType`  <a name="cfn-workspacesweb-identityprovider-identityprovidertype"></a>
The identity provider type.
*Required*: Yes
*Type*: String
*Allowed values*: `SAML | Facebook | Google | LoginWithAmazon | SignInWithApple | OIDC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortalArn`  <a name="cfn-workspacesweb-identityprovider-portalarn"></a>
The ARN of the identity provider.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-workspacesweb-identityprovider-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-workspacesweb-identityprovider-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-workspacesweb-identityprovider-return-values"></a>

### Ref
<a name="aws-resource-workspacesweb-identityprovider-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource's Amazon Resource Name (ARN).

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-workspacesweb-identityprovider-return-values-fn--getatt"></a>

####
<a name="aws-resource-workspacesweb-identityprovider-return-values-fn--getatt-fn--getatt"></a>

`IdentityProviderArn`  <a name="IdentityProviderArn-fn::getatt"></a>
The ARN of the identity provider.

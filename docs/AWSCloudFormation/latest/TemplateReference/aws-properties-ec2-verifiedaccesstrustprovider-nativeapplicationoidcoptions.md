---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessTrustProvider NativeApplicationOidcOptions
<a name="aws-properties-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions"></a>

Describes the OpenID Connect (OIDC) options.

## Syntax
<a name="aws-properties-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-syntax.json"></a>

```
{
  "[AuthorizationEndpoint](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-authorizationendpoint)" : {{String}},
  "[ClientId](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-clientid)" : {{String}},
  "[ClientSecret](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-clientsecret)" : {{String}},
  "[Issuer](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-issuer)" : {{String}},
  "[PublicSigningKeyEndpoint](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-publicsigningkeyendpoint)" : {{String}},
  "[Scope](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-scope)" : {{String}},
  "[TokenEndpoint](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-tokenendpoint)" : {{String}},
  "[UserInfoEndpoint](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-userinfoendpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-syntax.yaml"></a>

```
  [AuthorizationEndpoint](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-authorizationendpoint): {{String}}
  [ClientId](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-clientid): {{String}}
  [ClientSecret](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-clientsecret): {{String}}
  [Issuer](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-issuer): {{String}}
  [PublicSigningKeyEndpoint](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-publicsigningkeyendpoint): {{String}}
  [Scope](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-scope): {{String}}
  [TokenEndpoint](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-tokenendpoint): {{String}}
  [UserInfoEndpoint](#cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-userinfoendpoint): {{String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-properties"></a>

`AuthorizationEndpoint`  <a name="cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-authorizationendpoint"></a>
The authorization endpoint of the IdP.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-clientid"></a>
The OAuth 2.0 client identifier.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-clientsecret"></a>
The OAuth 2.0 client secret.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-issuer"></a>
The OIDC issuer identifier of the IdP.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicSigningKeyEndpoint`  <a name="cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-publicsigningkeyendpoint"></a>
The public signing key endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-scope"></a>
The set of user claims to be requested from the IdP.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenEndpoint`  <a name="cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-tokenendpoint"></a>
The token endpoint of the IdP.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserInfoEndpoint`  <a name="cfn-ec2-verifiedaccesstrustprovider-nativeapplicationoidcoptions-userinfoendpoint"></a>
The user info endpoint of the IdP.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

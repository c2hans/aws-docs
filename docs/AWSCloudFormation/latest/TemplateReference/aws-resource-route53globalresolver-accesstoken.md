---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53globalresolver-accesstoken.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53GlobalResolver::AccessToken
<a name="aws-resource-route53globalresolver-accesstoken"></a>

Creates an access token for a DNS view. Access tokens provide token-based authentication for DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) connections to the Route 53 Global Resolver.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Syntax
<a name="aws-resource-route53globalresolver-accesstoken-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53globalresolver-accesstoken-syntax.json"></a>

```
{
  "Type" : "AWS::Route53GlobalResolver::AccessToken",
  "Properties" : {
      "[ClientToken](#cfn-route53globalresolver-accesstoken-clienttoken)" : {{String}},
      "[DnsViewId](#cfn-route53globalresolver-accesstoken-dnsviewid)" : {{String}},
      "[ExpiresAt](#cfn-route53globalresolver-accesstoken-expiresat)" : {{String}},
      "[Name](#cfn-route53globalresolver-accesstoken-name)" : {{String}},
      "[Tags](#cfn-route53globalresolver-accesstoken-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53globalresolver-accesstoken-syntax.yaml"></a>

```
Type: AWS::Route53GlobalResolver::AccessToken
Properties:
  [ClientToken](#cfn-route53globalresolver-accesstoken-clienttoken): {{String}}
  [DnsViewId](#cfn-route53globalresolver-accesstoken-dnsviewid): {{String}}
  [ExpiresAt](#cfn-route53globalresolver-accesstoken-expiresat): {{String}}
  [Name](#cfn-route53globalresolver-accesstoken-name): {{String}}
  [Tags](#cfn-route53globalresolver-accesstoken-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53globalresolver-accesstoken-properties"></a>

`ClientToken`  <a name="cfn-route53globalresolver-accesstoken-clienttoken"></a>
A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same `clientToken` has the same result every time.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DnsViewId`  <a name="cfn-route53globalresolver-accesstoken-dnsviewid"></a>
The ID of the DNS view associated with the token.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExpiresAt`  <a name="cfn-route53globalresolver-accesstoken-expiresat"></a>
The date and time when the token expires.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-route53globalresolver-accesstoken-name"></a>
The name of the token.
*Required*: No
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9-_' ']+)`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-route53globalresolver-accesstoken-tags"></a>
An array of user-defined keys and optional values. These tags can be used for categorization and organization.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53globalresolver-accesstoken-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53globalresolver-accesstoken-return-values"></a>

### Ref
<a name="aws-resource-route53globalresolver-accesstoken-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53globalresolver-accesstoken-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53globalresolver-accesstoken-return-values-fn--getatt-fn--getatt"></a>

`AccessTokenId`  <a name="AccessTokenId-fn::getatt"></a>
The unique identifier for the access token.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the token.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the token was created.

`GlobalResolverId`  <a name="GlobalResolverId-fn::getatt"></a>
The ID of the global resolver associated with the token.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the token.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the token was last updated.

`Value`  <a name="Value-fn::getatt"></a>
The access token value. This token should be included in DoH and DoT requests for authentication. Keep this value secure as it provides access to your Route 53 Global Resolver.

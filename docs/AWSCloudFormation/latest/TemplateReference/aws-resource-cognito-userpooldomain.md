---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpooldomain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolDomain
<a name="aws-resource-cognito-userpooldomain"></a>

The AWS::Cognito::UserPoolDomain resource creates a new domain for a user pool.

## Syntax
<a name="aws-resource-cognito-userpooldomain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-userpooldomain-syntax.json"></a>

```
{
  "Type" : "AWS::Cognito::UserPoolDomain",
  "Properties" : {
      "[CustomDomainConfig](#cfn-cognito-userpooldomain-customdomainconfig)" : {{CustomDomainConfigType}},
      "[Domain](#cfn-cognito-userpooldomain-domain)" : {{String}},
      "[ManagedLoginVersion](#cfn-cognito-userpooldomain-managedloginversion)" : {{Integer}},
      "[Routing](#cfn-cognito-userpooldomain-routing)" : {{RoutingType}},
      "[UserPoolId](#cfn-cognito-userpooldomain-userpoolid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cognito-userpooldomain-syntax.yaml"></a>

```
Type: AWS::Cognito::UserPoolDomain
Properties:
  [CustomDomainConfig](#cfn-cognito-userpooldomain-customdomainconfig): {{
    CustomDomainConfigType}}
  [Domain](#cfn-cognito-userpooldomain-domain): {{String}}
  [ManagedLoginVersion](#cfn-cognito-userpooldomain-managedloginversion): {{Integer}}
  [Routing](#cfn-cognito-userpooldomain-routing): {{
    RoutingType}}
  [UserPoolId](#cfn-cognito-userpooldomain-userpoolid): {{String}}
```

## Properties
<a name="aws-resource-cognito-userpooldomain-properties"></a>

`CustomDomainConfig`  <a name="cfn-cognito-userpooldomain-customdomainconfig"></a>
The configuration for a custom domain that hosts the sign-up and sign-in pages for your application. Use this object to specify an SSL certificate that is managed by ACM.
When you create a custom domain, the passkey RP ID defaults to the custom domain. If you had a prefix domain active, this will cause passkey integration for your prefix domain to stop working due to a mismatch in RP ID. To keep the prefix domain passkey integration working, you can explicitly set RP ID to the prefix domain.
*Required*: No
*Type*: [CustomDomainConfigType](aws-properties-cognito-userpooldomain-customdomainconfigtype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domain`  <a name="cfn-cognito-userpooldomain-domain"></a>
The name of the domain that you want to update. For custom domains, this is the fully-qualified domain name, for example `auth.example.com`. For prefix domains, this is the prefix alone, such as `myprefix`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManagedLoginVersion`  <a name="cfn-cognito-userpooldomain-managedloginversion"></a>
A version number that indicates the state of managed login for your domain. Version `1` is hosted UI (classic). Version `2` is the newer managed login with the branding editor. For more information, see [Managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Routing`  <a name="cfn-cognito-userpooldomain-routing"></a>
The routing configuration for the user pool domain. Specifies failover settings for multi-region deployments.
*Required*: No
*Type*: [RoutingType](aws-properties-cognito-userpooldomain-routingtype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-cognito-userpooldomain-userpoolid"></a>
The ID of the user pool that is associated with the domain you're updating.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+_[0-9a-zA-Z]+`
*Minimum*: `1`
*Maximum*: `55`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cognito-userpooldomain-return-values"></a>

### Ref
<a name="aws-resource-cognito-userpooldomain-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns physicalResourceId, which is “Domain". For example:

 `{ "Ref": "your-test-domain" }`

For the Amazon Cognito user pool domain `your-test-domain`, Ref returns the name of the user pool domain.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cognito-userpooldomain-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cognito-userpooldomain-return-values-fn--getatt-fn--getatt"></a>

`CloudFrontDistribution`  <a name="CloudFrontDistribution-fn::getatt"></a>
The Amazon CloudFront endpoint that you use as the target of the alias that you set up with your Domain Name Service (DNS) provider.

## Examples
<a name="aws-resource-cognito-userpooldomain--examples"></a>

**Topics**
+ [Creating a new custom domain for a user pool](#aws-resource-cognito-userpooldomain--examples--Creating_a_new_custom_domain_for_a_user_pool)
+ [Creating a new default domain for a user pool](#aws-resource-cognito-userpooldomain--examples--Creating_a_new_default_domain_for_a_user_pool)

### Creating a new custom domain for a user pool
<a name="aws-resource-cognito-userpooldomain--examples--Creating_a_new_custom_domain_for_a_user_pool"></a>

The following example creates a custom domain, "my-test-user-pool-domain", in the referenced user pool.

#### JSON
<a name="aws-resource-cognito-userpooldomain--examples--Creating_a_new_custom_domain_for_a_user_pool--json"></a>

```
{
   "UserPoolDomain":{
      "Type":"AWS::Cognito::UserPoolDomain",
      "Properties":{
         "UserPoolId":{
            "Ref":"UserPool"
         },
         "Domain":"my-test-user-pool-domain.myapplication.com",
         "ManagedLoginVersion": "2",
         "CustomDomainConfig":{
            "CertificateArn":{
               "Ref":"CertificateArn"
            }
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-cognito-userpooldomain--examples--Creating_a_new_custom_domain_for_a_user_pool--yaml"></a>

```
UserPoolDomain:
  Type: AWS::Cognito::UserPoolDomain
  Properties:
    UserPoolId: !Ref UserPool
    Domain: "my-test-user-pool-domain.myapplication.com"
    ManagedLoginVersion: "2"
    CustomDomainConfig:
      CertificateArn: !Ref CertificateArn
```

### Creating a new default domain for a user pool
<a name="aws-resource-cognito-userpooldomain--examples--Creating_a_new_default_domain_for_a_user_pool"></a>

The following example creates a new default domain, "my-test-user-pool-domain", in the referenced user pool.

#### JSON
<a name="aws-resource-cognito-userpooldomain--examples--Creating_a_new_default_domain_for_a_user_pool--json"></a>

```
{
   "UserPoolDomain":{
      "Type":"AWS::Cognito::UserPoolDomain",
      "Properties":{
         "UserPoolId":{
            "Ref":"UserPool"
         },
         "Domain":"my-test-user-pool-domain",
         "ManagedLoginVersion": "2"
      }
   }
}
```

#### YAML
<a name="aws-resource-cognito-userpooldomain--examples--Creating_a_new_default_domain_for_a_user_pool--yaml"></a>

```
UserPoolDomain:
  Type: AWS::Cognito::UserPoolDomain
  Properties:
    UserPoolId: !Ref UserPool
    Domain: "my-test-user-pool-domain"
    ManagedLoginVersion: "2"
```

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-amplify-domain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::Domain
<a name="aws-resource-amplify-domain"></a>

 Specifies the AWS::Amplify::Domain resource that enables you to connect a custom domain to your app.

## Syntax
<a name="aws-resource-amplify-domain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-amplify-domain-syntax.json"></a>

```
{
  "Type" : "AWS::Amplify::Domain",
  "Properties" : {
      "[AppId](#cfn-amplify-domain-appid)" : {{String}},
      "[AutoSubDomainCreationPatterns](#cfn-amplify-domain-autosubdomaincreationpatterns)" : {{[ String, ... ]}},
      "[AutoSubDomainIAMRole](#cfn-amplify-domain-autosubdomainiamrole)" : {{String}},
      "[CertificateSettings](#cfn-amplify-domain-certificatesettings)" : {{CertificateSettings}},
      "[DomainName](#cfn-amplify-domain-domainname)" : {{String}},
      "[EnableAutoSubDomain](#cfn-amplify-domain-enableautosubdomain)" : {{Boolean}},
      "[SubDomainSettings](#cfn-amplify-domain-subdomainsettings)" : {{[ SubDomainSetting, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-amplify-domain-syntax.yaml"></a>

```
Type: AWS::Amplify::Domain
Properties:
  [AppId](#cfn-amplify-domain-appid): {{String}}
  [AutoSubDomainCreationPatterns](#cfn-amplify-domain-autosubdomaincreationpatterns): {{
    - String}}
  [AutoSubDomainIAMRole](#cfn-amplify-domain-autosubdomainiamrole): {{String}}
  [CertificateSettings](#cfn-amplify-domain-certificatesettings): {{
    CertificateSettings}}
  [DomainName](#cfn-amplify-domain-domainname): {{String}}
  [EnableAutoSubDomain](#cfn-amplify-domain-enableautosubdomain): {{Boolean}}
  [SubDomainSettings](#cfn-amplify-domain-subdomainsettings): {{
    - SubDomainSetting}}
```

## Properties
<a name="aws-resource-amplify-domain-properties"></a>

`AppId`  <a name="cfn-amplify-domain-appid"></a>
 The unique ID for an Amplify app.
*Required*: Yes
*Type*: String
*Pattern*: `d[a-z0-9]+`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AutoSubDomainCreationPatterns`  <a name="cfn-amplify-domain-autosubdomaincreationpatterns"></a>
 Sets the branch patterns for automatic subdomain creation.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoSubDomainIAMRole`  <a name="cfn-amplify-domain-autosubdomainiamrole"></a>
The required AWS Identity and Access Management (IAMlong) service role for the Amazon Resource Name (ARN) for automatically creating subdomains.
*Required*: No
*Type*: String
*Pattern*: `^$|^arn:.+:iam::\d{12}:role.+`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateSettings`  <a name="cfn-amplify-domain-certificatesettings"></a>
The type of SSL/TLS certificate to use for your custom domain. If you don't specify a certificate type, Amplify uses the default certificate that it provisions and manages for you.
*Required*: No
*Type*: [CertificateSettings](aws-properties-amplify-domain-certificatesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-amplify-domain-domainname"></a>
 The domain name for the domain association.
*Required*: Yes
*Type*: String
*Pattern*: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])(\.)?$`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableAutoSubDomain`  <a name="cfn-amplify-domain-enableautosubdomain"></a>
 Enables the automated creation of subdomains for branches.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubDomainSettings`  <a name="cfn-amplify-domain-subdomainsettings"></a>
 The setting for the subdomain.
*Required*: Yes
*Type*: Array of [SubDomainSetting](aws-properties-amplify-domain-subdomainsetting.md)
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-amplify-domain-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-amplify-domain-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-amplify-domain-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
ARN for the Domain Association.

`AutoSubDomainCreationPatterns`  <a name="AutoSubDomainCreationPatterns-fn::getatt"></a>
Branch patterns for the automatically created subdomain.

`AutoSubDomainIAMRole`  <a name="AutoSubDomainIAMRole-fn::getatt"></a>
The IAM service role for the subdomain.

`CertificateRecord`  <a name="CertificateRecord-fn::getatt"></a>
DNS Record for certificate verification.

`DomainName`  <a name="DomainName-fn::getatt"></a>
Name of the domain.

`DomainStatus`  <a name="DomainStatus-fn::getatt"></a>
Status for the Domain Association.

`EnableAutoSubDomain`  <a name="EnableAutoSubDomain-fn::getatt"></a>
Specifies whether the automated creation of subdomains for branches is enabled.

`StatusReason`  <a name="StatusReason-fn::getatt"></a>
Reason for the current status of the domain.

`UpdateStatus`  <a name="UpdateStatus-fn::getatt"></a>
The status of the domain update operation that is currently in progress. The following list describes the valid update states.
REQUESTING\_CERTIFICATE
The certificate is in the process of being updated.
PENDING\_VERIFICATION
Indicates that an Amplify managed certificate is in the process of being verified. This occurs during the creation of a custom domain or when a custom domain is updated to use a managed certificate.
IMPORTING\_CUSTOM\_CERTIFICATE
Indicates that an Amplify custom certificate is in the process of being imported. This occurs during the creation of a custom domain or when a custom domain is updated to use a custom certificate.
PENDING\_DEPLOYMENT
Indicates that the subdomain or certificate changes are being propagated.
AWAITING\_APP\_CNAME
Amplify is waiting for CNAME records corresponding to subdomains to be propagated. If your custom domain is on Route 53, Amplify handles this for you automatically. For more information about custom domains, see [Setting up custom domains](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html) in the *Amplify Hosting User Guide*.
UPDATE\_COMPLETE
The certificate has been associated with a domain.
UPDATE\_FAILED
The certificate has failed to be provisioned or associated, and there is no existing active certificate to roll back to.

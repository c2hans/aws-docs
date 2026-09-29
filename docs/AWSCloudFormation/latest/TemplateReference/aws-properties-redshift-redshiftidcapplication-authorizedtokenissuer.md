---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-redshiftidcapplication-authorizedtokenissuer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::RedshiftIdcApplication AuthorizedTokenIssuer
<a name="aws-properties-redshift-redshiftidcapplication-authorizedtokenissuer"></a>

The authorized token issuer for the Amazon Redshift IAM Identity Center application.

## Syntax
<a name="aws-properties-redshift-redshiftidcapplication-authorizedtokenissuer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-redshiftidcapplication-authorizedtokenissuer-syntax.json"></a>

```
{
  "[AuthorizedAudiencesList](#cfn-redshift-redshiftidcapplication-authorizedtokenissuer-authorizedaudienceslist)" : {{[ String, ... ]}},
  "[TrustedTokenIssuerArn](#cfn-redshift-redshiftidcapplication-authorizedtokenissuer-trustedtokenissuerarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-redshiftidcapplication-authorizedtokenissuer-syntax.yaml"></a>

```
  [AuthorizedAudiencesList](#cfn-redshift-redshiftidcapplication-authorizedtokenissuer-authorizedaudienceslist): {{
    - String}}
  [TrustedTokenIssuerArn](#cfn-redshift-redshiftidcapplication-authorizedtokenissuer-trustedtokenissuerarn): {{String}}
```

## Properties
<a name="aws-properties-redshift-redshiftidcapplication-authorizedtokenissuer-properties"></a>

`AuthorizedAudiencesList`  <a name="cfn-redshift-redshiftidcapplication-authorizedtokenissuer-authorizedaudienceslist"></a>
The list of audiences for the authorized token issuer for integrating Amazon Redshift with IDC Identity Center.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrustedTokenIssuerArn`  <a name="cfn-redshift-redshiftidcapplication-authorizedtokenissuer-trustedtokenissuerarn"></a>
The ARN for the authorized token issuer for integrating Amazon Redshift with IDC Identity Center.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:[a-zA-Z0-9-]+:[a-z0-9-]*:[0-9]*:.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

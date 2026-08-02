---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataAccessor DataAccessorAuthenticationConfiguration
<a name="aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration"></a>

A union type that contains the specific authentication configuration based on the authentication type selected.

## Syntax
<a name="aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration-syntax.json"></a>

```
{
  "[IdcTrustedTokenIssuerConfiguration](#cfn-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration-idctrustedtokenissuerconfiguration)" : {{DataAccessorIdcTrustedTokenIssuerConfiguration}}
}
```

### YAML
<a name="aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration-syntax.yaml"></a>

```
  [IdcTrustedTokenIssuerConfiguration](#cfn-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration-idctrustedtokenissuerconfiguration): {{
    DataAccessorIdcTrustedTokenIssuerConfiguration}}
```

## Properties
<a name="aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration-properties"></a>

`IdcTrustedTokenIssuerConfiguration`  <a name="cfn-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration-idctrustedtokenissuerconfiguration"></a>
Configuration for IAM Identity Center Trusted Token Issuer (TTI) authentication used when the authentication type is `AWS_IAM_IDC_TTI`.
*Required*: Yes
*Type*: [DataAccessorIdcTrustedTokenIssuerConfiguration](aws-properties-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

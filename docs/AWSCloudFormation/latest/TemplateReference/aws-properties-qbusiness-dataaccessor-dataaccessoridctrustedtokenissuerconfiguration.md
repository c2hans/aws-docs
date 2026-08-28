---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataAccessor DataAccessorIdcTrustedTokenIssuerConfiguration
<a name="aws-properties-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration"></a>

Configuration details for IAM Identity Center Trusted Token Issuer (TTI) authentication.

## Syntax
<a name="aws-properties-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration-syntax.json"></a>

```
{
  "[IdcTrustedTokenIssuerArn](#cfn-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration-idctrustedtokenissuerarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration-syntax.yaml"></a>

```
  [IdcTrustedTokenIssuerArn](#cfn-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration-idctrustedtokenissuerarn): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration-properties"></a>

`IdcTrustedTokenIssuerArn`  <a name="cfn-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration-idctrustedtokenissuerarn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center Trusted Token Issuer that will be used for authentication.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:sso::[0-9]{12}:trustedTokenIssuer/(sso)?ins-[a-zA-Z0-9-.]{16}/tti-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

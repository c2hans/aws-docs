---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataAccessor DataAccessorAuthenticationDetail
<a name="aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail"></a>

Contains the authentication configuration details for a data accessor. This structure defines how the ISV authenticates when accessing data through the data accessor.

## Syntax
<a name="aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail-syntax.json"></a>

```
{
  "[AuthenticationConfiguration](#cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-authenticationconfiguration)" : {{DataAccessorAuthenticationConfiguration}},
  "[AuthenticationType](#cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-authenticationtype)" : {{String}},
  "[ExternalIds](#cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-externalids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail-syntax.yaml"></a>

```
  [AuthenticationConfiguration](#cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-authenticationconfiguration): {{
    DataAccessorAuthenticationConfiguration}}
  [AuthenticationType](#cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-authenticationtype): {{String}}
  [ExternalIds](#cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-externalids): {{
    - String}}
```

## Properties
<a name="aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail-properties"></a>

`AuthenticationConfiguration`  <a name="cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-authenticationconfiguration"></a>
The specific authentication configuration based on the authentication type.
*Required*: No
*Type*: [DataAccessorAuthenticationConfiguration](aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthenticationType`  <a name="cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-authenticationtype"></a>
The type of authentication to use for the data accessor. This determines how the ISV authenticates when accessing data. You can use one of two authentication types:
+ `AWS_IAM_IDC_TTI` - Authentication using IAM Identity Center Trusted Token Issuer (TTI). This authentication type allows the ISV to use a trusted token issuer to generate tokens for accessing the data.
+ `AWS_IAM_IDC_AUTH_CODE` - Authentication using IAM Identity Center authorization code flow. This authentication type uses the standard OAuth 2.0 authorization code flow for authentication.
*Required*: Yes
*Type*: String
*Allowed values*: `AWS_IAM_IDC_TTI | AWS_IAM_IDC_AUTH_CODE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalIds`  <a name="cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-externalids"></a>
A list of external identifiers associated with this authentication configuration. These are used to correlate the data accessor with external systems.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `1000 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

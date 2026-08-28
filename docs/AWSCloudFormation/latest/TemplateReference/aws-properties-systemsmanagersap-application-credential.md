---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-systemsmanagersap-application-credential.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SystemsManagerSAP::Application Credential
<a name="aws-properties-systemsmanagersap-application-credential"></a>

The credentials of your SAP application.

## Syntax
<a name="aws-properties-systemsmanagersap-application-credential-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-systemsmanagersap-application-credential-syntax.json"></a>

```
{
  "[CredentialType](#cfn-systemsmanagersap-application-credential-credentialtype)" : {{String}},
  "[DatabaseName](#cfn-systemsmanagersap-application-credential-databasename)" : {{String}},
  "[SecretId](#cfn-systemsmanagersap-application-credential-secretid)" : {{String}}
}
```

### YAML
<a name="aws-properties-systemsmanagersap-application-credential-syntax.yaml"></a>

```
  [CredentialType](#cfn-systemsmanagersap-application-credential-credentialtype): {{String}}
  [DatabaseName](#cfn-systemsmanagersap-application-credential-databasename): {{String}}
  [SecretId](#cfn-systemsmanagersap-application-credential-secretid): {{String}}
```

## Properties
<a name="aws-properties-systemsmanagersap-application-credential-properties"></a>

`CredentialType`  <a name="cfn-systemsmanagersap-application-credential-credentialtype"></a>
The type of the application credentials.
*Required*: No
*Type*: String
*Allowed values*: `ADMIN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseName`  <a name="cfn-systemsmanagersap-application-credential-databasename"></a>
The name of the SAP HANA database.
*Required*: No
*Type*: String
*Pattern*: `^(?=.{1,100}$).*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecretId`  <a name="cfn-systemsmanagersap-application-credential-secretid"></a>
The secret ID created in AWS Secrets Manager to store the credentials of the SAP application.
*Required*: No
*Type*: String
*Pattern*: `^(?=.{1,100}$).*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

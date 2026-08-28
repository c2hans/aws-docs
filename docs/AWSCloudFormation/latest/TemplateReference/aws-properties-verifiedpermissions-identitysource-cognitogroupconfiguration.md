---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-identitysource-cognitogroupconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::IdentitySource CognitoGroupConfiguration
<a name="aws-properties-verifiedpermissions-identitysource-cognitogroupconfiguration"></a>

The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.

## Syntax
<a name="aws-properties-verifiedpermissions-identitysource-cognitogroupconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-identitysource-cognitogroupconfiguration-syntax.json"></a>

```
{
  "[GroupEntityType](#cfn-verifiedpermissions-identitysource-cognitogroupconfiguration-groupentitytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-identitysource-cognitogroupconfiguration-syntax.yaml"></a>

```
  [GroupEntityType](#cfn-verifiedpermissions-identitysource-cognitogroupconfiguration-groupentitytype): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-identitysource-cognitogroupconfiguration-properties"></a>

`GroupEntityType`  <a name="cfn-verifiedpermissions-identitysource-cognitogroupconfiguration-groupentitytype"></a>
The name of the schema entity type that's mapped to the user pool group. Defaults to `AWS::CognitoGroup`.
*Required*: Yes
*Type*: String
*Pattern*: `^([_a-zA-Z][_a-zA-Z0-9]*::)*[_a-zA-Z][_a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rolesanywhere-profile-attributemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RolesAnywhere::Profile AttributeMapping
<a name="aws-properties-rolesanywhere-profile-attributemapping"></a>

A mapping applied to the authenticating end-entity certificate.

## Syntax
<a name="aws-properties-rolesanywhere-profile-attributemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rolesanywhere-profile-attributemapping-syntax.json"></a>

```
{
  "[CertificateField](#cfn-rolesanywhere-profile-attributemapping-certificatefield)" : {{String}},
  "[MappingRules](#cfn-rolesanywhere-profile-attributemapping-mappingrules)" : {{[ MappingRule, ... ]}}
}
```

### YAML
<a name="aws-properties-rolesanywhere-profile-attributemapping-syntax.yaml"></a>

```
  [CertificateField](#cfn-rolesanywhere-profile-attributemapping-certificatefield): {{String}}
  [MappingRules](#cfn-rolesanywhere-profile-attributemapping-mappingrules): {{
    - MappingRule}}
```

## Properties
<a name="aws-properties-rolesanywhere-profile-attributemapping-properties"></a>

`CertificateField`  <a name="cfn-rolesanywhere-profile-attributemapping-certificatefield"></a>
Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.
*Required*: Yes
*Type*: String
*Allowed values*: `x509Subject | x509Issuer | x509SAN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MappingRules`  <a name="cfn-rolesanywhere-profile-attributemapping-mappingrules"></a>
A list of mapping entries for every supported specifier or sub-field.
*Required*: Yes
*Type*: Array of [MappingRule](aws-properties-rolesanywhere-profile-mappingrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

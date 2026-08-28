---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rolesanywhere-trustanchor-source.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RolesAnywhere::TrustAnchor Source
<a name="aws-properties-rolesanywhere-trustanchor-source"></a>

 Object representing the TrustAnchor type and its related certificate data.

## Syntax
<a name="aws-properties-rolesanywhere-trustanchor-source-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rolesanywhere-trustanchor-source-syntax.json"></a>

```
{
  "[SourceData](#cfn-rolesanywhere-trustanchor-source-sourcedata)" : {{SourceData}},
  "[SourceType](#cfn-rolesanywhere-trustanchor-source-sourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-rolesanywhere-trustanchor-source-syntax.yaml"></a>

```
  [SourceData](#cfn-rolesanywhere-trustanchor-source-sourcedata): {{
    SourceData}}
  [SourceType](#cfn-rolesanywhere-trustanchor-source-sourcetype): {{String}}
```

## Properties
<a name="aws-properties-rolesanywhere-trustanchor-source-properties"></a>

`SourceData`  <a name="cfn-rolesanywhere-trustanchor-source-sourcedata"></a>
 A union object representing the data field of the TrustAnchor depending on its type
*Required*: Yes
*Type*: [SourceData](aws-properties-rolesanywhere-trustanchor-sourcedata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceType`  <a name="cfn-rolesanywhere-trustanchor-source-sourcetype"></a>
 The type of the TrustAnchor.
*Required*: Yes
*Type*: String
*Allowed values*: `AWS_ACM_PCA | CERTIFICATE_BUNDLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

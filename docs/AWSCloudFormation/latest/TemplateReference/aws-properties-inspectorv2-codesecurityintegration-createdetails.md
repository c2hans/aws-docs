---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-codesecurityintegration-createdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityIntegration CreateDetails
<a name="aws-properties-inspectorv2-codesecurityintegration-createdetails"></a>

Contains details required to create a code security integration with a specific repository provider.

## Syntax
<a name="aws-properties-inspectorv2-codesecurityintegration-createdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-codesecurityintegration-createdetails-syntax.json"></a>

```
{
  "[gitlabSelfManaged](#cfn-inspectorv2-codesecurityintegration-createdetails-gitlabselfmanaged)" : {{CreateGitLabSelfManagedIntegrationDetail}}
}
```

### YAML
<a name="aws-properties-inspectorv2-codesecurityintegration-createdetails-syntax.yaml"></a>

```
  [gitlabSelfManaged](#cfn-inspectorv2-codesecurityintegration-createdetails-gitlabselfmanaged): {{
    CreateGitLabSelfManagedIntegrationDetail}}
```

## Properties
<a name="aws-properties-inspectorv2-codesecurityintegration-createdetails-properties"></a>

`gitlabSelfManaged`  <a name="cfn-inspectorv2-codesecurityintegration-createdetails-gitlabselfmanaged"></a>
Details specific to creating an integration with a self-managed GitLab instance.
*Required*: Yes
*Type*: [CreateGitLabSelfManagedIntegrationDetail](aws-properties-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

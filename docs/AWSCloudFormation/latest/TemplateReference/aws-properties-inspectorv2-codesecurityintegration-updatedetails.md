---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-codesecurityintegration-updatedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityIntegration UpdateDetails
<a name="aws-properties-inspectorv2-codesecurityintegration-updatedetails"></a>

Contains details required to update a code security integration with a specific repository provider.

## Syntax
<a name="aws-properties-inspectorv2-codesecurityintegration-updatedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-codesecurityintegration-updatedetails-syntax.json"></a>

```
{
  "[github](#cfn-inspectorv2-codesecurityintegration-updatedetails-github)" : {{UpdateGitHubIntegrationDetail}},
  "[gitlabSelfManaged](#cfn-inspectorv2-codesecurityintegration-updatedetails-gitlabselfmanaged)" : {{UpdateGitLabSelfManagedIntegrationDetail}}
}
```

### YAML
<a name="aws-properties-inspectorv2-codesecurityintegration-updatedetails-syntax.yaml"></a>

```
  [github](#cfn-inspectorv2-codesecurityintegration-updatedetails-github): {{
    UpdateGitHubIntegrationDetail}}
  [gitlabSelfManaged](#cfn-inspectorv2-codesecurityintegration-updatedetails-gitlabselfmanaged): {{
    UpdateGitLabSelfManagedIntegrationDetail}}
```

## Properties
<a name="aws-properties-inspectorv2-codesecurityintegration-updatedetails-properties"></a>

`github`  <a name="cfn-inspectorv2-codesecurityintegration-updatedetails-github"></a>
Details specific to updating an integration with GitHub.
*Required*: No
*Type*: [UpdateGitHubIntegrationDetail](aws-properties-inspectorv2-codesecurityintegration-updategithubintegrationdetail.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`gitlabSelfManaged`  <a name="cfn-inspectorv2-codesecurityintegration-updatedetails-gitlabselfmanaged"></a>
Details specific to updating an integration with a self-managed GitLab instance.
*Required*: No
*Type*: [UpdateGitLabSelfManagedIntegrationDetail](aws-properties-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

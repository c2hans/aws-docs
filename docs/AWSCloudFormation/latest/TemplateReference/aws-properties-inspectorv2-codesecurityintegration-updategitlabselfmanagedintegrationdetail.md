---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityIntegration UpdateGitLabSelfManagedIntegrationDetail
<a name="aws-properties-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail"></a>

Contains details required to update an integration with a self-managed GitLab instance.

## Syntax
<a name="aws-properties-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail-syntax.json"></a>

```
{
  "[authCode](#cfn-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail-authcode)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail-syntax.yaml"></a>

```
  [authCode](#cfn-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail-authcode): {{String}}
```

## Properties
<a name="aws-properties-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail-properties"></a>

`authCode`  <a name="cfn-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail-authcode"></a>
The authorization code received from the self-managed GitLab instance to update the integration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

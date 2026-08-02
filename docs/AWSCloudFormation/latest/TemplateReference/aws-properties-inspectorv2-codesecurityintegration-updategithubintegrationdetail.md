---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-codesecurityintegration-updategithubintegrationdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityIntegration UpdateGitHubIntegrationDetail
<a name="aws-properties-inspectorv2-codesecurityintegration-updategithubintegrationdetail"></a>

Contains details required to update an integration with GitHub.

## Syntax
<a name="aws-properties-inspectorv2-codesecurityintegration-updategithubintegrationdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-codesecurityintegration-updategithubintegrationdetail-syntax.json"></a>

```
{
  "[code](#cfn-inspectorv2-codesecurityintegration-updategithubintegrationdetail-code)" : {{String}},
  "[installationId](#cfn-inspectorv2-codesecurityintegration-updategithubintegrationdetail-installationid)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspectorv2-codesecurityintegration-updategithubintegrationdetail-syntax.yaml"></a>

```
  [code](#cfn-inspectorv2-codesecurityintegration-updategithubintegrationdetail-code): {{String}}
  [installationId](#cfn-inspectorv2-codesecurityintegration-updategithubintegrationdetail-installationid): {{String}}
```

## Properties
<a name="aws-properties-inspectorv2-codesecurityintegration-updategithubintegrationdetail-properties"></a>

`code`  <a name="cfn-inspectorv2-codesecurityintegration-updategithubintegrationdetail-code"></a>
The authorization code received from GitHub to update the integration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`installationId`  <a name="cfn-inspectorv2-codesecurityintegration-updategithubintegrationdetail-installationid"></a>
The installation ID of the GitHub App associated with the integration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

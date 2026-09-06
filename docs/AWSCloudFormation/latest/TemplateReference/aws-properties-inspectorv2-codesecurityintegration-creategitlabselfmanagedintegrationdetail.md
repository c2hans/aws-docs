---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityIntegration CreateGitLabSelfManagedIntegrationDetail
<a name="aws-properties-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail"></a>

Contains details required to create an integration with a self-managed GitLab instance.

## Syntax
<a name="aws-properties-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-syntax.json"></a>

```
{
  "[accessToken](#cfn-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-accesstoken)" : {{String}},
  "[instanceUrl](#cfn-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-instanceurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-syntax.yaml"></a>

```
  [accessToken](#cfn-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-accesstoken): {{String}}
  [instanceUrl](#cfn-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-instanceurl): {{String}}
```

## Properties
<a name="aws-properties-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-properties"></a>

`accessToken`  <a name="cfn-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-accesstoken"></a>
The personal access token used to authenticate with the self-managed GitLab instance.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`instanceUrl`  <a name="cfn-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-instanceurl"></a>
The URL of the self-managed GitLab instance.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[-a-zA-Z0-9()@:%_+.~#?&//=]{1,1024}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

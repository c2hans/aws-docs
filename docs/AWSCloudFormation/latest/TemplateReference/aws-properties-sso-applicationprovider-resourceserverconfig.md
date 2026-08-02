---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sso-applicationprovider-resourceserverconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::ApplicationProvider ResourceServerConfig
<a name="aws-properties-sso-applicationprovider-resourceserverconfig"></a>

A structure that describes the configuration of a resource server.

## Syntax
<a name="aws-properties-sso-applicationprovider-resourceserverconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sso-applicationprovider-resourceserverconfig-syntax.json"></a>

```
{
  "[Scopes](#cfn-sso-applicationprovider-resourceserverconfig-scopes)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-sso-applicationprovider-resourceserverconfig-syntax.yaml"></a>

```
  [Scopes](#cfn-sso-applicationprovider-resourceserverconfig-scopes): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-sso-applicationprovider-resourceserverconfig-properties"></a>

`Scopes`  <a name="cfn-sso-applicationprovider-resourceserverconfig-scopes"></a>
A list of the IAM Identity Center access scopes that are associated with this resource server.
*Required*: No
*Type*: Object of [ResourceServerScopeDetails](aws-properties-sso-applicationprovider-resourceserverscopedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

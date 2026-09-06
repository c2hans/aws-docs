---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-servicenowauthorizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service ServiceNowAuthorizationConfig
<a name="aws-properties-devopsagent-service-servicenowauthorizationconfig"></a>

The OAuth authorization configuration for a ServiceNow service.

## Syntax
<a name="aws-properties-devopsagent-service-servicenowauthorizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-servicenowauthorizationconfig-syntax.json"></a>

```
{
  "[OAuthClientCredentials](#cfn-devopsagent-service-servicenowauthorizationconfig-oauthclientcredentials)" : {{OAuthClientDetails}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-servicenowauthorizationconfig-syntax.yaml"></a>

```
  [OAuthClientCredentials](#cfn-devopsagent-service-servicenowauthorizationconfig-oauthclientcredentials): {{
    OAuthClientDetails}}
```

## Properties
<a name="aws-properties-devopsagent-service-servicenowauthorizationconfig-properties"></a>

`OAuthClientCredentials`  <a name="cfn-devopsagent-service-servicenowauthorizationconfig-oauthclientcredentials"></a>
The OAuth client credentials for authenticating with ServiceNow.
*Required*: No
*Type*: [OAuthClientDetails](aws-properties-devopsagent-service-oauthclientdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

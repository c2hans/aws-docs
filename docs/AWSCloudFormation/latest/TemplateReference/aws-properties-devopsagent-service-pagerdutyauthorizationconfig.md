---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-pagerdutyauthorizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service PagerDutyAuthorizationConfig
<a name="aws-properties-devopsagent-service-pagerdutyauthorizationconfig"></a>

The OAuth authorization configuration for a PagerDuty service.

## Syntax
<a name="aws-properties-devopsagent-service-pagerdutyauthorizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-pagerdutyauthorizationconfig-syntax.json"></a>

```
{
  "[OAuthClientCredentials](#cfn-devopsagent-service-pagerdutyauthorizationconfig-oauthclientcredentials)" : {{OAuthClientDetails}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-pagerdutyauthorizationconfig-syntax.yaml"></a>

```
  [OAuthClientCredentials](#cfn-devopsagent-service-pagerdutyauthorizationconfig-oauthclientcredentials): {{
    OAuthClientDetails}}
```

## Properties
<a name="aws-properties-devopsagent-service-pagerdutyauthorizationconfig-properties"></a>

`OAuthClientCredentials`  <a name="cfn-devopsagent-service-pagerdutyauthorizationconfig-oauthclientcredentials"></a>
OAuth client credentials authorization details.
*Required*: No
*Type*: [OAuthClientDetails](aws-properties-devopsagent-service-oauthclientdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

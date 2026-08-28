---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource WebCrawlerAuthenticationConfiguration
<a name="aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration"></a>

Provides the configuration information to connect to websites that require user authentication.

## Syntax
<a name="aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration-syntax.json"></a>

```
{
  "[BasicAuthentication](#cfn-kendra-datasource-webcrawlerauthenticationconfiguration-basicauthentication)" : {{[ WebCrawlerBasicAuthentication, ... ]}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration-syntax.yaml"></a>

```
  [BasicAuthentication](#cfn-kendra-datasource-webcrawlerauthenticationconfiguration-basicauthentication): {{
    - WebCrawlerBasicAuthentication}}
```

## Properties
<a name="aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration-properties"></a>

`BasicAuthentication`  <a name="cfn-kendra-datasource-webcrawlerauthenticationconfiguration-basicauthentication"></a>
The list of configuration information that's required to connect to and crawl a website host using basic authentication credentials.
The list includes the name and port number of the website host.
*Required*: No
*Type*: Array of [WebCrawlerBasicAuthentication](aws-properties-kendra-datasource-webcrawlerbasicauthentication.md)
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

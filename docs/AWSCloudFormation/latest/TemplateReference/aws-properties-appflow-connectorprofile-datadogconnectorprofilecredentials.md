---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile DatadogConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials"></a>

 The connector-specific credentials required by Datadog.

## Syntax
<a name="aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials-syntax.json"></a>

```
{
  "[ApiKey](#cfn-appflow-connectorprofile-datadogconnectorprofilecredentials-apikey)" : {{String}},
  "[ApplicationKey](#cfn-appflow-connectorprofile-datadogconnectorprofilecredentials-applicationkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials-syntax.yaml"></a>

```
  [ApiKey](#cfn-appflow-connectorprofile-datadogconnectorprofilecredentials-apikey): {{String}}
  [ApplicationKey](#cfn-appflow-connectorprofile-datadogconnectorprofilecredentials-applicationkey): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials-properties"></a>

`ApiKey`  <a name="cfn-appflow-connectorprofile-datadogconnectorprofilecredentials-apikey"></a>
 A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationKey`  <a name="cfn-appflow-connectorprofile-datadogconnectorprofilecredentials-applicationkey"></a>
 Application keys, in conjunction with your API key, give you full access to Datadog’s programmatic API. Application keys are associated with the user account that created them. The application key is used to log all requests made to the API.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials--seealso"></a>
+ [DatadogConnectorProfileCredentials](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DatadogConnectorProfileCredentials.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

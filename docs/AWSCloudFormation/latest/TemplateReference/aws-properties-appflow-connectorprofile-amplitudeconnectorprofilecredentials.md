---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile AmplitudeConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials"></a>

 The connector-specific credentials required when using Amplitude.

## Syntax
<a name="aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials-syntax.json"></a>

```
{
  "[ApiKey](#cfn-appflow-connectorprofile-amplitudeconnectorprofilecredentials-apikey)" : {{String}},
  "[SecretKey](#cfn-appflow-connectorprofile-amplitudeconnectorprofilecredentials-secretkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials-syntax.yaml"></a>

```
  [ApiKey](#cfn-appflow-connectorprofile-amplitudeconnectorprofilecredentials-apikey): {{String}}
  [SecretKey](#cfn-appflow-connectorprofile-amplitudeconnectorprofilecredentials-secretkey): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials-properties"></a>

`ApiKey`  <a name="cfn-appflow-connectorprofile-amplitudeconnectorprofilecredentials-apikey"></a>
 A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretKey`  <a name="cfn-appflow-connectorprofile-amplitudeconnectorprofilecredentials-secretkey"></a>
 The Secret Access Key portion of the credentials.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials--seealso"></a>
+ [AmplitudeConnectorProfileCredentials](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_AmplitudeConnectorProfileCredentials.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

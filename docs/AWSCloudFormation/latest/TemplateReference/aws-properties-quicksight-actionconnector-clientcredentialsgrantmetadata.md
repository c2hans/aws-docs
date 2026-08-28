---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-clientcredentialsgrantmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector ClientCredentialsGrantMetadata
<a name="aws-properties-quicksight-actionconnector-clientcredentialsgrantmetadata"></a>

Configuration for OAuth 2.0 client credentials grant authentication, including client ID, client secret, token endpoint, and optional scopes.

## Syntax
<a name="aws-properties-quicksight-actionconnector-clientcredentialsgrantmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-clientcredentialsgrantmetadata-syntax.json"></a>

```
{
  "[BaseEndpoint](#cfn-quicksight-actionconnector-clientcredentialsgrantmetadata-baseendpoint)" : {{String}},
  "[ClientCredentialsDetails](#cfn-quicksight-actionconnector-clientcredentialsgrantmetadata-clientcredentialsdetails)" : {{ClientCredentialsDetails}},
  "[ClientCredentialsSource](#cfn-quicksight-actionconnector-clientcredentialsgrantmetadata-clientcredentialssource)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-clientcredentialsgrantmetadata-syntax.yaml"></a>

```
  [BaseEndpoint](#cfn-quicksight-actionconnector-clientcredentialsgrantmetadata-baseendpoint): {{String}}
  [ClientCredentialsDetails](#cfn-quicksight-actionconnector-clientcredentialsgrantmetadata-clientcredentialsdetails): {{
    ClientCredentialsDetails}}
  [ClientCredentialsSource](#cfn-quicksight-actionconnector-clientcredentialsgrantmetadata-clientcredentialssource): {{String}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-clientcredentialsgrantmetadata-properties"></a>

`BaseEndpoint`  <a name="cfn-quicksight-actionconnector-clientcredentialsgrantmetadata-baseendpoint"></a>
The base endpoint URL for the external service.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientCredentialsDetails`  <a name="cfn-quicksight-actionconnector-clientcredentialsgrantmetadata-clientcredentialsdetails"></a>
The detailed client credentials configuration including client ID, client secret, and token endpoint.
*Required*: No
*Type*: [ClientCredentialsDetails](aws-properties-quicksight-actionconnector-clientcredentialsdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientCredentialsSource`  <a name="cfn-quicksight-actionconnector-clientcredentialsgrantmetadata-clientcredentialssource"></a>
The source of the client credentials configuration.
*Required*: No
*Type*: String
*Allowed values*: `PLAIN_CREDENTIALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

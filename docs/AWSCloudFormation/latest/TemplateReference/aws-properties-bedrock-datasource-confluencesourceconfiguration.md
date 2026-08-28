---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-confluencesourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource ConfluenceSourceConfiguration
<a name="aws-properties-bedrock-datasource-confluencesourceconfiguration"></a>

The endpoint information to connect to your Confluence data source.

## Syntax
<a name="aws-properties-bedrock-datasource-confluencesourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-confluencesourceconfiguration-syntax.json"></a>

```
{
  "[AuthType](#cfn-bedrock-datasource-confluencesourceconfiguration-authtype)" : {{String}},
  "[CredentialsSecretArn](#cfn-bedrock-datasource-confluencesourceconfiguration-credentialssecretarn)" : {{String}},
  "[HostType](#cfn-bedrock-datasource-confluencesourceconfiguration-hosttype)" : {{String}},
  "[HostUrl](#cfn-bedrock-datasource-confluencesourceconfiguration-hosturl)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-confluencesourceconfiguration-syntax.yaml"></a>

```
  [AuthType](#cfn-bedrock-datasource-confluencesourceconfiguration-authtype): {{String}}
  [CredentialsSecretArn](#cfn-bedrock-datasource-confluencesourceconfiguration-credentialssecretarn): {{String}}
  [HostType](#cfn-bedrock-datasource-confluencesourceconfiguration-hosttype): {{String}}
  [HostUrl](#cfn-bedrock-datasource-confluencesourceconfiguration-hosturl): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-confluencesourceconfiguration-properties"></a>

`AuthType`  <a name="cfn-bedrock-datasource-confluencesourceconfiguration-authtype"></a>
The supported authentication type to authenticate and connect to your Confluence instance.
*Required*: Yes
*Type*: String
*Allowed values*: `BASIC | OAUTH2_CLIENT_CREDENTIALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialsSecretArn`  <a name="cfn-bedrock-datasource-confluencesourceconfiguration-credentialssecretarn"></a>
The Amazon Resource Name of an AWS Secrets Manager secret that stores your authentication credentials for your Confluence instance URL. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see [Confluence connection configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/confluence-data-source-connector.html#configuration-confluence-connector).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostType`  <a name="cfn-bedrock-datasource-confluencesourceconfiguration-hosttype"></a>
The supported host type, whether online/cloud or server/on-premises.
*Required*: Yes
*Type*: String
*Allowed values*: `SAAS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostUrl`  <a name="cfn-bedrock-datasource-confluencesourceconfiguration-hosturl"></a>
The Confluence host URL or instance URL.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[A-Za-z0-9][^\s]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

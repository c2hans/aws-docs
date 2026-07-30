---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-salesforcesourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource SalesforceSourceConfiguration
<a name="aws-properties-bedrock-datasource-salesforcesourceconfiguration"></a>

The endpoint information to connect to your Salesforce data source.

## Syntax
<a name="aws-properties-bedrock-datasource-salesforcesourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-salesforcesourceconfiguration-syntax.json"></a>

```
{
  "[AuthType](#cfn-bedrock-datasource-salesforcesourceconfiguration-authtype)" : {{String}},
  "[CredentialsSecretArn](#cfn-bedrock-datasource-salesforcesourceconfiguration-credentialssecretarn)" : {{String}},
  "[HostUrl](#cfn-bedrock-datasource-salesforcesourceconfiguration-hosturl)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-salesforcesourceconfiguration-syntax.yaml"></a>

```
  [AuthType](#cfn-bedrock-datasource-salesforcesourceconfiguration-authtype): {{String}}
  [CredentialsSecretArn](#cfn-bedrock-datasource-salesforcesourceconfiguration-credentialssecretarn): {{String}}
  [HostUrl](#cfn-bedrock-datasource-salesforcesourceconfiguration-hosturl): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-salesforcesourceconfiguration-properties"></a>

`AuthType`  <a name="cfn-bedrock-datasource-salesforcesourceconfiguration-authtype"></a>
The supported authentication type to authenticate and connect to your Salesforce instance.
*Required*: Yes
*Type*: String
*Allowed values*: `OAUTH2_CLIENT_CREDENTIALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialsSecretArn`  <a name="cfn-bedrock-datasource-salesforcesourceconfiguration-credentialssecretarn"></a>
The Amazon Resource Name of an AWS Secrets Manager secret that stores your authentication credentials for your Salesforce instance URL. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see [Salesforce connection configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/salesforce-data-source-connector.html#configuration-salesforce-connector).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostUrl`  <a name="cfn-bedrock-datasource-salesforcesourceconfiguration-hosturl"></a>
The Salesforce host URL or instance URL.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[A-Za-z0-9][^\s]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

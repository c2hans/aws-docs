---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-sharepointsourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource SharePointSourceConfiguration
<a name="aws-properties-bedrock-datasource-sharepointsourceconfiguration"></a>

The endpoint information to connect to your SharePoint data source.

## Syntax
<a name="aws-properties-bedrock-datasource-sharepointsourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-sharepointsourceconfiguration-syntax.json"></a>

```
{
  "[AuthType](#cfn-bedrock-datasource-sharepointsourceconfiguration-authtype)" : {{String}},
  "[CredentialsSecretArn](#cfn-bedrock-datasource-sharepointsourceconfiguration-credentialssecretarn)" : {{String}},
  "[Domain](#cfn-bedrock-datasource-sharepointsourceconfiguration-domain)" : {{String}},
  "[HostType](#cfn-bedrock-datasource-sharepointsourceconfiguration-hosttype)" : {{String}},
  "[SiteUrls](#cfn-bedrock-datasource-sharepointsourceconfiguration-siteurls)" : {{[ String, ... ]}},
  "[TenantId](#cfn-bedrock-datasource-sharepointsourceconfiguration-tenantid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-sharepointsourceconfiguration-syntax.yaml"></a>

```
  [AuthType](#cfn-bedrock-datasource-sharepointsourceconfiguration-authtype): {{String}}
  [CredentialsSecretArn](#cfn-bedrock-datasource-sharepointsourceconfiguration-credentialssecretarn): {{String}}
  [Domain](#cfn-bedrock-datasource-sharepointsourceconfiguration-domain): {{String}}
  [HostType](#cfn-bedrock-datasource-sharepointsourceconfiguration-hosttype): {{String}}
  [SiteUrls](#cfn-bedrock-datasource-sharepointsourceconfiguration-siteurls): {{
    - String}}
  [TenantId](#cfn-bedrock-datasource-sharepointsourceconfiguration-tenantid): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-sharepointsourceconfiguration-properties"></a>

`AuthType`  <a name="cfn-bedrock-datasource-sharepointsourceconfiguration-authtype"></a>
The supported authentication type to authenticate and connect to your SharePoint site/sites.
*Required*: Yes
*Type*: String
*Allowed values*: `OAUTH2_CLIENT_CREDENTIALS | OAUTH2_SHAREPOINT_APP_ONLY_CLIENT_CREDENTIALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialsSecretArn`  <a name="cfn-bedrock-datasource-sharepointsourceconfiguration-credentialssecretarn"></a>
The Amazon Resource Name of an AWS Secrets Manager secret that stores your authentication credentials for your SharePoint site/sites. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see [SharePoint connection configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/sharepoint-data-source-connector.html#configuration-sharepoint-connector).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domain`  <a name="cfn-bedrock-datasource-sharepointsourceconfiguration-domain"></a>
The domain of your SharePoint instance or site URL/URLs.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostType`  <a name="cfn-bedrock-datasource-sharepointsourceconfiguration-hosttype"></a>
The supported host type, whether online/cloud or server/on-premises.
*Required*: Yes
*Type*: String
*Allowed values*: `ONLINE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SiteUrls`  <a name="cfn-bedrock-datasource-sharepointsourceconfiguration-siteurls"></a>
A list of one or more SharePoint site URLs.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenantId`  <a name="cfn-bedrock-datasource-sharepointsourceconfiguration-tenantid"></a>
The identifier of your Microsoft 365 tenant.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

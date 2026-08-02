---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-oauthclientapplication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::OAuthClientApplication
<a name="aws-resource-quicksight-oauthclientapplication"></a>

Creates an OAuthClientApplication.

## Syntax
<a name="aws-resource-quicksight-oauthclientapplication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-oauthclientapplication-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::OAuthClientApplication",
  "Properties" : {
      "[ClientId](#cfn-quicksight-oauthclientapplication-clientid)" : {{String}},
      "[ClientSecret](#cfn-quicksight-oauthclientapplication-clientsecret)" : {{String}},
      "[DataSourceType](#cfn-quicksight-oauthclientapplication-datasourcetype)" : {{String}},
      "[IdentityProviderVpcConnectionProperties](#cfn-quicksight-oauthclientapplication-identityprovidervpcconnectionproperties)" : {{IdentityProviderVpcConnectionProperties}},
      "[Name](#cfn-quicksight-oauthclientapplication-name)" : {{String}},
      "[OAuthAuthorizationEndpointUrl](#cfn-quicksight-oauthclientapplication-oauthauthorizationendpointurl)" : {{String}},
      "[OAuthClientApplicationId](#cfn-quicksight-oauthclientapplication-oauthclientapplicationid)" : {{String}},
      "[OAuthClientAuthenticationType](#cfn-quicksight-oauthclientapplication-oauthclientauthenticationtype)" : {{String}},
      "[OAuthScopes](#cfn-quicksight-oauthclientapplication-oauthscopes)" : {{String}},
      "[OAuthTokenEndpointUrl](#cfn-quicksight-oauthclientapplication-oauthtokenendpointurl)" : {{String}},
      "[Tags](#cfn-quicksight-oauthclientapplication-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-oauthclientapplication-syntax.yaml"></a>

```
Type: AWS::QuickSight::OAuthClientApplication
Properties:
  [ClientId](#cfn-quicksight-oauthclientapplication-clientid): {{String}}
  [ClientSecret](#cfn-quicksight-oauthclientapplication-clientsecret): {{String}}
  [DataSourceType](#cfn-quicksight-oauthclientapplication-datasourcetype): {{String}}
  [IdentityProviderVpcConnectionProperties](#cfn-quicksight-oauthclientapplication-identityprovidervpcconnectionproperties): {{
    IdentityProviderVpcConnectionProperties}}
  [Name](#cfn-quicksight-oauthclientapplication-name): {{String}}
  [OAuthAuthorizationEndpointUrl](#cfn-quicksight-oauthclientapplication-oauthauthorizationendpointurl): {{String}}
  [OAuthClientApplicationId](#cfn-quicksight-oauthclientapplication-oauthclientapplicationid): {{String}}
  [OAuthClientAuthenticationType](#cfn-quicksight-oauthclientapplication-oauthclientauthenticationtype): {{String}}
  [OAuthScopes](#cfn-quicksight-oauthclientapplication-oauthscopes): {{String}}
  [OAuthTokenEndpointUrl](#cfn-quicksight-oauthclientapplication-oauthtokenendpointurl): {{String}}
  [Tags](#cfn-quicksight-oauthclientapplication-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-quicksight-oauthclientapplication-properties"></a>

`ClientId`  <a name="cfn-quicksight-oauthclientapplication-clientid"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-quicksight-oauthclientapplication-clientsecret"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSourceType`  <a name="cfn-quicksight-oauthclientapplication-datasourcetype"></a>
The type of data source that the OAuthClientApplication is used with. Valid values are `SNOWFLAKE`.
*Required*: No
*Type*: String
*Allowed values*: `ADOBE_ANALYTICS | AMAZON_ELASTICSEARCH | AMAZON_OPENSEARCH | ATHENA | AURORA | AURORA_POSTGRESQL | AWS_IOT_ANALYTICS | BIGQUERY | CONFLUENCE | DATABRICKS | EXASOL | GITHUB | GOOGLESHEETS | GOOGLE_DRIVE | JIRA | MARIADB | MYSQL | ONE_DRIVE | ORACLE | POSTGRESQL | PRESTO | QBUSINESS | REDSHIFT | S3 | S3_KNOWLEDGE_BASE | S3_TABLES | SALESFORCE | SERVICENOW | SHAREPOINT | SNOWFLAKE | SPARK | SQLSERVER | STARBURST | TERADATA | TIMESTREAM | TRINO | TWITTER | WEB_CRAWLER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviderVpcConnectionProperties`  <a name="cfn-quicksight-oauthclientapplication-identityprovidervpcconnectionproperties"></a>
VPC connection properties.
*Required*: No
*Type*: [IdentityProviderVpcConnectionProperties](aws-properties-quicksight-oauthclientapplication-identityprovidervpcconnectionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-oauthclientapplication-name"></a>
The display name of the OAuthClientApplication.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthAuthorizationEndpointUrl`  <a name="cfn-quicksight-oauthclientapplication-oauthauthorizationendpointurl"></a>
The authorization endpoint URL of the identity provider that is used to obtain authorization codes.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthClientApplicationId`  <a name="cfn-quicksight-oauthclientapplication-oauthclientapplicationid"></a>
The ID of the OAuthClientApplication. This ID is unique per AWS Region for each AWS account.
*Required*: Yes
*Type*: String
*Pattern*: `[^/][^\u0000-\u001f]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OAuthClientAuthenticationType`  <a name="cfn-quicksight-oauthclientapplication-oauthclientauthenticationtype"></a>
The OAuth client authentication type used by the OAuthClientApplication. Valid values are `TOKEN`.
*Required*: Yes
*Type*: String
*Allowed values*: `TOKEN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OAuthScopes`  <a name="cfn-quicksight-oauthclientapplication-oauthscopes"></a>
The OAuth scopes that are requested when the OAuthClientApplication obtains an access token from the identity provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthTokenEndpointUrl`  <a name="cfn-quicksight-oauthclientapplication-oauthtokenendpointurl"></a>
The token endpoint URL of the identity provider that is used to obtain access tokens.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-oauthclientapplication-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-oauthclientapplication-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-oauthclientapplication-return-values"></a>

### Ref
<a name="aws-resource-quicksight-oauthclientapplication-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-oauthclientapplication-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-oauthclientapplication-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the OAuthClientApplication.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time that the OAuthClientApplication was created.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The time that the OAuthClientApplication was last updated.

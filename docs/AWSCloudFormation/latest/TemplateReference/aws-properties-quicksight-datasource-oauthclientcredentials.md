---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-oauthclientcredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource OAuthClientCredentials
<a name="aws-properties-quicksight-datasource-oauthclientcredentials"></a>

The OAuth 2.0 client credentials used for authenticating a data source connection. Use this structure to provide a client ID, client secret, and username directly instead of referencing a secret stored in Amazon Secrets Manager. This structure supports data sources that use two-legged OAuth (2LO) authentication, such as Snowflake.

## Syntax
<a name="aws-properties-quicksight-datasource-oauthclientcredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-oauthclientcredentials-syntax.json"></a>

```
{
  "[ClientId](#cfn-quicksight-datasource-oauthclientcredentials-clientid)" : {{String}},
  "[ClientSecret](#cfn-quicksight-datasource-oauthclientcredentials-clientsecret)" : {{String}},
  "[Username](#cfn-quicksight-datasource-oauthclientcredentials-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-oauthclientcredentials-syntax.yaml"></a>

```
  [ClientId](#cfn-quicksight-datasource-oauthclientcredentials-clientid): {{String}}
  [ClientSecret](#cfn-quicksight-datasource-oauthclientcredentials-clientsecret): {{String}}
  [Username](#cfn-quicksight-datasource-oauthclientcredentials-username): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-oauthclientcredentials-properties"></a>

`ClientId`  <a name="cfn-quicksight-datasource-oauthclientcredentials-clientid"></a>
The client ID of the OAuth 2.0 application that is registered with the data source provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-quicksight-datasource-oauthclientcredentials-clientsecret"></a>
The client secret of the OAuth 2.0 application that is registered with the data source provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-quicksight-datasource-oauthclientcredentials-username"></a>
The username of the account that is used for OAuth 2.0 client credentials authentication with the data source provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

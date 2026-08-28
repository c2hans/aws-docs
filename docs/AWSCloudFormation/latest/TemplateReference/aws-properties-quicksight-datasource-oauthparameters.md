---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-oauthparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource OAuthParameters
<a name="aws-properties-quicksight-datasource-oauthparameters"></a>

An object that contains information needed to create a data source connection that uses OAuth client credentials. This option is available for data source connections that are made with Snowflake and Starburst.

## Syntax
<a name="aws-properties-quicksight-datasource-oauthparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-oauthparameters-syntax.json"></a>

```
{
  "[IdentityProviderResourceUri](#cfn-quicksight-datasource-oauthparameters-identityproviderresourceuri)" : {{String}},
  "[IdentityProviderVpcConnectionProperties](#cfn-quicksight-datasource-oauthparameters-identityprovidervpcconnectionproperties)" : {{VpcConnectionProperties}},
  "[OAuthScope](#cfn-quicksight-datasource-oauthparameters-oauthscope)" : {{String}},
  "[TokenProviderUrl](#cfn-quicksight-datasource-oauthparameters-tokenproviderurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-oauthparameters-syntax.yaml"></a>

```
  [IdentityProviderResourceUri](#cfn-quicksight-datasource-oauthparameters-identityproviderresourceuri): {{String}}
  [IdentityProviderVpcConnectionProperties](#cfn-quicksight-datasource-oauthparameters-identityprovidervpcconnectionproperties): {{
    VpcConnectionProperties}}
  [OAuthScope](#cfn-quicksight-datasource-oauthparameters-oauthscope): {{String}}
  [TokenProviderUrl](#cfn-quicksight-datasource-oauthparameters-tokenproviderurl): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-oauthparameters-properties"></a>

`IdentityProviderResourceUri`  <a name="cfn-quicksight-datasource-oauthparameters-identityproviderresourceuri"></a>
The resource uri of the identity provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviderVpcConnectionProperties`  <a name="cfn-quicksight-datasource-oauthparameters-identityprovidervpcconnectionproperties"></a>
Property description not available.
*Required*: No
*Type*: [VpcConnectionProperties](aws-properties-quicksight-datasource-vpcconnectionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthScope`  <a name="cfn-quicksight-datasource-oauthparameters-oauthscope"></a>
The OAuth scope.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenProviderUrl`  <a name="cfn-quicksight-datasource-oauthparameters-tokenproviderurl"></a>
The token endpoint URL of the identity provider.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

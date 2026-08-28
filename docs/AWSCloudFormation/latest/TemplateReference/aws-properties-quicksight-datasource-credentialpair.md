---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-credentialpair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource CredentialPair
<a name="aws-properties-quicksight-datasource-credentialpair"></a>

The combination of user name and password that are used as credentials.

## Syntax
<a name="aws-properties-quicksight-datasource-credentialpair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-credentialpair-syntax.json"></a>

```
{
  "[AlternateDataSourceParameters](#cfn-quicksight-datasource-credentialpair-alternatedatasourceparameters)" : {{[ DataSourceParameters, ... ]}},
  "[Password](#cfn-quicksight-datasource-credentialpair-password)" : {{String}},
  "[Username](#cfn-quicksight-datasource-credentialpair-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-credentialpair-syntax.yaml"></a>

```
  [AlternateDataSourceParameters](#cfn-quicksight-datasource-credentialpair-alternatedatasourceparameters): {{
    - DataSourceParameters}}
  [Password](#cfn-quicksight-datasource-credentialpair-password): {{String}}
  [Username](#cfn-quicksight-datasource-credentialpair-username): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-credentialpair-properties"></a>

`AlternateDataSourceParameters`  <a name="cfn-quicksight-datasource-credentialpair-alternatedatasourceparameters"></a>
A set of alternate data source parameters that you want to share for these credentials. The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the `DataSourceParameters` structure that's in the request with the structures in the `AlternateDataSourceParameters` allow list. If the structures are an exact match, the request is allowed to use the new data source with the existing credentials. If the `AlternateDataSourceParameters` list is null, the `DataSourceParameters` originally used with these `Credentials` is automatically allowed.
*Required*: No
*Type*: Array of [DataSourceParameters](aws-properties-quicksight-datasource-datasourceparameters.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Password`  <a name="cfn-quicksight-datasource-credentialpair-password"></a>
Password.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-quicksight-datasource-credentialpair-username"></a>
User name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

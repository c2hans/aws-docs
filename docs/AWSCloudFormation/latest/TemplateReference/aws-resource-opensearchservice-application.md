---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opensearchservice-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Application
<a name="aws-resource-opensearchservice-application"></a>

Creates an OpenSearch UI application. For more information, see [Using the OpenSearch user interface in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html).

## Syntax
<a name="aws-resource-opensearchservice-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-opensearchservice-application-syntax.json"></a>

```
{
  "Type" : "AWS::OpenSearchService::Application",
  "Properties" : {
      "[AppConfigs](#cfn-opensearchservice-application-appconfigs)" : {{[ AppConfig, ... ]}},
      "[DataSources](#cfn-opensearchservice-application-datasources)" : {{[ DataSource, ... ]}},
      "[Endpoint](#cfn-opensearchservice-application-endpoint)" : {{String}},
      "[IamIdentityCenterOptions](#cfn-opensearchservice-application-iamidentitycenteroptions)" : {{IamIdentityCenterOptions}},
      "[Name](#cfn-opensearchservice-application-name)" : {{String}},
      "[Tags](#cfn-opensearchservice-application-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-opensearchservice-application-syntax.yaml"></a>

```
Type: AWS::OpenSearchService::Application
Properties:
  [AppConfigs](#cfn-opensearchservice-application-appconfigs): {{
    - AppConfig}}
  [DataSources](#cfn-opensearchservice-application-datasources): {{
    - DataSource}}
  [Endpoint](#cfn-opensearchservice-application-endpoint): {{String}}
  [IamIdentityCenterOptions](#cfn-opensearchservice-application-iamidentitycenteroptions): {{
    IamIdentityCenterOptions}}
  [Name](#cfn-opensearchservice-application-name): {{String}}
  [Tags](#cfn-opensearchservice-application-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-opensearchservice-application-properties"></a>

`AppConfigs`  <a name="cfn-opensearchservice-application-appconfigs"></a>
Property description not available.
*Required*: No
*Type*: Array of [AppConfig](aws-properties-opensearchservice-application-appconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSources`  <a name="cfn-opensearchservice-application-datasources"></a>
Property description not available.
*Required*: No
*Type*: Array of [DataSource](aws-properties-opensearchservice-application-datasource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-opensearchservice-application-endpoint"></a>
The endpoint URL of an OpenSearch application.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamIdentityCenterOptions`  <a name="cfn-opensearchservice-application-iamidentitycenteroptions"></a>
Settings container for integrating IAM Identity Center with OpenSearch UI applications, which enables enabling secure user authentication and access control across multiple data sources. This setup supports single sign-on (SSO) through IAM Identity Center, allowing centralized user management.
*Required*: No
*Type*: [IamIdentityCenterOptions](aws-properties-opensearchservice-application-iamidentitycenteroptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-opensearchservice-application-name"></a>
The name of an OpenSearch application.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z][a-z0-9\-]+`
*Minimum*: `3`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-opensearchservice-application-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-opensearchservice-application-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-opensearchservice-application-return-values"></a>

### Ref
<a name="aws-resource-opensearchservice-application-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-opensearchservice-application-return-values-fn--getatt"></a>

####
<a name="aws-resource-opensearchservice-application-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of an OpenSearch application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

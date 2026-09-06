---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-application-appconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Application AppConfig
<a name="aws-properties-opensearchservice-application-appconfig"></a>

Configuration settings for an OpenSearch application. For more information, see [Using the OpenSearch user interface in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html).

## Syntax
<a name="aws-properties-opensearchservice-application-appconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-application-appconfig-syntax.json"></a>

```
{
  "[Key](#cfn-opensearchservice-application-appconfig-key)" : {{String}},
  "[Value](#cfn-opensearchservice-application-appconfig-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-application-appconfig-syntax.yaml"></a>

```
  [Key](#cfn-opensearchservice-application-appconfig-key): {{String}}
  [Value](#cfn-opensearchservice-application-appconfig-value): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-application-appconfig-properties"></a>

`Key`  <a name="cfn-opensearchservice-application-appconfig-key"></a>
The configuration item to set, such as the admin role for the OpenSearch application.
*Required*: Yes
*Type*: String
*Allowed values*: `opensearchDashboards.dashboardAdmin.users | opensearchDashboards.dashboardAdmin.groups`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-opensearchservice-application-appconfig-value"></a>
The value assigned to the configuration key, such as an IAM user ARN.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

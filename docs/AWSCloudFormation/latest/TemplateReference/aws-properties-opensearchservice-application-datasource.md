---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-application-datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Application DataSource
<a name="aws-properties-opensearchservice-application-datasource"></a>

Data sources that are associated with an OpenSearch application.

## Syntax
<a name="aws-properties-opensearchservice-application-datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-application-datasource-syntax.json"></a>

```
{
  "[DataSourceArn](#cfn-opensearchservice-application-datasource-datasourcearn)" : {{String}},
  "[DataSourceDescription](#cfn-opensearchservice-application-datasource-datasourcedescription)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-application-datasource-syntax.yaml"></a>

```
  [DataSourceArn](#cfn-opensearchservice-application-datasource-datasourcearn): {{String}}
  [DataSourceDescription](#cfn-opensearchservice-application-datasource-datasourcedescription): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-application-datasource-properties"></a>

`DataSourceArn`  <a name="cfn-opensearchservice-application-datasource-datasourcearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSourceDescription`  <a name="cfn-opensearchservice-application-datasource-datasourcedescription"></a>
Detailed description of a data source.
*Required*: No
*Type*: String
*Pattern*: `^([a-zA-Z0-9_])*[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

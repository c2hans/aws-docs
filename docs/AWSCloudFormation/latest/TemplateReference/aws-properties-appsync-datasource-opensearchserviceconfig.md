---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-datasource-opensearchserviceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DataSource OpenSearchServiceConfig
<a name="aws-properties-appsync-datasource-opensearchserviceconfig"></a>

The `OpenSearchServiceConfig` property type specifies the `AwsRegion` and `Endpoints` for an Amazon OpenSearch Service domain in your account for an AWS AppSync data source.

`OpenSearchServiceConfig` is a property of the [AWS::AppSync::DataSource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html) property type.

## Syntax
<a name="aws-properties-appsync-datasource-opensearchserviceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-datasource-opensearchserviceconfig-syntax.json"></a>

```
{
  "[AwsRegion](#cfn-appsync-datasource-opensearchserviceconfig-awsregion)" : {{String}},
  "[Endpoint](#cfn-appsync-datasource-opensearchserviceconfig-endpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-datasource-opensearchserviceconfig-syntax.yaml"></a>

```
  [AwsRegion](#cfn-appsync-datasource-opensearchserviceconfig-awsregion): {{String}}
  [Endpoint](#cfn-appsync-datasource-opensearchserviceconfig-endpoint): {{String}}
```

## Properties
<a name="aws-properties-appsync-datasource-opensearchserviceconfig-properties"></a>

`AwsRegion`  <a name="cfn-appsync-datasource-opensearchserviceconfig-awsregion"></a>
The AWS Region.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-appsync-datasource-opensearchserviceconfig-endpoint"></a>
The endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

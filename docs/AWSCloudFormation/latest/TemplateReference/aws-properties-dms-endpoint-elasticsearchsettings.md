---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-endpoint-elasticsearchsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::Endpoint ElasticsearchSettings
<a name="aws-properties-dms-endpoint-elasticsearchsettings"></a>

Provides information that defines an OpenSearch endpoint. This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about the available settings, see [ Extra connection attributes when using OpenSearch as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration) in the *AWS Database Migration Service User Guide*.

## Syntax
<a name="aws-properties-dms-endpoint-elasticsearchsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-endpoint-elasticsearchsettings-syntax.json"></a>

```
{
  "[EndpointUri](#cfn-dms-endpoint-elasticsearchsettings-endpointuri)" : {{String}},
  "[ErrorRetryDuration](#cfn-dms-endpoint-elasticsearchsettings-errorretryduration)" : {{Integer}},
  "[FullLoadErrorPercentage](#cfn-dms-endpoint-elasticsearchsettings-fullloaderrorpercentage)" : {{Integer}},
  "[ServiceAccessRoleArn](#cfn-dms-endpoint-elasticsearchsettings-serviceaccessrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-endpoint-elasticsearchsettings-syntax.yaml"></a>

```
  [EndpointUri](#cfn-dms-endpoint-elasticsearchsettings-endpointuri): {{String}}
  [ErrorRetryDuration](#cfn-dms-endpoint-elasticsearchsettings-errorretryduration): {{Integer}}
  [FullLoadErrorPercentage](#cfn-dms-endpoint-elasticsearchsettings-fullloaderrorpercentage): {{Integer}}
  [ServiceAccessRoleArn](#cfn-dms-endpoint-elasticsearchsettings-serviceaccessrolearn): {{String}}
```

## Properties
<a name="aws-properties-dms-endpoint-elasticsearchsettings-properties"></a>

`EndpointUri`  <a name="cfn-dms-endpoint-elasticsearchsettings-endpointuri"></a>
The endpoint for the OpenSearch cluster. AWS DMS uses HTTPS if a transport protocol (either HTTP or HTTPS) isn't specified.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ErrorRetryDuration`  <a name="cfn-dms-endpoint-elasticsearchsettings-errorretryduration"></a>
The maximum number of seconds for which DMS retries failed API requests to the OpenSearch cluster.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FullLoadErrorPercentage`  <a name="cfn-dms-endpoint-elasticsearchsettings-fullloaderrorpercentage"></a>
The maximum percentage of records that can fail to be written before a full load operation stops.
To avoid early failure, this counter is only effective after 1,000 records are transferred. OpenSearch also has the concept of error monitoring during the last 10 minutes of an Observation Window. If transfer of all records fail in the last 10 minutes, the full load operation stops.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceAccessRoleArn`  <a name="cfn-dms-endpoint-elasticsearchsettings-serviceaccessrolearn"></a>
The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

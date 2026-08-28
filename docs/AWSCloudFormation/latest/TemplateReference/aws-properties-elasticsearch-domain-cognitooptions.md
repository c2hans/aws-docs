---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticsearch-domain-cognitooptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Elasticsearch::Domain CognitoOptions
<a name="aws-properties-elasticsearch-domain-cognitooptions"></a>

Configures OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.

**Important**
The `AWS::Elasticsearch::Domain` resource is being replaced by the [AWS::OpenSearchService::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html) resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see [New resource types](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource) in the *Amazon OpenSearch Service Developer Guide*.

## Syntax
<a name="aws-properties-elasticsearch-domain-cognitooptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticsearch-domain-cognitooptions-syntax.json"></a>

```
{
  "[Enabled](#cfn-elasticsearch-domain-cognitooptions-enabled)" : {{Boolean}},
  "[IdentityPoolId](#cfn-elasticsearch-domain-cognitooptions-identitypoolid)" : {{String}},
  "[RoleArn](#cfn-elasticsearch-domain-cognitooptions-rolearn)" : {{String}},
  "[UserPoolId](#cfn-elasticsearch-domain-cognitooptions-userpoolid)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticsearch-domain-cognitooptions-syntax.yaml"></a>

```
  [Enabled](#cfn-elasticsearch-domain-cognitooptions-enabled): {{Boolean}}
  [IdentityPoolId](#cfn-elasticsearch-domain-cognitooptions-identitypoolid): {{String}}
  [RoleArn](#cfn-elasticsearch-domain-cognitooptions-rolearn): {{String}}
  [UserPoolId](#cfn-elasticsearch-domain-cognitooptions-userpoolid): {{String}}
```

## Properties
<a name="aws-properties-elasticsearch-domain-cognitooptions-properties"></a>

`Enabled`  <a name="cfn-elasticsearch-domain-cognitooptions-enabled"></a>
Whether to enable or disable Amazon Cognito authentication for OpenSearch Dashboards. See [Amazon Cognito authentication for OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityPoolId`  <a name="cfn-elasticsearch-domain-cognitooptions-identitypoolid"></a>
The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication. Required if you enable Cognito authentication.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-elasticsearch-domain-cognitooptions-rolearn"></a>
The `AmazonESCognitoAccess` role that allows OpenSearch Service to configure your user pool and identity pool. Required if you enable Cognito authentication.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-elasticsearch-domain-cognitooptions-userpoolid"></a>
The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication. Required if you enable Cognito authentication.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

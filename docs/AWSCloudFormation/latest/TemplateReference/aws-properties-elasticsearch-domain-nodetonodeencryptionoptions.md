---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticsearch-domain-nodetonodeencryptionoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Elasticsearch::Domain NodeToNodeEncryptionOptions
<a name="aws-properties-elasticsearch-domain-nodetonodeencryptionoptions"></a>

Specifies whether node-to-node encryption is enabled.

**Important**
The `AWS::Elasticsearch::Domain` resource is being replaced by the [AWS::OpenSearchService::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html) resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see [New resource types](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource) in the *Amazon OpenSearch Service Developer Guide*.

## Syntax
<a name="aws-properties-elasticsearch-domain-nodetonodeencryptionoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticsearch-domain-nodetonodeencryptionoptions-syntax.json"></a>

```
{
  "[Enabled](#cfn-elasticsearch-domain-nodetonodeencryptionoptions-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-elasticsearch-domain-nodetonodeencryptionoptions-syntax.yaml"></a>

```
  [Enabled](#cfn-elasticsearch-domain-nodetonodeencryptionoptions-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-elasticsearch-domain-nodetonodeencryptionoptions-properties"></a>

`Enabled`  <a name="cfn-elasticsearch-domain-nodetonodeencryptionoptions-enabled"></a>
Specifies whether node-to-node encryption is enabled, as a Boolean.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

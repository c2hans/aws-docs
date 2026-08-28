---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase AppIntegrationsConfiguration
<a name="aws-properties-wisdom-knowledgebase-appintegrationsconfiguration"></a>

Configuration information for Amazon AppIntegrations to automatically ingest content.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-appintegrationsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-appintegrationsconfiguration-syntax.json"></a>

```
{
  "[AppIntegrationArn](#cfn-wisdom-knowledgebase-appintegrationsconfiguration-appintegrationarn)" : {{String}},
  "[ObjectFields](#cfn-wisdom-knowledgebase-appintegrationsconfiguration-objectfields)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-appintegrationsconfiguration-syntax.yaml"></a>

```
  [AppIntegrationArn](#cfn-wisdom-knowledgebase-appintegrationsconfiguration-appintegrationarn): {{String}}
  [ObjectFields](#cfn-wisdom-knowledgebase-appintegrationsconfiguration-objectfields): {{
    - String}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-appintegrationsconfiguration-properties"></a>

`AppIntegrationArn`  <a name="cfn-wisdom-knowledgebase-appintegrationsconfiguration-appintegrationarn"></a>
The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content.
+  For [ Salesforce](https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm), your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least `Id`, `ArticleNumber`, `VersionNumber`, `Title`, `PublishStatus`, and `IsDeleted` as source fields.
+  For [ ServiceNow](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api), your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least `number`, `short_description`, `sys_mod_count`, `workflow_state`, and `active` as source fields.
+  For [ Zendesk](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/), your AppIntegrations DataIntegration must have an ObjectConfiguration if `objectFields` is not provided, including at least `id`, `title`, `updated_at`, and `draft` as source fields.
+  For [SharePoint](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index), your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among `docx`, `pdf`, `html`, `htm`, and `txt`.
+  For [Amazon S3](https://aws.amazon.com/s3/), the ObjectConfiguration and FileConfiguration of your AppIntegrations DataIntegration must be null. The `SourceURI` of your DataIntegration must use the following format: `s3://your_s3_bucket_name`.
**Important**
The bucket policy of the corresponding S3 bucket must allow the AWS principal `app-integrations.amazonaws.com` to perform `s3:ListBucket`, `s3:GetObject`, and `s3:GetBucketLocation` against the bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ObjectFields`  <a name="cfn-wisdom-knowledgebase-appintegrationsconfiguration-objectfields"></a>
The fields from the source that are made available to your agents in Amazon Q in Connect. Optional if ObjectConfiguration is included in the provided DataIntegration.
+  For [ Salesforce](https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm), you must include at least `Id`, `ArticleNumber`, `VersionNumber`, `Title`, `PublishStatus`, and `IsDeleted`.
+ For [ ServiceNow](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api), you must include at least `number`, `short_description`, `sys_mod_count`, `workflow_state`, and `active`.
+ For [ Zendesk](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/), you must include at least `id`, `title`, `updated_at`, and `draft`.
Make sure to include additional fields. These fields are indexed and used to source recommendations.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `4096 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

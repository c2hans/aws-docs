---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_AppIntegrationsConfiguration.html
---

# AppIntegrationsConfiguration
<a name="API_amazon-q-connect_AppIntegrationsConfiguration"></a>

Configuration information for Amazon AppIntegrations to automatically ingest content.

## Contents
<a name="API_amazon-q-connect_AppIntegrationsConfiguration_Contents"></a>

 ** appIntegrationArn **   <a name="connect-Type-amazon-q-connect_AppIntegrationsConfiguration-appIntegrationArn"></a>
The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content.
+  For [ Salesforce](https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm), your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least `Id`, `ArticleNumber`, `VersionNumber`, `Title`, `PublishStatus`, and `IsDeleted` as source fields.
+  For [ ServiceNow](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api), your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least `number`, `short_description`, `sys_mod_count`, `workflow_state`, and `active` as source fields.
+  For [ Zendesk](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/), your AppIntegrations DataIntegration must have an ObjectConfiguration if `objectFields` is not provided, including at least `id`, `title`, `updated_at`, and `draft` as source fields.
+  For [SharePoint](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index), your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among `docx`, `pdf`, `html`, `htm`, and `txt`.
+  For [Amazon S3](http://aws.amazon.com/s3/), the ObjectConfiguration and FileConfiguration of your AppIntegrations DataIntegration must be null. The `SourceURI` of your DataIntegration must use the following format: `s3://your_s3_bucket_name`.
**Important**
The bucket policy of the corresponding S3 bucket must allow the AWS principal `app-integrations.amazonaws.com` to perform `s3:ListBucket`, `s3:GetObject`, and `s3:GetBucketLocation` against the bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+`
Required: Yes

 ** objectFields **   <a name="connect-Type-amazon-q-connect_AppIntegrationsConfiguration-objectFields"></a>
The fields from the source that are made available to your agents in Amazon Q in Connect. Optional if ObjectConfiguration is included in the provided DataIntegration.
+  For [ Salesforce](https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm), you must include at least `Id`, `ArticleNumber`, `VersionNumber`, `Title`, `PublishStatus`, and `IsDeleted`.
+ For [ ServiceNow](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api), you must include at least `number`, `short_description`, `sys_mod_count`, `workflow_state`, and `active`.
+ For [ Zendesk](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/), you must include at least `id`, `title`, `updated_at`, and `draft`.
Make sure to include additional fields. These fields are indexed and used to source recommendations.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_AppIntegrationsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AppIntegrationsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AppIntegrationsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AppIntegrationsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

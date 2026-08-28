---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_OpenSearchWorkspace.html
---

# OpenSearchWorkspace
<a name="API_OpenSearchWorkspace"></a>

This structure contains information about the OpenSearch Service workspace used for this integration. An OpenSearch Service workspace is the collection of dashboards along with other OpenSearch Service tools. This workspace was created automatically as part of the integration setup. For more information, see [Centralized OpenSearch user interface (Dashboards) with OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html).

## Contents
<a name="API_OpenSearchWorkspace_Contents"></a>

 ** status **   <a name="CWL-Type-OpenSearchWorkspace-status"></a>
This structure contains information about the status of an OpenSearch Service resource.
Type: [OpenSearchResourceStatus](API_OpenSearchResourceStatus.md) object
Required: No

 ** workspaceId **   <a name="CWL-Type-OpenSearchWorkspace-workspaceId"></a>
The ID of this workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

## See Also
<a name="API_OpenSearchWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/OpenSearchWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/OpenSearchWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/OpenSearchWorkspace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

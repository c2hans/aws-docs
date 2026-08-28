---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_IntegrationDetails.html
---

# IntegrationDetails
<a name="API_IntegrationDetails"></a>

This structure contains information about the integration configuration. For an integration with OpenSearch Service, this includes information about OpenSearch Service resources such as the collection, the workspace, and policies.

This structure is returned by a [GetIntegration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetIntegration.html) operation.

## Contents
<a name="API_IntegrationDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** openSearchIntegrationDetails **   <a name="CWL-Type-IntegrationDetails-openSearchIntegrationDetails"></a>
This structure contains complete information about one integration between CloudWatch Logs and OpenSearch Service.
Type: [OpenSearchIntegrationDetails](API_OpenSearchIntegrationDetails.md) object
Required: No

## See Also
<a name="API_IntegrationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/IntegrationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/IntegrationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/IntegrationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

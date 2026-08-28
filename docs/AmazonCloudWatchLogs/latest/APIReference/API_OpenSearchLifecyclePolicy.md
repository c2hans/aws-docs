---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_OpenSearchLifecyclePolicy.html
---

# OpenSearchLifecyclePolicy
<a name="API_OpenSearchLifecyclePolicy"></a>

This structure contains information about the OpenSearch Service data lifecycle policy used for this integration. The lifecycle policy determines the lifespan of the data in the collection. It was automatically created as part of the integration setup.

For more information, see [Using data lifecycle policies with OpenSearch Service Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html) in the OpenSearch Service Developer Guide.

## Contents
<a name="API_OpenSearchLifecyclePolicy_Contents"></a>

 ** policyName **   <a name="CWL-Type-OpenSearchLifecyclePolicy-policyName"></a>
The name of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** status **   <a name="CWL-Type-OpenSearchLifecyclePolicy-status"></a>
This structure contains information about the status of this OpenSearch Service resource.
Type: [OpenSearchResourceStatus](API_OpenSearchResourceStatus.md) object
Required: No

## See Also
<a name="API_OpenSearchLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/OpenSearchLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/OpenSearchLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/OpenSearchLifecyclePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

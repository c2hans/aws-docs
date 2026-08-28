---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_UnprocessedUpdateAction.html
---

# UnprocessedUpdateAction
<a name="API_UnprocessedUpdateAction"></a>

Update action that has failed to be processed for the corresponding apply/stop request

## Contents
<a name="API_UnprocessedUpdateAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CacheClusterId **
The ID of the cache cluster
Type: String
Required: No

 ** ErrorMessage **
The error message that describes the reason the request was not processed
Type: String
Required: No

 ** ErrorType **
The error type for requests that are not processed
Type: String
Required: No

 ** ReplicationGroupId **
The replication group ID
Type: String
Required: No

 ** ServiceUpdateName **
The unique ID of the service update
Type: String
Required: No

## See Also
<a name="API_UnprocessedUpdateAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/UnprocessedUpdateAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/UnprocessedUpdateAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/UnprocessedUpdateAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

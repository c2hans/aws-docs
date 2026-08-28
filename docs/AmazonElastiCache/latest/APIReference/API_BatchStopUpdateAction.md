---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_BatchStopUpdateAction.html
---

# BatchStopUpdateAction
<a name="API_BatchStopUpdateAction"></a>

Stop the service update. For more information on service updates and stopping them, see [Stopping Service Updates](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/stopping-self-service-updates.html).

## Request Parameters
<a name="API_BatchStopUpdateAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ServiceUpdateName **
The unique ID of the service update
Type: String
Required: Yes

 **CacheClusterIds.member.N**
The cache cluster IDs
Type: Array of strings
Array Members: Maximum number of 20 items.
Required: No

 **ReplicationGroupIds.member.N**
The replication group IDs
Type: Array of strings
Array Members: Maximum number of 20 items.
Required: No

## Response Elements
<a name="API_BatchStopUpdateAction_ResponseElements"></a>

The following elements are returned by the service.

 **ProcessedUpdateActions.ProcessedUpdateAction.N**
Update actions that have been processed successfully
Type: Array of [ProcessedUpdateAction](API_ProcessedUpdateAction.md) objects

 **UnprocessedUpdateActions.UnprocessedUpdateAction.N**
Update actions that haven't been processed successfully
Type: Array of [UnprocessedUpdateAction](API_UnprocessedUpdateAction.md) objects

## Errors
<a name="API_BatchStopUpdateAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** ServiceUpdateNotFoundFault **
The service update doesn't exist
HTTP Status Code: 404

## See Also
<a name="API_BatchStopUpdateAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/BatchStopUpdateAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/BatchStopUpdateAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/BatchStopUpdateAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/BatchStopUpdateAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/BatchStopUpdateAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/BatchStopUpdateAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/BatchStopUpdateAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/BatchStopUpdateAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/BatchStopUpdateAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/BatchStopUpdateAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

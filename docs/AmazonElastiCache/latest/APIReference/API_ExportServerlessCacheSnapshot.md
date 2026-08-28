---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ExportServerlessCacheSnapshot.html
---

# ExportServerlessCacheSnapshot
<a name="API_ExportServerlessCacheSnapshot"></a>

Provides the functionality to export the serverless cache snapshot data to Amazon S3. Available for Valkey and Redis OSS only.

## Request Parameters
<a name="API_ExportServerlessCacheSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** S3BucketName **
Name of the Amazon S3 bucket to export the snapshot to. The Amazon S3 bucket must also be in same region as the snapshot. Available for Valkey and Redis OSS only.
Type: String
Required: Yes

 ** ServerlessCacheSnapshotName **
The identifier of the serverless cache snapshot to be exported to S3. Available for Valkey and Redis OSS only.
Type: String
Required: Yes

## Response Elements
<a name="API_ExportServerlessCacheSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** ServerlessCacheSnapshot **
The state of a serverless cache at a specific point in time, to the millisecond. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: [ServerlessCacheSnapshot](API_ServerlessCacheSnapshot.md) object

## Errors
<a name="API_ExportServerlessCacheSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidServerlessCacheSnapshotStateFault **
The state of the serverless cache snapshot was not received. Available for Valkey, Redis OSS and Serverless Memcached only.
HTTP Status Code: 400

 ** ServerlessCacheSnapshotNotFoundFault **
This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.
HTTP Status Code: 404

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## See Also
<a name="API_ExportServerlessCacheSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/ExportServerlessCacheSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/ExportServerlessCacheSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ExportServerlessCacheSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/ExportServerlessCacheSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ExportServerlessCacheSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/ExportServerlessCacheSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/ExportServerlessCacheSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/ExportServerlessCacheSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/ExportServerlessCacheSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ExportServerlessCacheSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

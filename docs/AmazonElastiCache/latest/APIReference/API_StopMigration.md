---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_StopMigration.html
---

# StopMigration
<a name="API_StopMigration"></a>

Stops an ongoing data sync between the source and the serverless cache. The migration remains open and the data sync can be restarted. This operation is valid only while the migration is syncing; during cutover it returns `InvalidServerlessCacheStateFault`.

## Request Parameters
<a name="API_StopMigration_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ServerlessCacheName **
The name of the serverless cache for which to stop the data sync.
Type: String
Required: Yes

## Response Elements
<a name="API_StopMigration_ResponseElements"></a>

The following element is returned by the service.

 ** ServerlessCache **
Provides the details of the serverless cache for which the data sync stopped.
Type: [ServerlessCache](API_ServerlessCache.md) object

## Errors
<a name="API_StopMigration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidServerlessCacheStateFault **
The account for these credentials is not currently active.
HTTP Status Code: 400

 ** ServerlessCacheNotFoundFault **
The serverless cache was not found or does not exist.
HTTP Status Code: 404

 ** ServerlessCacheNotUnderMigrationFault **
The serverless cache is not currently under migration.
HTTP Status Code: 400

## See Also
<a name="API_StopMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/StopMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/StopMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/StopMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/StopMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/StopMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/StopMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/StopMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/StopMigration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/StopMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/StopMigration)

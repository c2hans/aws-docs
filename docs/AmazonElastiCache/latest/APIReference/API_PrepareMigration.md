---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_PrepareMigration.html
---

# PrepareMigration
<a name="API_PrepareMigration"></a>

Prepares the serverless cache for data migration by validating the configuration and setting up the migration resources.

## Request Parameters
<a name="API_PrepareMigration_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **CustomerNodeEndpointList.member.N**
The list of endpoints from which to migrate data. For serverless cache migrations, the list should have only one element.
Type: Array of [CustomerNodeEndpoint](API_CustomerNodeEndpoint.md) objects
Required: Yes

 ** ServerlessCacheName **
The name of the serverless cache to prepare for migration.
Type: String
Required: Yes

 ** SourceAuthenticationConfiguration **
The authentication configuration for connecting to the source during migration.
Type: [SourceAuthenticationConfiguration](API_SourceAuthenticationConfiguration.md) object
Required: No

 ** SourceTlsConfiguration **
The TLS configuration for connecting to the source during migration.
Type: [SourceTlsConfiguration](API_SourceTlsConfiguration.md) object
Required: No

## Response Elements
<a name="API_PrepareMigration_ResponseElements"></a>

The following element is returned by the service.

 ** ServerlessCache **
Provides the details of the serverless cache prepared for migration.
Type: [ServerlessCache](API_ServerlessCache.md) object

## Errors
<a name="API_PrepareMigration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidServerlessCacheStateFault **
The account for these credentials is not currently active.
HTTP Status Code: 400

 ** ServerlessCacheAlreadyUnderMigrationFault **
A migration is already in progress for this serverless cache. You cannot start another migration until the current one completes.
HTTP Status Code: 400

 ** ServerlessCacheNotFoundFault **
The serverless cache was not found or does not exist.
HTTP Status Code: 404

## See Also
<a name="API_PrepareMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/PrepareMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/PrepareMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/PrepareMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/PrepareMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/PrepareMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/PrepareMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/PrepareMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/PrepareMigration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/PrepareMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/PrepareMigration)

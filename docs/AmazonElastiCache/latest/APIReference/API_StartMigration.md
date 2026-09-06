---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_StartMigration.html
---

# StartMigration
<a name="API_StartMigration"></a>

Start the migration of data.

## Request Parameters
<a name="API_StartMigration_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **CustomerNodeEndpointList.member.N**
List of endpoints from which data should be migrated. For Valkey or Redis OSS (cluster mode disabled), the list should have only one element.
Type: Array of [CustomerNodeEndpoint](API_CustomerNodeEndpoint.md) objects
Required: Yes

 ** ReplicationGroupId **
The ID of the replication group to which data should be migrated.
Type: String
Required: Yes

## Response Elements
<a name="API_StartMigration_ResponseElements"></a>

The following element is returned by the service.

 ** ReplicationGroup **
Contains all of the attributes of a specific Valkey or Redis OSS replication group.
Type: [ReplicationGroup](API_ReplicationGroup.md) object

## Errors
<a name="API_StartMigration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidReplicationGroupState **
The requested replication group is not in the `available` state.
HTTP Status Code: 400

 ** ReplicationGroupAlreadyUnderMigrationFault **
The targeted replication group is not available.
HTTP Status Code: 400

 ** ReplicationGroupNotFoundFault **
The specified replication group does not exist.
HTTP Status Code: 404

## See Also
<a name="API_StartMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/StartMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/StartMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/StartMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/StartMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/StartMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/StartMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/StartMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/StartMigration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/StartMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/StartMigration)

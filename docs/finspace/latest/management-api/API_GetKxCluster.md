---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxCluster.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# GetKxCluster
<a name="API_GetKxCluster"></a>

Retrieves information about a kdb cluster.

## Request Syntax
<a name="API_GetKxCluster_RequestSyntax"></a>

```
GET /kx/environments/{{environmentId}}/clusters/{{clusterName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetKxCluster_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clusterName](#API_GetKxCluster_RequestSyntax) **   <a name="finspace-GetKxCluster-request-uri-clusterName"></a>
The name of the cluster that you want to retrieve.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [environmentId](#API_GetKxCluster_RequestSyntax) **   <a name="finspace-GetKxCluster-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`
Required: Yes

## Request Body
<a name="API_GetKxCluster_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetKxCluster_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "autoScalingConfiguration": {
      "autoScalingMetric": "string",
      "maxNodeCount": number,
      "metricTarget": number,
      "minNodeCount": number,
      "scaleInCooldownSeconds": number,
      "scaleOutCooldownSeconds": number
   },
   "availabilityZoneId": "string",
   "azMode": "string",
   "cacheStorageConfigurations": [
      {
         "size": number,
         "type": "string"
      }
   ],
   "capacityConfiguration": {
      "nodeCount": number,
      "nodeType": "string"
   },
   "clusterDescription": "string",
   "clusterName": "string",
   "clusterType": "string",
   "code": {
      "s3Bucket": "string",
      "s3Key": "string",
      "s3ObjectVersion": "string"
   },
   "commandLineArguments": [
      {
         "key": "string",
         "value": "string"
      }
   ],
   "createdTimestamp": number,
   "databases": [
      {
         "cacheConfigurations": [
            {
               "cacheType": "string",
               "dataviewName": "string",
               "dbPaths": [ "string" ]
            }
         ],
         "changesetId": "string",
         "databaseName": "string",
         "dataviewConfiguration": {
            "changesetId": "string",
            "dataviewName": "string",
            "dataviewVersionId": "string",
            "segmentConfigurations": [
               {
                  "dbPaths": [ "string" ],
                  "onDemand": boolean,
                  "volumeName": "string"
               }
            ]
         },
         "dataviewName": "string"
      }
   ],
   "executionRole": "string",
   "initializationScript": "string",
   "lastModifiedTimestamp": number,
   "releaseLabel": "string",
   "savedownStorageConfiguration": {
      "size": number,
      "type": "string",
      "volumeName": "string"
   },
   "scalingGroupConfiguration": {
      "cpu": number,
      "memoryLimit": number,
      "memoryReservation": number,
      "nodeCount": number,
      "scalingGroupName": "string"
   },
   "status": "string",
   "statusReason": "string",
   "tickerplantLogConfiguration": {
      "tickerplantLogVolumes": [ "string" ]
   },
   "volumes": [
      {
         "volumeName": "string",
         "volumeType": "string"
      }
   ],
   "vpcConfiguration": {
      "ipAddressType": "string",
      "securityGroupIds": [ "string" ],
      "subnetIds": [ "string" ],
      "vpcId": "string"
   }
}
```

## Response Elements
<a name="API_GetKxCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autoScalingConfiguration](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-autoScalingConfiguration"></a>
The configuration based on which FinSpace will scale in or scale out nodes in your cluster.
Type: [AutoScalingConfiguration](API_AutoScalingConfiguration.md) object

 ** [availabilityZoneId](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-availabilityZoneId"></a>
 The availability zone identifiers for the requested regions.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [azMode](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-azMode"></a>
The number of availability zones you want to assign per cluster. This can be one of the following
+  `SINGLE` – Assigns one availability zone per cluster.
+  `MULTI` – Assigns all the availability zones per cluster.
Type: String
Valid Values: `SINGLE | MULTI`

 ** [cacheStorageConfigurations](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-cacheStorageConfigurations"></a>
The configurations for a read only cache storage associated with a cluster. This cache will be stored as an FSx Lustre that reads from the S3 store.
Type: Array of [KxCacheStorageConfiguration](API_KxCacheStorageConfiguration.md) objects

 ** [capacityConfiguration](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-capacityConfiguration"></a>
A structure for the metadata of a cluster. It includes information like the CPUs needed, memory of instances, and number of instances.
Type: [CapacityConfiguration](API_CapacityConfiguration.md) object

 ** [clusterDescription](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-clusterDescription"></a>
A description of the cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`

 ** [clusterName](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-clusterName"></a>
A unique name for the cluster.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [clusterType](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-clusterType"></a>
Specifies the type of KDB database that is being created. The following types are available:
+ HDB – A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.
+ RDB – A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the `savedownStorageConfiguration` parameter.
+ GATEWAY – A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.
+ GP – A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only `SINGLE` AZ mode.
+ Tickerplant – A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.
Type: String
Valid Values: `HDB | RDB | GATEWAY | GP | TICKERPLANT`

 ** [code](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-code"></a>
The details of the custom code that you want to use inside a cluster when analyzing a data. It consists of the S3 source bucket, location, S3 object version, and the relative path from where the custom code is loaded into the cluster.
Type: [CodeConfiguration](API_CodeConfiguration.md) object

 ** [commandLineArguments](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-commandLineArguments"></a>
Defines key-value pairs to make them available inside the cluster.
Type: Array of [KxCommandLineArgument](API_KxCommandLineArgument.md) objects

 ** [createdTimestamp](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-createdTimestamp"></a>
The timestamp at which the cluster was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [databases](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-databases"></a>
 A list of databases mounted on the cluster.
Type: Array of [KxDatabaseConfiguration](API_KxDatabaseConfiguration.md) objects

 ** [executionRole](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-executionRole"></a>
 An IAM role that defines a set of permissions associated with a cluster. These permissions are assumed when a cluster attempts to access another cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn:aws[a-z0-9-]*:iam::\d{12}:role\/[\w-\/.@+=,]{1,1017}$`

 ** [initializationScript](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-initializationScript"></a>
Specifies a Q program that will be run at launch of a cluster. It is a relative path within *.zip* file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, `somedir/init.q`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\_\-\.\/\\]+$`

 ** [lastModifiedTimestamp](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-lastModifiedTimestamp"></a>
The last time that the cluster was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [releaseLabel](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-releaseLabel"></a>
The version of FinSpace managed kdb to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Pattern: `^[a-zA-Z0-9._-]+$`

 ** [savedownStorageConfiguration](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-savedownStorageConfiguration"></a>
The size and type of the temporary storage that is used to hold data during the savedown process. This parameter is required when you choose `clusterType` as RDB. All the data written to this storage space is lost when the cluster node is restarted.
Type: [KxSavedownStorageConfiguration](API_KxSavedownStorageConfiguration.md) object

 ** [scalingGroupConfiguration](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-scalingGroupConfiguration"></a>
The structure that stores the capacity configuration details of a scaling group.
Type: [KxScalingGroupConfiguration](API_KxScalingGroupConfiguration.md) object

 ** [status](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-status"></a>
The status of cluster creation.
+ PENDING – The cluster is pending creation.
+ CREATING – The cluster creation process is in progress.
+ CREATE\_FAILED – The cluster creation process has failed.
+ RUNNING – The cluster creation process is running.
+ UPDATING – The cluster is in the process of being updated.
+ DELETING – The cluster is in the process of being deleted.
+ DELETED – The cluster has been deleted.
+ DELETE\_FAILED – The cluster failed to delete.
Type: String
Valid Values: `PENDING | CREATING | CREATE_FAILED | RUNNING | UPDATING | DELETING | DELETED | DELETE_FAILED`

 ** [statusReason](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-statusReason"></a>
The error message when a failed state occurs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`

 ** [tickerplantLogConfiguration](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-tickerplantLogConfiguration"></a>
 A configuration to store the Tickerplant logs. It consists of a list of volumes that will be mounted to your cluster. For the cluster type `Tickerplant`, the location of the TP volume on the cluster will be available by using the global variable `.aws.tp_log_path`.
Type: [TickerplantLogConfiguration](API_TickerplantLogConfiguration.md) object

 ** [volumes](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-volumes"></a>
 A list of volumes attached to the cluster.
Type: Array of [Volume](API_Volume.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [vpcConfiguration](#API_GetKxCluster_ResponseSyntax) **   <a name="finspace-GetKxCluster-response-vpcConfiguration"></a>
Configuration details about the network where the Privatelink endpoint of the cluster resides.
Type: [VpcConfiguration](API_VpcConfiguration.md) object

## Errors
<a name="API_GetKxCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit or quota is exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetKxCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/GetKxCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/GetKxCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/GetKxCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/GetKxCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/GetKxCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/GetKxCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/GetKxCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/GetKxCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/GetKxCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/GetKxCluster)

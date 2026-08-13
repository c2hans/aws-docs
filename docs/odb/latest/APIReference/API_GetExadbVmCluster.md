---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_GetExadbVmCluster.html
---

# GetExadbVmCluster
<a name="API_GetExadbVmCluster"></a>

Returns information about the specified Exascale VM cluster.

## Request Syntax
<a name="API_GetExadbVmCluster_RequestSyntax"></a>

```
{
   "exadbVmClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetExadbVmCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [exadbVmClusterId](#API_GetExadbVmCluster_RequestSyntax) **   <a name="odb-GetExadbVmCluster-request-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

## Response Syntax
<a name="API_GetExadbVmCluster_ResponseSyntax"></a>

```
{
   "exadbVmCluster": {
      "clusterName": "string",
      "createdAt": "string",
      "dataCollectionOptions": {
         "isDiagnosticsEventsEnabled": boolean,
         "isHealthMonitoringEnabled": boolean,
         "isIncidentLogsEnabled": boolean
      },
      "displayName": "string",
      "domain": "string",
      "enabledEcpuCount": number,
      "exadbVmClusterArn": "string",
      "exadbVmClusterId": "string",
      "exascaleDbStorageVaultArn": "string",
      "exascaleDbStorageVaultId": "string",
      "giVersion": "string",
      "gridImageId": "string",
      "gridImageType": "string",
      "hostname": "string",
      "iamRoles": [
         {
            "awsIntegration": "string",
            "iamRoleArn": "string",
            "status": "string",
            "statusReason": "string"
         }
      ],
      "iormConfigCache": {
         "dbPlans": [
            {
               "dbName": "string",
               "flashCacheLimit": "string",
               "share": number
            }
         ],
         "lifecycleDetails": "string",
         "lifecycleState": "string",
         "objective": "string"
      },
      "lastUpdateHistoryEntryId": "string",
      "licenseModel": "string",
      "listenerPort": number,
      "memorySizeInGBs": number,
      "nodeCount": number,
      "ocid": "string",
      "ociResourceAnchorName": "string",
      "ociUrl": "string",
      "odbNetworkArn": "string",
      "odbNetworkId": "string",
      "percentProgress": number,
      "scanDnsName": "string",
      "scanDnsRecordId": "string",
      "scanIpIds": [ "string" ],
      "scanListenerPortTcp": number,
      "scanListenerPortTcpSsl": number,
      "shape": "string",
      "shapeAttribute": "string",
      "snapshotFileSystemStorage": {
         "totalSizeInGBs": number
      },
      "sshPublicKeys": [ "string" ],
      "status": "string",
      "statusReason": "string",
      "systemVersion": "string",
      "timeZone": "string",
      "totalEcpuCount": number,
      "totalFileSystemStorage": {
         "totalSizeInGBs": number
      },
      "vipIds": [ "string" ],
      "vmFileSystemStorage": {
         "totalSizeInGBs": number
      }
   }
}
```

## Response Elements
<a name="API_GetExadbVmCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [exadbVmCluster](#API_GetExadbVmCluster_ResponseSyntax) **   <a name="odb-GetExadbVmCluster-response-exadbVmCluster"></a>
The Exascale VM cluster.
Type: [ExadbVmCluster](API_ExadbVmCluster.md) object

## Errors
<a name="API_GetExadbVmCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_GetExadbVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/GetExadbVmCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/GetExadbVmCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/GetExadbVmCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/GetExadbVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/GetExadbVmCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/GetExadbVmCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/GetExadbVmCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/GetExadbVmCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/GetExadbVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/GetExadbVmCluster)

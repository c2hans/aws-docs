---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListCloudVmClusters.html
---

# ListCloudVmClusters
<a name="API_ListCloudVmClusters"></a>

Returns information about the VM clusters owned by your AWS account or only the ones on the specified Exadata infrastructure.

## Request Syntax
<a name="API_ListCloudVmClusters_RequestSyntax"></a>

```
{
   "cloudExadataInfrastructureId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCloudVmClusters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudExadataInfrastructureId](#API_ListCloudVmClusters_RequestSyntax) **   <a name="odb-ListCloudVmClusters-request-cloudExadataInfrastructureId"></a>
The unique identifier of the Oracle Exadata infrastructure.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** [maxResults](#API_ListCloudVmClusters_RequestSyntax) **   <a name="odb-ListCloudVmClusters-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Default: `10`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListCloudVmClusters_RequestSyntax) **   <a name="odb-ListCloudVmClusters-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_ListCloudVmClusters_ResponseSyntax"></a>

```
{
   "cloudVmClusters": [
      {
         "cloudExadataInfrastructureArn": "string",
         "cloudExadataInfrastructureId": "string",
         "cloudVmClusterArn": "string",
         "cloudVmClusterId": "string",
         "clusterName": "string",
         "computeModel": "string",
         "cpuCoreCount": number,
         "createdAt": "string",
         "dataCollectionOptions": {
            "isDiagnosticsEventsEnabled": boolean,
            "isHealthMonitoringEnabled": boolean,
            "isIncidentLogsEnabled": boolean
         },
         "dataStorageSizeInTBs": number,
         "dbNodeStorageSizeInGBs": number,
         "dbServers": [ "string" ],
         "diskRedundancy": "string",
         "displayName": "string",
         "domain": "string",
         "giVersion": "string",
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
         "isLocalBackupEnabled": boolean,
         "isSparseDiskgroupEnabled": boolean,
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
         "shape": "string",
         "sshPublicKeys": [ "string" ],
         "status": "string",
         "statusReason": "string",
         "storageSizeInGBs": number,
         "systemVersion": "string",
         "timeZone": "string",
         "vipIds": [ "string" ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCloudVmClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cloudVmClusters](#API_ListCloudVmClusters_ResponseSyntax) **   <a name="odb-ListCloudVmClusters-response-cloudVmClusters"></a>
The list of VM clusters along with their properties.
Type: Array of [CloudVmClusterSummary](API_CloudVmClusterSummary.md) objects

 ** [nextToken](#API_ListCloudVmClusters_ResponseSyntax) **   <a name="odb-ListCloudVmClusters-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

## Errors
<a name="API_ListCloudVmClusters_Errors"></a>

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
<a name="API_ListCloudVmClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListCloudVmClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListCloudVmClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListCloudVmClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListCloudVmClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListCloudVmClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListCloudVmClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListCloudVmClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListCloudVmClusters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListCloudVmClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListCloudVmClusters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListDbNodes.html
---

# ListDbNodes
<a name="API_ListDbNodes"></a>

Returns information about the DB nodes for the specified VM cluster.

## Request Syntax
<a name="API_ListDbNodes_RequestSyntax"></a>

```
{
   "cloudVmClusterId": "{{string}}",
   "exadbVmClusterId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDbNodes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudVmClusterId](#API_ListDbNodes_RequestSyntax) **   <a name="odb-ListDbNodes-request-cloudVmClusterId"></a>
The unique identifier of the VM cluster. You must specify either this parameter or `exadbVmClusterId`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** [exadbVmClusterId](#API_ListDbNodes_RequestSyntax) **   <a name="odb-ListDbNodes-request-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster. You must specify either this parameter or `cloudVmClusterId`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** [maxResults](#API_ListDbNodes_RequestSyntax) **   <a name="odb-ListDbNodes-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Default: `10`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListDbNodes_RequestSyntax) **   <a name="odb-ListDbNodes-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_ListDbNodes_ResponseSyntax"></a>

```
{
   "dbNodes": [
      {
         "additionalDetails": "string",
         "backupIpId": "string",
         "backupVnic2Id": "string",
         "backupVnicId": "string",
         "cpuCoreCount": number,
         "createdAt": "string",
         "dbNodeArn": "string",
         "dbNodeId": "string",
         "dbNodeStorageSizeInGBs": number,
         "dbServerId": "string",
         "dbSystemId": "string",
         "faultDomain": "string",
         "hostIpId": "string",
         "hostname": "string",
         "maintenanceType": "string",
         "memorySizeInGBs": number,
         "ocid": "string",
         "ociResourceAnchorName": "string",
         "softwareStorageSizeInGB": number,
         "status": "string",
         "statusReason": "string",
         "timeMaintenanceWindowEnd": "string",
         "timeMaintenanceWindowStart": "string",
         "totalCpuCoreCount": number,
         "vnic2Id": "string",
         "vnicId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDbNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dbNodes](#API_ListDbNodes_ResponseSyntax) **   <a name="odb-ListDbNodes-response-dbNodes"></a>
The list of DB nodes along with their properties.
Type: Array of [DbNodeSummary](API_DbNodeSummary.md) objects

 ** [nextToken](#API_ListDbNodes_ResponseSyntax) **   <a name="odb-ListDbNodes-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

## Errors
<a name="API_ListDbNodes_Errors"></a>

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
<a name="API_ListDbNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListDbNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListDbNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListDbNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListDbNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListDbNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListDbNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListDbNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListDbNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListDbNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListDbNodes)

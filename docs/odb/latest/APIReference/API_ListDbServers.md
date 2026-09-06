---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListDbServers.html
---

# ListDbServers
<a name="API_ListDbServers"></a>

Returns information about the database servers that belong to the specified Exadata infrastructure.

## Request Syntax
<a name="API_ListDbServers_RequestSyntax"></a>

```
{
   "cloudExadataInfrastructureId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDbServers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudExadataInfrastructureId](#API_ListDbServers_RequestSyntax) **   <a name="odb-ListDbServers-request-cloudExadataInfrastructureId"></a>
The unique identifier of the Oracle Exadata infrastructure.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [maxResults](#API_ListDbServers_RequestSyntax) **   <a name="odb-ListDbServers-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Default: `10`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListDbServers_RequestSyntax) **   <a name="odb-ListDbServers-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_ListDbServers_ResponseSyntax"></a>

```
{
   "dbServers": [
      {
         "autonomousVirtualMachineIds": [ "string" ],
         "autonomousVmClusterIds": [ "string" ],
         "computeModel": "string",
         "cpuCoreCount": number,
         "createdAt": "string",
         "dbNodeStorageSizeInGBs": number,
         "dbServerId": "string",
         "dbServerPatchingDetails": {
            "estimatedPatchDuration": number,
            "patchingStatus": "string",
            "timePatchingEnded": "string",
            "timePatchingStarted": "string"
         },
         "displayName": "string",
         "exadataInfrastructureId": "string",
         "maxCpuCount": number,
         "maxDbNodeStorageInGBs": number,
         "maxMemoryInGBs": number,
         "memorySizeInGBs": number,
         "ocid": "string",
         "ociResourceAnchorName": "string",
         "shape": "string",
         "status": "string",
         "statusReason": "string",
         "vmClusterIds": [ "string" ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDbServers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dbServers](#API_ListDbServers_ResponseSyntax) **   <a name="odb-ListDbServers-response-dbServers"></a>
The list of database servers along with their properties.
Type: Array of [DbServerSummary](API_DbServerSummary.md) objects

 ** [nextToken](#API_ListDbServers_ResponseSyntax) **   <a name="odb-ListDbServers-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

## Errors
<a name="API_ListDbServers_Errors"></a>

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
<a name="API_ListDbServers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListDbServers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListDbServers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListDbServers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListDbServers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListDbServers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListDbServers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListDbServers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListDbServers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListDbServers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListDbServers)

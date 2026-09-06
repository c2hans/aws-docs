---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListExascaleDbStorageVaults.html
---

# ListExascaleDbStorageVaults
<a name="API_ListExascaleDbStorageVaults"></a>

Returns information about the Exascale storage vaults owned by your AWS account.

## Request Syntax
<a name="API_ListExascaleDbStorageVaults_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListExascaleDbStorageVaults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListExascaleDbStorageVaults_RequestSyntax) **   <a name="odb-ListExascaleDbStorageVaults-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListExascaleDbStorageVaults_RequestSyntax) **   <a name="odb-ListExascaleDbStorageVaults-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_ListExascaleDbStorageVaults_ResponseSyntax"></a>

```
{
   "exascaleDbStorageVaults": [
      {
         "additionalFlashCacheInPercent": number,
         "attachedShapeAttributes": [ "string" ],
         "autoscaleLimitInGBs": number,
         "availabilityZone": "string",
         "availabilityZoneId": "string",
         "createdAt": "string",
         "description": "string",
         "displayName": "string",
         "exascaleDbStorageVaultArn": "string",
         "exascaleDbStorageVaultId": "string",
         "highCapacityDatabaseStorage": {
            "availableSizeInGBs": number,
            "totalSizeInGBs": number
         },
         "isAutoscaleEnabled": boolean,
         "ocid": "string",
         "ociResourceAnchorName": "string",
         "ociUrl": "string",
         "percentProgress": number,
         "status": "string",
         "statusReason": "string",
         "timeZone": "string",
         "vmClusterArns": [ "string" ],
         "vmClusterCount": number,
         "vmClusterIds": [ "string" ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListExascaleDbStorageVaults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [exascaleDbStorageVaults](#API_ListExascaleDbStorageVaults_ResponseSyntax) **   <a name="odb-ListExascaleDbStorageVaults-response-exascaleDbStorageVaults"></a>
The list of Exascale storage vaults.
Type: Array of [ExascaleDbStorageVaultSummary](API_ExascaleDbStorageVaultSummary.md) objects

 ** [nextToken](#API_ListExascaleDbStorageVaults_ResponseSyntax) **   <a name="odb-ListExascaleDbStorageVaults-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

## Errors
<a name="API_ListExascaleDbStorageVaults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

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
<a name="API_ListExascaleDbStorageVaults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListExascaleDbStorageVaults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListExascaleDbStorageVaults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListExascaleDbStorageVaults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListExascaleDbStorageVaults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListExascaleDbStorageVaults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListExascaleDbStorageVaults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListExascaleDbStorageVaults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListExascaleDbStorageVaults)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListExascaleDbStorageVaults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListExascaleDbStorageVaults)

---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListGiMinorVersions.html
---

# ListGiMinorVersions
<a name="API_ListGiMinorVersions"></a>

Returns a list of the Oracle Grid Infrastructure (GI) minor versions for the specified major version.

## Request Syntax
<a name="API_ListGiMinorVersions_RequestSyntax"></a>

```
{
   "availabilityZone": "{{string}}",
   "availabilityZoneId": "{{string}}",
   "giVersion": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "shapeFamily": "{{string}}"
}
```

## Request Parameters
<a name="API_ListGiMinorVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [availabilityZone](#API_ListGiMinorVersions_RequestSyntax) **   <a name="odb-ListGiMinorVersions-request-availabilityZone"></a>
The Availability Zone to filter GI minor versions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [availabilityZoneId](#API_ListGiMinorVersions_RequestSyntax) **   <a name="odb-ListGiMinorVersions-request-availabilityZoneId"></a>
The Availability Zone ID to filter GI minor versions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [giVersion](#API_ListGiMinorVersions_RequestSyntax) **   <a name="odb-ListGiMinorVersions-request-giVersion"></a>
The Oracle Grid Infrastructure (GI) major version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [maxResults](#API_ListGiMinorVersions_RequestSyntax) **   <a name="odb-ListGiMinorVersions-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListGiMinorVersions_RequestSyntax) **   <a name="odb-ListGiMinorVersions-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [shapeFamily](#API_ListGiMinorVersions_RequestSyntax) **   <a name="odb-ListGiMinorVersions-request-shapeFamily"></a>
The shape family for the GI minor version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_ListGiMinorVersions_ResponseSyntax"></a>

```
{
   "giMinorVersions": [
      {
         "gridImageId": "string",
         "version": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListGiMinorVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [giMinorVersions](#API_ListGiMinorVersions_ResponseSyntax) **   <a name="odb-ListGiMinorVersions-response-giMinorVersions"></a>
The list of GI minor versions.
Type: Array of [GiMinorVersionSummary](API_GiMinorVersionSummary.md) objects

 ** [nextToken](#API_ListGiMinorVersions_ResponseSyntax) **   <a name="odb-ListGiMinorVersions-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

## Errors
<a name="API_ListGiMinorVersions_Errors"></a>

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
<a name="API_ListGiMinorVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListGiMinorVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListGiMinorVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListGiMinorVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListGiMinorVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListGiMinorVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListGiMinorVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListGiMinorVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListGiMinorVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListGiMinorVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListGiMinorVersions)

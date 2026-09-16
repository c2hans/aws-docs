---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListSystemVersions.html
---

# ListSystemVersions
<a name="API_ListSystemVersions"></a>

Returns information about the system versions that are available for a VM cluster for the specified `giVersion` and `shape`.

## Request Syntax
<a name="API_ListSystemVersions_RequestSyntax"></a>

```
{
   "giVersion": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "shape": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSystemVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [giVersion](#API_ListSystemVersions_RequestSyntax) **   <a name="odb-ListSystemVersions-request-giVersion"></a>
The software version of the Exadata Grid Infrastructure (GI).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Required: Yes

 ** [maxResults](#API_ListSystemVersions_RequestSyntax) **   <a name="odb-ListSystemVersions-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Default: `10`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListSystemVersions_RequestSyntax) **   <a name="odb-ListSystemVersions-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [shape](#API_ListSystemVersions_RequestSyntax) **   <a name="odb-ListSystemVersions-request-shape"></a>
The Exadata hardware system model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_ListSystemVersions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "systemVersions": [
      {
         "giVersion": "string",
         "shape": "string",
         "systemVersions": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_ListSystemVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSystemVersions_ResponseSyntax) **   <a name="odb-ListSystemVersions-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 ** [systemVersions](#API_ListSystemVersions_ResponseSyntax) **   <a name="odb-ListSystemVersions-response-systemVersions"></a>
The list of system versions.
Type: Array of [SystemVersionSummary](API_SystemVersionSummary.md) objects

## Errors
<a name="API_ListSystemVersions_Errors"></a>

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
<a name="API_ListSystemVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListSystemVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListSystemVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListSystemVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListSystemVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListSystemVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListSystemVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListSystemVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListSystemVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListSystemVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListSystemVersions)

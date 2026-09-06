---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetReadSet.html
---

# GetReadSet
<a name="API_GetReadSet"></a>

Retrieves detailed information from parts of a read set and returns the read set in the same format that it was uploaded. You must have read sets uploaded to your sequence store in order to run this operation.

## Request Syntax
<a name="API_GetReadSet_RequestSyntax"></a>

```
GET /sequencestore/{{sequenceStoreId}}/readset/{{id}}?file={{file}}&partNumber={{partNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetReadSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [file](#API_GetReadSet_RequestSyntax) **   <a name="omics-GetReadSet-request-uri-file"></a>
The file to retrieve.
Valid Values: `SOURCE1 | SOURCE2 | INDEX`

 ** [id](#API_GetReadSet_RequestSyntax) **   <a name="omics-GetReadSet-request-uri-id"></a>
The read set's ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** [partNumber](#API_GetReadSet_RequestSyntax) **   <a name="omics-GetReadSet-request-uri-partNumber"></a>
The part number to retrieve.
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: Yes

 ** [sequenceStoreId](#API_GetReadSet_RequestSyntax) **   <a name="omics-GetReadSet-request-uri-sequenceStoreId"></a>
The read set's sequence store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetReadSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReadSet_ResponseSyntax"></a>

```
HTTP/1.1 200

{{payload}}
```

## Response Elements
<a name="API_GetReadSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [payload](#API_GetReadSet_ResponseSyntax) **   <a name="omics-GetReadSet-response-payload"></a>
The read set file payload.

## Errors
<a name="API_GetReadSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RangeNotSatisfiableException **
The ranges specified in the request are not valid.
HTTP Status Code: 416

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetReadSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetReadSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetReadSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetReadSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetReadSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetReadSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetReadSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetReadSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetReadSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetReadSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetReadSet)

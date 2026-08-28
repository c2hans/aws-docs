---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetReference.html
---

# GetReference
<a name="API_GetReference"></a>

Downloads parts of data from a reference genome and returns the reference file in the same format that it was uploaded.

For more information, see [Creating a HealthOmics reference store](https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_GetReference_RequestSyntax"></a>

```
GET /referencestore/{{referenceStoreId}}/reference/{{id}}?file={{file}}&partNumber={{partNumber}} HTTP/1.1
Range: {{range}}
```

## URI Request Parameters
<a name="API_GetReference_RequestParameters"></a>

The request uses the following URI parameters.

 ** [file](#API_GetReference_RequestSyntax) **   <a name="omics-GetReference-request-uri-file"></a>
The file to retrieve.
Valid Values: `SOURCE | INDEX`

 ** [id](#API_GetReference_RequestSyntax) **   <a name="omics-GetReference-request-uri-id"></a>
The reference's ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** [partNumber](#API_GetReference_RequestSyntax) **   <a name="omics-GetReference-request-uri-partNumber"></a>
The part number to retrieve.
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: Yes

 ** [range](#API_GetReference_RequestSyntax) **   <a name="omics-GetReference-request-range"></a>
The range to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{N}||\p{P}]+`

 ** [referenceStoreId](#API_GetReference_RequestSyntax) **   <a name="omics-GetReference-request-uri-referenceStoreId"></a>
The reference's store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetReference_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReference_ResponseSyntax"></a>

```
HTTP/1.1 200

{{payload}}
```

## Response Elements
<a name="API_GetReference_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [payload](#API_GetReference_ResponseSyntax) **   <a name="omics-GetReference-response-payload"></a>
The reference file payload.

## Errors
<a name="API_GetReference_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetReference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetReference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetReference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetReference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetReference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetReference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetReference)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

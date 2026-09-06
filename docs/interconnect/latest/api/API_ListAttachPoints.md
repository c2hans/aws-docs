---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_ListAttachPoints.html
---

# ListAttachPoints
<a name="API_ListAttachPoints"></a>

Lists all [AttachPoint](API_AttachPoint.md) options the caller has access to that are valid for the specified [Environment](API_Environment.md).

## Request Parameters
<a name="API_ListAttachPoints_RequestParameters"></a>

 ** environmentId **
The identifier of the [Environment](API_Environment.md) for which to list valid Attach Points.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** maxResults **
The max number of list results in a single paginated response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
A pagination token from a previous paginated response indicating you wish to get the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Elements
<a name="API_ListAttachPoints_ResponseElements"></a>

The following elements are returned by the service.

 ** attachPoints **
The valid [AttachPoint](API_AttachPoint.md)
Type: Array of [AttachPointDescriptor](API_AttachPointDescriptor.md) objects

 ** nextToken **
A pagination token indicating that there are more results that can be fetched.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListAttachPoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The calling principal is not allowed to access the specified resource, or the resource does not exist.
HTTP Status Code: 403

 ** InterconnectClientException **
The request was denied due to incorrect client supplied parameters.
HTTP Status Code: 400

 ** InterconnectServerException **
The request resulted in an exception internal to the service.
HTTP Status Code: 500

 ** InterconnectValidationException **
The input fails to satisfy the constraints specified.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request specifies a resource that does not exist on the server.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The requested operation would result in the calling principal exceeding their allotted quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_ListAttachPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/interconnect-2022-07-26/ListAttachPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/interconnect-2022-07-26/ListAttachPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/ListAttachPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/interconnect-2022-07-26/ListAttachPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/ListAttachPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/interconnect-2022-07-26/ListAttachPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/interconnect-2022-07-26/ListAttachPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/interconnect-2022-07-26/ListAttachPoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/interconnect-2022-07-26/ListAttachPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/ListAttachPoints)

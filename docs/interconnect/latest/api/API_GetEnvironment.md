---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_GetEnvironment.html
---

# GetEnvironment
<a name="API_GetEnvironment"></a>

Describes a specific [Environment](API_Environment.md)

## Request Parameters
<a name="API_GetEnvironment_RequestParameters"></a>

 ** id **
The identifier of the specific [Environment](API_Environment.md) to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Elements
<a name="API_GetEnvironment_ResponseElements"></a>

The following element is returned by the service.

 ** environment **
The requested [Environment](API_Environment.md) structure.
Type: [Environment](API_Environment.md) object

## Errors
<a name="API_GetEnvironment_Errors"></a>

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
<a name="API_GetEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/interconnect-2022-07-26/GetEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/interconnect-2022-07-26/GetEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/GetEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/interconnect-2022-07-26/GetEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/GetEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/interconnect-2022-07-26/GetEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/interconnect-2022-07-26/GetEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/interconnect-2022-07-26/GetEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/interconnect-2022-07-26/GetEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/GetEnvironment)

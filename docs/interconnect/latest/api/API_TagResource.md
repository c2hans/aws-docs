---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Add new tags to the specified resource.

Currently this only supports [Connection](API_Connection.md) resources.

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

 ** arn **
The ARN of the resource that should receive the new tags.
Currently this must be an ARN for a [Connection](API_Connection.md) resource.
Type: String
Length Constraints: Minimum length of 59. Maximum length of 150.
Pattern: `arn:aws[a-z-]*:interconnect:[^:]+:[0-9]{12}:connection/(mcc|lmcc)-[a-z0-9]{8}`
Required: Yes

 ** tags **
A map of tags to apply to the specified resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## Errors
<a name="API_TagResource_Errors"></a>

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
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/interconnect-2022-07-26/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/interconnect-2022-07-26/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/interconnect-2022-07-26/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/interconnect-2022-07-26/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/interconnect-2022-07-26/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/interconnect-2022-07-26/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/interconnect-2022-07-26/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/TagResource)

---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_DescribeConnectionProposal.html
---

# DescribeConnectionProposal
<a name="API_DescribeConnectionProposal"></a>

Describes the details of a connection proposal generated at a partner's portal. This proposal is delivered in the form of an Activation Key.

## Request Syntax
<a name="API_DescribeConnectionProposal_RequestSyntax"></a>

```
{
   "activationKey": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConnectionProposal_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [activationKey](#API_DescribeConnectionProposal_RequestSyntax) **   <a name="interconnect-DescribeConnectionProposal-request-activationKey"></a>
An Activation Key that was generated on a supported partner's portal. This key captures the desired parameters from the initial creation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_DescribeConnectionProposal_ResponseSyntax"></a>

```
{
   "bandwidth": "string",
   "environmentId": "string",
   "location": "string",
   "provider": { ... }
}
```

## Response Elements
<a name="API_DescribeConnectionProposal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bandwidth](#API_DescribeConnectionProposal_ResponseSyntax) **   <a name="interconnect-DescribeConnectionProposal-response-bandwidth"></a>
The bandwidth of the proposed [Connection](API_Connection.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Pattern: `\d+[MG]bps`

 ** [environmentId](#API_DescribeConnectionProposal_ResponseSyntax) **   <a name="interconnect-DescribeConnectionProposal-response-environmentId"></a>
The identifier of the [Environment](API_Environment.md) upon which the [Connection](API_Connection.md) would be placed if this proposal were accepted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [location](#API_DescribeConnectionProposal_ResponseSyntax) **   <a name="interconnect-DescribeConnectionProposal-response-location"></a>
The partner specific location distinguisher of the specific [Environment](API_Environment.md) of the proposal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [provider](#API_DescribeConnectionProposal_ResponseSyntax) **   <a name="interconnect-DescribeConnectionProposal-response-provider"></a>
The partner provider of the specific [Environment](API_Environment.md) of the proposal.
Type: [Provider](API_Provider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_DescribeConnectionProposal_Errors"></a>

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
<a name="API_DescribeConnectionProposal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/interconnect-2022-07-26/DescribeConnectionProposal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/interconnect-2022-07-26/DescribeConnectionProposal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/DescribeConnectionProposal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/interconnect-2022-07-26/DescribeConnectionProposal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/DescribeConnectionProposal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/interconnect-2022-07-26/DescribeConnectionProposal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/interconnect-2022-07-26/DescribeConnectionProposal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/interconnect-2022-07-26/DescribeConnectionProposal)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/interconnect-2022-07-26/DescribeConnectionProposal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/DescribeConnectionProposal)

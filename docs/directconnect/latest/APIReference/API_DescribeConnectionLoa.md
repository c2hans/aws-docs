---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnectionLoa.html
---

# DescribeConnectionLoa
<a name="API_DescribeConnectionLoa"></a>

**Note**
Deprecated. Use [DescribeLoa](API_DescribeLoa.md) instead.

Gets the LOA-CFA for a connection.

The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that your APN partner or service provider uses when establishing your cross connect to AWS at the colocation facility. For more information, see [Requesting Cross Connects at Direct Connect Locations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html) in the * Direct Connect User Guide*.

## Request Syntax
<a name="API_DescribeConnectionLoa_RequestSyntax"></a>

```
{
   "connectionId": "{{string}}",
   "loaContentType": "{{string}}",
   "providerName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConnectionLoa_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [connectionId](#API_DescribeConnectionLoa_RequestSyntax) **   <a name="DX-DescribeConnectionLoa-request-connectionId"></a>
The ID of the connection.
Type: String
Required: Yes

 ** [loaContentType](#API_DescribeConnectionLoa_RequestSyntax) **   <a name="DX-DescribeConnectionLoa-request-loaContentType"></a>
The standard media type for the LOA-CFA document. The only supported value is application/pdf.
Type: String
Valid Values: `application/pdf`
Required: No

 ** [providerName](#API_DescribeConnectionLoa_RequestSyntax) **   <a name="DX-DescribeConnectionLoa-request-providerName"></a>
The name of the APN partner or service provider who establishes connectivity on your behalf. If you specify this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeConnectionLoa_ResponseSyntax"></a>

```
{
   "loa": {
      "loaContent": blob,
      "loaContentType": "string"
   }
}
```

## Response Elements
<a name="API_DescribeConnectionLoa_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [loa](#API_DescribeConnectionLoa_ResponseSyntax) **   <a name="DX-DescribeConnectionLoa-response-loa"></a>
The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).
Type: [Loa](API_Loa.md) object

## Errors
<a name="API_DescribeConnectionLoa_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConnectionLoa_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeConnectionLoa)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeConnectionLoa)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeConnectionLoa)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeConnectionLoa)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeConnectionLoa)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeConnectionLoa)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeConnectionLoa)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeConnectionLoa)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeConnectionLoa)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeConnectionLoa)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

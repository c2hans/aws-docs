---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfcAttachment.html
---

# CreateRfcAttachment
<a name="API_CreateRfcAttachment"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Create an attachment for an existing RFC.

## Request Syntax
<a name="API_CreateRfcAttachment_RequestSyntax"></a>

```
{
   "Content": {{blob}},
   "FileName": "{{string}}",
   "RfcId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateRfcAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Content](#API_CreateRfcAttachment_RequestSyntax) **   <a name="amscm-CreateRfcAttachment-request-Content"></a>
The content of the RFC attachment, which is binary data.
Type: Base64-encoded binary data object
Required: Yes

 ** [FileName](#API_CreateRfcAttachment_RequestSyntax) **   <a name="amscm-CreateRfcAttachment-request-FileName"></a>
The file name of the RFC attachment.
Type: String
Required: Yes

 ** [RfcId](#API_CreateRfcAttachment_RequestSyntax) **   <a name="amscm-CreateRfcAttachment-request-RfcId"></a>
The RFC identifier for an RFC attachment request.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateRfcAttachment_ResponseSyntax"></a>

```
{
   "AttachmentId": "string",
   "RfcId": "string"
}
```

## Response Elements
<a name="API_CreateRfcAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentId](#API_CreateRfcAttachment_ResponseSyntax) **   <a name="amscm-CreateRfcAttachment-response-AttachmentId"></a>
The attachment identifier in an RFC attachment response.
Type: String

 ** [RfcId](#API_CreateRfcAttachment_ResponseSyntax) **   <a name="amscm-CreateRfcAttachment-response-RfcId"></a>
The RFC identifier in an RFC attachment request.
Type: String

## Errors
<a name="API_CreateRfcAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

 ** InvalidRfcStateException **
The RFC is not in a state that allows the requested operation. Actual status code: 409
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource could not be located. Actual status code: 404
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
You have exceeded your service quotas.
HTTP Status Code: 400

## See Also
<a name="API_CreateRfcAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/CreateRfcAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/CreateRfcAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/CreateRfcAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/CreateRfcAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/CreateRfcAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/CreateRfcAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/CreateRfcAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/CreateRfcAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/CreateRfcAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/CreateRfcAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

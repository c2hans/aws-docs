---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_GetRfcAttachment.html
---

# GetRfcAttachment
<a name="API_GetRfcAttachment"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Retrieve the attachment from an RFC.

## Request Syntax
<a name="API_GetRfcAttachment_RequestSyntax"></a>

```
{
   "AttachmentId": "{{string}}",
   "RfcId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRfcAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttachmentId](#API_GetRfcAttachment_RequestSyntax) **   <a name="amscm-GetRfcAttachment-request-AttachmentId"></a>
The attachment identifier in an RFC attachment GET request.
Type: String
Required: Yes

 ** [RfcId](#API_GetRfcAttachment_RequestSyntax) **   <a name="amscm-GetRfcAttachment-request-RfcId"></a>
The RFC identifier in an RFC attachment GET request.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetRfcAttachment_ResponseSyntax"></a>

```
{
   "RfcAttachment": {
      "AttachmentId": "string",
      "Content": blob,
      "ContentLengthInBytes": number,
      "ContentType": "string",
      "CreatedBy": "string",
      "CreatedTime": "string",
      "FileName": "string",
      "RfcId": "string"
   }
}
```

## Response Elements
<a name="API_GetRfcAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RfcAttachment](#API_GetRfcAttachment_ResponseSyntax) **   <a name="amscm-GetRfcAttachment-response-RfcAttachment"></a>
The RFC attachment in an RFC attachment GET response.
Type: [RfcAttachment](API_RfcAttachment.md) object

## Errors
<a name="API_GetRfcAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource could not be located. Actual status code: 404
HTTP Status Code: 400

## See Also
<a name="API_GetRfcAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/GetRfcAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/GetRfcAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/GetRfcAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/GetRfcAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/GetRfcAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/GetRfcAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/GetRfcAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/GetRfcAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/GetRfcAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/GetRfcAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

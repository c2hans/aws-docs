---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveMessage.html
---

# GetArchiveMessage
<a name="API_GetArchiveMessage"></a>

Returns a pre-signed URL that provides temporary download access to the specific email message stored in the archive.

## Request Syntax
<a name="API_GetArchiveMessage_RequestSyntax"></a>

```
{
   "ArchivedMessageId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetArchiveMessage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArchivedMessageId](#API_GetArchiveMessage_RequestSyntax) **   <a name="sesmailmanager-GetArchiveMessage-request-ArchivedMessageId"></a>
The unique identifier of the archived email message.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetArchiveMessage_ResponseSyntax"></a>

```
{
   "Envelope": {
      "From": "string",
      "Helo": "string",
      "To": [ "string" ]
   },
   "MessageDownloadLink": "string",
   "Metadata": {
      "ConfigurationSet": "string",
      "IngressPointId": "string",
      "RuleSetId": "string",
      "SenderHostname": "string",
      "SenderIpAddress": "string",
      "SendingMethod": "string",
      "SendingPool": "string",
      "SourceArn": "string",
      "SourceIdentity": "string",
      "Timestamp": number,
      "TlsCipherSuite": "string",
      "TlsProtocol": "string",
      "TrafficPolicyId": "string"
   }
}
```

## Response Elements
<a name="API_GetArchiveMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Envelope](#API_GetArchiveMessage_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveMessage-response-Envelope"></a>
The SMTP envelope information of the email.
Type: [Envelope](API_Envelope.md) object

 ** [MessageDownloadLink](#API_GetArchiveMessage_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveMessage-response-MessageDownloadLink"></a>
A pre-signed URL to temporarily download the full message content.
Type: String

 ** [Metadata](#API_GetArchiveMessage_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveMessage-response-Metadata"></a>
The metadata about the email.
Type: [Metadata](API_Metadata.md) object

## Errors
<a name="API_GetArchiveMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetArchiveMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetArchiveMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetArchiveMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetArchiveMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetArchiveMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetArchiveMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetArchiveMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetArchiveMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetArchiveMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetArchiveMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetArchiveMessage)

---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveMessageContent.html
---

# GetArchiveMessageContent
<a name="API_GetArchiveMessageContent"></a>

Returns the textual content of a specific email message stored in the archive. Attachments are not included.

## Request Syntax
<a name="API_GetArchiveMessageContent_RequestSyntax"></a>

```
{
   "ArchivedMessageId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetArchiveMessageContent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArchivedMessageId](#API_GetArchiveMessageContent_RequestSyntax) **   <a name="sesmailmanager-GetArchiveMessageContent-request-ArchivedMessageId"></a>
The unique identifier of the archived email message.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetArchiveMessageContent_ResponseSyntax"></a>

```
{
   "Body": {
      "Html": "string",
      "MessageMalformed": boolean,
      "Text": "string"
   }
}
```

## Response Elements
<a name="API_GetArchiveMessageContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Body](#API_GetArchiveMessageContent_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveMessageContent-response-Body"></a>
The textual body content of the email message.
Type: [MessageBody](API_MessageBody.md) object

## Errors
<a name="API_GetArchiveMessageContent_Errors"></a>

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
<a name="API_GetArchiveMessageContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetArchiveMessageContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetArchiveMessageContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetArchiveMessageContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetArchiveMessageContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetArchiveMessageContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetArchiveMessageContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetArchiveMessageContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetArchiveMessageContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetArchiveMessageContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetArchiveMessageContent)

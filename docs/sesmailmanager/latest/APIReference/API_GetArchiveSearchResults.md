---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveSearchResults.html
---

# GetArchiveSearchResults
<a name="API_GetArchiveSearchResults"></a>

Returns the results of a completed email archive search job.

## Request Syntax
<a name="API_GetArchiveSearchResults_RequestSyntax"></a>

```
{
   "SearchId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetArchiveSearchResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SearchId](#API_GetArchiveSearchResults_RequestSyntax) **   <a name="sesmailmanager-GetArchiveSearchResults-request-SearchId"></a>
The identifier of the completed search job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_GetArchiveSearchResults_ResponseSyntax"></a>

```
{
   "Rows": [
      {
         "ArchivedMessageId": "string",
         "Cc": "string",
         "Date": "string",
         "Envelope": {
            "From": "string",
            "Helo": "string",
            "To": [ "string" ]
         },
         "From": "string",
         "HasAttachments": boolean,
         "IngressPointId": "string",
         "InReplyTo": "string",
         "MessageId": "string",
         "ReceivedHeaders": [ "string" ],
         "ReceivedTimestamp": number,
         "SenderHostname": "string",
         "SenderIpAddress": "string",
         "SourceArn": "string",
         "Subject": "string",
         "To": "string",
         "XMailer": "string",
         "XOriginalMailer": "string",
         "XPriority": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetArchiveSearchResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Rows](#API_GetArchiveSearchResults_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveSearchResults-response-Rows"></a>
The list of email result objects matching the search criteria.
Type: Array of [Row](API_Row.md) objects

## Errors
<a name="API_GetArchiveSearchResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetArchiveSearchResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetArchiveSearchResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetArchiveSearchResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetArchiveSearchResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetArchiveSearchResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetArchiveSearchResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetArchiveSearchResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetArchiveSearchResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetArchiveSearchResults)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetArchiveSearchResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetArchiveSearchResults)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

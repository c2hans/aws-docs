---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_AddCommunicationToCase.html
---

# AddCommunicationToCase
<a name="API_AddCommunicationToCase"></a>

Adds additional customer communication to an Support case. Use the `caseId` parameter to identify the case to which to add communication. You can list a set of email addresses to copy on the communication by using the `ccEmailAddresses` parameter. The `communicationBody` value contains the text of the communication.

**Note**
You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the AWS Support API.
If you call the AWS Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_AddCommunicationToCase_RequestSyntax"></a>

```
{
   "attachmentSetId": "{{string}}",
   "caseId": "{{string}}",
   "ccEmailAddresses": [ "{{string}}" ],
   "communicationBody": "{{string}}"
}
```

## Request Parameters
<a name="API_AddCommunicationToCase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attachmentSetId](#API_AddCommunicationToCase_RequestSyntax) **   <a name="AWSSupport-AddCommunicationToCase-request-attachmentSetId"></a>
The ID of a set of one or more attachments for the communication to add to the case. Create the set by calling [AddAttachmentsToSet](API_AddAttachmentsToSet.md)
Type: String

 ** [caseId](#API_AddCommunicationToCase_RequestSyntax) **   <a name="AWSSupport-AddCommunicationToCase-request-caseId"></a>
The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-exen-2025-c4c1d2bf33c5cf47*
Type: String

 ** [ccEmailAddresses](#API_AddCommunicationToCase_RequestSyntax) **   <a name="AWSSupport-AddCommunicationToCase-request-ccEmailAddresses"></a>
The email addresses in the CC line of an email to be added to the support case.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [communicationBody](#API_AddCommunicationToCase_RequestSyntax) **   <a name="AWSSupport-AddCommunicationToCase-request-communicationBody"></a>
The body of an email communication to add to the support case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.

## Response Syntax
<a name="API_AddCommunicationToCase_ResponseSyntax"></a>

```
{
   "result": boolean
}
```

## Response Elements
<a name="API_AddCommunicationToCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [result](#API_AddCommunicationToCase_ResponseSyntax) **   <a name="AWSSupport-AddCommunicationToCase-response-result"></a>
True if [AddCommunicationToCase](#API_AddCommunicationToCase) succeeds. Otherwise, returns an error.
Type: Boolean

## Errors
<a name="API_AddCommunicationToCase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AttachmentSetExpired **
The expiration time of the attachment set has passed. The set expires 1 hour after it is created.
 ** message **
The expiration time of the attachment set has passed. The set expires one hour after it is created.
HTTP Status Code: 400

 ** AttachmentSetIdNotFound **
An attachment set with the specified ID could not be found.
 ** message **
An attachment set with the specified ID could not be found.
HTTP Status Code: 400

 ** CaseIdNotFound **
The requested `caseId` couldn't be located.
 ** message **
The requested `CaseId` could not be located.
HTTP Status Code: 400

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

## See Also
<a name="API_AddCommunicationToCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/AddCommunicationToCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/AddCommunicationToCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/AddCommunicationToCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/AddCommunicationToCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/AddCommunicationToCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/AddCommunicationToCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/AddCommunicationToCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/AddCommunicationToCase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/AddCommunicationToCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/AddCommunicationToCase)

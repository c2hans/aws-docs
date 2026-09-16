---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CreateCase.html
---

# CreateCase
<a name="API_CreateCase"></a>

Creates a case in the Support Center. This operation is similar to how you create a case in the Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.

The Support API doesn't support requesting service limit increases. You can submit a service limit increase in the following ways:
+ Submit a request from the Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.
+ Use the Service Quotas [RequestServiceQuotaIncrease](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html) operation.

**Important**
 AWS Support automatically redacts sensitive information from support cases to protect your data. The following information is replaced with `[REDACTED_BY_AWS]` and is not stored:
 AWS secret keys - The complete key is replaced. Example: `[REDACTED_BY_AWS]`
Private keys - The complete key is replaced. Example: `[REDACTED_BY_AWS]`
Credit card numbers - The number is redacted, but the last 4 digits remain. Example: `[REDACTED_BY_AWS]-7016`
This sensitive information is never required by AWS Support.

A successful `CreateCase` request returns a Support case number. You can use the [DescribeCases](API_DescribeCases.md) operation and specify the case number to get existing Support cases. After you create a case, use the [AddCommunicationToCase](API_AddCommunicationToCase.md) operation to add additional communication or attachments to an existing case.

The `caseId` is separate from the `displayId` that appears in the [AWS Support Center](https://console.aws.amazon.com/support). Use the [DescribeCases](API_DescribeCases.md) operation to get the `displayId`.

**Note**
You must have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan to use the AWS Support API. If you're in an AWS Region that doesn't offer one of these AWS Support plans, or if you haven't transitioned to one of these plans, you can use the AWS Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.
If you call the AWS Support API from an account that doesn't have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_CreateCase_RequestSyntax"></a>

```
{
   "attachmentSetId": "{{string}}",
   "categoryCode": "{{string}}",
   "ccEmailAddresses": [ "{{string}}" ],
   "communicationBody": "{{string}}",
   "dryRun": {{boolean}},
   "issueType": "{{string}}",
   "language": "{{string}}",
   "serviceCode": "{{string}}",
   "severityCode": "{{string}}",
   "subject": "{{string}}",
   "uploadIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreateCase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attachmentSetId](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-attachmentSetId"></a>
The ID of a set of one or more attachments for the case. Create the set by using the [AddAttachmentsToSet](API_AddAttachmentsToSet.md) operation. Each attachment in the set must be 5 MB or smaller. To attach files larger than 5 MB, use `uploadIds`.
Type: String

 ** [categoryCode](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-categoryCode"></a>
The category of problem for the support case. You also use the [DescribeServices](API_DescribeServices.md) operation to get the category code for a service. Each AWS service defines its own set of category codes.
Type: String

 ** [ccEmailAddresses](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-ccEmailAddresses"></a>
A list of email addresses that AWS Support copies on case correspondence. AWS Support identifies the account that creates the case when you specify your AWS credentials in an HTTP POST method or use the [AWS SDKs](http://aws.amazon.com/tools/).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [communicationBody](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-communicationBody"></a>
The communication body text that describes the issue. This text appears in the **Description** field on the AWS Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.

 ** [dryRun](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-dryRun"></a>
Specifies whether to validate the request without actually creating the case. When set to `true`, the request is validated but no case is created, and the operation returns a `DryRunOperationException`. When omitted or set to `false`, the request runs normally.
Type: Boolean

 ** [issueType](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-issueType"></a>
The type of issue for the case. You can specify `customer-service` or `technical`. If you don't specify a value, the default is `technical`.
Type: String

 ** [language](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-language"></a>
The language in which AWS Support handles the case. AWS Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.
Type: String

 ** [serviceCode](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-serviceCode"></a>
The code for the AWS service. You can use the [DescribeServices](API_DescribeServices.md) operation to get the possible `serviceCode` values.
Type: String

 ** [severityCode](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-severityCode"></a>
A value that indicates the urgency of the case. This value determines the response time according to your service level agreement with AWS Support. You can use the [DescribeSeverityLevels](API_DescribeSeverityLevels.md) operation to get the possible values for `severityCode`.
For more information, see [SeverityLevel](API_SeverityLevel.md) and [Choosing a Severity](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity) in the * AWS Support User Guide*.
The availability of severity levels depends on the support plan for the AWS account.
Type: String

 ** [subject](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-subject"></a>
The title of the support case. The title appears in the **Subject** field on the AWS Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.
Type: String

 ** [uploadIds](#API_CreateCase_RequestSyntax) **   <a name="AWSSupport-CreateCase-request-uploadIds"></a>
A list of upload IDs that identify attachments to add to the case. Each `uploadId` is returned by the [GetAttachmentUploadLinks](API_GetAttachmentUploadLinks.md) operation. The upload must reach the `attachment-ready` state by calling [CompleteAttachmentUpload](API_CompleteAttachmentUpload.md) before it can be passed here. Use `uploadIds` to attach files of any supported size, including files larger than 5 MB.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Response Syntax
<a name="API_CreateCase_ResponseSyntax"></a>

```
{
   "caseId": "string"
}
```

## Response Elements
<a name="API_CreateCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [caseId](#API_CreateCase_ResponseSyntax) **   <a name="AWSSupport-CreateCase-response-caseId"></a>
The support case ID requested or returned in the call. The case ID is an alphanumeric string in the following format: case-*12345678910-exen-2025-c4c1d2bf33c5cf47*
Type: String

## Errors
<a name="API_CreateCase_Errors"></a>

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

 ** CaseCreationLimitExceeded **
The case creation limit for the account has been exceeded.
 ** message **
An error message that indicates that you have exceeded the number of cases you can have open.
HTTP Status Code: 400

 ** DryRunOperationException **
The request was valid, but the operation wasn't performed because `dryRun` was set to `true`.
HTTP Status Code: 400

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

## See Also
<a name="API_CreateCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/CreateCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/CreateCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/CreateCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/CreateCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/CreateCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/CreateCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/CreateCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/CreateCase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/CreateCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/CreateCase)

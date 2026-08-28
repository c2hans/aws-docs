---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateFindingsFeedback.html
---

# UpdateFindingsFeedback
<a name="API_UpdateFindingsFeedback"></a>

Marks the specified GuardDuty findings as useful or not useful.

## Request Syntax
<a name="API_UpdateFindingsFeedback_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/findings/feedback HTTP/1.1
Content-type: application/json

{
   "comments": "{{string}}",
   "feedback": "{{string}}",
   "findingIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateFindingsFeedback_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_UpdateFindingsFeedback_RequestSyntax) **   <a name="guardduty-UpdateFindingsFeedback-request-uri-DetectorId"></a>
The ID of the detector that is associated with the findings for which you want to update the feedback.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_UpdateFindingsFeedback_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [comments](#API_UpdateFindingsFeedback_RequestSyntax) **   <a name="guardduty-UpdateFindingsFeedback-request-comments"></a>
Additional feedback about the GuardDuty findings.
Type: String
Required: No

 ** [feedback](#API_UpdateFindingsFeedback_RequestSyntax) **   <a name="guardduty-UpdateFindingsFeedback-request-feedback"></a>
The feedback for the finding.
Type: String
Valid Values: `USEFUL | NOT_USEFUL`
Required: Yes

 ** [findingIds](#API_UpdateFindingsFeedback_RequestSyntax) **   <a name="guardduty-UpdateFindingsFeedback-request-findingIds"></a>
The IDs of the findings that you want to mark as useful or not useful.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_UpdateFindingsFeedback_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateFindingsFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateFindingsFeedback_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_UpdateFindingsFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/UpdateFindingsFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/UpdateFindingsFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UpdateFindingsFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/UpdateFindingsFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UpdateFindingsFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/UpdateFindingsFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/UpdateFindingsFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/UpdateFindingsFeedback)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/UpdateFindingsFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UpdateFindingsFeedback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

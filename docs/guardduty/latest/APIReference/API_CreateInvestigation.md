---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateInvestigation.html
---

# CreateInvestigation
<a name="API_CreateInvestigation"></a>

This API is currently available as a preview. During the preview, you can initiate up to 10 investigations per account per day, with a total limit of 100 investigations per account. This feature is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and Asia Pacific (Tokyo).

Initiates a GuardDuty investigation that automatically analyzes security findings, correlates related activity, performs account-level analysis, and produces a structured investigation summary with recommended next steps.

Only the administrator account can create an investigation. Member accounts don't have permission to create investigations from their accounts.

To use this operation, the `AI_ANALYST` feature must be enabled on your detector.

This feature uses Amazon Bedrock models that leverage Cross-Region Inference (CRIS), which automatically selects the optimal AWS Region within your geography to process the investigation analysis and generate the investigation report. This maximizes available compute resources, model availability, and delivers the best customer experience. Your data remains stored only in the Region where the investigation request originates, however, investigation data and summary results may be processed outside that Region. All data is transmitted encrypted across Amazon's secure network. For more information, see [GuardDuty Investigation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-investigation.html).

## Request Syntax
<a name="API_CreateInvestigation_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/investigation HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "triggerPrompt": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateInvestigation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_CreateInvestigation_RequestSyntax) **   <a name="guardduty-CreateInvestigation-request-uri-DetectorId"></a>
The unique ID of the GuardDuty detector for the account in which the investigation is created.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_CreateInvestigation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateInvestigation_RequestSyntax) **   <a name="guardduty-CreateInvestigation-request-clientToken"></a>
The idempotency token for the create request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [triggerPrompt](#API_CreateInvestigation_RequestSyntax) **   <a name="guardduty-CreateInvestigation-request-triggerPrompt"></a>
A natural-language description of what to investigate. For example:
+  `"Investigate finding 1ab2c3d4e5f6a7b8c9d0e1f2a3b4c5d6 in account 123456789012"`
+  `"Analyze findings in account with id 123456789012"`
+  `"Analyze findings in my organization"`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_CreateInvestigation_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "investigationId": "string"
}
```

## Response Elements
<a name="API_CreateInvestigation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [investigationId](#API_CreateInvestigation_ResponseSyntax) **   <a name="guardduty-CreateInvestigation-response-investigationId"></a>
The unique identifier of the newly created investigation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-fA-F0-9\-]+`

## Errors
<a name="API_CreateInvestigation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An access denied exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 403

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
<a name="API_CreateInvestigation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/CreateInvestigation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/CreateInvestigation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CreateInvestigation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/CreateInvestigation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CreateInvestigation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/CreateInvestigation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/CreateInvestigation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/CreateInvestigation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/CreateInvestigation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CreateInvestigation)

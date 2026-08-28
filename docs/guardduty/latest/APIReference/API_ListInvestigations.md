---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListInvestigations.html
---

# ListInvestigations
<a name="API_ListInvestigations"></a>

This API is currently available as a preview. This feature is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and Asia Pacific (Tokyo).

Returns a list of investigations associated with the specified GuardDuty detector.

An administrator account sees all investigations across the organization. Member accounts see only the investigations that belong to them.

## Request Syntax
<a name="API_ListInvestigations_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/investigation/list HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortCriteria": {
      "attributeName": "{{string}}",
      "orderBy": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListInvestigations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_ListInvestigations_RequestSyntax) **   <a name="guardduty-ListInvestigations-request-uri-DetectorId"></a>
The unique ID of the GuardDuty detector whose investigations you want to list.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_ListInvestigations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListInvestigations_RequestSyntax) **   <a name="guardduty-ListInvestigations-request-maxResults"></a>
You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListInvestigations_RequestSyntax) **   <a name="guardduty-ListInvestigations-request-nextToken"></a>
You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9+/=_\-]+`
Required: No

 ** [sortCriteria](#API_ListInvestigations_RequestSyntax) **   <a name="guardduty-ListInvestigations-request-sortCriteria"></a>
Represents the criteria used for sorting investigations.
Type: [InvestigationSortCriteria](API_InvestigationSortCriteria.md) object
Required: No

## Response Syntax
<a name="API_ListInvestigations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "investigations": [
      {
         "accountId": "string",
         "confidence": "string",
         "endTime": number,
         "investigationId": "string",
         "riskLevel": "string",
         "startTime": number,
         "status": "string",
         "title": "string",
         "triggerPrompt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListInvestigations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [investigations](#API_ListInvestigations_ResponseSyntax) **   <a name="guardduty-ListInvestigations-response-investigations"></a>
A list of investigation summaries associated with the specified detector.
Type: Array of [InvestigationSummary](API_InvestigationSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [nextToken](#API_ListInvestigations_ResponseSyntax) **   <a name="guardduty-ListInvestigations-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9+/=_\-]+`

## Errors
<a name="API_ListInvestigations_Errors"></a>

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
<a name="API_ListInvestigations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListInvestigations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListInvestigations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListInvestigations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListInvestigations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListInvestigations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListInvestigations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListInvestigations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListInvestigations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListInvestigations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListInvestigations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

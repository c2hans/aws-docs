---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCustomDetectionRuleAssociations.html
---

# ListCustomDetectionRuleAssociations
<a name="API_ListCustomDetectionRuleAssociations"></a>

Returns all custom detection rule associations for your account. You can filter by rule ID and mode.

## Request Syntax
<a name="API_ListCustomDetectionRuleAssociations_RequestSyntax"></a>

```
GET /custom-detection-rule/association?maxResults={{MaxResults}}&mode={{Mode}}&nextToken={{NextToken}}&ruleId={{RuleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCustomDetectionRuleAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListCustomDetectionRuleAssociations_RequestSyntax) **   <a name="guardduty-ListCustomDetectionRuleAssociations-request-uri-MaxResults"></a>
The maximum number of results to return in a single page. Minimum value of 1, maximum value of 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [Mode](#API_ListCustomDetectionRuleAssociations_RequestSyntax) **   <a name="guardduty-ListCustomDetectionRuleAssociations-request-uri-Mode"></a>
The rule execution mode to filter associations by.
Valid Values: `LIVE | DRY_RUN`

 ** [NextToken](#API_ListCustomDetectionRuleAssociations_RequestSyntax) **   <a name="guardduty-ListCustomDetectionRuleAssociations-request-uri-NextToken"></a>
A pagination token from a previous response. Use this token to retrieve the next page of results.

 ** [RuleId](#API_ListCustomDetectionRuleAssociations_RequestSyntax) **   <a name="guardduty-ListCustomDetectionRuleAssociations-request-uri-RuleId"></a>
The unique identifier for the custom detection rule to filter associations by.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`

## Request Body
<a name="API_ListCustomDetectionRuleAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCustomDetectionRuleAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "ruleAssociations": [
      {
         "arn": "string",
         "associationId": "string",
         "createdAt": number,
         "expiresAt": number,
         "mode": "string",
         "ruleId": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListCustomDetectionRuleAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListCustomDetectionRuleAssociations_ResponseSyntax) **   <a name="guardduty-ListCustomDetectionRuleAssociations-response-nextToken"></a>
A pagination token to retrieve the next page of results. If this field is empty, there are no additional results.
Type: String

 ** [ruleAssociations](#API_ListCustomDetectionRuleAssociations_ResponseSyntax) **   <a name="guardduty-ListCustomDetectionRuleAssociations-response-ruleAssociations"></a>
A list of custom detection rule association summaries.
Type: Array of [AssociationSummary](API_AssociationSummary.md) objects

## Errors
<a name="API_ListCustomDetectionRuleAssociations_Errors"></a>

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
<a name="API_ListCustomDetectionRuleAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListCustomDetectionRuleAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListCustomDetectionRuleAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListCustomDetectionRuleAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListCustomDetectionRuleAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListCustomDetectionRuleAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListCustomDetectionRuleAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListCustomDetectionRuleAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListCustomDetectionRuleAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListCustomDetectionRuleAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListCustomDetectionRuleAssociations)

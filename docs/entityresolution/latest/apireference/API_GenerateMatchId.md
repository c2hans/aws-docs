---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GenerateMatchId.html
---

# GenerateMatchId
<a name="API_GenerateMatchId"></a>

Generates or retrieves Match IDs for records using a rule-based matching workflow. When you call this operation, it processes your records against the workflow's matching rules to identify potential matches. For existing records, it retrieves their Match IDs and associated rules. For records without matches, it generates new Match IDs. The operation saves results to Amazon S3.

The processing type (`processingType`) you choose affects both the accuracy and response time of the operation. Additional charges apply for each API call, whether made through the AWS Entity Resolution console or directly via the API. The rule-based matching workflow must exist and be active before calling this operation.

## Request Syntax
<a name="API_GenerateMatchId_RequestSyntax"></a>

```
POST /matchingworkflows/{{workflowName}}/generateMatches HTTP/1.1
Content-type: application/json

{
   "processingType": "{{string}}",
   "records": [
      {
         "inputSourceARN": "{{string}}",
         "recordAttributeMap": {
            "{{string}}" : "{{string}}"
         },
         "uniqueId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_GenerateMatchId_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowName](#API_GenerateMatchId_RequestSyntax) **   <a name="API-GenerateMatchId-request-uri-workflowName"></a>
 The name of the rule-based matching workflow.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_GenerateMatchId_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [processingType](#API_GenerateMatchId_RequestSyntax) **   <a name="API-GenerateMatchId-request-processingType"></a>
The processing mode that determines how Match IDs are generated and results are saved. Each mode provides different levels of accuracy, response time, and completeness of results.
If not specified, defaults to `CONSISTENT`.
 `CONSISTENT`: Performs immediate lookup and matching against all existing records, with results saved synchronously. Provides highest accuracy but slower response time.
 `EVENTUAL` (shown as *Background* in the console): Performs initial match ID lookup or generation immediately, with record updates processed asynchronously in the background. Offers faster initial response time, with complete matching results available later in S3.
 `EVENTUAL_NO_LOOKUP` (shown as *Quick ID generation* in the console): Generates new match IDs without checking existing matches, with updates processed asynchronously. Provides fastest response time but should only be used for records known to be unique.
Advanced matching workflows don't support the `processingType` field.
Type: String
Valid Values: `CONSISTENT | EVENTUAL | EVENTUAL_NO_LOOKUP`
Required: No

 ** [records](#API_GenerateMatchId_RequestSyntax) **   <a name="API-GenerateMatchId-request-records"></a>
 The records to match.
Type: Array of [Record](API_Record.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## Response Syntax
<a name="API_GenerateMatchId_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedRecords": [
      {
         "errorMessage": "string",
         "inputSourceARN": "string",
         "uniqueId": "string"
      }
   ],
   "matchGroups": [
      {
         "matchId": "string",
         "matchRule": "string",
         "records": [
            {
               "inputSourceARN": "string",
               "recordId": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GenerateMatchId_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedRecords](#API_GenerateMatchId_ResponseSyntax) **   <a name="API-GenerateMatchId-response-failedRecords"></a>
 The records that didn't receive a generated Match ID.
Type: Array of [FailedRecord](API_FailedRecord.md) objects

 ** [matchGroups](#API_GenerateMatchId_ResponseSyntax) **   <a name="API-GenerateMatchId-response-matchGroups"></a>
 The match groups from the generated match ID.
Type: Array of [MatchGroup](API_MatchGroup.md) objects

## Errors
<a name="API_GenerateMatchId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_GenerateMatchId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/GenerateMatchId)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/GenerateMatchId)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/GenerateMatchId)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/GenerateMatchId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GenerateMatchId)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/GenerateMatchId)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/GenerateMatchId)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/GenerateMatchId)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/GenerateMatchId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/GenerateMatchId)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

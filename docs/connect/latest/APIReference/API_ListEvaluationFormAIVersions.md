---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListEvaluationFormAIVersions.html
---

# ListEvaluationFormAIVersions
<a name="API_ListEvaluationFormAIVersions"></a>

Lists the available AI versions for evaluation forms in the specified Connect Customer instance.

## Request Syntax
<a name="API_ListEvaluationFormAIVersions_RequestSyntax"></a>

```
GET /instances/{{InstanceId}}/evaluation-form-ai-versions?contactInteractionType={{ContactInteractionType}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEvaluationFormAIVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactInteractionType](#API_ListEvaluationFormAIVersions_RequestSyntax) **   <a name="connect-ListEvaluationFormAIVersions-request-uri-ContactInteractionType"></a>
The contact interaction type for the evaluation form.
Valid Values: `AGENT | AUTOMATED | CUSTOMER`
Required: Yes

 ** [InstanceId](#API_ListEvaluationFormAIVersions_RequestSyntax) **   <a name="connect-ListEvaluationFormAIVersions-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListEvaluationFormAIVersions_RequestSyntax) **   <a name="connect-ListEvaluationFormAIVersions-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListEvaluationFormAIVersions_RequestSyntax) **   <a name="connect-ListEvaluationFormAIVersions-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListEvaluationFormAIVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEvaluationFormAIVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AIVersionSummaries": [
      {
         "AIVersionLifecycle": {
            "EndOfLifeTime": number,
            "StartOfLifeTime": number,
            "Status": "string"
         },
         "AIVersionName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEvaluationFormAIVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AIVersionSummaries](#API_ListEvaluationFormAIVersions_ResponseSyntax) **   <a name="connect-ListEvaluationFormAIVersions-response-AIVersionSummaries"></a>
The list of AI version summaries.
Type: Array of [EvaluationFormAIVersionSummary](API_EvaluationFormAIVersionSummary.md) objects

 ** [NextToken](#API_ListEvaluationFormAIVersions_ResponseSyntax) **   <a name="connect-ListEvaluationFormAIVersions-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListEvaluationFormAIVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_ListEvaluationFormAIVersions_Examples"></a>

### Example
<a name="API_ListEvaluationFormAIVersions_Example_1"></a>

The following example lists the available AI versions for agent evaluation forms.

#### Sample Request
<a name="API_ListEvaluationFormAIVersions_Example_1_Request"></a>

```
{
   "InstanceId": "12345678-1234-1234-1234-123456789012",
   "ContactInteractionType": "AGENT"
}
```

#### Sample Response
<a name="API_ListEvaluationFormAIVersions_Example_1_Response"></a>

```
{
   "AIVersionSummaries": [
      {
         "AIVersionName": "AGENT_EVALUATION_2025-11-12",
         "AIVersionLifecycle": {
            "Status": "Active",
            "StartOfLifeTime": "2025-11-12T00:00:00.000Z"
         }
      },
      {
         "AIVersionName": "AGENT_EVALUATION_2025-09-01",
         "AIVersionLifecycle": {
            "Status": "Deprecated",
            "StartOfLifeTime": "2025-09-01T00:00:00.000Z",
            "EndOfLifeTime": "2025-12-01T00:00:00.000Z"
         }
      }
   ]
}
```

## See Also
<a name="API_ListEvaluationFormAIVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListEvaluationFormAIVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListEvaluationFormAIVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListEvaluationFormAIVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListEvaluationFormAIVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListEvaluationFormAIVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListEvaluationFormAIVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListEvaluationFormAIVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListEvaluationFormAIVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListEvaluationFormAIVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListEvaluationFormAIVersions)

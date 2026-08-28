---
source_url: https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_ListHumanLoops.html
---

# ListHumanLoops
<a name="API_ListHumanLoops"></a>

Returns information about human loops, given the specified parameters. If a human loop was deleted, it will not be included.

## Request Syntax
<a name="API_ListHumanLoops_RequestSyntax"></a>

```
GET /human-loops?CreationTimeAfter={{CreationTimeAfter}}&CreationTimeBefore={{CreationTimeBefore}}&FlowDefinitionArn={{FlowDefinitionArn}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&SortOrder={{SortOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHumanLoops_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CreationTimeAfter](#API_ListHumanLoops_RequestSyntax) **   <a name="augmentedai-ListHumanLoops-request-uri-CreationTimeAfter"></a>
(Optional) The timestamp of the date when you want the human loops to begin in ISO 8601 format. For example, `2020-02-24`.

 ** [CreationTimeBefore](#API_ListHumanLoops_RequestSyntax) **   <a name="augmentedai-ListHumanLoops-request-uri-CreationTimeBefore"></a>
(Optional) The timestamp of the date before which you want the human loops to begin in ISO 8601 format. For example, `2020-02-24`.

 ** [FlowDefinitionArn](#API_ListHumanLoops_RequestSyntax) **   <a name="augmentedai-ListHumanLoops-request-uri-FlowDefinitionArn"></a>
The Amazon Resource Name (ARN) of a flow definition.
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:flow-definition/.*`
Required: Yes

 ** [MaxResults](#API_ListHumanLoops_RequestSyntax) **   <a name="augmentedai-ListHumanLoops-request-uri-MaxResults"></a>
The total number of items to return. If the total number of available items is more than the value specified in `MaxResults`, then a `NextToken` is returned in the output. You can use this token to display the next page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListHumanLoops_RequestSyntax) **   <a name="augmentedai-ListHumanLoops-request-uri-NextToken"></a>
A token to display the next page of results.
Length Constraints: Maximum length of 8192.
Pattern: `.*`

 ** [SortOrder](#API_ListHumanLoops_RequestSyntax) **   <a name="augmentedai-ListHumanLoops-request-uri-SortOrder"></a>
Optional. The order for displaying results. Valid values: `Ascending` and `Descending`.
Valid Values: `Ascending | Descending`

## Request Body
<a name="API_ListHumanLoops_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHumanLoops_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HumanLoopSummaries": [
      {
         "CreationTime": number,
         "FailureReason": "string",
         "FlowDefinitionArn": "string",
         "HumanLoopName": "string",
         "HumanLoopStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListHumanLoops_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HumanLoopSummaries](#API_ListHumanLoops_ResponseSyntax) **   <a name="augmentedai-ListHumanLoops-response-HumanLoopSummaries"></a>
An array of objects that contain information about the human loops.
Type: Array of [HumanLoopSummary](API_HumanLoopSummary.md) objects

 ** [NextToken](#API_ListHumanLoops_ResponseSyntax) **   <a name="augmentedai-ListHumanLoops-response-NextToken"></a>
A token to display the next page of results.
Type: String
Length Constraints: Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListHumanLoops_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## See Also
<a name="API_ListHumanLoops_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-a2i-runtime-2019-11-07/ListHumanLoops)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-a2i-runtime-2019-11-07/ListHumanLoops)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-a2i-runtime-2019-11-07/ListHumanLoops)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-a2i-runtime-2019-11-07/ListHumanLoops)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-a2i-runtime-2019-11-07/ListHumanLoops)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-a2i-runtime-2019-11-07/ListHumanLoops)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-a2i-runtime-2019-11-07/ListHumanLoops)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-a2i-runtime-2019-11-07/ListHumanLoops)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-a2i-runtime-2019-11-07/ListHumanLoops)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-a2i-runtime-2019-11-07/ListHumanLoops)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Augmented AI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query augmented-ai` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

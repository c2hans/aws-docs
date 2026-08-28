---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ListAssistants.html
---

# ListAssistants
<a name="API_amazon-q-connect_ListAssistants"></a>

Lists information about assistants.

## Request Syntax
<a name="API_amazon-q-connect_ListAssistants_RequestSyntax"></a>

```
GET /assistants?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_ListAssistants_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_amazon-q-connect_ListAssistants_RequestSyntax) **   <a name="connect-amazon-q-connect_ListAssistants-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_amazon-q-connect_ListAssistants_RequestSyntax) **   <a name="connect-amazon-q-connect_ListAssistants-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_amazon-q-connect_ListAssistants_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_ListAssistants_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assistantSummaries": [
      {
         "aiAgentConfiguration": {
            "string" : {
               "aiAgentId": "string"
            }
         },
         "assistantArn": "string",
         "assistantId": "string",
         "capabilityConfiguration": {
            "type": "string"
         },
         "description": "string",
         "integrationConfiguration": {
            "topicIntegrationArn": "string"
         },
         "name": "string",
         "orchestratorConfigurationList": [
            {
               "aiAgentId": "string",
               "orchestratorUseCase": "string"
            }
         ],
         "serverSideEncryptionConfiguration": {
            "kmsKeyId": "string"
         },
         "status": "string",
         "tags": {
            "string" : "string"
         },
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_amazon-q-connect_ListAssistants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assistantSummaries](#API_amazon-q-connect_ListAssistants_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListAssistants-response-assistantSummaries"></a>
Information about the assistants.
Type: Array of [AssistantSummary](API_amazon-q-connect_AssistantSummary.md) objects

 ** [nextToken](#API_amazon-q-connect_ListAssistants_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListAssistants-response-nextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_amazon-q-connect_ListAssistants_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_ListAssistants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/ListAssistants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/ListAssistants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ListAssistants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/ListAssistants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ListAssistants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/ListAssistants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/ListAssistants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/ListAssistants)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/ListAssistants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ListAssistants)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

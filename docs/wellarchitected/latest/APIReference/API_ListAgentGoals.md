---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentGoals.html
---

# ListAgentGoals
<a name="API_ListAgentGoals"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Lists optimization goals associated with a specified profile. Goals define specific targets and objectives for the optimization process.

## Request Syntax
<a name="API_ListAgentGoals_RequestSyntax"></a>

```
GET /api/v1/agent-profiles/{{profileArn}}/goals?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAgentGoals_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAgentGoals_RequestSyntax) **   <a name="wellarchitected-ListAgentGoals-request-uri-maxResults"></a>
The maximum number of goals to return in a single response.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAgentGoals_RequestSyntax) **   <a name="wellarchitected-ListAgentGoals-request-uri-nextToken"></a>
A pagination token returned from a previous call to continue retrieving results.
Length Constraints: Minimum length of 1.
Pattern: `[A-Za-z0-9+\/=_-]+`

 ** [profileArn](#API_ListAgentGoals_RequestSyntax) **   <a name="wellarchitected-ListAgentGoals-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the optimization profile to list goals for.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_ListAgentGoals_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAgentGoals_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": "string",
         "createdBy": "string",
         "description": "string",
         "id": "string",
         "lastModifiedAt": "string",
         "lastModifiedBy": "string",
         "pillars": [ "string" ],
         "profileArn": "string",
         "title": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAgentGoals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAgentGoals_ResponseSyntax) **   <a name="wellarchitected-ListAgentGoals-response-items"></a>
A list of goal summaries associated with the profile.
Type: Array of [GoalSummary](API_GoalSummary.md) objects

 ** [nextToken](#API_ListAgentGoals_ResponseSyntax) **   <a name="wellarchitected-ListAgentGoals-response-nextToken"></a>
A pagination token to retrieve the next set of results, if available.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[A-Za-z0-9+\/=_-]+`

## Errors
<a name="API_ListAgentGoals_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListAgentGoals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListAgentGoals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListAgentGoals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListAgentGoals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListAgentGoals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListAgentGoals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListAgentGoals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListAgentGoals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListAgentGoals)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListAgentGoals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListAgentGoals)

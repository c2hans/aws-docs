---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentGoal.html
---

# GetAgentGoal
<a name="API_GetAgentGoal"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Retrieves detailed information about a specific optimization goal.

## Request Syntax
<a name="API_GetAgentGoal_RequestSyntax"></a>

```
GET /api/v1/agent-profiles/{{profileArn}}/goals/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgentGoal_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetAgentGoal_RequestSyntax) **   <a name="wellarchitected-GetAgentGoal-request-uri-id"></a>
The unique identifier of the goal to retrieve.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [profileArn](#API_GetAgentGoal_RequestSyntax) **   <a name="wellarchitected-GetAgentGoal-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the profile containing the goal.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_GetAgentGoal_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentGoal_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "goal": {
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
}
```

## Response Elements
<a name="API_GetAgentGoal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [goal](#API_GetAgentGoal_ResponseSyntax) **   <a name="wellarchitected-GetAgentGoal-response-goal"></a>
The retrieved goal summary.
Type: [GoalSummary](API_GoalSummary.md) object

## Errors
<a name="API_GetAgentGoal_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

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
<a name="API_GetAgentGoal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetAgentGoal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetAgentGoal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetAgentGoal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetAgentGoal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetAgentGoal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetAgentGoal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetAgentGoal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetAgentGoal)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetAgentGoal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetAgentGoal)

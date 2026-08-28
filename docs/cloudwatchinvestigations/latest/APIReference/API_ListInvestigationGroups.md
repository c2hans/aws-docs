---
source_url: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_ListInvestigationGroups.html
---

# ListInvestigationGroups
<a name="API_ListInvestigationGroups"></a>

Returns the ARN and name of each investigation group in the account.

## Request Syntax
<a name="API_ListInvestigationGroups_RequestSyntax"></a>

```
GET /investigationGroups?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInvestigationGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListInvestigationGroups_RequestSyntax) **   <a name="cloudwatchinvestigations-ListInvestigationGroups-request-uri-maxResults"></a>
The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListInvestigationGroups_RequestSyntax) **   <a name="cloudwatchinvestigations-ListInvestigationGroups-request-uri-nextToken"></a>
Include this value, if it was returned by the previous operation, to get the next set of service operations.
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Request Body
<a name="API_ListInvestigationGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInvestigationGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "investigationGroups": [
      {
         "arn": "string",
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListInvestigationGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [investigationGroups](#API_ListInvestigationGroups_ResponseSyntax) **   <a name="cloudwatchinvestigations-ListInvestigationGroups-response-investigationGroups"></a>
An array of structures, where each structure contains the information about one investigation group in the account.
Type: Array of [ListInvestigationGroupsModel](API_ListInvestigationGroupsModel.md) objects

 ** [nextToken](#API_ListInvestigationGroups_ResponseSyntax) **   <a name="cloudwatchinvestigations-ListInvestigationGroups-response-nextToken"></a>
Include this value in your next use of this operation to get the next set of service operations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListInvestigationGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation couldn't be completed because of a conflict in resource states.
HTTP Status Code: 409

 ** ForbiddenException **
Access id denied for this operation, or this operation is not valid for the specified resource.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. You can try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429

 ** ValidationException **
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400

## See Also
<a name="API_ListInvestigationGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/aiops-2018-05-10/ListInvestigationGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/aiops-2018-05-10/ListInvestigationGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/aiops-2018-05-10/ListInvestigationGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/aiops-2018-05-10/ListInvestigationGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/aiops-2018-05-10/ListInvestigationGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/aiops-2018-05-10/ListInvestigationGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/aiops-2018-05-10/ListInvestigationGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/aiops-2018-05-10/ListInvestigationGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/aiops-2018-05-10/ListInvestigationGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/aiops-2018-05-10/ListInvestigationGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch investigations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchinvestigations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

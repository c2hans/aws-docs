---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListTagSyncTasks.html
---

# ListTagSyncTasks
<a name="API_ListTagSyncTasks"></a>

Returns a list of tag-sync tasks.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:ListTagSyncTasks` with the group passed in the filters as the resource or \* if using no filters

## Request Syntax
<a name="API_ListTagSyncTasks_RequestSyntax"></a>

```
POST /list-tag-sync-tasks HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "GroupArn": "{{string}}",
         "GroupName": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListTagSyncTasks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTagSyncTasks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListTagSyncTasks_RequestSyntax) **   <a name="ARG-ListTagSyncTasks-request-Filters"></a>
The Amazon resource name (ARN) or name of the application group for which you want to return a list of tag-sync tasks.
Type: Array of [ListTagSyncTasksFilter](API_ListTagSyncTasksFilter.md) objects
Required: No

 ** [MaxResults](#API_ListTagSyncTasks_RequestSyntax) **   <a name="ARG-ListTagSyncTasks-request-MaxResults"></a>
The maximum number of results to be included in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListTagSyncTasks_RequestSyntax) **   <a name="ARG-ListTagSyncTasks-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value provided by a previous call's `NextToken` response to indicate where the output should continue from.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9+/]*={0,2}$`
Required: No

## Response Syntax
<a name="API_ListTagSyncTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TagSyncTasks": [
      {
         "CreatedAt": number,
         "ErrorMessage": "string",
         "GroupArn": "string",
         "GroupName": "string",
         "ResourceQuery": {
            "Query": "string",
            "Type": "string"
         },
         "RoleArn": "string",
         "Status": "string",
         "TagKey": "string",
         "TagValue": "string",
         "TaskArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagSyncTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTagSyncTasks_ResponseSyntax) **   <a name="ARG-ListTagSyncTasks-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9+/]*={0,2}$`

 ** [TagSyncTasks](#API_ListTagSyncTasks_ResponseSyntax) **   <a name="ARG-ListTagSyncTasks-response-TagSyncTasks"></a>
A list of tag-sync tasks and information about each task.
Type: Array of [TagSyncTaskItem](API_TagSyncTaskItem.md) objects

## Errors
<a name="API_ListTagSyncTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The request includes one or more parameters that violate validation rules.
HTTP Status Code: 400

 ** ForbiddenException **
The caller isn't authorized to make the request. Check permissions.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal error occurred while processing the request. Try again later.
HTTP Status Code: 500

 ** MethodNotAllowedException **
The request uses an HTTP method that isn't allowed for the specified resource.
HTTP Status Code: 405

 ** TooManyRequestsException **
You've exceeded throttling limits by making too many requests in a period of time.
HTTP Status Code: 429

 ** UnauthorizedException **
The request was rejected because it doesn't have valid credentials for the target resource.
HTTP Status Code: 401

## See Also
<a name="API_ListTagSyncTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/ListTagSyncTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/ListTagSyncTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/ListTagSyncTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/ListTagSyncTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/ListTagSyncTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/ListTagSyncTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/ListTagSyncTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/ListTagSyncTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/ListTagSyncTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/ListTagSyncTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

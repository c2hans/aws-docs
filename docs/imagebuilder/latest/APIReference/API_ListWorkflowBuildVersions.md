---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflowBuildVersions.html
---

# ListWorkflowBuildVersions
<a name="API_ListWorkflowBuildVersions"></a>

Returns a list of build versions for a specific workflow resource.

## Request Syntax
<a name="API_ListWorkflowBuildVersions_RequestSyntax"></a>

```
POST /ListWorkflowBuildVersions HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "workflowVersionArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWorkflowBuildVersions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWorkflowBuildVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListWorkflowBuildVersions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowBuildVersions-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListWorkflowBuildVersions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowBuildVersions-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [workflowVersionArn](#API_ListWorkflowBuildVersions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowBuildVersions-request-workflowVersionArn"></a>
The Amazon Resource Name (ARN) of the workflow resource for which to get a list of build versions. The version segments can contain wildcards (`x`) to match multiple versions of the workflow. If you don't specify an ARN, the response lists build versions for all of the workflows in your account.
Type: String
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

## Response Syntax
<a name="API_ListWorkflowBuildVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "workflowSummaryList": [
      {
         "arn": "string",
         "changeDescription": "string",
         "dateCreated": "string",
         "description": "string",
         "name": "string",
         "owner": "string",
         "state": {
            "reason": "string",
            "status": "string"
         },
         "tags": {
            "string" : "string"
         },
         "type": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkflowBuildVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkflowBuildVersions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowBuildVersions-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [workflowSummaryList](#API_ListWorkflowBuildVersions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowBuildVersions-response-workflowSummaryList"></a>
A list that contains metadata for the build versions of the workflow resource specified in the request.
Type: Array of [WorkflowSummary](API_WorkflowSummary.md) objects

## Errors
<a name="API_ListWorkflowBuildVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_ListWorkflowBuildVersions_Examples"></a>

### List the build versions of a workflow
<a name="API_ListWorkflowBuildVersions_Example_1"></a>

The following example lists the build versions that exist for version 1.0.0 of the specified workflow, with the most recent build version first and the change description for each build version showing what changed.

#### Sample Request
<a name="API_ListWorkflowBuildVersions_Example_1_Request"></a>

```
POST /ListWorkflowBuildVersions HTTP/1.1
Content-type: application/json

{
    "workflowVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0"
}
```

#### Sample Response
<a name="API_ListWorkflowBuildVersions_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "workflowSummaryList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0/2",
            "name": "my-example-workflow",
            "version": "1.0.0",
            "description": "Workflow to build my example image",
            "changeDescription": "Added a step to collect image metadata from the build instance",
            "type": "BUILD",
            "owner": "111122223333",
            "dateCreated": "2026-09-09T19:56:38.339Z"
        },
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0/1",
            "name": "my-example-workflow",
            "version": "1.0.0",
            "description": "Workflow to build my example image",
            "changeDescription": "Initial version",
            "type": "BUILD",
            "owner": "111122223333",
            "dateCreated": "2026-09-09T19:56:35.992Z"
        }
    ]
}
```

## See Also
<a name="API_ListWorkflowBuildVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListWorkflowBuildVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListWorkflowBuildVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListWorkflowBuildVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListWorkflowBuildVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListWorkflowBuildVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListWorkflowBuildVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListWorkflowBuildVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListWorkflowBuildVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListWorkflowBuildVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListWorkflowBuildVersions)

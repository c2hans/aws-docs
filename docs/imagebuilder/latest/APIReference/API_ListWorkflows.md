---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflows.html
---

# ListWorkflows
<a name="API_ListWorkflows"></a>

Lists workflow versions based on filtering parameters. To list the build versions of a specific workflow version, call [ListWorkflowBuildVersions](API_ListWorkflowBuildVersions.md).

## Request Syntax
<a name="API_ListWorkflows_RequestSyntax"></a>

```
POST /ListWorkflows HTTP/1.1
Content-type: application/json

{
   "byName": {{boolean}},
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "owner": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWorkflows_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWorkflows_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [byName](#API_ListWorkflows_RequestSyntax) **   <a name="imagebuilder-ListWorkflows-request-byName"></a>
Specifies whether to return one entry per workflow name, with all versions of each workflow aggregated. Defaults to `false`, which returns one entry per workflow version. You can't combine this option with the `version` filter.
Type: Boolean
Required: No

 ** [filters](#API_ListWorkflows_RequestSyntax) **   <a name="imagebuilder-ListWorkflows-request-filters"></a>
Filters to narrow the list of workflows. You can filter on `name`, `version`, `description`, and `type`.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_ListWorkflows_RequestSyntax) **   <a name="imagebuilder-ListWorkflows-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListWorkflows_RequestSyntax) **   <a name="imagebuilder-ListWorkflows-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [owner](#API_ListWorkflows_RequestSyntax) **   <a name="imagebuilder-ListWorkflows-request-owner"></a>
Filters results based on the workflow owner. By default, this request returns the workflows that your account owns (`Self`). Specify `Amazon` to list the workflows that Image Builder manages. Image Builder rejects the `Shared` and `ThirdParty` owner values for workflows, and `AWSMarketplace` returns no results.
Type: String
Valid Values: `Self | Shared | Amazon | ThirdParty | AWSMarketplace`
Required: No

## Response Syntax
<a name="API_ListWorkflows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "workflowVersionList": [
      {
         "arn": "string",
         "dateCreated": "string",
         "description": "string",
         "name": "string",
         "owner": "string",
         "type": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkflows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkflows_ResponseSyntax) **   <a name="imagebuilder-ListWorkflows-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [workflowVersionList](#API_ListWorkflows_ResponseSyntax) **   <a name="imagebuilder-ListWorkflows-response-workflowVersionList"></a>
A list of workflow versions that match the request criteria.
Type: Array of [WorkflowVersion](API_WorkflowVersion.md) objects

## Errors
<a name="API_ListWorkflows_Errors"></a>

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
<a name="API_ListWorkflows_Examples"></a>

### List workflows that you own
<a name="API_ListWorkflows_Example_1"></a>

The following example lists the workflow versions that you own.

#### Sample Request
<a name="API_ListWorkflows_Example_1_Request"></a>

```
POST /ListWorkflows HTTP/1.1
Content-type: application/json

{
    "owner": "Self"
}
```

#### Sample Response
<a name="API_ListWorkflows_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "workflowVersionList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-build-workflow/1.0.0",
            "name": "my-example-build-workflow",
            "version": "1.0.0",
            "description": "Builds my example image",
            "type": "BUILD",
            "owner": "111122223333",
            "dateCreated": "2026-09-09T19:56:09.033Z"
        },
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/test/my-example-test-workflow/1.0.0",
            "name": "my-example-test-workflow",
            "version": "1.0.0",
            "description": "Tests my example image",
            "type": "TEST",
            "owner": "111122223333",
            "dateCreated": "2026-09-09T19:56:12.440Z"
        }
    ]
}
```

## See Also
<a name="API_ListWorkflows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListWorkflows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListWorkflows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListWorkflows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListWorkflows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListWorkflows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListWorkflows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListWorkflows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListWorkflows)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListWorkflows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListWorkflows)

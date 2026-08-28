---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListLifecycleExecutionResources.html
---

# ListLifecycleExecutionResources
<a name="API_ListLifecycleExecutionResources"></a>

List resources that the runtime instance of the image lifecycle identified for lifecycle actions.

## Request Syntax
<a name="API_ListLifecycleExecutionResources_RequestSyntax"></a>

```
POST /ListLifecycleExecutionResources HTTP/1.1
Content-type: application/json

{
   "lifecycleExecutionId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "parentResourceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListLifecycleExecutionResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLifecycleExecutionResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [lifecycleExecutionId](#API_ListLifecycleExecutionResources_RequestSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-request-lifecycleExecutionId"></a>
Use the unique identifier for a runtime instance of the lifecycle policy to get runtime details.
Type: String
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

 ** [maxResults](#API_ListLifecycleExecutionResources_RequestSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-request-maxResults"></a>
Specify the maximum number of items to return in a request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListLifecycleExecutionResources_RequestSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-request-nextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [parentResourceId](#API_ListLifecycleExecutionResources_RequestSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-request-parentResourceId"></a>
You can leave this empty to get a list of Image Builder resources that were identified for lifecycle actions.
To get a list of associated resources that are impacted for an individual resource (the parent), specify its Amazon Resource Name (ARN). Associated resources are produced from your image and distributed when you run a build, such as AMIs or container images stored in ECR repositories.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListLifecycleExecutionResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lifecycleExecutionId": "string",
   "lifecycleExecutionState": {
      "reason": "string",
      "status": "string"
   },
   "nextToken": "string",
   "resources": [
      {
         "accountId": "string",
         "action": {
            "name": "string",
            "reason": "string"
         },
         "endTime": number,
         "imageUris": [ "string" ],
         "region": "string",
         "resourceId": "string",
         "snapshots": [
            {
               "snapshotId": "string",
               "state": {
                  "reason": "string",
                  "status": "string"
               }
            }
         ],
         "startTime": number,
         "state": {
            "reason": "string",
            "status": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListLifecycleExecutionResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecycleExecutionId](#API_ListLifecycleExecutionResources_ResponseSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-response-lifecycleExecutionId"></a>
Runtime details for the specified runtime instance of the lifecycle policy.
Type: String
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

 ** [lifecycleExecutionState](#API_ListLifecycleExecutionResources_ResponseSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-response-lifecycleExecutionState"></a>
The current state of the lifecycle runtime instance.
Type: [LifecycleExecutionState](API_LifecycleExecutionState.md) object

 ** [nextToken](#API_ListLifecycleExecutionResources_ResponseSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [resources](#API_ListLifecycleExecutionResources_ResponseSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-response-resources"></a>
A list of resources that were identified for lifecycle actions.
Type: Array of [LifecycleExecutionResource](API_LifecycleExecutionResource.md) objects

## Errors
<a name="API_ListLifecycleExecutionResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_ListLifecycleExecutionResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListLifecycleExecutionResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListLifecycleExecutionResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListLifecycleExecutionResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListLifecycleExecutionResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListLifecycleExecutionResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListLifecycleExecutionResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListLifecycleExecutionResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListLifecycleExecutionResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListLifecycleExecutionResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListLifecycleExecutionResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

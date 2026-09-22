---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListLifecycleExecutions.html
---

# ListLifecycleExecutions
<a name="API_ListLifecycleExecutions"></a>

Retrieves the lifecycle runtime history for the specified resource.

## Request Syntax
<a name="API_ListLifecycleExecutions_RequestSyntax"></a>

```
POST /ListLifecycleExecutions HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListLifecycleExecutions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLifecycleExecutions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListLifecycleExecutions_RequestSyntax) **   <a name="imagebuilder-ListLifecycleExecutions-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListLifecycleExecutions_RequestSyntax) **   <a name="imagebuilder-ListLifecycleExecutions-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [resourceArn](#API_ListLifecycleExecutions_RequestSyntax) **   <a name="imagebuilder-ListLifecycleExecutions-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource for which to list lifecycle executions. Specify a lifecycle policy ARN to list its executions, or an image build version ARN to list the executions that [StartResourceStateUpdate](API_StartResourceStateUpdate.md) started for that image. Other ARN types aren't valid for this request.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: Yes

## Response Syntax
<a name="API_ListLifecycleExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lifecycleExecutions": [
      {
         "endTime": number,
         "lifecycleExecutionId": "string",
         "lifecyclePolicyArn": "string",
         "resourcesImpactedSummary": {
            "hasImpactedResources": boolean
         },
         "startTime": number,
         "state": {
            "reason": "string",
            "status": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLifecycleExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecycleExecutions](#API_ListLifecycleExecutions_ResponseSyntax) **   <a name="imagebuilder-ListLifecycleExecutions-response-lifecycleExecutions"></a>
A list of lifecycle runtime instances for the specified resource.
Type: Array of [LifecycleExecution](API_LifecycleExecution.md) objects

 ** [nextToken](#API_ListLifecycleExecutions_ResponseSyntax) **   <a name="imagebuilder-ListLifecycleExecutions-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

## Errors
<a name="API_ListLifecycleExecutions_Errors"></a>

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
<a name="API_ListLifecycleExecutions_Examples"></a>

### List lifecycle executions for an image build version
<a name="API_ListLifecycleExecutions_Example_1"></a>

The following example lists the lifecycle executions that have run against the specified image build version. The execution shown was started with StartResourceStateUpdate rather than a lifecycle policy, so it has no lifecyclePolicyArn.

#### Sample Request
<a name="API_ListLifecycleExecutions_Example_1_Request"></a>

```
POST /ListLifecycleExecutions HTTP/1.1
Content-type: application/json

{
    "resourceArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1"
}
```

#### Sample Response
<a name="API_ListLifecycleExecutions_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "lifecycleExecutions": [
        {
            "lifecycleExecutionId": "lce-401aefc3-a829-46f6-8fc2-91497988a503",
            "resourcesImpactedSummary": {
                "hasImpactedResources": false
            },
            "state": {
                "status": "IN_PROGRESS"
            },
            "startTime": 1788990149.801
        }
    ]
}
```

## See Also
<a name="API_ListLifecycleExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListLifecycleExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListLifecycleExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListLifecycleExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListLifecycleExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListLifecycleExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListLifecycleExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListLifecycleExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListLifecycleExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListLifecycleExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListLifecycleExecutions)

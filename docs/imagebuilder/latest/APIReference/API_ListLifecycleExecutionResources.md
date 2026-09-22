---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListLifecycleExecutionResources.html
---

# ListLifecycleExecutionResources
<a name="API_ListLifecycleExecutionResources"></a>

Lists resources that the runtime instance of the image lifecycle identified for lifecycle actions.

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
The unique identifier for a runtime instance of the lifecycle policy.
Type: String
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

 ** [maxResults](#API_ListLifecycleExecutionResources_RequestSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListLifecycleExecutionResources_RequestSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [parentResourceId](#API_ListLifecycleExecutionResources_RequestSyntax) **   <a name="imagebuilder-ListLifecycleExecutionResources-request-parentResourceId"></a>
The Amazon Resource Name (ARN) of an image build version to get the output resources for, such as AMIs or container images in Amazon ECR. You can get this value from the `resourceId` in the top-level response. If you leave this property empty, the response lists the Image Builder resources that the lifecycle execution identified for lifecycle actions. If the image build version that you specify in `parentResourceId` wasn't part of this lifecycle execution, the response contains an empty list.
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
The unique identifier for the runtime instance of the lifecycle policy.
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
<a name="API_ListLifecycleExecutionResources_Examples"></a>

### List the resources that a lifecycle execution acted on
<a name="API_ListLifecycleExecutionResources_Example_1"></a>

The following example lists the resources that the specified lifecycle execution acted on. For a scheduled resource state update that hasn't started to apply changes yet, the resources list is empty.

#### Sample Request
<a name="API_ListLifecycleExecutionResources_Example_1_Request"></a>

```
POST /ListLifecycleExecutionResources HTTP/1.1
Content-type: application/json

{
    "lifecycleExecutionId": "lce-401aefc3-a829-46f6-8fc2-91497988a503"
}
```

#### Sample Response
<a name="API_ListLifecycleExecutionResources_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "resources": [],
    "lifecycleExecutionId": "lce-401aefc3-a829-46f6-8fc2-91497988a503",
    "lifecycleExecutionState": {
        "status": "IN_PROGRESS"
    }
}
```

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListLifecycleExecutionResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListLifecycleExecutionResources)

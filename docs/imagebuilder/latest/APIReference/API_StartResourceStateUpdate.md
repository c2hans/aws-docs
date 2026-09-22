---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_StartResourceStateUpdate.html
---

# StartResourceStateUpdate
<a name="API_StartResourceStateUpdate"></a>

Begins an ad-hoc state change for the specified image build version. This is a one-time operation - if you schedule the update, it runs only once. If the request includes underlying resources, or schedules the update far enough in the future, Image Builder runs the update as an asynchronous lifecycle execution and returns its identifier. Otherwise, for target states other than `DELETED`, the state change applies immediately. If a request that starts a lifecycle execution arrives while the image already has one in progress, Image Builder rejects it.

## Request Syntax
<a name="API_StartResourceStateUpdate_RequestSyntax"></a>

```
PUT /StartResourceStateUpdate HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "exclusionRules": {
      "amis": {
         "isPublic": {{boolean}},
         "lastLaunched": {
            "unit": "{{string}}",
            "value": {{number}}
         },
         "regions": [ "{{string}}" ],
         "sharedAccounts": [ "{{string}}" ],
         "tagMap": {
            "{{string}}" : "{{string}}"
         }
      }
   },
   "executionRole": "{{string}}",
   "includeResources": {
      "amis": {{boolean}},
      "containers": {{boolean}},
      "snapshots": {{boolean}}
   },
   "resourceArn": "{{string}}",
   "state": {
      "status": "{{string}}"
   },
   "updateAt": {{number}}
}
```

## URI Request Parameters
<a name="API_StartResourceStateUpdate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartResourceStateUpdate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartResourceStateUpdate_RequestSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [exclusionRules](#API_StartResourceStateUpdate_RequestSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-request-exclusionRules"></a>
Rules that Image Builder evaluates against each of the image's AMIs. Matching AMIs and their snapshots are skipped. Exclusion rules only take effect when the request includes AMIs. If the target state is `DELETED` and any resource was skipped, the Image Builder image resource itself is also retained. For the `DEPRECATED` and `DISABLED` target states, Image Builder updates the image resource's state regardless of exclusions.
Type: [ResourceStateUpdateExclusionRules](API_ResourceStateUpdateExclusionRules.md) object
Required: No

 ** [executionRole](#API_StartResourceStateUpdate_RequestSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-request-executionRole"></a>
The name or Amazon Resource Name (ARN) of the IAM role that's used to update image state. You must provide this property together with `includeResources`. Neither is valid without the other.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** [includeResources](#API_StartResourceStateUpdate_RequestSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-request-includeResources"></a>
Specifies which underlying resources to update, in addition to the Image Builder image resource itself. Snapshots and containers are only valid for the `DELETED` state. To set an image to `DELETED`, you must include its underlying resources. To delete only the Image Builder image record, use the [DeleteImage](API_DeleteImage.md) operation instead.
Type: [ResourceStateUpdateIncludeResources](API_ResourceStateUpdateIncludeResources.md) object
Required: No

 ** [resourceArn](#API_StartResourceStateUpdate_RequestSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the image build version to update. The image must be in one of these terminal states: `AVAILABLE`, `DEPRECATED`, `DISABLED`, `FAILED`, or `CANCELLED`. Images with `FAILED` or `CANCELLED` status can transition only to `DELETED`.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: Yes

 ** [state](#API_StartResourceStateUpdate_RequestSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-request-state"></a>
Specifies the lifecycle action to take for this request. For AMI-based images, valid values are `AVAILABLE`, `DEPRECATED`, `DISABLED`, and `DELETED`. For container-based images, only `DELETED` is supported.
Type: [ResourceState](API_ResourceState.md) object
Required: Yes

 ** [updateAt](#API_StartResourceStateUpdate_RequestSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-request-updateAt"></a>
The timestamp that indicates when resources are updated by a lifecycle action. This property is valid only when the target status is `DEPRECATED`, and the value must be a future time. If you don't specify a value, Image Builder begins the state update right away. For a scheduled deprecation, included AMIs get their EC2 deprecation time set immediately, and Image Builder schedules the image resource to transition to `DEPRECATED` at that time.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_StartResourceStateUpdate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lifecycleExecutionId": "string",
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_StartResourceStateUpdate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecycleExecutionId](#API_StartResourceStateUpdate_ResponseSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-response-lifecycleExecutionId"></a>
Identifies the lifecycle execution that performs the resource state update. Image Builder only returns this field when it started a lifecycle execution for the update. Use it with [GetLifecycleExecution](API_GetLifecycleExecution.md) to track progress.
Type: String
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

 ** [resourceArn](#API_StartResourceStateUpdate_ResponseSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-response-resourceArn"></a>
The requested Amazon Resource Name (ARN) of the Image Builder resource for the asynchronous update.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

## Errors
<a name="API_StartResourceStateUpdate_Errors"></a>

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

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
At least one of the resources referenced by your request does not exist.
HTTP Status Code: 404

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_StartResourceStateUpdate_Examples"></a>

### Schedule an image build version for deprecation
<a name="API_StartResourceStateUpdate_Example_1"></a>

The following example schedules the specified image build version and its AMI to move to the DEPRECATED state at the requested future time. It returns the ID of the lifecycle execution that applies the update.

#### Sample Request
<a name="API_StartResourceStateUpdate_Example_1_Request"></a>

```
PUT /StartResourceStateUpdate HTTP/1.1
Content-type: application/json

{
    "resourceArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1",
    "state": {
        "status": "DEPRECATED"
    },
    "executionRole": "arn:aws:iam::111122223333:role/my-example-state-update-role",
    "includeResources": {
        "amis": true
    },
    "updateAt": 1789161600,
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE24680"
}
```

#### Sample Response
<a name="API_StartResourceStateUpdate_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "lifecycleExecutionId": "lce-401aefc3-a829-46f6-8fc2-91497988a503",
    "resourceArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1"
}
```

## See Also
<a name="API_StartResourceStateUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/StartResourceStateUpdate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/StartResourceStateUpdate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/StartResourceStateUpdate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/StartResourceStateUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/StartResourceStateUpdate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/StartResourceStateUpdate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/StartResourceStateUpdate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/StartResourceStateUpdate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/StartResourceStateUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/StartResourceStateUpdate)

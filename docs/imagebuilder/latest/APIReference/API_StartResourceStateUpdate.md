---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_StartResourceStateUpdate.html
---

# StartResourceStateUpdate
<a name="API_StartResourceStateUpdate"></a>

Begins an asynchronous resource state update for lifecycle changes to the specified image resources.

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
A unique, case-sensitive identifier you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [exclusionRules](#API_StartResourceStateUpdate_RequestSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-request-exclusionRules"></a>
Skip action on the image resource and associated resources if specified exclusion rules are met.
Type: [ResourceStateUpdateExclusionRules](API_ResourceStateUpdateExclusionRules.md) object
Required: No

 ** [executionRole](#API_StartResourceStateUpdate_RequestSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-request-executionRole"></a>
The name or Amazon Resource Name (ARN) of the IAM role that’s used to update image state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** [includeResources](#API_StartResourceStateUpdate_RequestSyntax) **   <a name="imagebuilder-StartResourceStateUpdate-request-includeResources"></a>
Specifies which image resources to include in the state update. When specified, the lifecycle action applies to underlying resources. These resources include AMIs, snapshots, and containers in addition to the Image Builder image resource. Requires `executionRole` to also be specified. To delete an image and its underlying resources, you must specify `includeResources`. To delete only the Image Builder image record without affecting underlying resources, use the `DeleteImage` API instead.
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
Specifies the timestamp when the state transition takes effect. Use this parameter only when the target status is `DEPRECATED`. The value must be a future time.
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
Identifies the lifecycle runtime instance that started the resource state update.
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
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
At least one of the resources referenced by your request does not exist.
HTTP Status Code: 404

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

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

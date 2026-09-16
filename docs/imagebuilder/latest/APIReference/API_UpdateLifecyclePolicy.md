---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateLifecyclePolicy.html
---

# UpdateLifecyclePolicy
<a name="API_UpdateLifecyclePolicy"></a>

Updates the specified lifecycle policy.

## Request Syntax
<a name="API_UpdateLifecyclePolicy_RequestSyntax"></a>

```
PUT /UpdateLifecyclePolicy HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "executionRole": "{{string}}",
   "lifecyclePolicyArn": "{{string}}",
   "policyDetails": [
      {
         "action": {
            "includeResources": {
               "amis": {{boolean}},
               "containers": {{boolean}},
               "snapshots": {{boolean}}
            },
            "type": "{{string}}"
         },
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
            },
            "tagMap": {
               "{{string}}" : "{{string}}"
            }
         },
         "filter": {
            "retainAtLeast": {{number}},
            "type": "{{string}}",
            "unit": "{{string}}",
            "value": {{number}}
         }
      }
   ],
   "resourceSelection": {
      "recipes": [
         {
            "name": "{{string}}",
            "semanticVersion": "{{string}}"
         }
      ],
      "tagMap": {
         "{{string}}" : "{{string}}"
      }
   },
   "resourceType": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateLifecyclePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateLifecyclePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [description](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-description"></a>
Optional description for the lifecycle policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [executionRole](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-executionRole"></a>
The name or Amazon Resource Name (ARN) of the IAM role that Image Builder uses to update the lifecycle policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: Yes

 ** [lifecyclePolicyArn](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-lifecyclePolicyArn"></a>
The Amazon Resource Name (ARN) of the lifecycle policy resource.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws):lifecycle-policy/[a-z0-9-_]+$`
Required: Yes

 ** [policyDetails](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-policyDetails"></a>
The configuration details for a lifecycle policy resource.
Type: Array of [LifecyclePolicyDetail](API_LifecyclePolicyDetail.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: Yes

 ** [resourceSelection](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-resourceSelection"></a>
Selection criteria for resources that the lifecycle policy applies to.
Type: [LifecyclePolicyResourceSelection](API_LifecyclePolicyResourceSelection.md) object
Required: Yes

 ** [resourceType](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-resourceType"></a>
The type of image resource that the lifecycle policy applies to.
Type: String
Valid Values: `AMI_IMAGE | CONTAINER_IMAGE`
Required: Yes

 ** [status](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-status"></a>
Indicates whether the lifecycle policy resource is enabled.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

## Response Syntax
<a name="API_UpdateLifecyclePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lifecyclePolicyArn": "string"
}
```

## Response Elements
<a name="API_UpdateLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecyclePolicyArn](#API_UpdateLifecyclePolicy_ResponseSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-response-lifecyclePolicyArn"></a>
The Amazon Resource Name (ARN) of the image lifecycle policy resource that was updated.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws):lifecycle-policy/[a-z0-9-_]+$`

## Errors
<a name="API_UpdateLifecyclePolicy_Errors"></a>

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

 ** InvalidParameterCombinationException **
You have specified two or more mutually exclusive parameters. Review the error message for details.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_UpdateLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/UpdateLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/UpdateLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/UpdateLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/UpdateLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/UpdateLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/UpdateLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/UpdateLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/UpdateLifecyclePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/UpdateLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/UpdateLifecyclePolicy)

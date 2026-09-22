---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateLifecyclePolicy.html
---

# UpdateLifecyclePolicy
<a name="API_UpdateLifecyclePolicy"></a>

Updates the specified lifecycle policy. The request replaces the existing policy configuration rather than merging changes, so re-specify every setting that you want to keep. The `resourceType` must match the existing policy's value.

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
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [description](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-description"></a>
Optional description for the lifecycle policy. Because the update replaces the entire configuration, omitting this property removes any existing description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [executionRole](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-executionRole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions.
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
Selection criteria for resources that the lifecycle policy applies to. You must specify exactly one selection criteria: either recipes or a tag map, not both.
Type: [LifecyclePolicyResourceSelection](API_LifecyclePolicyResourceSelection.md) object
Required: Yes

 ** [resourceType](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-resourceType"></a>
The type of image resource that the lifecycle policy applies to. The value must match the policy's existing resource type. You can't change the resource type of an existing lifecycle policy.
Type: String
Valid Values: `AMI_IMAGE | CONTAINER_IMAGE`
Required: Yes

 ** [status](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-UpdateLifecyclePolicy-request-status"></a>
Indicates whether the lifecycle policy resource is enabled. Defaults to `ENABLED` when omitted, so updating a disabled policy without setting this property re-enables it.
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

 ** InvalidParameterCombinationException **
You have specified a combination of parameters that isn't valid. For example, two mutually exclusive parameters, or a parameter without its required companion parameter. Review the error message for details.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_UpdateLifecyclePolicy_Examples"></a>

### Update a lifecycle policy
<a name="API_UpdateLifecyclePolicy_Example_1"></a>

The following example updates a lifecycle policy to delete AMI images and their associated snapshots after 12 months, retaining the 3 most recent images.

#### Sample Request
<a name="API_UpdateLifecyclePolicy_Example_1_Request"></a>

```
PUT /UpdateLifecyclePolicy HTTP/1.1
Content-type: application/json

{
    "lifecyclePolicyArn": "arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-policy",
    "description": "Deletes AMI images and their snapshots after 12 months, retaining the 3 most recent",
    "status": "ENABLED",
    "executionRole": "arn:aws:iam::111122223333:role/my-example-lifecycle-role",
    "resourceType": "AMI_IMAGE",
    "policyDetails": [
        {
            "action": {
                "type": "DELETE",
                "includeResources": {
                    "amis": true,
                    "snapshots": true
                }
            },
            "filter": {
                "type": "AGE",
                "value": 12,
                "unit": "MONTHS",
                "retainAtLeast": 3
            }
        }
    ],
    "resourceSelection": {
        "tagMap": {
            "environment": "production"
        }
    },
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa"
}
```

#### Sample Response
<a name="API_UpdateLifecyclePolicy_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "lifecyclePolicyArn": "arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-policy"
}
```

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

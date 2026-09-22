---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateLifecyclePolicy.html
---

# CreateLifecyclePolicy
<a name="API_CreateLifecyclePolicy"></a>

Creates a lifecycle policy resource.

## Request Syntax
<a name="API_CreateLifecyclePolicy_RequestSyntax"></a>

```
PUT /CreateLifecyclePolicy HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "dryRun": {{boolean}},
   "executionRole": "{{string}}",
   "name": "{{string}}",
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
   "status": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateLifecyclePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateLifecyclePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [description](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-request-description"></a>
Optional description for the lifecycle policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [dryRun](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-request-dryRun"></a>
Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a `DryRunOperationException` error response.
Type: Boolean
Required: No

 ** [executionRole](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-request-executionRole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions. You must have permission to pass the role, and the role's trust policy must allow the Image Builder service principal to assume it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: Yes

 ** [name](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-request-name"></a>
The name of the lifecycle policy to create. Policy names must be unique to your account in each AWS Region. Image Builder generates the policy ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. You can't change the name after creation.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** [policyDetails](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-request-policyDetails"></a>
Configuration details for the lifecycle policy rules. A policy can contain at most one rule per action type: one `DELETE`, one `DEPRECATE`, and one `DISABLE`.
Type: Array of [LifecyclePolicyDetail](API_LifecyclePolicyDetail.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: Yes

 ** [resourceSelection](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-request-resourceSelection"></a>
Selection criteria for the resources that the lifecycle policy applies to. You must specify exactly one selection criteria: either recipes or a tag map, not both.
Type: [LifecyclePolicyResourceSelection](API_LifecyclePolicyResourceSelection.md) object
Required: Yes

 ** [resourceType](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-request-resourceType"></a>
The type of Image Builder resource that the lifecycle policy applies to. The resource type determines the allowed rule actions: policies for AMI-based Image Builder images support `DELETE`, `DEPRECATE`, and `DISABLE`, and policies for container-based Image Builder images support only `DELETE`. You can't change the resource type after creation.
Type: String
Valid Values: `AMI_IMAGE | CONTAINER_IMAGE`
Required: Yes

 ** [status](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-request-status"></a>
Indicates whether the lifecycle policy resource is enabled. If you don't specify a status, it defaults to `ENABLED`. Only enabled policies run on their schedule.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** [tags](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-request-tags"></a>
Tags to apply to the lifecycle policy resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateLifecyclePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "lifecyclePolicyArn": "string"
}
```

## Response Elements
<a name="API_CreateLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreateLifecyclePolicy_ResponseSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [lifecyclePolicyArn](#API_CreateLifecyclePolicy_ResponseSyntax) **   <a name="imagebuilder-CreateLifecyclePolicy-response-lifecyclePolicyArn"></a>
The Amazon Resource Name (ARN) of the lifecycle policy that the request created.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws):lifecycle-policy/[a-z0-9-_]+$`

## Errors
<a name="API_CreateLifecyclePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** DryRunOperationException **
The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.
HTTP Status Code: 412

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The resource that you are trying to create already exists.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded the number of permitted resources or operations for this service. For service quotas, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder).
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_CreateLifecyclePolicy_Examples"></a>

### Create a lifecycle policy
<a name="API_CreateLifecyclePolicy_Example_1"></a>

The following example creates a lifecycle policy that deletes AMI-based images six months after they were created, selecting the images that match the specified resource tags.

#### Sample Request
<a name="API_CreateLifecyclePolicy_Example_1_Request"></a>

```
PUT /CreateLifecyclePolicy HTTP/1.1
Content-type: application/json

{
    "name": "my-example-lifecycle-policy",
    "executionRole": "arn:aws:iam::111122223333:role/my-example-lifecycle-role",
    "resourceType": "AMI_IMAGE",
    "policyDetails": [
        {
            "action": {
                "type": "DELETE"
            },
            "filter": {
                "type": "AGE",
                "value": 6,
                "unit": "MONTHS"
            }
        }
    ],
    "resourceSelection": {
        "tagMap": {
            "Environment": "test"
        }
    },
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE13579"
}
```

#### Sample Response
<a name="API_CreateLifecyclePolicy_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE13579",
    "lifecyclePolicyArn": "arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-lifecycle-policy"
}
```

### Create a lifecycle policy with exclusion rules
<a name="API_CreateLifecyclePolicy_Example_2"></a>

The following example creates a lifecycle policy that deletes images created from the specified recipe version after six months. The policy excludes images whose AMIs launched an instance within the last 30 days or are tagged to be retained.

#### Sample Request
<a name="API_CreateLifecyclePolicy_Example_2_Request"></a>

```
PUT /CreateLifecyclePolicy HTTP/1.1
Content-type: application/json

{
    "name": "my-example-lifecycle-policy",
    "executionRole": "arn:aws:iam::111122223333:role/my-example-lifecycle-role",
    "resourceType": "AMI_IMAGE",
    "policyDetails": [
        {
            "action": {
                "type": "DELETE"
            },
            "filter": {
                "type": "AGE",
                "value": 6,
                "unit": "MONTHS"
            },
            "exclusionRules": {
                "amis": {
                    "lastLaunched": {
                        "value": 30,
                        "unit": "DAYS"
                    },
                    "tagMap": {
                        "Retention": "keep"
                    }
                }
            }
        }
    ],
    "resourceSelection": {
        "recipes": [
            {
                "name": "my-example-recipe",
                "semanticVersion": "1.0.0"
            }
        ]
    },
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE43210"
}
```

#### Sample Response
<a name="API_CreateLifecyclePolicy_Example_2_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE43210",
    "lifecyclePolicyArn": "arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-lifecycle-policy"
}
```

## See Also
<a name="API_CreateLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/CreateLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/CreateLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CreateLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/CreateLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CreateLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/CreateLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/CreateLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/CreateLifecyclePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateLifecyclePolicy)

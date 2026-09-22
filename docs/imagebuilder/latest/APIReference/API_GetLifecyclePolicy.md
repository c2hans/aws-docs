---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetLifecyclePolicy.html
---

# GetLifecyclePolicy
<a name="API_GetLifecyclePolicy"></a>

Retrieves details for the specified image lifecycle policy.

## Request Syntax
<a name="API_GetLifecyclePolicy_RequestSyntax"></a>

```
GET /GetLifecyclePolicy?lifecyclePolicyArn={{lifecyclePolicyArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLifecyclePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [lifecyclePolicyArn](#API_GetLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-GetLifecyclePolicy-request-uri-lifecyclePolicyArn"></a>
Specifies the Amazon Resource Name (ARN) of the image lifecycle policy resource to get.
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws):lifecycle-policy/[a-z0-9-_]+$`
Required: Yes

## Request Body
<a name="API_GetLifecyclePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLifecyclePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lifecyclePolicy": {
      "arn": "string",
      "dateCreated": number,
      "dateLastRun": number,
      "dateUpdated": number,
      "description": "string",
      "executionRole": "string",
      "name": "string",
      "policyDetails": [
         {
            "action": {
               "includeResources": {
                  "amis": boolean,
                  "containers": boolean,
                  "snapshots": boolean
               },
               "type": "string"
            },
            "exclusionRules": {
               "amis": {
                  "isPublic": boolean,
                  "lastLaunched": {
                     "unit": "string",
                     "value": number
                  },
                  "regions": [ "string" ],
                  "sharedAccounts": [ "string" ],
                  "tagMap": {
                     "string" : "string"
                  }
               },
               "tagMap": {
                  "string" : "string"
               }
            },
            "filter": {
               "retainAtLeast": number,
               "type": "string",
               "unit": "string",
               "value": number
            }
         }
      ],
      "resourceSelection": {
         "recipes": [
            {
               "name": "string",
               "semanticVersion": "string"
            }
         ],
         "tagMap": {
            "string" : "string"
         }
      },
      "resourceType": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_GetLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecyclePolicy](#API_GetLifecyclePolicy_ResponseSyntax) **   <a name="imagebuilder-GetLifecyclePolicy-response-lifecyclePolicy"></a>
The details of the lifecycle policy that the request retrieved.
Type: [LifecyclePolicy](API_LifecyclePolicy.md) object

## Errors
<a name="API_GetLifecyclePolicy_Errors"></a>

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
<a name="API_GetLifecyclePolicy_Examples"></a>

### Get the details of a lifecycle policy
<a name="API_GetLifecyclePolicy_Example_1"></a>

The following example retrieves the full definition of the specified lifecycle policy.

#### Sample Request
<a name="API_GetLifecyclePolicy_Example_1_Request"></a>

```
GET /GetLifecyclePolicy?lifecyclePolicyArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Alifecycle-policy%2Fmy-example-lifecycle-policy HTTP/1.1
```

#### Sample Response
<a name="API_GetLifecyclePolicy_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "lifecyclePolicy": {
        "arn": "arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-lifecycle-policy",
        "name": "my-example-lifecycle-policy",
        "description": "Deletes AMIs and snapshots for builds older than six months, keeping at least the five most recent",
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
                    "value": 6,
                    "unit": "MONTHS",
                    "retainAtLeast": 5
                }
            }
        ],
        "resourceSelection": {
            "tagMap": {
                "Environment": "my-example-environment"
            }
        },
        "dateCreated": 1788982478.409,
        "tags": {}
    }
}
```

## See Also
<a name="API_GetLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetLifecyclePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetLifecyclePolicy)

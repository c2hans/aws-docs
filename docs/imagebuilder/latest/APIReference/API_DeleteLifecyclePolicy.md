---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteLifecyclePolicy.html
---

# DeleteLifecyclePolicy
<a name="API_DeleteLifecyclePolicy"></a>

Deletes the specified lifecycle policy resource. Deleting the policy removes its schedule, so no further lifecycle runs occur for that policy. If a lifecycle execution is in progress for the policy, Image Builder cancels it. Deletion doesn't revert actions that the policy already applied to your resources.

## Request Syntax
<a name="API_DeleteLifecyclePolicy_RequestSyntax"></a>

```
DELETE /DeleteLifecyclePolicy?lifecyclePolicyArn={{lifecyclePolicyArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteLifecyclePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [lifecyclePolicyArn](#API_DeleteLifecyclePolicy_RequestSyntax) **   <a name="imagebuilder-DeleteLifecyclePolicy-request-uri-lifecyclePolicyArn"></a>
The Amazon Resource Name (ARN) of the lifecycle policy resource to delete.
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws):lifecycle-policy/[a-z0-9-_]+$`
Required: Yes

## Request Body
<a name="API_DeleteLifecyclePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteLifecyclePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lifecyclePolicyArn": "string"
}
```

## Response Elements
<a name="API_DeleteLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecyclePolicyArn](#API_DeleteLifecyclePolicy_ResponseSyntax) **   <a name="imagebuilder-DeleteLifecyclePolicy-response-lifecyclePolicyArn"></a>
The Amazon Resource Name (ARN) of the lifecycle policy that was deleted.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws):lifecycle-policy/[a-z0-9-_]+$`

## Errors
<a name="API_DeleteLifecyclePolicy_Errors"></a>

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

 ** ResourceDependencyException **
You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_DeleteLifecyclePolicy_Examples"></a>

### Delete a lifecycle policy
<a name="API_DeleteLifecyclePolicy_Example_1"></a>

The following example deletes the specified lifecycle policy.

#### Sample Request
<a name="API_DeleteLifecyclePolicy_Example_1_Request"></a>

```
DELETE /DeleteLifecyclePolicy?lifecyclePolicyArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Alifecycle-policy%2Fmy-example-lifecycle-policy HTTP/1.1
```

#### Sample Response
<a name="API_DeleteLifecyclePolicy_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "lifecyclePolicyArn": "arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-lifecycle-policy"
}
```

## See Also
<a name="API_DeleteLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/DeleteLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/DeleteLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/DeleteLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/DeleteLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/DeleteLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/DeleteLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/DeleteLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/DeleteLifecyclePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/DeleteLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/DeleteLifecyclePolicy)

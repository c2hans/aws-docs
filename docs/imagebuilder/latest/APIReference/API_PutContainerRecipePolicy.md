---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_PutContainerRecipePolicy.html
---

# PutContainerRecipePolicy
<a name="API_PutContainerRecipePolicy"></a>

Applies a policy to a container recipe. The preferred way to share resources is with the RAM API [CreateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html). If you use the PutContainerRecipePolicy operation instead, you must also call the RAM API [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html). Otherwise, the resource isn't visible to the principals that it's shared with.

## Request Syntax
<a name="API_PutContainerRecipePolicy_RequestSyntax"></a>

```
PUT /PutContainerRecipePolicy HTTP/1.1
Content-type: application/json

{
   "containerRecipeArn": "{{string}}",
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutContainerRecipePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutContainerRecipePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [containerRecipeArn](#API_PutContainerRecipePolicy_RequestSyntax) **   <a name="imagebuilder-PutContainerRecipePolicy-request-containerRecipeArn"></a>
The Amazon Resource Name (ARN) of the container recipe that this policy should be applied to.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: Yes

 ** [policy](#API_PutContainerRecipePolicy_RequestSyntax) **   <a name="imagebuilder-PutContainerRecipePolicy-request-policy"></a>
The policy to apply to the container recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30000.
Required: Yes

## Response Syntax
<a name="API_PutContainerRecipePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "containerRecipeArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_PutContainerRecipePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [containerRecipeArn](#API_PutContainerRecipePolicy_ResponseSyntax) **   <a name="imagebuilder-PutContainerRecipePolicy-response-containerRecipeArn"></a>
The Amazon Resource Name (ARN) of the container recipe that this policy was applied to.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`

 ** [requestId](#API_PutContainerRecipePolicy_ResponseSyntax) **   <a name="imagebuilder-PutContainerRecipePolicy-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_PutContainerRecipePolicy_Errors"></a>

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

 ** InvalidParameterValueException **
The value that you provided for the specified parameter is invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
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
<a name="API_PutContainerRecipePolicy_Examples"></a>

### Share a container recipe with another account
<a name="API_PutContainerRecipePolicy_Example_1"></a>

The following example applies a resource policy that grants another AWS account permission to view and use the specified container recipe.

#### Sample Request
<a name="API_PutContainerRecipePolicy_Example_1_Request"></a>

```
PUT /PutContainerRecipePolicy HTTP/1.1
Content-type: application/json

{
    "containerRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe-shared/1.0.0",
    "policy": "{\"Version\": \"2012-10-17\", \"Statement\": [{\"Sid\": \"AllowSharedAccountContainerRecipeAccess\", \"Effect\": \"Allow\", \"Principal\": {\"AWS\": \"arn:aws:iam::444455556666:root\"}, \"Action\": [\"imagebuilder:GetContainerRecipe\", \"imagebuilder:ListContainerRecipes\"], \"Resource\": \"arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe-shared/1.0.0\"}]}"
}
```

#### Sample Response
<a name="API_PutContainerRecipePolicy_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "dd917975-9d5d-49ce-9d94-daa753088dec",
    "containerRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe-shared/1.0.0"
}
```

## See Also
<a name="API_PutContainerRecipePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/PutContainerRecipePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/PutContainerRecipePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/PutContainerRecipePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/PutContainerRecipePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/PutContainerRecipePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/PutContainerRecipePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/PutContainerRecipePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/PutContainerRecipePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/PutContainerRecipePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/PutContainerRecipePolicy)

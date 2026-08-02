---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Attaches a resource-based permission policy to the AWS Migration Hub Refactor Spaces environment. The policy must contain the same actions and condition statements as the `arn:aws:ram::aws:permission/AWSRAMDefaultPermissionRefactorSpacesEnvironment` permission in AWS Resource Access Manager. The policy must not contain new lines or blank lines.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
PUT /resourcepolicy HTTP/1.1
Content-type: application/json

{
   "Policy": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Policy](#API_PutResourcePolicy_RequestSyntax) **   <a name="migrationhubrefactorspaces-PutResourcePolicy-request-Policy"></a>
A JSON-formatted string for an AWS resource-based policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300000.
Pattern: `.*\S.*`
Required: Yes

 ** [ResourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="migrationhubrefactorspaces-PutResourcePolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource to which the policy is being attached.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** InvalidResourcePolicyException **
The resource policy is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied because the request was throttled.
 ** QuotaCode **
Service quota requirement to identify originating quota. Reached throttling quota exception.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying.
 ** ServiceCode **
Service quota requirement to identify originating service. Reached throttling quota exception service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/PutResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/PutResourcePolicy)

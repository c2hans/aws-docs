---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeletePolicyAssignment.html
---

# DeletePolicyAssignment

Removes a governance policy from an Amazon Quick Sight principal. If the principal doesn't have the specified policy, the request succeeds and makes no change. If the principal has a different policy of the same type, the request fails with a `ConflictException`.

## Request Syntax
<a name="API_DeletePolicyAssignment_RequestSyntax"></a>

```
DELETE /governance-policy-mgmt/accounts/{{AccountId}}/policy-assignments?PolicyArn={{PolicyArn}}&PrincipalArn={{PrincipalArn}}&Revision={{Revision}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePolicyAssignment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountId](#API_DeletePolicyAssignment_RequestSyntax) **   <a name="QS-DeletePolicyAssignment-request-uri-AccountId"></a>
The ID of the AWS account that contains the principal.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [PolicyArn](#API_DeletePolicyAssignment_RequestSyntax) **   <a name="QS-DeletePolicyAssignment-request-uri-PolicyArn"></a>
The ARN of the policy to remove. The operation removes the assignment only if the principal currently has this policy.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`
Required: Yes

 ** [PrincipalArn](#API_DeletePolicyAssignment_RequestSyntax) **   <a name="QS-DeletePolicyAssignment-request-uri-PrincipalArn"></a>
The ARN of the user, group, or account to remove the policy from.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** [Revision](#API_DeletePolicyAssignment_RequestSyntax) **   <a name="QS-DeletePolicyAssignment-request-uri-Revision"></a>
The revision of the assignment from your most recent read. If the assignment has changed since that revision, the request fails with a `ConflictException`. If you don't specify a value, the operation doesn't check the revision.
Valid Range: Minimum value of 1.

## Request Body
<a name="API_DeletePolicyAssignment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePolicyAssignment_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeletePolicyAssignment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePolicyAssignment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** FieldList **
A list of the request fields that failed validation.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

## See Also
<a name="API_DeletePolicyAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeletePolicyAssignment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeletePolicyAssignment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeletePolicyAssignment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeletePolicyAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeletePolicyAssignment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeletePolicyAssignment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeletePolicyAssignment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeletePolicyAssignment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeletePolicyAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeletePolicyAssignment)

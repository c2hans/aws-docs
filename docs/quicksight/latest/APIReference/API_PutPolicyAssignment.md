---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PutPolicyAssignment.html
---

# PutPolicyAssignment

Assigns a governance policy to an Amazon Quick Sight principal. A principal can have one policy of each policy type. If the principal already has a policy of the same type, this operation replaces it.

To make the change conditional, specify `ExistingPolicyArn`, `Revision`, or both. If the current assignment doesn't match, the request fails with a `ConflictException` and makes no change. If the principal already has the specified policy, the request succeeds and makes no change.

## Request Syntax
<a name="API_PutPolicyAssignment_RequestSyntax"></a>

```
PUT /governance-policy-mgmt/accounts/{{AccountId}}/policy-assignments HTTP/1.1
Content-type: application/json

{
   "ExistingPolicyArn": "{{string}}",
   "PolicyArn": "{{string}}",
   "PrincipalArn": "{{string}}",
   "Revision": {{number}}
}
```

## URI Request Parameters
<a name="API_PutPolicyAssignment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountId](#API_PutPolicyAssignment_RequestSyntax) **   <a name="QS-PutPolicyAssignment-request-uri-AccountId"></a>
The ID of the AWS account that contains the policy and the principal.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_PutPolicyAssignment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PolicyArn](#API_PutPolicyAssignment_RequestSyntax) **   <a name="QS-PutPolicyAssignment-request-PolicyArn"></a>
The Amazon Resource Name (ARN) of the policy to assign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`
Required: Yes

 ** [PrincipalArn](#API_PutPolicyAssignment_RequestSyntax) **   <a name="QS-PutPolicyAssignment-request-PrincipalArn"></a>
The ARN of the user, group, or account to assign the policy to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** [ExistingPolicyArn](#API_PutPolicyAssignment_RequestSyntax) **   <a name="QS-PutPolicyAssignment-request-ExistingPolicyArn"></a>
The ARN of the policy that you expect the principal to have before this request. If the principal has a different policy of the same type, or no policy of that type, the request fails with a `ConflictException` and makes no change. If you don't specify a value, the operation doesn't check the existing assignment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`
Required: No

 ** [Revision](#API_PutPolicyAssignment_RequestSyntax) **   <a name="QS-PutPolicyAssignment-request-Revision"></a>
The revision of the assignment from your most recent read. If the assignment has changed since that revision, the request fails with a `ConflictException`. If you don't specify a value, the operation doesn't check the revision.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_PutPolicyAssignment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PolicyArn": "string",
   "ReplacedPolicyArn": "string",
   "Revision": number
}
```

## Response Elements
<a name="API_PutPolicyAssignment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyArn](#API_PutPolicyAssignment_ResponseSyntax) **   <a name="QS-PutPolicyAssignment-response-PolicyArn"></a>
The ARN of the policy that is now assigned to the principal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`

 ** [Revision](#API_PutPolicyAssignment_ResponseSyntax) **   <a name="QS-PutPolicyAssignment-response-Revision"></a>
The revision of the assignment after this request. Use this value in later requests to detect concurrent changes.
Type: Long
Valid Range: Minimum value of 1.

 ** [ReplacedPolicyArn](#API_PutPolicyAssignment_ResponseSyntax) **   <a name="QS-PutPolicyAssignment-response-ReplacedPolicyArn"></a>
The ARN of the policy that this request replaced. This value is absent if the principal had no policy of this type before the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`

## Errors
<a name="API_PutPolicyAssignment_Errors"></a>

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
<a name="API_PutPolicyAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/PutPolicyAssignment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/PutPolicyAssignment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PutPolicyAssignment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/PutPolicyAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PutPolicyAssignment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/PutPolicyAssignment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/PutPolicyAssignment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/PutPolicyAssignment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/PutPolicyAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PutPolicyAssignment)

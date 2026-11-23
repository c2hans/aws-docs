---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchPutPolicyAssignmentByPolicy.html
---

# BatchPutPolicyAssignmentByPolicy

Assigns a governance policy to multiple Amazon Quick Sight principals in a single request. If a principal already has a policy of the same type, this operation replaces it.

Each entry succeeds or fails independently. Check the `Errors` list in the response for entries that failed.

## Request Syntax
<a name="API_BatchPutPolicyAssignmentByPolicy_RequestSyntax"></a>

```
POST /governance-policy-mgmt/accounts/{{AccountId}}/policy-assignments/batch-put HTTP/1.1
Content-type: application/json

{
   "Assignments": [
      {
         "ExistingPolicyArn": "{{string}}",
         "PrincipalArn": "{{string}}",
         "Revision": {{number}}
      }
   ],
   "PolicyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchPutPolicyAssignmentByPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountId](#API_BatchPutPolicyAssignmentByPolicy_RequestSyntax) **   <a name="QS-BatchPutPolicyAssignmentByPolicy-request-uri-AccountId"></a>
The ID of the AWS account that contains the policy and the principals.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_BatchPutPolicyAssignmentByPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Assignments](#API_BatchPutPolicyAssignmentByPolicy_RequestSyntax) **   <a name="QS-BatchPutPolicyAssignmentByPolicy-request-Assignments"></a>
A list of 1–50 principals to assign the policy to. Each principal ARN must be unique within the request.
Type: Array of [PutAssignmentEntry](API_PutAssignmentEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

 ** [PolicyArn](#API_BatchPutPolicyAssignmentByPolicy_RequestSyntax) **   <a name="QS-BatchPutPolicyAssignmentByPolicy-request-PolicyArn"></a>
The ARN of the policy to assign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`
Required: Yes

## Response Syntax
<a name="API_BatchPutPolicyAssignmentByPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "PrincipalArn": "string"
      }
   ],
   "PolicyArn": "string",
   "Success": [
      {
         "PrincipalArn": "string",
         "ReplacedPolicyArn": "string",
         "Revision": number
      }
   ]
}
```

## Response Elements
<a name="API_BatchPutPolicyAssignmentByPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchPutPolicyAssignmentByPolicy_ResponseSyntax) **   <a name="QS-BatchPutPolicyAssignmentByPolicy-response-Errors"></a>
A list of principals that the policy couldn't be assigned to, with the reason for each failure.
Type: Array of [BatchPutPolicyAssignmentError](API_BatchPutPolicyAssignmentError.md) objects

 ** [PolicyArn](#API_BatchPutPolicyAssignmentByPolicy_ResponseSyntax) **   <a name="QS-BatchPutPolicyAssignmentByPolicy-response-PolicyArn"></a>
The ARN of the policy from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`

 ** [Success](#API_BatchPutPolicyAssignmentByPolicy_ResponseSyntax) **   <a name="QS-BatchPutPolicyAssignmentByPolicy-response-Success"></a>
A list of principals that the policy was assigned to.
Type: Array of [BatchPutPolicyAssignmentSuccess](API_BatchPutPolicyAssignmentSuccess.md) objects

## Errors
<a name="API_BatchPutPolicyAssignmentByPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

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
<a name="API_BatchPutPolicyAssignmentByPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/BatchPutPolicyAssignmentByPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/BatchPutPolicyAssignmentByPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BatchPutPolicyAssignmentByPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/BatchPutPolicyAssignmentByPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BatchPutPolicyAssignmentByPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/BatchPutPolicyAssignmentByPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/BatchPutPolicyAssignmentByPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/BatchPutPolicyAssignmentByPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/BatchPutPolicyAssignmentByPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BatchPutPolicyAssignmentByPolicy)

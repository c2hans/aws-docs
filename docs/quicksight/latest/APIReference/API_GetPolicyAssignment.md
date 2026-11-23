---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetPolicyAssignment.html
---

# GetPolicyAssignment

Describes the policy of the specified type that an Amazon Quick Sight principal has. If the principal has no policy of that type, the response contains no policy details.

## Request Syntax
<a name="API_GetPolicyAssignment_RequestSyntax"></a>

```
GET /governance-policy-mgmt/accounts/{{AccountId}}/policy-assignments?PolicyType={{PolicyType}}&PrincipalArn={{PrincipalArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPolicyAssignment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountId](#API_GetPolicyAssignment_RequestSyntax) **   <a name="QS-GetPolicyAssignment-request-uri-AccountId"></a>
The ID of the AWS account that contains the principal.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [PolicyType](#API_GetPolicyAssignment_RequestSyntax) **   <a name="QS-GetPolicyAssignment-request-uri-PolicyType"></a>
The type of policy to describe. Choose one of the following values:
+  `LIMITS_PROFILE` – A limits profile that sets resource usage limits.
+  `CUSTOM_PERMISSIONS` – A custom permissions profile that restricts the capabilities available to a principal.
Valid Values: `LIMITS_PROFILE | CUSTOM_PERMISSIONS`
Required: Yes

 ** [PrincipalArn](#API_GetPolicyAssignment_RequestSyntax) **   <a name="QS-GetPolicyAssignment-request-uri-PrincipalArn"></a>
The ARN of the user, group, or account.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

## Request Body
<a name="API_GetPolicyAssignment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPolicyAssignment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PolicyArn": "string",
   "PolicyName": "string",
   "Revision": number,
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_GetPolicyAssignment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyArn](#API_GetPolicyAssignment_ResponseSyntax) **   <a name="QS-GetPolicyAssignment-response-PolicyArn"></a>
The ARN of the policy that the principal has. The response doesn't include this value if the principal has no policy of the requested type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`

 ** [PolicyName](#API_GetPolicyAssignment_ResponseSyntax) **   <a name="QS-GetPolicyAssignment-response-PolicyName"></a>
The display name of the assigned policy. This value is absent if the policy has no name or the name can't be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [Revision](#API_GetPolicyAssignment_ResponseSyntax) **   <a name="QS-GetPolicyAssignment-response-Revision"></a>
The current revision of the assignment. Pass this value in a later `PutPolicyAssignment` or `DeletePolicyAssignment` request to make sure that the assignment hasn't changed.
Type: Long
Valid Range: Minimum value of 1.

 ** [UpdatedAt](#API_GetPolicyAssignment_ResponseSyntax) **   <a name="QS-GetPolicyAssignment-response-UpdatedAt"></a>
The date and time that the assignment was last updated.
Type: Timestamp

## Errors
<a name="API_GetPolicyAssignment_Errors"></a>

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
<a name="API_GetPolicyAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/GetPolicyAssignment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/GetPolicyAssignment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GetPolicyAssignment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/GetPolicyAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GetPolicyAssignment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/GetPolicyAssignment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/GetPolicyAssignment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/GetPolicyAssignment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/GetPolicyAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GetPolicyAssignment)

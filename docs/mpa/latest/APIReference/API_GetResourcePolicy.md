---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetResourcePolicy.html
---

# GetResourcePolicy
<a name="API_GetResourcePolicy"></a>

Returns details about a policy for a resource.

## Request Syntax
<a name="API_GetResourcePolicy_RequestSyntax"></a>

```
POST /GetResourcePolicy HTTP/1.1
Content-type: application/json

{
   "PolicyName": "{{string}}",
   "PolicyType": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PolicyName](#API_GetResourcePolicy_RequestSyntax) **   <a name="mpa-GetResourcePolicy-request-PolicyName"></a>
Name of the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** [PolicyType](#API_GetResourcePolicy_RequestSyntax) **   <a name="mpa-GetResourcePolicy-request-PolicyType"></a>
The type of policy.
Type: String
Valid Values: `AWS_MANAGED | AWS_RAM`
Required: Yes

 ** [ResourceArn](#API_GetResourcePolicy_RequestSyntax) **   <a name="mpa-GetResourcePolicy-request-ResourceArn"></a>
Amazon Resource Name (ARN) for the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

## Response Syntax
<a name="API_GetResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PolicyDocument": "string",
   "PolicyName": "string",
   "PolicyType": "string",
   "PolicyVersionArn": "string",
   "ResourceArn": "string"
}
```

## Response Elements
<a name="API_GetResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyDocument](#API_GetResourcePolicy_ResponseSyntax) **   <a name="mpa-GetResourcePolicy-response-PolicyDocument"></a>
Document that contains the contents for the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 400000.

 ** [PolicyName](#API_GetResourcePolicy_ResponseSyntax) **   <a name="mpa-GetResourcePolicy-response-PolicyName"></a>
Name of the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.

 ** [PolicyType](#API_GetResourcePolicy_ResponseSyntax) **   <a name="mpa-GetResourcePolicy-response-PolicyType"></a>
The type of policy
Type: String
Valid Values: `AWS_MANAGED | AWS_RAM`

 ** [PolicyVersionArn](#API_GetResourcePolicy_ResponseSyntax) **   <a name="mpa-GetResourcePolicy-response-PolicyVersionArn"></a>
Amazon Resource Name (ARN) for the policy version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [ResourceArn](#API_GetResourcePolicy_ResponseSyntax) **   <a name="mpa-GetResourcePolicy-response-ResourceArn"></a>
Amazon Resource Name (ARN) for the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Errors
<a name="API_GetResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You do not have sufficient access to perform this action. Check your permissions, and try again.
 ** Message **
Message for the `AccessDeniedException` error.
HTTP Status Code: 403

 [InvalidParameterException](API_InvalidParameterException.md)
The request contains an invalid parameter value.
 ** Message **
Message for the `InvalidParameterException` error.
HTTP Status Code: 400

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The specified resource doesn't exist. Check the resource ID, and try again.
 ** Message **
Message for the `ResourceNotFoundException` error.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling.
 ** Message **
Message for the `ThrottlingException` error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the constraints specified by an AWS service.
 ** Message **
Message for the `ValidationException` error.
HTTP Status Code: 400

## See Also
<a name="API_GetResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/GetResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/GetResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/GetResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/GetResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/GetResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/GetResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/GetResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/GetResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/GetResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/GetResourcePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

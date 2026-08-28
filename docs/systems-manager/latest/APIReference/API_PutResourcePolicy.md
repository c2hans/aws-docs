---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Creates or updates a Systems Manager resource policy. A resource policy helps you to define the IAM entity (for example, an AWS account) that can manage your Systems Manager resources. The following resources support Systems Manager resource policies.
+  `OpsItemGroup` - The resource policy for `OpsItemGroup` enables AWS accounts to view and interact with OpsCenter operational work items (OpsItems).
+  `Parameter` - The resource policy is used to share a parameter with other accounts using AWS Resource Access Manager (AWS RAM).

  To share a parameter, it must be in the advanced parameter tier. For information about parameter tiers, see [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html). For information about changing an existing standard parameter to an advanced parameter, see [Changing a standard parameter to an advanced parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html#parameter-store-advanced-parameters-enabling).

  To share a `SecureString` parameter, it must be encrypted with a customer managed key, and you must share the key separately through AWS Key Management Service. AWS managed keys cannot be shared. Parameters encrypted with the default AWS managed key can be updated to use a customer managed key instead. For AWS KMS key definitions, see [AWS KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) in the * AWS Key Management Service Developer Guide*.
**Important**
While you can share a parameter using the Systems Manager `PutResourcePolicy` operation, we recommend using AWS Resource Access Manager (AWS RAM) instead. This is because using `PutResourcePolicy` requires the extra step of promoting the parameter to a standard AWS RAM Resource Share using the AWS RAM [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html) API operation. Otherwise, the parameter won't be returned by the Systems Manager [DescribeParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html) API operation using the `--shared` option.
For more information, see [Sharing a parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html#share) in the * AWS Systems Manager User Guide*

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
{
   "Policy": "{{string}}",
   "PolicyHash": "{{string}}",
   "PolicyId": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Policy](#API_PutResourcePolicy_RequestSyntax) **   <a name="systemsmanager-PutResourcePolicy-request-Policy"></a>
A policy you want to associate with a resource.
Type: String
Pattern: `^(?!\s*$).+`
Required: Yes

 ** [PolicyHash](#API_PutResourcePolicy_RequestSyntax) **   <a name="systemsmanager-PutResourcePolicy-request-PolicyHash"></a>
ID of the current policy version. The hash helps to prevent a situation where multiple users attempt to overwrite a policy. You must provide this hash when updating or deleting a policy.
Type: String
Required: No

 ** [PolicyId](#API_PutResourcePolicy_RequestSyntax) **   <a name="systemsmanager-PutResourcePolicy-request-PolicyId"></a>
The policy ID.
Type: String
Required: No

 ** [ResourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="systemsmanager-PutResourcePolicy-request-ResourceArn"></a>
Amazon Resource Name (ARN) of the resource to which you want to attach a policy.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
{
   "PolicyHash": "string",
   "PolicyId": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyHash](#API_PutResourcePolicy_ResponseSyntax) **   <a name="systemsmanager-PutResourcePolicy-response-PolicyHash"></a>
ID of the current policy version.
Type: String

 ** [PolicyId](#API_PutResourcePolicy_ResponseSyntax) **   <a name="systemsmanager-PutResourcePolicy-response-PolicyId"></a>
The policy ID. To update a policy, you must specify `PolicyId` and `PolicyHash`.
Type: String

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** MalformedResourcePolicyDocumentException **
The specified policy document is malformed or invalid, or excessive `PutResourcePolicy` or `DeleteResourcePolicy` calls have been made.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified parameter to be shared could not be found.
HTTP Status Code: 400

 ** ResourcePolicyConflictException **
The hash provided in the call doesn't match the stored hash. This exception is thrown when trying to update an obsolete policy version or when multiple requests to update a policy are sent.
HTTP Status Code: 400

 ** ResourcePolicyInvalidParameterException **
One or more parameters specified for the call aren't valid. Verify the parameters and their values and try again.
HTTP Status Code: 400

 ** ResourcePolicyLimitExceededException **
The [PutResourcePolicy](#API_PutResourcePolicy) API action enforces two limits. A policy can't be greater than 1024 bytes in size. And only one policy can be attached to `OpsItemGroup`. Verify these limits and try again.
HTTP Status Code: 400

 ** ResourcePolicyNotFoundException **
No policies with the specified policy ID and hash could be found.
HTTP Status Code: 400

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/PutResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PutResourcePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

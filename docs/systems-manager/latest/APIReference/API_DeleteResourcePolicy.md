---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteResourcePolicy.html
---

# DeleteResourcePolicy
<a name="API_DeleteResourcePolicy"></a>

Deletes a Systems Manager resource policy. A resource policy helps you to define the IAM entity (for example, an AWS account) that can manage your Systems Manager resources. The following resources support Systems Manager resource policies.
+  `OpsItemGroup` - The resource policy for `OpsItemGroup` enables AWS accounts to view and interact with OpsCenter operational work items (OpsItems).
+  `Parameter` - The resource policy is used to share a parameter with other accounts using AWS Resource Access Manager (AWS RAM). For more information about cross-account sharing of parameters, see [Working with shared parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html) in the * AWS Systems Manager User Guide*.

## Request Syntax
<a name="API_DeleteResourcePolicy_RequestSyntax"></a>

```
{
   "PolicyHash": "{{string}}",
   "PolicyId": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteResourcePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PolicyHash](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="systemsmanager-DeleteResourcePolicy-request-PolicyHash"></a>
ID of the current policy version. The hash helps to prevent multiple calls from attempting to overwrite a policy.
Type: String
Required: Yes

 ** [PolicyId](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="systemsmanager-DeleteResourcePolicy-request-PolicyId"></a>
The policy ID.
Type: String
Required: Yes

 ** [ResourceArn](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="systemsmanager-DeleteResourcePolicy-request-ResourceArn"></a>
Amazon Resource Name (ARN) of the resource to which the policies are attached.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## Response Elements
<a name="API_DeleteResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourcePolicy_Errors"></a>

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

 ** ResourcePolicyNotFoundException **
No policies with the specified policy ID and hash could be found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteResourcePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

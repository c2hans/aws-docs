---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_InvokeLambdaAction.html
---

# InvokeLambdaAction
<a name="API_InvokeLambdaAction"></a>

The action to invoke an AWS Lambda function for processing the email.

## Contents
<a name="API_InvokeLambdaAction_Contents"></a>

 ** FunctionArn **   <a name="sesmailmanager-Type-InvokeLambdaAction-FunctionArn"></a>
The Amazon Resource Name (ARN) of the Lambda function to invoke.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** InvocationType **   <a name="sesmailmanager-Type-InvokeLambdaAction-InvocationType"></a>
The invocation type of the Lambda function. Use EVENT for asynchronous invocation or REQUEST\_RESPONSE for synchronous invocation.
Type: String
Valid Values: `EVENT | REQUEST_RESPONSE`
Required: Yes

 ** RoleArn **   <a name="sesmailmanager-Type-InvokeLambdaAction-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to use to invoke the Lambda function.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** ActionFailurePolicy **   <a name="sesmailmanager-Type-InvokeLambdaAction-ActionFailurePolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the AWS Lambda function no longer exists.
Type: String
Valid Values: `CONTINUE | DROP`
Required: No

 ** RetryTimeMinutes **   <a name="sesmailmanager-Type-InvokeLambdaAction-RetryTimeMinutes"></a>
The maximum time in minutes that the email processing can be retried if the Lambda invocation fails. The maximum value is 2160 minutes (36 hours).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2160.
Required: No

## See Also
<a name="API_InvokeLambdaAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/InvokeLambdaAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/InvokeLambdaAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/InvokeLambdaAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkforce.html
---

# DeleteWorkforce
<a name="API_DeleteWorkforce"></a>

Use this operation to delete a workforce.

If you want to create a new workforce in an AWS Region where a workforce already exists, use this operation to delete the existing workforce and then use [CreateWorkforce](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateWorkforce.html) to create a new workforce.

**Important**
If a private workforce contains one or more work teams, you must use the [DeleteWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkteam.html) operation to delete all work teams before you delete the workforce. If you try to delete a workforce that contains one or more work teams, you will receive a `ResourceInUse` error.

## Request Syntax
<a name="API_DeleteWorkforce_RequestSyntax"></a>

```
{
   "WorkforceName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteWorkforce_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WorkforceName](#API_DeleteWorkforce_RequestSyntax) **   <a name="sagemaker-DeleteWorkforce-request-WorkforceName"></a>
The name of the workforce.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]){0,62}`
Required: Yes

## Response Elements
<a name="API_DeleteWorkforce_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWorkforce_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteWorkforce_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteWorkforce)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteWorkforce)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteWorkforce)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteWorkforce)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteWorkforce)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteWorkforce)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteWorkforce)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteWorkforce)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteWorkforce)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteWorkforce)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

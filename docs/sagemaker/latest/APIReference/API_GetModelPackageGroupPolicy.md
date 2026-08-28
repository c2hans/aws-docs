---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetModelPackageGroupPolicy.html
---

# GetModelPackageGroupPolicy
<a name="API_GetModelPackageGroupPolicy"></a>

Gets a resource policy that manages access for a model group. For information about resource policies, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) in the * AWS Identity and Access Management User Guide.*.

## Request Syntax
<a name="API_GetModelPackageGroupPolicy_RequestSyntax"></a>

```
{
   "ModelPackageGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetModelPackageGroupPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ModelPackageGroupName](#API_GetModelPackageGroupPolicy_RequestSyntax) **   <a name="sagemaker-GetModelPackageGroupPolicy-request-ModelPackageGroupName"></a>
The name of the model group for which to get the resource policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_GetModelPackageGroupPolicy_ResponseSyntax"></a>

```
{
   "ResourcePolicy": "string"
}
```

## Response Elements
<a name="API_GetModelPackageGroupPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourcePolicy](#API_GetModelPackageGroupPolicy_ResponseSyntax) **   <a name="sagemaker-GetModelPackageGroupPolicy-response-ResourcePolicy"></a>
The resource policy for the model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `.*`

## Errors
<a name="API_GetModelPackageGroupPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetModelPackageGroupPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/GetModelPackageGroupPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/GetModelPackageGroupPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/GetModelPackageGroupPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/GetModelPackageGroupPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/GetModelPackageGroupPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/GetModelPackageGroupPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/GetModelPackageGroupPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/GetModelPackageGroupPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/GetModelPackageGroupPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/GetModelPackageGroupPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

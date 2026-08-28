---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PutModelPackageGroupPolicy.html
---

# PutModelPackageGroupPolicy
<a name="API_PutModelPackageGroupPolicy"></a>

Adds a resouce policy to control access to a model group. For information about resoure policies, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) in the * AWS Identity and Access Management User Guide.*.

## Request Syntax
<a name="API_PutModelPackageGroupPolicy_RequestSyntax"></a>

```
{
   "ModelPackageGroupName": "{{string}}",
   "ResourcePolicy": "{{string}}"
}
```

## Request Parameters
<a name="API_PutModelPackageGroupPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ModelPackageGroupName](#API_PutModelPackageGroupPolicy_RequestSyntax) **   <a name="sagemaker-PutModelPackageGroupPolicy-request-ModelPackageGroupName"></a>
The name of the model group to add a resource policy to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ResourcePolicy](#API_PutModelPackageGroupPolicy_RequestSyntax) **   <a name="sagemaker-PutModelPackageGroupPolicy-request-ResourcePolicy"></a>
The resource policy for the model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `.*`
Required: Yes

## Response Syntax
<a name="API_PutModelPackageGroupPolicy_ResponseSyntax"></a>

```
{
   "ModelPackageGroupArn": "string"
}
```

## Response Elements
<a name="API_PutModelPackageGroupPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelPackageGroupArn](#API_PutModelPackageGroupPolicy_ResponseSyntax) **   <a name="sagemaker-PutModelPackageGroupPolicy-response-ModelPackageGroupArn"></a>
The Amazon Resource Name (ARN) of the model package group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package-group/[\S]{1,2048}`

## Errors
<a name="API_PutModelPackageGroupPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

## See Also
<a name="API_PutModelPackageGroupPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/PutModelPackageGroupPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/PutModelPackageGroupPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PutModelPackageGroupPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/PutModelPackageGroupPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PutModelPackageGroupPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/PutModelPackageGroupPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/PutModelPackageGroupPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/PutModelPackageGroupPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/PutModelPackageGroupPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PutModelPackageGroupPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AssociateTrialComponent.html
---

# AssociateTrialComponent
<a name="API_AssociateTrialComponent"></a>

Associates a trial component with a trial. A trial component can be associated with multiple trials. To disassociate a trial component from a trial, call the [DisassociateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DisassociateTrialComponent.html) API.

## Request Syntax
<a name="API_AssociateTrialComponent_RequestSyntax"></a>

```
{
   "TrialComponentName": "{{string}}",
   "TrialName": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateTrialComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrialComponentName](#API_AssociateTrialComponent_RequestSyntax) **   <a name="sagemaker-AssociateTrialComponent-request-TrialComponentName"></a>
The name of the component to associated with the trial.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

 ** [TrialName](#API_AssociateTrialComponent_RequestSyntax) **   <a name="sagemaker-AssociateTrialComponent-request-TrialName"></a>
The name of the trial to associate with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_AssociateTrialComponent_ResponseSyntax"></a>

```
{
   "TrialArn": "string",
   "TrialComponentArn": "string"
}
```

## Response Elements
<a name="API_AssociateTrialComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrialArn](#API_AssociateTrialComponent_ResponseSyntax) **   <a name="sagemaker-AssociateTrialComponent-response-TrialArn"></a>
The Amazon Resource Name (ARN) of the trial.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial/.*`

 ** [TrialComponentArn](#API_AssociateTrialComponent_ResponseSyntax) **   <a name="sagemaker-AssociateTrialComponent-response-TrialComponentArn"></a>
The Amazon Resource Name (ARN) of the trial component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial-component/.*`

## Errors
<a name="API_AssociateTrialComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_AssociateTrialComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/AssociateTrialComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/AssociateTrialComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AssociateTrialComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/AssociateTrialComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AssociateTrialComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/AssociateTrialComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/AssociateTrialComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/AssociateTrialComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/AssociateTrialComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AssociateTrialComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

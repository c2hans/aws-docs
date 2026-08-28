---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutEvaluations.html
---

# PutEvaluations
<a name="API_PutEvaluations"></a>

Used by an AWS Lambda function to deliver evaluation results to AWS Config. This operation is required in every AWS Lambda function that is invoked by an AWS Config rule.

## Request Syntax
<a name="API_PutEvaluations_RequestSyntax"></a>

```
{
   "Evaluations": [
      {
         "Annotation": "{{string}}",
         "ComplianceResourceId": "{{string}}",
         "ComplianceResourceType": "{{string}}",
         "ComplianceType": "{{string}}",
         "OrderingTimestamp": {{number}}
      }
   ],
   "ResultToken": "{{string}}",
   "TestMode": {{boolean}}
}
```

## Request Parameters
<a name="API_PutEvaluations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Evaluations](#API_PutEvaluations_RequestSyntax) **   <a name="config-PutEvaluations-request-Evaluations"></a>
The assessments that the AWS Lambda function performs. Each evaluation identifies an AWS resource and indicates whether it complies with the AWS Config rule that invokes the AWS Lambda function.
Type: Array of [Evaluation](API_Evaluation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [ResultToken](#API_PutEvaluations_RequestSyntax) **   <a name="config-PutEvaluations-request-ResultToken"></a>
An encrypted token that associates an evaluation with an AWS Config rule. Identifies the rule and the event that triggered the evaluation.
Type: String
Required: Yes

 ** [TestMode](#API_PutEvaluations_RequestSyntax) **   <a name="config-PutEvaluations-request-TestMode"></a>
Use this parameter to specify a test run for `PutEvaluations`. You can verify whether your AWS Lambda function will deliver evaluation results to AWS Config. No updates occur to your existing evaluations, and evaluation results are not sent to AWS Config.
When `TestMode` is `true`, `PutEvaluations` doesn't require a valid value for the `ResultToken` parameter, but the value cannot be null.
Type: Boolean
Required: No

## Response Syntax
<a name="API_PutEvaluations_ResponseSyntax"></a>

```
{
   "FailedEvaluations": [
      {
         "Annotation": "string",
         "ComplianceResourceId": "string",
         "ComplianceResourceType": "string",
         "ComplianceType": "string",
         "OrderingTimestamp": number
      }
   ]
}
```

## Response Elements
<a name="API_PutEvaluations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedEvaluations](#API_PutEvaluations_ResponseSyntax) **   <a name="config-PutEvaluations-response-FailedEvaluations"></a>
Requests that failed because of a client or server error.
Type: Array of [Evaluation](API_Evaluation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_PutEvaluations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** InvalidResultTokenException **
The specified `ResultToken` is not valid.
HTTP Status Code: 400

 ** NoSuchConfigRuleException **
The AWS Config rule in the request is not valid. Verify that the rule is an AWS Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.
HTTP Status Code: 400

## See Also
<a name="API_PutEvaluations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutEvaluations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutEvaluations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutEvaluations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutEvaluations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutEvaluations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutEvaluations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutEvaluations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutEvaluations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutEvaluations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutEvaluations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

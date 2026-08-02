---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html
---

# StartResourceEvaluation
<a name="API_StartResourceEvaluation"></a>

Runs an on-demand evaluation for the specified resource to determine whether the resource details will comply with configured AWS Config rules. You can also use it for evaluation purposes. AWS Config recommends using an evaluation context. It runs an execution against the resource details with all of the AWS Config rules in your account that match with the specified proactive mode and resource type.

**Note**
Ensure you have the `cloudformation:DescribeType` role setup to validate the resource type schema.
You can find the [Resource type schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html) in "* AWS public extensions*" within the AWS CloudFormation registry or with the following CLI commmand: `aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type RESOURCE`.
For more information, see [Managing extensions through the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-view) and [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the AWS CloudFormation User Guide.

## Request Syntax
<a name="API_StartResourceEvaluation_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "EvaluationContext": {
      "EvaluationContextIdentifier": "{{string}}"
   },
   "EvaluationMode": "{{string}}",
   "EvaluationTimeout": {{number}},
   "ResourceDetails": {
      "ResourceConfiguration": "{{string}}",
      "ResourceConfigurationSchemaType": "{{string}}",
      "ResourceId": "{{string}}",
      "ResourceType": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_StartResourceEvaluation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_StartResourceEvaluation_RequestSyntax) **   <a name="config-StartResourceEvaluation-request-ClientToken"></a>
A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request.
Avoid reusing the same client token for other API requests. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, other than the Region or Availability Zone, the retry fails with an IdempotentParameterMismatch error.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 256.
Required: No

 ** [EvaluationContext](#API_StartResourceEvaluation_RequestSyntax) **   <a name="config-StartResourceEvaluation-request-EvaluationContext"></a>
Returns an `EvaluationContext` object.
Type: [EvaluationContext](API_EvaluationContext.md) object
Required: No

 ** [EvaluationMode](#API_StartResourceEvaluation_RequestSyntax) **   <a name="config-StartResourceEvaluation-request-EvaluationMode"></a>
The mode of an evaluation.
The only valid value for this API is `PROACTIVE`.
Type: String
Valid Values: `DETECTIVE | PROACTIVE`
Required: Yes

 ** [EvaluationTimeout](#API_StartResourceEvaluation_RequestSyntax) **   <a name="config-StartResourceEvaluation-request-EvaluationTimeout"></a>
The timeout for an evaluation. The default is 900 seconds. You cannot specify a number greater than 3600. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3600.
Required: No

 ** [ResourceDetails](#API_StartResourceEvaluation_RequestSyntax) **   <a name="config-StartResourceEvaluation-request-ResourceDetails"></a>
Returns a `ResourceDetails` object.
Type: [ResourceDetails](API_ResourceDetails.md) object
Required: Yes

## Response Syntax
<a name="API_StartResourceEvaluation_ResponseSyntax"></a>

```
{
   "ResourceEvaluationId": "string"
}
```

## Response Elements
<a name="API_StartResourceEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceEvaluationId](#API_StartResourceEvaluation_ResponseSyntax) **   <a name="config-StartResourceEvaluation-response-ResourceEvaluationId"></a>
A unique ResourceEvaluationId that is associated with a single execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors
<a name="API_StartResourceEvaluation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatch **
Using the same client token with one or more different parameters. Specify a new client token with the parameter changes and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

## See Also
<a name="API_StartResourceEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/StartResourceEvaluation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/StartResourceEvaluation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/StartResourceEvaluation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/StartResourceEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/StartResourceEvaluation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/StartResourceEvaluation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/StartResourceEvaluation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/StartResourceEvaluation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/StartResourceEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/StartResourceEvaluation)

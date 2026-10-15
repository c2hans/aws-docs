---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Lambdas.html
---

# Lambdas
<a name="API_Lambdas"></a>

Configuration for AWS Lambda functions used in a Region switch plan.

## Contents
<a name="API_Lambdas_Contents"></a>

 ** arn **   <a name="regionswitch-Type-Lambdas-arn"></a>
The Amazon Resource Name (ARN) of the Lambda function.
Type: String
Required: No

 ** crossAccountRole **   <a name="regionswitch-Type-Lambdas-crossAccountRole"></a>
The cross account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-Lambdas-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

 ** payload **   <a name="regionswitch-Type-Lambdas-payload"></a>
The JSON payload to send to the Lambda function invocation. If you don't specify a payload, Region switch invokes the function with only the execution metadata.
If you provide a JSON object, Region switch merges execution metadata keys (`InvokedBy`, `PlanArn`, `ExecutionId`, `StepName`) into the top level. If one of your keys has the same name as a metadata key, your key takes precedence.
If you provide any other JSON type (string, number, boolean, or array), Region switch forwards it to the Lambda function unchanged, without adding metadata.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 786432.
Required: No

## See Also
<a name="API_Lambdas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Lambdas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Lambdas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Lambdas)

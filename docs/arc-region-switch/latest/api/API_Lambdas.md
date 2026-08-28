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

## See Also
<a name="API_Lambdas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Lambdas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Lambdas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Lambdas)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

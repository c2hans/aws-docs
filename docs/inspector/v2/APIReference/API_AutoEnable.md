---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AutoEnable.html
---

# AutoEnable
<a name="API_AutoEnable"></a>

Represents which scan types are automatically enabled for new members of your Amazon Inspector organization.

## Contents
<a name="API_AutoEnable_Contents"></a>

 ** ec2 **   <a name="inspector2-Type-AutoEnable-ec2"></a>
Represents whether Amazon EC2 scans are automatically enabled for new members of your Amazon Inspector organization.
Type: Boolean
Required: Yes

 ** ecr **   <a name="inspector2-Type-AutoEnable-ecr"></a>
Represents whether Amazon ECR scans are automatically enabled for new members of your Amazon Inspector organization.
Type: Boolean
Required: Yes

 ** codeRepository **   <a name="inspector2-Type-AutoEnable-codeRepository"></a>
Represents whether code repository scans are automatically enabled for new members of your Amazon Inspector organization.
Type: Boolean
Required: No

 ** lambda **   <a name="inspector2-Type-AutoEnable-lambda"></a>
Represents whether AWS Lambda standard scans are automatically enabled for new members of your Amazon Inspector organization.
Type: Boolean
Required: No

 ** lambdaCode **   <a name="inspector2-Type-AutoEnable-lambdaCode"></a>
Represents whether Lambda code scans are automatically enabled for new members of your Amazon Inspector organization.
Type: Boolean
Required: No

## See Also
<a name="API_AutoEnable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AutoEnable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AutoEnable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AutoEnable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

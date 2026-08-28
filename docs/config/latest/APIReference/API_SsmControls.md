---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_SsmControls.html
---

# SsmControls
<a name="API_SsmControls"></a>

 AWS Systems Manager (SSM) specific remediation controls.

## Contents
<a name="API_SsmControls_Contents"></a>

 ** ConcurrentExecutionRatePercentage **   <a name="config-Type-SsmControls-ConcurrentExecutionRatePercentage"></a>
The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule. You can specify a percentage, such as 10%. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** ErrorPercentage **   <a name="config-Type-SsmControls-ErrorPercentage"></a>
The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule. You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_SsmControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/SsmControls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/SsmControls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/SsmControls)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

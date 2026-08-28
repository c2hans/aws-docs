---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationParameterValue.html
---

# RemediationParameterValue
<a name="API_RemediationParameterValue"></a>

The value is either a dynamic (resource) value or a static value. You must select either a dynamic value or a static value.

## Contents
<a name="API_RemediationParameterValue_Contents"></a>

 ** ResourceValue **   <a name="config-Type-RemediationParameterValue-ResourceValue"></a>
The value is dynamic and changes at run-time.
Type: [ResourceValue](API_ResourceValue.md) object
Required: No

 ** StaticValue **   <a name="config-Type-RemediationParameterValue-StaticValue"></a>
The value is static and does not change at run-time.
Type: [StaticValue](API_StaticValue.md) object
Required: No

## See Also
<a name="API_RemediationParameterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/RemediationParameterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/RemediationParameterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/RemediationParameterValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackScope.html
---

# ConformancePackScope

Defines which resources trigger an evaluation for the AWS Config rules in a conformance pack. The scope is a tag key, or a combination of a tag key and value, that is applied to every rule in the conformance pack. Specify a scope to constrain which resources trigger an evaluation for the rules. Otherwise, evaluations of rules in the conformance pack are triggered when any resource in your recording group changes in configuration.

## Contents
<a name="API_ConformancePackScope_Contents"></a>

 ** TagKey **   <a name="config-Type-ConformancePackScope-TagKey"></a>
The tag key that applies to only those AWS resources that you want to trigger an evaluation for the rules in the conformance pack. Defines the [Scope:TagKey](API_Scope.md#config-Type-Scope-TagKey) of all AWS Config rules in the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** TagValue **   <a name="config-Type-ConformancePackScope-TagValue"></a>
The tag value that applies to only those AWS resources that you want to trigger an evaluation for the rules in the conformance pack. If you do not specify a value for `TagValue`, resources that have the tag key `TagKey` trigger an evaluation, regardless of the tag value. Defines the [Scope:TagValue](API_Scope.md#config-Type-Scope-TagValue) of all AWS Config rules in the conformance pack.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ConformancePackScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConformancePackScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConformancePackScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConformancePackScope)

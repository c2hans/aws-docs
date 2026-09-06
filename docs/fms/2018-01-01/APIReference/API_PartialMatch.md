---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PartialMatch.html
---

# PartialMatch
<a name="API_PartialMatch"></a>

The reference rule that partially matches the `ViolationTarget` rule and violation reason.

## Contents
<a name="API_PartialMatch_Contents"></a>

 ** Reference **   <a name="fms-Type-PartialMatch-Reference"></a>
The reference rule from the primary security group of the AWS Firewall Manager policy.
Type: String
Required: No

 ** TargetViolationReasons **   <a name="fms-Type-PartialMatch-TargetViolationReasons"></a>
The violation reason.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `\w+`
Required: No

## See Also
<a name="API_PartialMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/PartialMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/PartialMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/PartialMatch)

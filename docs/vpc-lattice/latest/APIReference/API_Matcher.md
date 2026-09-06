---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_Matcher.html
---

# Matcher
<a name="API_Matcher"></a>

Describes the codes to use when checking for a successful response from a target for health checks.

## Contents
<a name="API_Matcher_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** httpCode **   <a name="vpclattice-Type-Matcher-httpCode"></a>
The HTTP code to use when checking for a successful response from a target.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Pattern: `.*(^[0-9-,]+$|(^$)).*`
Required: No

## See Also
<a name="API_Matcher_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/Matcher)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/Matcher)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/Matcher)

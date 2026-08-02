---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_HeaderMatchType.html
---

# HeaderMatchType
<a name="API_HeaderMatchType"></a>

Describes a header match type.

## Contents
<a name="API_HeaderMatchType_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** contains **   <a name="vpclattice-Type-HeaderMatchType-contains"></a>
A contains type match.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** exact **   <a name="vpclattice-Type-HeaderMatchType-exact"></a>
An exact type match.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** prefix **   <a name="vpclattice-Type-HeaderMatchType-prefix"></a>
A prefix type match. Matches the value with the prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_HeaderMatchType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/HeaderMatchType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/HeaderMatchType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/HeaderMatchType)

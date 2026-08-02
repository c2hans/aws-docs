---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_HeaderMatch.html
---

# HeaderMatch
<a name="API_HeaderMatch"></a>

Describes the constraints for a header match. Matches incoming requests with rule based on request header value before applying rule action.

## Contents
<a name="API_HeaderMatch_Contents"></a>

 ** match **   <a name="vpclattice-Type-HeaderMatch-match"></a>
The header match type.
Type: [HeaderMatchType](API_HeaderMatchType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** name **   <a name="vpclattice-Type-HeaderMatch-name"></a>
The name of the header.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** caseSensitive **   <a name="vpclattice-Type-HeaderMatch-caseSensitive"></a>
Indicates whether the match is case sensitive.
Type: Boolean
Required: No

## See Also
<a name="API_HeaderMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/HeaderMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/HeaderMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/HeaderMatch)

---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_Cost.html
---

# Cost
<a name="API_Cost"></a>

Defines a cost object.

## Contents
<a name="API_Cost_Contents"></a>

 ** amount **   <a name="resiliencehub-Type-Cost-amount"></a>
The cost amount.
Type: Double
Required: Yes

 ** currency **   <a name="resiliencehub-Type-Cost-currency"></a>
The cost currency, for example `USD`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3.
Required: Yes

 ** frequency **   <a name="resiliencehub-Type-Cost-frequency"></a>
The cost frequency.
Type: String
Valid Values: `Hourly | Daily | Monthly | Yearly`
Required: Yes

## See Also
<a name="API_Cost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/Cost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/Cost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/Cost)

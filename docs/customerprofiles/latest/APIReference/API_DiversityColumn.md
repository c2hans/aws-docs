---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DiversityColumn.html
---

# DiversityColumn
<a name="API_connect-customer-profiles_DiversityColumn"></a>

Defines a diversity constraint for a single item column, specifying a cap type and a target value or placeholder that controls how many recommended items may share the same column value.

## Contents
<a name="API_connect-customer-profiles_DiversityColumn_Contents"></a>

 ** CapType **   <a name="connect-Type-connect-customer-profiles_DiversityColumn-CapType"></a>
The type of diversity cap to apply. Valid values are `PERCENTAGE` (interpret `Target` as a percentage of returned items) and `VALUE` (interpret `Target` as an absolute count).
Type: String
Valid Values: `PERCENTAGE | VALUE`
Required: Yes

 ** Name **   <a name="connect-Type-connect-customer-profiles_DiversityColumn-Name"></a>
The name of the item catalog column on which to apply the diversity cap. The column must be defined in the recommender schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** Target **   <a name="connect-Type-connect-customer-profiles_DiversityColumn-Target"></a>
The diversity cap target. Either an integer literal (for example, `"25"`) or a placeholder expression of the form `$name` whose value is supplied at inference time through `GetProfileRecommendations`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(\d+|\$[a-z_]+)`
Required: Yes

## See Also
<a name="API_connect-customer-profiles_DiversityColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/DiversityColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/DiversityColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/DiversityColumn)

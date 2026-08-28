---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ExtraLengthValueProfileDimension.html
---

# ExtraLengthValueProfileDimension
<a name="API_connect-customer-profiles_ExtraLengthValueProfileDimension"></a>

Object that segments on various Customer profile's fields that are larger than normal.

## Contents
<a name="API_connect-customer-profiles_ExtraLengthValueProfileDimension_Contents"></a>

 ** DimensionType **   <a name="connect-Type-connect-customer-profiles_ExtraLengthValueProfileDimension-DimensionType"></a>
The action to segment with.
Type: String
Valid Values: `INCLUSIVE | EXCLUSIVE | CONTAINS | BEGINS_WITH | ENDS_WITH`
Required: Yes

 ** Values **   <a name="connect-Type-connect-customer-profiles_ExtraLengthValueProfileDimension-Values"></a>
The values to apply the DimensionType on.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## See Also
<a name="API_connect-customer-profiles_ExtraLengthValueProfileDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ExtraLengthValueProfileDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ExtraLengthValueProfileDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ExtraLengthValueProfileDimension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

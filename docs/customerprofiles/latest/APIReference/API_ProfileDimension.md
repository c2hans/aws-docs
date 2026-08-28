---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ProfileDimension.html
---

# ProfileDimension
<a name="API_connect-customer-profiles_ProfileDimension"></a>

Object to hold the dimensions of a profile's fields to segment on.

## Contents
<a name="API_connect-customer-profiles_ProfileDimension_Contents"></a>

 ** DimensionType **   <a name="connect-Type-connect-customer-profiles_ProfileDimension-DimensionType"></a>
The action to segment on.
Type: String
Valid Values: `INCLUSIVE | EXCLUSIVE | CONTAINS | BEGINS_WITH | ENDS_WITH`
Required: Yes

 ** Values **   <a name="connect-Type-connect-customer-profiles_ProfileDimension-Values"></a>
The values to apply the DimensionType on.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_connect-customer-profiles_ProfileDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ProfileDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ProfileDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ProfileDimension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

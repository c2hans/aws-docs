---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_Dimension.html
---

# Dimension
<a name="API_connect-customer-profiles_Dimension"></a>

Object that holds what profile and calculated attributes to segment on.

## Contents
<a name="API_connect-customer-profiles_Dimension_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CalculatedAttributes **   <a name="connect-Type-connect-customer-profiles_Dimension-CalculatedAttributes"></a>
Object that holds the calculated attributes to segment on.
Type: String to [CalculatedAttributeDimension](API_connect-customer-profiles_CalculatedAttributeDimension.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: No

 ** ProfileAttributes **   <a name="connect-Type-connect-customer-profiles_Dimension-ProfileAttributes"></a>
Object that holds the profile attributes to segment on.
Type: [ProfileAttributes](API_connect-customer-profiles_ProfileAttributes.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_Dimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/Dimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/Dimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/Dimension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

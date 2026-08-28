---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ProfileTypeDimension.html
---

# ProfileTypeDimension
<a name="API_connect-customer-profiles_ProfileTypeDimension"></a>

Object to hold the dimension of a profile type field to segment on.

## Contents
<a name="API_connect-customer-profiles_ProfileTypeDimension_Contents"></a>

 ** DimensionType **   <a name="connect-Type-connect-customer-profiles_ProfileTypeDimension-DimensionType"></a>
The action to segment on.
Type: String
Valid Values: `INCLUSIVE | EXCLUSIVE`
Required: Yes

 ** Values **   <a name="connect-Type-connect-customer-profiles_ProfileTypeDimension-Values"></a>
The values to apply the DimensionType on.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ACCOUNT_PROFILE | PROFILE`
Required: Yes

## See Also
<a name="API_connect-customer-profiles_ProfileTypeDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ProfileTypeDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ProfileTypeDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ProfileTypeDimension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ProfileQueryResult.html
---

# ProfileQueryResult
<a name="API_connect-customer-profiles_ProfileQueryResult"></a>

Object that holds the results for membership.

## Contents
<a name="API_connect-customer-profiles_ProfileQueryResult_Contents"></a>

 ** ProfileId **   <a name="connect-Type-connect-customer-profiles_ProfileQueryResult-ProfileId"></a>
The profile id the result belongs to.
Type: String
Required: Yes

 ** QueryResult **   <a name="connect-Type-connect-customer-profiles_ProfileQueryResult-QueryResult"></a>
Describes whether the profile was absent or present in the segment.
Type: String
Valid Values: `PRESENT | ABSENT`
Required: Yes

 ** Profile **   <a name="connect-Type-connect-customer-profiles_ProfileQueryResult-Profile"></a>
The standard profile of a customer.
Type: [Profile](API_connect-customer-profiles_Profile.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_ProfileQueryResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ProfileQueryResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ProfileQueryResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ProfileQueryResult)

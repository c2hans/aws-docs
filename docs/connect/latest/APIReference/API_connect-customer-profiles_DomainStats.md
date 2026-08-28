---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_DomainStats.html
---

# DomainStats
<a name="API_connect-customer-profiles_DomainStats"></a>

Usage-specific statistics about the domain.

## Contents
<a name="API_connect-customer-profiles_DomainStats_Contents"></a>

 ** MeteringProfileCount **   <a name="connect-Type-connect-customer-profiles_DomainStats-MeteringProfileCount"></a>
The number of profiles that you are currently paying for in the domain. If you have more than 100 objects associated with a single profile, that profile counts as two profiles. If you have more than 200 objects, that profile counts as three, and so on.
Type: Long
Required: No

 ** ObjectCount **   <a name="connect-Type-connect-customer-profiles_DomainStats-ObjectCount"></a>
The total number of objects in domain.
Type: Long
Required: No

 ** ProfileCount **   <a name="connect-Type-connect-customer-profiles_DomainStats-ProfileCount"></a>
The total number of profiles currently in the domain.
Type: Long
Required: No

 ** TotalSize **   <a name="connect-Type-connect-customer-profiles_DomainStats-TotalSize"></a>
The total size, in bytes, of all objects in the domain.
Type: Long
Required: No

## See Also
<a name="API_connect-customer-profiles_DomainStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/DomainStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/DomainStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/DomainStats)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

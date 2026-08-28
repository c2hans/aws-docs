---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ConflictResolution.html
---

# ConflictResolution
<a name="API_connect-customer-profiles_ConflictResolution"></a>

How the auto-merging process should resolve conflicts between different profiles.

## Contents
<a name="API_connect-customer-profiles_ConflictResolution_Contents"></a>

 ** ConflictResolvingModel **   <a name="connect-Type-connect-customer-profiles_ConflictResolution-ConflictResolvingModel"></a>
How the auto-merging process should resolve conflicts between different profiles.
+  `RECENCY`: Uses the data that was most recently updated.
+  `SOURCE`: Uses the data from a specific source. For example, if a company has been aquired or two departments have merged, data from the specified source is used. If two duplicate profiles are from the same source, then `RECENCY` is used again.
Type: String
Valid Values: `RECENCY | SOURCE`
Required: Yes

 ** SourceName **   <a name="connect-Type-connect-customer-profiles_ConflictResolution-SourceName"></a>
The `ObjectType` name that is used to resolve profile merging conflicts when choosing `SOURCE` as the `ConflictResolvingModel`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_connect-customer-profiles_ConflictResolution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ConflictResolution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ConflictResolution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ConflictResolution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

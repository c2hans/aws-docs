---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_Group.html
---

# Group
<a name="API_connect-customer-profiles_Group"></a>

Contains dimensions that determine what to segment on.

## Contents
<a name="API_connect-customer-profiles_Group_Contents"></a>

 ** Dimensions **   <a name="connect-Type-connect-customer-profiles_Group-Dimensions"></a>
Defines the attributes to segment on.
Type: Array of [Dimension](API_connect-customer-profiles_Dimension.md) objects
Required: No

 ** SourceSegments **   <a name="connect-Type-connect-customer-profiles_Group-SourceSegments"></a>
Defines the starting source of data.
Type: Array of [SourceSegment](API_connect-customer-profiles_SourceSegment.md) objects
Required: No

 ** SourceType **   <a name="connect-Type-connect-customer-profiles_Group-SourceType"></a>
Defines how to interact with the source data.
Type: String
Valid Values: `ALL | ANY | NONE`
Required: No

 ** Type **   <a name="connect-Type-connect-customer-profiles_Group-Type"></a>
Defines how to interact with the profiles found in the current filtering.
Type: String
Valid Values: `ALL | ANY | NONE`
Required: No

## See Also
<a name="API_connect-customer-profiles_Group_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/Group)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/Group)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/Group)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

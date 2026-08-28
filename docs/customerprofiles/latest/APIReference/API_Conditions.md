---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_Conditions.html
---

# Conditions
<a name="API_connect-customer-profiles_Conditions"></a>

The conditions including range, object count, and threshold for the calculated attribute.

## Contents
<a name="API_connect-customer-profiles_Conditions_Contents"></a>

 ** ObjectCount **   <a name="connect-Type-connect-customer-profiles_Conditions-ObjectCount"></a>
The number of profile objects used for the calculated attribute.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** Range **   <a name="connect-Type-connect-customer-profiles_Conditions-Range"></a>
The relative time period over which data is included in the aggregation.
Type: [Range](API_connect-customer-profiles_Range.md) object
Required: No

 ** Threshold **   <a name="connect-Type-connect-customer-profiles_Conditions-Threshold"></a>
The threshold for the calculated attribute.
Type: [Threshold](API_connect-customer-profiles_Threshold.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_Conditions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/Conditions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/Conditions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/Conditions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

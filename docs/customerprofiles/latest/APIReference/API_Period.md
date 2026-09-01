---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_Period.html
---

# Period
<a name="API_connect-customer-profiles_Period"></a>

Defines a limit and the time period during which it is enforced.

## Contents
<a name="API_connect-customer-profiles_Period_Contents"></a>

 ** Unit **   <a name="connect-Type-connect-customer-profiles_Period-Unit"></a>
The unit of time.
Type: String
Valid Values: `MINUTES | HOURS | DAYS | WEEKS | MONTHS`
Required: Yes

 ** Value **   <a name="connect-Type-connect-customer-profiles_Period-Value"></a>
The amount of time of the specified unit.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: Yes

 ** MaxInvocationsPerProfile **   <a name="connect-Type-connect-customer-profiles_Period-MaxInvocationsPerProfile"></a>
The maximum allowed number of destination invocations per profile.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** Unlimited **   <a name="connect-Type-connect-customer-profiles_Period-Unlimited"></a>
If set to true, there is no limit on the number of destination invocations per profile. The default is false.
Type: Boolean
Required: No

## See Also
<a name="API_connect-customer-profiles_Period_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/Period)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/Period)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/Period)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

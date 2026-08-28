---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Filter the selection by using a condition.

## Contents
<a name="API_Filter_Contents"></a>

 ** condition **   <a name="IncidentManager-Type-Filter-condition"></a>
The condition accepts before or after a specified time, equal to a string, or equal to an integer.
Type: [Condition](API_Condition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** key **   <a name="IncidentManager-Type-Filter-key"></a>
The key that you're filtering on.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

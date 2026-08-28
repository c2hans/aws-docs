---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A filter object that is used to return more specific results from a describe operation. Filters can be used to match a set of resources by specific criteria.

## Contents
<a name="API_Filter_Contents"></a>

 ** Name **   <a name="licensemanagerlinuxsubscriptions-Type-Filter-Name"></a>
The type of name to filter by.
Type: String
Required: No

 ** Operator **   <a name="licensemanagerlinuxsubscriptions-Type-Filter-Operator"></a>
An operator for filtering results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Valid Values: `Equal | NotEqual | Contains`
Required: No

 ** Values **   <a name="licensemanagerlinuxsubscriptions-Type-Filter-Values"></a>
One or more values for the name to filter by.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager Linux Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-linux-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

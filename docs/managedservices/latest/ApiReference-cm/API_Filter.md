---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

An attribute and value pair to use for narrowing search results.

## Contents
<a name="API_Filter_Contents"></a>

 ** Attribute **   <a name="amscm-Type-Filter-Attribute"></a>
The parameter name to filter on.
Type: String
Required: Yes

 ** Condition **   <a name="amscm-Type-Filter-Condition"></a>
Supported filter conditions.
Valid values: `After | Before | Between | Contains | Equals`.
Type: String
Required: No

 ** Value **   <a name="amscm-Type-Filter-Value"></a>
 *This member has been deprecated.*
The value of the corresponding attribute to use.
Type: String
Required: No

 ** Values **   <a name="amscm-Type-Filter-Values"></a>
The list of comma-separated values of the corresponding attribute to use.
Type: Array of strings
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_NodeConfigurationOptionsFilter.html
---

# NodeConfigurationOptionsFilter
<a name="API_NodeConfigurationOptionsFilter"></a>

A set of elements to filter the returned node configurations.

## Contents
<a name="API_NodeConfigurationOptionsFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **
The name of the element to filter.
Type: String
Valid Values: `NodeType | NumberOfNodes | EstimatedDiskUtilizationPercent | Mode`
Required: No

 ** Operator **
The filter operator. If filter Name is NodeType only the 'in' operator is supported. Provide one value to evaluate for 'eq', 'lt', 'le', 'gt', and 'ge'. Provide two values to evaluate for 'between'. Provide a list of values for 'in'.
Type: String
Valid Values: `eq | lt | gt | le | ge | in | between`
Required: No

 ** Value.item.N **
List of values. Compare Name using Operator to Values. If filter Name is NumberOfNodes, then values can range from 0 to 200. If filter Name is EstimatedDiskUtilizationPercent, then values can range from 0 to 100. For example, filter NumberOfNodes (name) GT (operator) 3 (values).
Type: Array of strings
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_NodeConfigurationOptionsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/NodeConfigurationOptionsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/NodeConfigurationOptionsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/NodeConfigurationOptionsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

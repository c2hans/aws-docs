---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataPathSort.html
---

# DataPathSort
<a name="API_DataPathSort"></a>

Allows data paths to be sorted by a specific data value.

## Contents
<a name="API_DataPathSort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Direction **   <a name="QS-Type-DataPathSort-Direction"></a>
Determines the sort direction.
Type: String
Valid Values: `ASC | DESC`
Required: Yes

 ** SortPaths **   <a name="QS-Type-DataPathSort-SortPaths"></a>
The list of data paths that need to be sorted.
Type: Array of [DataPathValue](API_DataPathValue.md) objects
Array Members: Maximum number of 20 items.
Required: Yes

## See Also
<a name="API_DataPathSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataPathSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataPathSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataPathSort)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

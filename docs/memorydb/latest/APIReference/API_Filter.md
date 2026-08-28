---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Used to streamline results of a search based on the property being filtered.

## Contents
<a name="API_Filter_Contents"></a>

 ** Name **   <a name="MemoryDB-Type-Filter-Name"></a>
The property being filtered. For example, UserName.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Values **   <a name="MemoryDB-Type-Filter-Values"></a>
The property values to filter on. For example, "user-123".
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

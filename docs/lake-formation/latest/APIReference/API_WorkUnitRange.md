---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_WorkUnitRange.html
---

# WorkUnitRange
<a name="API_WorkUnitRange"></a>

Defines the valid range of work unit IDs for querying the execution service.

## Contents
<a name="API_WorkUnitRange_Contents"></a>

 ** WorkUnitIdMax **   <a name="lakeformation-Type-WorkUnitRange-WorkUnitIdMax"></a>
Defines the maximum work unit ID in the range. The maximum value is inclusive.
Type: Long
Required: Yes

 ** WorkUnitIdMin **   <a name="lakeformation-Type-WorkUnitRange-WorkUnitIdMin"></a>
Defines the minimum work unit ID in the range.
Type: Long
Required: Yes

 ** WorkUnitToken **   <a name="lakeformation-Type-WorkUnitRange-WorkUnitToken"></a>
A work token used to query the execution service.
Type: String
Required: Yes

## See Also
<a name="API_WorkUnitRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/WorkUnitRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/WorkUnitRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/WorkUnitRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

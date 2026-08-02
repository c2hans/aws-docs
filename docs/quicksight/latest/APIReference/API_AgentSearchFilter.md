---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AgentSearchFilter.html
---

# AgentSearchFilter
<a name="API_AgentSearchFilter"></a>

A filter to apply when searching agents.

## Contents
<a name="API_AgentSearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-AgentSearchFilter-Name"></a>
The name of the field to filter on.
Type: String
Valid Values: `DIRECT_QUICKSIGHT_OWNER | DIRECT_QUICKSIGHT_VIEWER_OR_OWNER | DIRECT_QUICKSIGHT_SOLE_OWNER | AGENT_NAME`
Required: No

 ** Operator **   <a name="QS-Type-AgentSearchFilter-Operator"></a>
The comparison operator to use for the filter.
Type: String
Valid Values: `StringEquals | StringLike`
Required: No

 ** Value **   <a name="QS-Type-AgentSearchFilter-Value"></a>
The value to filter on.
Type: String
Required: No

## See Also
<a name="API_AgentSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AgentSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AgentSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AgentSearchFilter)

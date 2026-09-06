---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ActionConnectorSearchFilter.html
---

# ActionConnectorSearchFilter
<a name="API_ActionConnectorSearchFilter"></a>

A filter used to search for action connectors based on specific criteria.

## Contents
<a name="API_ActionConnectorSearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-ActionConnectorSearchFilter-Name"></a>
The name of the filter attribute (e.g., ACTION\_CONNECTOR\_NAME, ACTION\_CONNECTOR\_TYPE, QUICKSIGHT\_VIEWER\_OR\_OWNER).
Type: String
Length Constraints: Minimum length of 1.
Valid Values: `ACTION_CONNECTOR_NAME | ACTION_CONNECTOR_TYPE | QUICKSIGHT_OWNER | QUICKSIGHT_VIEWER_OR_OWNER | DIRECT_QUICKSIGHT_SOLE_OWNER | DIRECT_QUICKSIGHT_OWNER | DIRECT_QUICKSIGHT_VIEWER_OR_OWNER`
Required: Yes

 ** Operator **   <a name="QS-Type-ActionConnectorSearchFilter-Operator"></a>
The comparison operator to use for the filter (e.g., StringEquals, StringLike).
Type: String
Valid Values: `StringEquals | StringLike`
Required: Yes

 ** Value **   <a name="QS-Type-ActionConnectorSearchFilter-Value"></a>
The value to compare against using the specified operator.
Type: String
Required: Yes

## See Also
<a name="API_ActionConnectorSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ActionConnectorSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ActionConnectorSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ActionConnectorSearchFilter)

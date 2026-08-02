---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DestinationTable.html
---

# DestinationTable
<a name="API_DestinationTable"></a>

Defines a destination table in data preparation that receives the final transformed data.

## Contents
<a name="API_DestinationTable_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alias **   <a name="QS-Type-DestinationTable-Alias"></a>
Alias for the destination table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** Source **   <a name="QS-Type-DestinationTable-Source"></a>
The source configuration that specifies which transform operation provides data to this destination table.
Type: [DestinationTableSource](API_DestinationTableSource.md) object
Required: Yes

## See Also
<a name="API_DestinationTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DestinationTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DestinationTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DestinationTable)

---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ImportTableOperation.html
---

# ImportTableOperation
<a name="API_ImportTableOperation"></a>

A transform operation that imports data from a source table.

## Contents
<a name="API_ImportTableOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alias **   <a name="QS-Type-ImportTableOperation-Alias"></a>
Alias for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** Source **   <a name="QS-Type-ImportTableOperation-Source"></a>
The source configuration that specifies which source table to import and any column mappings.
Type: [ImportTableOperationSource](API_ImportTableOperationSource.md) object
Required: Yes

## See Also
<a name="API_ImportTableOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ImportTableOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ImportTableOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ImportTableOperation)

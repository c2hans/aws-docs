---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_InheritedAllowedResultReceivers.html
---

# InheritedAllowedResultReceivers
<a name="API_InheritedAllowedResultReceivers"></a>

Contains the inherited allowed result receivers constraint and its sources from parent tables.

## Contents
<a name="API_InheritedAllowedResultReceivers_Contents"></a>

 ** sources **   <a name="API-Type-InheritedAllowedResultReceivers-sources"></a>
The list of parent tables that contribute to this inherited constraint.
Type: Array of [InheritedAllowedResultReceiversSource](API_InheritedAllowedResultReceiversSource.md) objects
Required: Yes

 ** value **   <a name="API-Type-InheritedAllowedResultReceivers-value"></a>
The effective list of AWS account IDs allowed to receive results, inherited from parent tables.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

## See Also
<a name="API_InheritedAllowedResultReceivers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/InheritedAllowedResultReceivers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/InheritedAllowedResultReceivers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/InheritedAllowedResultReceivers)

---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergeOperations.html
---

# MergeOperations
<a name="API_MergeOperations"></a>

Information about the file operation conflicts in a merge operation.

## Contents
<a name="API_MergeOperations_Contents"></a>

 ** destination **   <a name="CodeCommit-Type-MergeOperations-destination"></a>
The operation on a file in the destination of a merge or pull request.
Type: String
Valid Values: `A | M | D`
Required: No

 ** source **   <a name="CodeCommit-Type-MergeOperations-source"></a>
The operation (add, modify, or delete) on a file in the source of a merge or pull request.
Type: String
Valid Values: `A | M | D`
Required: No

## See Also
<a name="API_MergeOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/MergeOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/MergeOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/MergeOperations)

---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ObjectTypes.html
---

# ObjectTypes
<a name="API_ObjectTypes"></a>

Information about the type of an object in a merge operation.

## Contents
<a name="API_ObjectTypes_Contents"></a>

 ** base **   <a name="CodeCommit-Type-ObjectTypes-base"></a>
The type of the object in the base commit of the merge.
Type: String
Valid Values: `FILE | DIRECTORY | GIT_LINK | SYMBOLIC_LINK`
Required: No

 ** destination **   <a name="CodeCommit-Type-ObjectTypes-destination"></a>
The type of the object in the destination branch.
Type: String
Valid Values: `FILE | DIRECTORY | GIT_LINK | SYMBOLIC_LINK`
Required: No

 ** source **   <a name="CodeCommit-Type-ObjectTypes-source"></a>
The type of the object in the source branch.
Type: String
Valid Values: `FILE | DIRECTORY | GIT_LINK | SYMBOLIC_LINK`
Required: No

## See Also
<a name="API_ObjectTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ObjectTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ObjectTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ObjectTypes)

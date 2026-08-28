---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_OperationUnion.html
---

# OperationUnion
<a name="API_OperationUnion"></a>

A union type representing the operation to perform on a construct during a mapping update.

## Contents
<a name="API_OperationUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** delete **   <a name="mgn-Type-OperationUnion-delete"></a>
A delete operation to remove a construct from the mapping.
Type: [DeleteOperation](API_DeleteOperation.md) object
Required: No

 ** merge **   <a name="mgn-Type-OperationUnion-merge"></a>
A merge operation to combine constructs from different segments.
Type: [MergeOperation](API_MergeOperation.md) object
Required: No

 ** split **   <a name="mgn-Type-OperationUnion-split"></a>
A split operation to divide a construct into multiple constructs with specified CIDR blocks.
Type: [SplitOperation](API_SplitOperation.md) object
Required: No

 ** update **   <a name="mgn-Type-OperationUnion-update"></a>
An update operation to modify construct properties.
Type: [UpdateOperation](API_UpdateOperation.md) object
Required: No

## See Also
<a name="API_OperationUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/OperationUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/OperationUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/OperationUnion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

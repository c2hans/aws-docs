---
source_url: https://docs.aws.amazon.com/ebs/latest/APIReference/API_ChangedBlock.html
---

# ChangedBlock
<a name="API_ChangedBlock"></a>

A block of data in an Amazon Elastic Block Store snapshot that is different from another snapshot of the same volume/snapshot lineage.

## Contents
<a name="API_ChangedBlock_Contents"></a>

 ** BlockIndex **   <a name="ebs-Type-ChangedBlock-BlockIndex"></a>
The block index.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** FirstBlockToken **   <a name="ebs-Type-ChangedBlock-FirstBlockToken"></a>
The block token for the block index of the `FirstSnapshotId` specified in the `ListChangedBlocks` operation. This value is absent if the first snapshot does not have the changed block that is on the second snapshot.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9+/=]+$`
Required: No

 ** SecondBlockToken **   <a name="ebs-Type-ChangedBlock-SecondBlockToken"></a>
The block token for the block index of the `SecondSnapshotId` specified in the `ListChangedBlocks` operation.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9+/=]+$`
Required: No

## See Also
<a name="API_ChangedBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ebs-2019-11-02/ChangedBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ebs-2019-11-02/ChangedBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ebs-2019-11-02/ChangedBlock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Block Store. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ebs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

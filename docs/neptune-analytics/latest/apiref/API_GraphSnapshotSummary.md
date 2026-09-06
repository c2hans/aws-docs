---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GraphSnapshotSummary.html
---

# GraphSnapshotSummary
<a name="API_GraphSnapshotSummary"></a>

Details about a graph snapshot.

## Contents
<a name="API_GraphSnapshotSummary_Contents"></a>

 ** arn **   <a name="neptunegraph-Type-GraphSnapshotSummary-arn"></a>
The ARN of the graph snapshot.
Type: String
Required: Yes

 ** id **   <a name="neptunegraph-Type-GraphSnapshotSummary-id"></a>
The unique identifier of the graph snapshot.
Type: String
Pattern: `gs-[a-z0-9]{10}`
Required: Yes

 ** name **   <a name="neptunegraph-Type-GraphSnapshotSummary-name"></a>
The snapshot name. For example: `my-snapshot-1`.
The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!gs-)[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: Yes

 ** kmsKeyIdentifier **   <a name="neptunegraph-Type-GraphSnapshotSummary-kmsKeyIdentifier"></a>
The ID of the KMS key used to encrypt and decrypt the snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
Required: No

 ** snapshotCreateTime **   <a name="neptunegraph-Type-GraphSnapshotSummary-snapshotCreateTime"></a>
The time when the snapshot was created.
Type: Timestamp
Required: No

 ** sourceGraphId **   <a name="neptunegraph-Type-GraphSnapshotSummary-sourceGraphId"></a>
The graph identifier for the graph for which a snapshot is to be created.
Type: String
Pattern: `g-[a-z0-9]{10}`
Required: No

 ** status **   <a name="neptunegraph-Type-GraphSnapshotSummary-status"></a>
The status of the graph snapshot.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | FAILED`
Required: No

## See Also
<a name="API_GraphSnapshotSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/GraphSnapshotSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/GraphSnapshotSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/GraphSnapshotSummary)

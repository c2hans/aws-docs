---
source_url: https://docs.aws.amazon.com/directoryservice/latest/devguide/API_SnapshotLimits.html
---

# SnapshotLimits
<a name="API_SnapshotLimits"></a>

Contains manual snapshot limit information for a directory.

## Contents
<a name="API_SnapshotLimits_Contents"></a>

 ** ManualSnapshotsCurrentCount **   <a name="DirectoryService-Type-SnapshotLimits-ManualSnapshotsCurrentCount"></a>
The current number of manual snapshots of the directory.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ManualSnapshotsLimit **   <a name="DirectoryService-Type-SnapshotLimits-ManualSnapshotsLimit"></a>
The maximum number of manual snapshots allowed.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ManualSnapshotsLimitReached **   <a name="DirectoryService-Type-SnapshotLimits-ManualSnapshotsLimitReached"></a>
Indicates if the manual snapshot limit has been reached.
Type: Boolean
Required: No

## See Also
<a name="API_SnapshotLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/SnapshotLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/SnapshotLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/SnapshotLimits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

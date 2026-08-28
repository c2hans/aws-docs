---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisteredUserSnapshotJobResult.html
---

# RegisteredUserSnapshotJobResult
<a name="API_RegisteredUserSnapshotJobResult"></a>

A structure that contains information about files that are requested for registered user during a `StartDashboardSnapshotJob` API call.

## Contents
<a name="API_RegisteredUserSnapshotJobResult_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FileGroups **   <a name="QS-Type-RegisteredUserSnapshotJobResult-FileGroups"></a>
A list of `SnapshotJobResultFileGroup` objects that contain information on the files that are requested for registered user during a `StartDashboardSnapshotJob` API call. If the job succeeds, these objects contain the location where the snapshot artifacts are stored. If the job fails, the objects contain information about the error that caused the job to fail.
Type: Array of [SnapshotJobResultFileGroup](API_SnapshotJobResultFileGroup.md) objects
Required: No

## See Also
<a name="API_RegisteredUserSnapshotJobResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RegisteredUserSnapshotJobResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RegisteredUserSnapshotJobResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RegisteredUserSnapshotJobResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

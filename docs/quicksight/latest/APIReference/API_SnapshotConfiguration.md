---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SnapshotConfiguration.html
---

# SnapshotConfiguration
<a name="API_SnapshotConfiguration"></a>

Describes the configuration of the dashboard snapshot.

## Contents
<a name="API_SnapshotConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FileGroups **   <a name="QS-Type-SnapshotConfiguration-FileGroups"></a>
A list of `SnapshotJobResultFileGroup` objects that contain information about the snapshot that is generated. This list can hold a maximum of 6 `FileGroup` configurations.
Type: Array of [SnapshotFileGroup](API_SnapshotFileGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 7 items.
Required: Yes

 ** DestinationConfiguration **   <a name="QS-Type-SnapshotConfiguration-DestinationConfiguration"></a>
A structure that contains information on the Amazon S3 bucket that the generated snapshot is stored in.
Type: [SnapshotDestinationConfiguration](API_SnapshotDestinationConfiguration.md) object
Required: No

 ** Parameters **   <a name="QS-Type-SnapshotConfiguration-Parameters"></a>
A list of Quick Sight parameters and the list's override values.
Type: [Parameters](API_Parameters.md) object
Required: No

## See Also
<a name="API_SnapshotConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SnapshotConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SnapshotConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SnapshotConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

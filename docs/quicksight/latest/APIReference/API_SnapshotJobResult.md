---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SnapshotJobResult.html
---

# SnapshotJobResult
<a name="API_SnapshotJobResult"></a>

An object that provides information on the result of a snapshot job. This object provides information about the job, the job status, and the location of the generated file.

## Contents
<a name="API_SnapshotJobResult_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnonymousUsers **   <a name="QS-Type-SnapshotJobResult-AnonymousUsers"></a>
 A list of `AnonymousUserSnapshotJobResult` objects that contain information on anonymous users and their user configurations. This data provided by you when you make a `StartDashboardSnapshotJob` API call.
Type: Array of [AnonymousUserSnapshotJobResult](API_AnonymousUserSnapshotJobResult.md) objects
Required: No

 ** RegisteredUsers **   <a name="QS-Type-SnapshotJobResult-RegisteredUsers"></a>
A list of `RegisteredUserSnapshotJobResult` objects that contain information about files that are requested for registered user during a `StartDashboardSnapshotJob` API call.
Type: Array of [RegisteredUserSnapshotJobResult](API_RegisteredUserSnapshotJobResult.md) objects
Required: No

## See Also
<a name="API_SnapshotJobResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SnapshotJobResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SnapshotJobResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SnapshotJobResult)

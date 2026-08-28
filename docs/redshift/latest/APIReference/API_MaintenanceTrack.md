---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_MaintenanceTrack.html
---

# MaintenanceTrack
<a name="API_MaintenanceTrack"></a>

Defines a maintenance track that determines which Amazon Redshift version to apply during a maintenance window. If the value for `MaintenanceTrack` is `current`, the cluster is updated to the most recently certified maintenance release. If the value is `trailing`, the cluster is updated to the previously certified maintenance release.

## Contents
<a name="API_MaintenanceTrack_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DatabaseVersion **
The version number for the cluster release.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** MaintenanceTrackName **
The name of the maintenance track. Possible values are `current` and `trailing`.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** UpdateTargets.UpdateTarget.N **
An array of [UpdateTarget](API_UpdateTarget.md) objects to update with the maintenance track.
Type: Array of [UpdateTarget](API_UpdateTarget.md) objects
Required: No

## See Also
<a name="API_MaintenanceTrack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/MaintenanceTrack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/MaintenanceTrack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/MaintenanceTrack)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

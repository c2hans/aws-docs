---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ClusterDetails.html
---

# ClusterDetails
<a name="API_ClusterDetails"></a>

Details about the task or pod in the cluster.

## Contents
<a name="API_ClusterDetails_Contents"></a>

 ** clusterMetadata **   <a name="inspector2-Type-ClusterDetails-clusterMetadata"></a>
The metadata for a cluster.
Type: [ClusterMetadata](API_ClusterMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** lastInUse **   <a name="inspector2-Type-ClusterDetails-lastInUse"></a>
The last timestamp when Amazon Inspector recorded the image in use in the task or pod in the cluster.
Type: Timestamp
Required: Yes

 ** runningUnitCount **   <a name="inspector2-Type-ClusterDetails-runningUnitCount"></a>
The number of tasks or pods where an image was running on the cluster.
Type: Long
Required: No

 ** stoppedUnitCount **   <a name="inspector2-Type-ClusterDetails-stoppedUnitCount"></a>
The number of tasks or pods where an image was stopped on the cluster in the last 24 hours.
Type: Long
Required: No

## See Also
<a name="API_ClusterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ClusterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ClusterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ClusterDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

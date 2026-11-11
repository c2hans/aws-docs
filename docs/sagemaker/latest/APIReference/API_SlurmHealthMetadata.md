---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SlurmHealthMetadata.html
---

# SlurmHealthMetadata
<a name="API_SlurmHealthMetadata"></a>

Metadata information about the health of a Slurm component on the controller node of a HyperPod cluster.

## Contents
<a name="API_SlurmHealthMetadata_Contents"></a>

 ** Component **   <a name="sagemaker-Type-SlurmHealthMetadata-Component"></a>
The Slurm component that the health information describes. The valid value is `Slurmdbd`, the Slurm accounting daemon.
Type: String
Valid Values: `Slurmdbd`
Required: Yes

 ** Status **   <a name="sagemaker-Type-SlurmHealthMetadata-Status"></a>
The health of the component. Valid values are `Healthy` and `Unhealthy`.
Type: String
Valid Values: `Healthy | Unhealthy`
Required: Yes

 ** Reason **   <a name="sagemaker-Type-SlurmHealthMetadata-Reason"></a>
The reason the component is unhealthy. Valid values:
+  `DaemonDown`: The daemon is not running, so job accounting records are not being written.
+  `DaemonDisabled`: The daemon is running and its accounting database is responding, but the daemon is not enabled to start automatically. Job accounting stops the next time the controller node restarts.
+  `DbUnreachable`: The daemon is running, but its accounting database did not respond. Job accounting records might not be written.
This field is omitted when the component is healthy.
Type: String
Valid Values: `DaemonDown | DaemonDisabled | DbUnreachable`
Required: No

## See Also
<a name="API_SlurmHealthMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SlurmHealthMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SlurmHealthMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SlurmHealthMetadata)

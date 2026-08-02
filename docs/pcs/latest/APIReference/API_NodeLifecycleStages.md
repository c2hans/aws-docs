---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_NodeLifecycleStages.html
---

# NodeLifecycleStages
<a name="API_NodeLifecycleStages"></a>

The stages of a compute node's lifecycle where you can configure scripts to run.

## Contents
<a name="API_NodeLifecycleStages_Contents"></a>

 ** nodeBootstrapped **   <a name="PCS-Type-NodeLifecycleStages-nodeBootstrapped"></a>
The scripts to run after AWS PCS finishes setting up the compute node and before the Slurm daemon (`slurmd`) starts. Use this stage for tasks that must complete before the node accepts jobs, such as mounting shared storage, configuring networking, or installing software packages.
Type: Array of [NodeLifecycleScript](API_NodeLifecycleScript.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** nodeReady **   <a name="PCS-Type-NodeLifecycleStages-nodeReady"></a>
The scripts to run after the Slurm daemon (`slurmd`) starts and the compute node registers with the Slurm controller. Use this stage for tasks that require Slurm to be running, such as running Slurm commands.
Type: Array of [NodeLifecycleScript](API_NodeLifecycleScript.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

## See Also
<a name="API_NodeLifecycleStages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/NodeLifecycleStages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/NodeLifecycleStages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/NodeLifecycleStages)

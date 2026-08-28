---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_SlurmCustomSetting.html
---

# SlurmCustomSetting
<a name="API_SlurmCustomSetting"></a>

Additional settings that directly map to Slurm settings.

**Important**
 AWS PCS supports a subset of Slurm settings. For more information, see [Configuring custom Slurm settings in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings.html) in the * AWS PCS User Guide*.

## Contents
<a name="API_SlurmCustomSetting_Contents"></a>

 ** parameterName **   <a name="PCS-Type-SlurmCustomSetting-parameterName"></a>
 AWS PCS supports custom Slurm settings for clusters, compute node groups, and queues. For more information, see [Configuring custom Slurm settings in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings.html) in the * AWS PCS User Guide*.
Type: String
Required: Yes

 ** parameterValue **   <a name="PCS-Type-SlurmCustomSetting-parameterValue"></a>
The values for the configured Slurm settings.
Type: String
Required: Yes

## See Also
<a name="API_SlurmCustomSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/SlurmCustomSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/SlurmCustomSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/SlurmCustomSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

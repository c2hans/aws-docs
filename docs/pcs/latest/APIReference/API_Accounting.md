---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_Accounting.html
---

# Accounting
<a name="API_Accounting"></a>

The accounting configuration includes configurable settings for Slurm accounting. It's a property of the **ClusterSlurmConfiguration** object.

## Contents
<a name="API_Accounting_Contents"></a>

 ** mode **   <a name="PCS-Type-Accounting-mode"></a>
The default value for `mode` is `NONE`. A value of `STANDARD` means Slurm accounting is enabled.
Type: String
Valid Values: `STANDARD | NONE`
Required: Yes

 ** defaultPurgeTimeInDays **   <a name="PCS-Type-Accounting-defaultPurgeTimeInDays"></a>
The default value for all purge settings for `slurmdbd.conf`. For more information, see the [slurmdbd.conf documentation at SchedMD](https://slurm.schedmd.com/slurmdbd.conf.html).
The default value for `defaultPurgeTimeInDays` is `-1`.
A value of `-1` means there is no purge time and records persist as long as the cluster exists.
 `0` isn't a valid value.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 10000.
Required: No

## See Also
<a name="API_Accounting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/Accounting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/Accounting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/Accounting)

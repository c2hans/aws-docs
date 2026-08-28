---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateAccountingRequest.html
---

# UpdateAccountingRequest
<a name="API_UpdateAccountingRequest"></a>

The accounting configuration includes configurable settings for Slurm accounting.

## Contents
<a name="API_UpdateAccountingRequest_Contents"></a>

 ** defaultPurgeTimeInDays **   <a name="PCS-Type-UpdateAccountingRequest-defaultPurgeTimeInDays"></a>
The default value for all purge settings for `slurmdbd.conf`. For more information, see the [slurmdbd.conf documentation at SchedMD](https://slurm.schedmd.com/slurmdbd.conf.html).
The default value for `defaultPurgeTimeInDays` is `-1`.
A value of `-1` means there is no purge time and records persist as long as the cluster exists.
 `0` isn't a valid value.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 10000.
Required: No

 ** mode **   <a name="PCS-Type-UpdateAccountingRequest-mode"></a>
The default value for `mode` is `NONE`. A value of `STANDARD` means Slurm accounting is enabled.
Type: String
Valid Values: `STANDARD | NONE`
Required: No

## See Also
<a name="API_UpdateAccountingRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/UpdateAccountingRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/UpdateAccountingRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/UpdateAccountingRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

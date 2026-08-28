---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_PatchSummary.html
---

# PatchSummary
<a name="API_PatchSummary"></a>

Provides an overview of the patch compliance status for an instance against a selected compliance standard.

## Contents
<a name="API_PatchSummary_Contents"></a>

 ** Id **   <a name="securityhub-Type-PatchSummary-Id"></a>
The identifier of the compliance standard that was used to determine the patch compliance status.
Length Constraints: Minimum length of 1. Maximum length of 256.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** FailedCount **   <a name="securityhub-Type-PatchSummary-FailedCount"></a>
The number of patches from the compliance standard that failed to install.
The value can be an integer from `0` to `100000`.
Type: Integer
Required: No

 ** InstalledCount **   <a name="securityhub-Type-PatchSummary-InstalledCount"></a>
The number of patches from the compliance standard that were installed successfully.
The value can be an integer from `0` to `100000`.
Type: Integer
Required: No

 ** InstalledOtherCount **   <a name="securityhub-Type-PatchSummary-InstalledOtherCount"></a>
The number of installed patches that are not part of the compliance standard.
The value can be an integer from `0` to `100000`.
Type: Integer
Required: No

 ** InstalledPendingReboot **   <a name="securityhub-Type-PatchSummary-InstalledPendingReboot"></a>
The number of patches that were applied, but that require the instance to be rebooted in order to be marked as installed.
The value can be an integer from `0` to `100000`.
Type: Integer
Required: No

 ** InstalledRejectedCount **   <a name="securityhub-Type-PatchSummary-InstalledRejectedCount"></a>
The number of patches that are installed but are also on a list of patches that the customer rejected.
The value can be an integer from `0` to `100000`.
Type: Integer
Required: No

 ** MissingCount **   <a name="securityhub-Type-PatchSummary-MissingCount"></a>
The number of patches that are part of the compliance standard but are not installed. The count includes patches that failed to install.
The value can be an integer from `0` to `100000`.
Type: Integer
Required: No

 ** Operation **   <a name="securityhub-Type-PatchSummary-Operation"></a>
The type of patch operation performed. For Patch Manager, the values are `SCAN` and `INSTALL`.
Length Constraints: Minimum length of 1. Maximum length of 256.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OperationEndTime **   <a name="securityhub-Type-PatchSummary-OperationEndTime"></a>
Indicates when the operation completed.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** OperationStartTime **   <a name="securityhub-Type-PatchSummary-OperationStartTime"></a>
Indicates when the operation started.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** RebootOption **   <a name="securityhub-Type-PatchSummary-RebootOption"></a>
The reboot option specified for the instance.
Length Constraints: Minimum length of 1. Maximum length of 256.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_PatchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/PatchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/PatchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/PatchSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

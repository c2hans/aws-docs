---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_Exclusions.html
---

# Exclusions
<a name="API_Exclusions"></a>

 **[Default policies only]** Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.

## Contents
<a name="API_Exclusions_Contents"></a>

 ** ExcludeBootVolumes **   <a name="dlm-Type-Exclusions-ExcludeBootVolumes"></a>
 **[Default policies for EBS snapshots only]** Indicates whether to exclude volumes that are attached to instances as the boot volume. If you exclude boot volumes, only volumes attached as data (non-boot) volumes will be backed up by the policy. To exclude boot volumes, specify `true`.
Type: Boolean
Required: No

 ** ExcludeTags **   <a name="dlm-Type-Exclusions-ExcludeTags"></a>
 **[Default policies for EBS-backed AMIs only]** Specifies whether to exclude volumes that have specific tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** ExcludeVolumeTypes **   <a name="dlm-Type-Exclusions-ExcludeVolumeTypes"></a>
 **[Default policies for EBS snapshots only]** Specifies the volume types to exclude. Volumes of the specified types will not be targeted by the policy.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 6 items.
Required: No

## See Also
<a name="API_Exclusions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/Exclusions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/Exclusions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/Exclusions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

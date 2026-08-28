---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteVolumeOntapResponse.html
---

# DeleteVolumeOntapResponse
<a name="API_DeleteVolumeOntapResponse"></a>

The response object for the Amazon FSx for NetApp ONTAP volume being deleted in the `DeleteVolume` operation.

## Contents
<a name="API_DeleteVolumeOntapResponse_Contents"></a>

 ** FinalBackupId **   <a name="FSx-Type-DeleteVolumeOntapResponse-FinalBackupId"></a>
The ID of the source backup. Specifies the backup that you are copying.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 128.
Pattern: `^(backup-[0-9a-f]{8,})$`
Required: No

 ** FinalBackupTags **   <a name="FSx-Type-DeleteVolumeOntapResponse-FinalBackupTags"></a>
A list of `Tag` values, with a maximum of 50 elements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_DeleteVolumeOntapResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteVolumeOntapResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteVolumeOntapResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteVolumeOntapResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

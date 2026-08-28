---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_VmwareTag.html
---

# VmwareTag
<a name="API_VmwareTag"></a>

A VMware tag is a tag attached to a specific virtual machine. A [tag](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_Tag.html) is a key-value pair you can use to manage, filter, and search for your resources.

The content of VMware tags can be matched to AWS tags.

## Contents
<a name="API_VmwareTag_Contents"></a>

 ** VmwareCategory **   <a name="bgw-Type-VmwareTag-VmwareCategory"></a>
The is the category of VMware.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: No

 ** VmwareTagDescription **   <a name="bgw-Type-VmwareTag-VmwareTagDescription"></a>
This is a user-defined description of a VMware tag.
Type: String
Required: No

 ** VmwareTagName **   <a name="bgw-Type-VmwareTag-VmwareTagName"></a>
This is the user-defined name of a VMware tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: No

## See Also
<a name="API_VmwareTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/VmwareTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/VmwareTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/VmwareTag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Backup gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bgw` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

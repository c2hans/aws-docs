---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_VmwareToAwsTagMapping.html
---

# VmwareToAwsTagMapping
<a name="API_VmwareToAwsTagMapping"></a>

This displays the mapping of VMware tags to the corresponding AWS tags.

## Contents
<a name="API_VmwareToAwsTagMapping_Contents"></a>

 ** AwsTagKey **   <a name="bgw-Type-VmwareToAwsTagMapping-AwsTagKey"></a>
The key part of the AWS tag's key-value pair.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

 ** AwsTagValue **   <a name="bgw-Type-VmwareToAwsTagMapping-AwsTagValue"></a>
The value part of the AWS tag's key-value pair.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[^\x00]*`
Required: Yes

 ** VmwareCategory **   <a name="bgw-Type-VmwareToAwsTagMapping-VmwareCategory"></a>
The is the category of VMware.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** VmwareTagName **   <a name="bgw-Type-VmwareToAwsTagMapping-VmwareTagName"></a>
This is the user-defined name of a VMware tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

## See Also
<a name="API_VmwareToAwsTagMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/VmwareToAwsTagMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/VmwareToAwsTagMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/VmwareToAwsTagMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Backup gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bgw` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

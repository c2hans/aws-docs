---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DiskInfo.html
---

# DiskInfo
<a name="API_DiskInfo"></a>

Describes a disk.

## Contents
<a name="API_DiskInfo_Contents"></a>

 ** isSystemDisk **   <a name="Lightsail-Type-DiskInfo-isSystemDisk"></a>
A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
Type: Boolean
Required: No

 ** name **   <a name="Lightsail-Type-DiskInfo-name"></a>
The disk name.
Type: String
Required: No

 ** path **   <a name="Lightsail-Type-DiskInfo-path"></a>
The disk path.
Type: String
Pattern: `.*\S.*`
Required: No

 ** sizeInGb **   <a name="Lightsail-Type-DiskInfo-sizeInGb"></a>
The size of the disk in GB (`32`).
Type: Integer
Required: No

## See Also
<a name="API_DiskInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DiskInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DiskInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DiskInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DiskMap.html
---

# DiskMap
<a name="API_DiskMap"></a>

Describes a block storage disk mapping.

## Contents
<a name="API_DiskMap_Contents"></a>

 ** newDiskName **   <a name="Lightsail-Type-DiskMap-newDiskName"></a>
The new disk name (`my-new-disk`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** originalDiskPath **   <a name="Lightsail-Type-DiskMap-originalDiskPath"></a>
The original disk path exposed to the instance (for example, `/dev/sdh`).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_DiskMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DiskMap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DiskMap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DiskMap)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentLatestVersion.html
---

# ComponentLatestVersion
<a name="API_ComponentLatestVersion"></a>

Contains information about the latest version of a component.

## Contents
<a name="API_ComponentLatestVersion_Contents"></a>

 ** arn **   <a name="greengrassv2-Type-ComponentLatestVersion-arn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the component version.
Type: String
Pattern: `arn:[^:]*:greengrass:[^:]*:(aws|[0-9]+):components:[^:]+:versions:[^:]+`
Required: No

 ** componentVersion **   <a name="greengrassv2-Type-ComponentLatestVersion-componentVersion"></a>
The version of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** creationTimestamp **   <a name="greengrassv2-Type-ComponentLatestVersion-creationTimestamp"></a>
The time at which the component was created, expressed in ISO 8601 format.
Type: Timestamp
Required: No

 ** description **   <a name="greengrassv2-Type-ComponentLatestVersion-description"></a>
The description of the component version.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** platforms **   <a name="greengrassv2-Type-ComponentLatestVersion-platforms"></a>
The platforms that the component version supports.
Type: Array of [ComponentPlatform](API_ComponentPlatform.md) objects
Required: No

 ** publisher **   <a name="greengrassv2-Type-ComponentLatestVersion-publisher"></a>
The publisher of the component version.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ComponentLatestVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ComponentLatestVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ComponentLatestVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ComponentLatestVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

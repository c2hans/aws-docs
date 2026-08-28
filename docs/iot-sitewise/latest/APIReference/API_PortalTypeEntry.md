---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PortalTypeEntry.html
---

# PortalTypeEntry
<a name="API_PortalTypeEntry"></a>

The configuration entry associated with the specific portal type. The `portalTypeConfiguration` is a map of the `portalTypeKey` to the `PortalTypeEntry`.

## Contents
<a name="API_PortalTypeEntry_Contents"></a>

 ** portalTools **   <a name="iotsitewise-Type-PortalTypeEntry-portalTools"></a>
The array of tools associated with the specified portal type. The possible values are `ASSISTANT` and `DASHBOARD`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## See Also
<a name="API_PortalTypeEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PortalTypeEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PortalTypeEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PortalTypeEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

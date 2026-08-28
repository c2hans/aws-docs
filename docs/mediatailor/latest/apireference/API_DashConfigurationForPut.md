---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DashConfigurationForPut.html
---

# DashConfigurationForPut
<a name="API_DashConfigurationForPut"></a>

The configuration for DASH PUT operations.

## Contents
<a name="API_DashConfigurationForPut_Contents"></a>

 ** MpdLocation **   <a name="mediatailor-Type-DashConfigurationForPut-MpdLocation"></a>
The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are `DISABLED` and `EMT_DEFAULT`. The `EMT_DEFAULT` setting enables the inclusion of the tag and is the default value.
Type: String
Required: No

 ** OriginManifestType **   <a name="mediatailor-Type-DashConfigurationForPut-OriginManifestType"></a>
The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to `SINGLE_PERIOD`. The default setting is `MULTI_PERIOD`. For multi-period manifests, omit this setting or set it to `MULTI_PERIOD`.
Type: String
Valid Values: `SINGLE_PERIOD | MULTI_PERIOD`
Required: No

## See Also
<a name="API_DashConfigurationForPut_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DashConfigurationForPut)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DashConfigurationForPut)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DashConfigurationForPut)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

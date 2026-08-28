---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ScteDash.html
---

# ScteDash
<a name="API_ScteDash"></a>

The SCTE configuration.

## Contents
<a name="API_ScteDash_Contents"></a>

 ** AdMarkerDash **   <a name="mediapackage-Type-ScteDash-AdMarkerDash"></a>
Choose how ad markers are included in the packaged content. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output.
Value description:
+  `Binary` - The SCTE-35 marker is expressed as a hex-string (Base64 string) rather than full XML.
+  `XML` - The SCTE marker is expressed fully in XML.
Type: String
Valid Values: `BINARY | XML`
Required: No

 ** ScteInManifests **   <a name="mediapackage-Type-ScteDash-ScteInManifests"></a>
Controls which SCTE-35 events appear in DASH manifests. `ALL` includes all non-implicit SCTE-35 events. `MATCHES_FILTER` includes only events whose type matches the configured `ScteFilter`.
If you don't specify a value, the default is `ALL`.
Type: String
Valid Values: `ALL | MATCHES_FILTER`
Required: No

## See Also
<a name="API_ScteDash_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ScteDash)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ScteDash)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ScteDash)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

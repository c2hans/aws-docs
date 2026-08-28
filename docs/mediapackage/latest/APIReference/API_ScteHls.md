---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ScteHls.html
---

# ScteHls
<a name="API_ScteHls"></a>

The SCTE configuration.

## Contents
<a name="API_ScteHls_Contents"></a>

 ** AdMarkerHls **   <a name="mediapackage-Type-ScteHls-AdMarkerHls"></a>
Ad markers indicate when ads should be inserted during playback. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output. Choose what you want MediaPackage to do with the ad markers.
Value description:
+ SCTE35\_ENHANCED - Generate industry-standard CUE tag ad markers in HLS manifests based on SCTE-35 input messages from the input stream.
+ DATERANGE - Insert EXT-X-DATERANGE tags to signal ad and program transition events in TS and CMAF manifests. If you use DATERANGE, you must set a programDateTimeIntervalSeconds value of 1 or higher. To learn more about DATERANGE, see [SCTE-35 Ad Marker EXT-X-DATERANGE](http://docs.aws.amazon.com/mediapackage/latest/ug/scte-35-ad-marker-ext-x-daterange.html).
Type: String
Valid Values: `DATERANGE | SCTE35_ENHANCED`
Required: No

 ** ScteInManifests **   <a name="mediapackage-Type-ScteHls-ScteInManifests"></a>
Controls which SCTE-35 events appear in HLS manifests. `ALL` includes all non-implicit SCTE-35 events. `MATCHES_FILTER` includes only events whose type matches the configured `ScteFilter`.
If you don't specify a value, the default is `ALL`.
Type: String
Valid Values: `ALL | MATCHES_FILTER`
Required: No

## See Also
<a name="API_ScteHls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ScteHls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ScteHls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ScteHls)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

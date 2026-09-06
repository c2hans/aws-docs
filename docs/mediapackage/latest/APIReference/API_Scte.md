---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_Scte.html
---

# Scte
<a name="API_Scte"></a>

The SCTE configuration.

## Contents
<a name="API_Scte_Contents"></a>

 ** CustomAdTypes **   <a name="mediapackage-Type-Scte-CustomAdTypes"></a>
A list of additional non-Ad SCTE-35 event types to treat as advertisements. When configured, events matching these types produce ad markers (such as `SCTE35-OUT` and `SCTE35-IN` in HLS DATERANGE tags) in manifests.
Valid values: `PROGRAM` \| `CHAPTER` \| `UNSCHEDULED_EVENT` \| `ALTERNATE_CONTENT_OPPORTUNITY` \| `NETWORK`
If you don't specify any values, the default is empty (only default ad types are used).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Valid Values: `PROGRAM | CHAPTER | UNSCHEDULED_EVENT | ALTERNATE_CONTENT_OPPORTUNITY | NETWORK`
Required: No

 ** ScteFilter **   <a name="mediapackage-Type-Scte-ScteFilter"></a>
The SCTE-35 message types that you want to be treated as ad markers in the output.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Valid Values: `SPLICE_INSERT | BREAK | PROVIDER_ADVERTISEMENT | DISTRIBUTOR_ADVERTISEMENT | PROVIDER_PLACEMENT_OPPORTUNITY | DISTRIBUTOR_PLACEMENT_OPPORTUNITY | PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY | DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY | PROGRAM | CHAPTER | UNSCHEDULED_EVENT | ALTERNATE_CONTENT_OPPORTUNITY | NETWORK | PROVIDER_PROMO | DISTRIBUTOR_PROMO | PROVIDER_AD_BLOCK | DISTRIBUTOR_AD_BLOCK | CONTENT_IDENTIFICATION | CALL_AD_SERVER`
Required: No

 ** ScteInSegments **   <a name="mediapackage-Type-Scte-ScteInSegments"></a>
Controls whether SCTE-35 messages are included in segment files.
+ None – SCTE-35 messages are not included in segments (default)
+ All – SCTE-35 messages are embedded in segment data
+ MatchesFilter – SCTE-35 messages which match the ScteFilter are embedded in segment data
 For DASH manifests, when set to `All` or `MatchesFilter`, an `InbandEventStream` tag signals that SCTE messages are present in segments. This setting works independently of manifest ad markers.
Type: String
Valid Values: `NONE | ALL | MATCHES_FILTER`
Required: No

## See Also
<a name="API_Scte_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/Scte)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/Scte)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/Scte)

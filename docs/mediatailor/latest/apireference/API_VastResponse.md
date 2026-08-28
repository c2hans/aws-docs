---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_VastResponse.html
---

# VastResponse
<a name="API_VastResponse"></a>

The settings that control how MediaTailor processes VAST responses from the ad decision server.

## Contents
<a name="API_VastResponse_Contents"></a>

 ** AdSequencingMode **   <a name="mediatailor-Type-VastResponse-AdSequencingMode"></a>
The ad sequencing mode that controls how MediaTailor handles sequenced and standalone ads in VAST responses. `FOLLOW_AD_SEQUENCE` inserts sequenced ads in increasing order for both live and VOD workflows, using standalone ads only as replacements when a sequenced ad fails. `FOLLOW_AD_SEQUENCE_ONLY_LIVE` enables ad sequencing for live workflows only. `FOLLOW_AD_SEQUENCE_ONLY_VOD` enables ad sequencing for VOD workflows only. `IGNORE_AD_SEQUENCE` inserts ads in the order they appear in the VAST response, regardless of sequence attributes. The default behavior is `IGNORE_AD_SEQUENCE`.
Type: String
Valid Values: `FOLLOW_AD_SEQUENCE | IGNORE_AD_SEQUENCE | FOLLOW_AD_SEQUENCE_ONLY_LIVE | FOLLOW_AD_SEQUENCE_ONLY_VOD`
Required: No

## See Also
<a name="API_VastResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/VastResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/VastResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/VastResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

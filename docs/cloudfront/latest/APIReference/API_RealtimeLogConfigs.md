---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_RealtimeLogConfigs.html
---

# RealtimeLogConfigs
<a name="API_RealtimeLogConfigs"></a>

A list of real-time log configurations.

## Contents
<a name="API_RealtimeLogConfigs_Contents"></a>

 ** IsTruncated **   <a name="cloudfront-Type-RealtimeLogConfigs-IsTruncated"></a>
A flag that indicates whether there are more real-time log configurations than are contained in this list.
Type: Boolean
Required: Yes

 ** Marker **   <a name="cloudfront-Type-RealtimeLogConfigs-Marker"></a>
This parameter indicates where this list of real-time log configurations begins. This list includes real-time log configurations that occur after the marker.
Type: String
Required: Yes

 ** MaxItems **   <a name="cloudfront-Type-RealtimeLogConfigs-MaxItems"></a>
The maximum number of real-time log configurations requested.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-RealtimeLogConfigs-Items"></a>
Contains the list of real-time log configurations.
Type: Array of [RealtimeLogConfig](API_RealtimeLogConfig.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-RealtimeLogConfigs-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing real-time log configurations where you left off.
Type: String
Required: No

## See Also
<a name="API_RealtimeLogConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/RealtimeLogConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/RealtimeLogConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/RealtimeLogConfigs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

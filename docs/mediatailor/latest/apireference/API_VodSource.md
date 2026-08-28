---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_VodSource.html
---

# VodSource
<a name="API_VodSource"></a>

VOD source configuration parameters.

## Contents
<a name="API_VodSource_Contents"></a>

 ** Arn **   <a name="mediatailor-Type-VodSource-Arn"></a>
The ARN for the VOD source.
Type: String
Required: Yes

 ** HttpPackageConfigurations **   <a name="mediatailor-Type-VodSource-HttpPackageConfigurations"></a>
The HTTP package configurations for the VOD source.
Type: Array of [HttpPackageConfiguration](API_HttpPackageConfiguration.md) objects
Required: Yes

 ** SourceLocationName **   <a name="mediatailor-Type-VodSource-SourceLocationName"></a>
The name of the source location that the VOD source is associated with.
Type: String
Required: Yes

 ** VodSourceName **   <a name="mediatailor-Type-VodSource-VodSourceName"></a>
The name of the VOD source.
Type: String
Required: Yes

 ** CreationTime **   <a name="mediatailor-Type-VodSource-CreationTime"></a>
The timestamp that indicates when the VOD source was created.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="mediatailor-Type-VodSource-LastModifiedTime"></a>
The timestamp that indicates when the VOD source was last modified.
Type: Timestamp
Required: No

 ** tags **   <a name="mediatailor-Type-VodSource-tags"></a>
The tags assigned to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

## See Also
<a name="API_VodSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/VodSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/VodSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/VodSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

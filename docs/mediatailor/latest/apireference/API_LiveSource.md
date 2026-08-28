---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_LiveSource.html
---

# LiveSource
<a name="API_LiveSource"></a>

Live source configuration parameters.

## Contents
<a name="API_LiveSource_Contents"></a>

 ** Arn **   <a name="mediatailor-Type-LiveSource-Arn"></a>
The ARN for the live source.
Type: String
Required: Yes

 ** HttpPackageConfigurations **   <a name="mediatailor-Type-LiveSource-HttpPackageConfigurations"></a>
The HTTP package configurations for the live source.
Type: Array of [HttpPackageConfiguration](API_HttpPackageConfiguration.md) objects
Required: Yes

 ** LiveSourceName **   <a name="mediatailor-Type-LiveSource-LiveSourceName"></a>
The name that's used to refer to a live source.
Type: String
Required: Yes

 ** SourceLocationName **   <a name="mediatailor-Type-LiveSource-SourceLocationName"></a>
The name of the source location.
Type: String
Required: Yes

 ** CreationTime **   <a name="mediatailor-Type-LiveSource-CreationTime"></a>
The timestamp that indicates when the live source was created.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="mediatailor-Type-LiveSource-LastModifiedTime"></a>
The timestamp that indicates when the live source was last modified.
Type: Timestamp
Required: No

 ** tags **   <a name="mediatailor-Type-LiveSource-tags"></a>
The tags assigned to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

## See Also
<a name="API_LiveSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/LiveSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/LiveSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/LiveSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

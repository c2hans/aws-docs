---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3AccessPointConfiguration.html
---

# S3AccessPointConfiguration
<a name="API_S3AccessPointConfiguration"></a>

The configuration for an Amazon S3 access point or multi-region access point for the bucket. You can propose up to 10 access points or multi-region access points per bucket. If the proposed Amazon S3 access point configuration is for an existing bucket, the access preview uses the proposed access point configuration in place of the existing access points. To propose an access point without a policy, you can provide an empty string as the access point policy. For more information, see [Creating access points](https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html). For more information about access point policy limits, see [Access points restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points-restrictions-limitations.html).

## Contents
<a name="API_S3AccessPointConfiguration_Contents"></a>

 ** accessPointPolicy **   <a name="accessanalyzer-Type-S3AccessPointConfiguration-accessPointPolicy"></a>
The access point or multi-region access point policy.
Type: String
Required: No

 ** networkOrigin **   <a name="accessanalyzer-Type-S3AccessPointConfiguration-networkOrigin"></a>
The proposed `Internet` and `VpcConfiguration` to apply to this Amazon S3 access point. `VpcConfiguration` does not apply to multi-region access points. If the access preview is for a new resource and neither is specified, the access preview uses `Internet` for the network origin. If the access preview is for an existing resource and neither is specified, the access preview uses the existing network origin.
Type: [NetworkOriginConfiguration](API_NetworkOriginConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** publicAccessBlock **   <a name="accessanalyzer-Type-S3AccessPointConfiguration-publicAccessBlock"></a>
The proposed `S3PublicAccessBlock` configuration to apply to this Amazon S3 access point or multi-region access point.
Type: [S3PublicAccessBlockConfiguration](API_S3PublicAccessBlockConfiguration.md) object
Required: No

## See Also
<a name="API_S3AccessPointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3AccessPointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3AccessPointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3AccessPointConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3ExpressDirectoryAccessPointConfiguration.html
---

# S3ExpressDirectoryAccessPointConfiguration
<a name="API_S3ExpressDirectoryAccessPointConfiguration"></a>

Proposed configuration for an access point attached to an Amazon S3 directory bucket. You can propose up to 10 access points per bucket. If the proposed access point configuration is for an existing Amazon S3 directory bucket, the access preview uses the proposed access point configuration in place of the existing access points. To propose an access point without a policy, you can provide an empty string as the access point policy. For more information about access points for Amazon S3 directory buckets, see [Managing access to directory buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html) in the Amazon Simple Storage Service User Guide.

## Contents
<a name="API_S3ExpressDirectoryAccessPointConfiguration_Contents"></a>

 ** accessPointPolicy **   <a name="accessanalyzer-Type-S3ExpressDirectoryAccessPointConfiguration-accessPointPolicy"></a>
The proposed access point policy for an Amazon S3 directory bucket access point.
Type: String
Required: No

 ** networkOrigin **   <a name="accessanalyzer-Type-S3ExpressDirectoryAccessPointConfiguration-networkOrigin"></a>
The proposed `InternetConfiguration` or `VpcConfiguration` to apply to the Amazon S3 access point. You can make the access point accessible from the internet, or you can specify that all requests made through that access point must originate from a specific virtual private cloud (VPC). You can specify only one type of network configuration. For more information, see [Creating access points](https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html).
Type: [NetworkOriginConfiguration](API_NetworkOriginConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_S3ExpressDirectoryAccessPointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3ExpressDirectoryAccessPointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3ExpressDirectoryAccessPointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3ExpressDirectoryAccessPointConfiguration)

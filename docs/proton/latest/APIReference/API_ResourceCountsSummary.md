---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ResourceCountsSummary.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ResourceCountsSummary
<a name="API_ResourceCountsSummary"></a>

Summary counts of each AWS Proton resource types.

## Contents
<a name="API_ResourceCountsSummary_Contents"></a>

 ** total **   <a name="proton-Type-ResourceCountsSummary-total"></a>
The total number of resources of this type in the AWS account.
Type: Integer
Required: Yes

 ** behindMajor **   <a name="proton-Type-ResourceCountsSummary-behindMajor"></a>
The number of resources of this type in the AWS account that need a major template version update.
Type: Integer
Required: No

 ** behindMinor **   <a name="proton-Type-ResourceCountsSummary-behindMinor"></a>
The number of resources of this type in the AWS account that need a minor template version update.
Type: Integer
Required: No

 ** failed **   <a name="proton-Type-ResourceCountsSummary-failed"></a>
The number of resources of this type in the AWS account that failed to deploy.
Type: Integer
Required: No

 ** upToDate **   <a name="proton-Type-ResourceCountsSummary-upToDate"></a>
The number of resources of this type in the AWS account that are up-to-date with their template.
Type: Integer
Required: No

## See Also
<a name="API_ResourceCountsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ResourceCountsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ResourceCountsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ResourceCountsSummary)

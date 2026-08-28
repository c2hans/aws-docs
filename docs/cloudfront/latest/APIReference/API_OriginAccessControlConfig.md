---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginAccessControlConfig.html
---

# OriginAccessControlConfig
<a name="API_OriginAccessControlConfig"></a>

A CloudFront origin access control configuration.

## Contents
<a name="API_OriginAccessControlConfig_Contents"></a>

 ** Name **   <a name="cloudfront-Type-OriginAccessControlConfig-Name"></a>
A name to identify the origin access control. You can specify up to 64 characters.
Type: String
Required: Yes

 ** OriginAccessControlOriginType **   <a name="cloudfront-Type-OriginAccessControlConfig-OriginAccessControlOriginType"></a>
The type of origin that this origin access control is for.
Type: String
Valid Values: `s3 | mediastore | mediapackagev2 | lambda`
Required: Yes

 ** SigningBehavior **   <a name="cloudfront-Type-OriginAccessControlConfig-SigningBehavior"></a>
Specifies which requests CloudFront signs (adds authentication information to). Specify `always` for the most common use case. For more information, see [origin access control advanced settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#oac-advanced-settings) in the *Amazon CloudFront Developer Guide*.
This field can have one of the following values:
+  `always` – CloudFront signs all origin requests, overwriting the `Authorization` header from the viewer request if one exists.
+  `never` – CloudFront doesn't sign any origin requests. This value turns off origin access control for all origins in all distributions that use this origin access control.
+  `no-override` – If the viewer request doesn't contain the `Authorization` header, then CloudFront signs the origin request. If the viewer request contains the `Authorization` header, then CloudFront doesn't sign the origin request and instead passes along the `Authorization` header from the viewer request. **WARNING: To pass along the `Authorization` header from the viewer request, you *must* add the `Authorization` header to a [cache policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html) for all cache behaviors that use origins associated with this origin access control.**
Type: String
Valid Values: `never | always | no-override`
Required: Yes

 ** SigningProtocol **   <a name="cloudfront-Type-OriginAccessControlConfig-SigningProtocol"></a>
The signing protocol of the origin access control, which determines how CloudFront signs (authenticates) requests. The only valid value is `sigv4`.
Type: String
Valid Values: `sigv4`
Required: Yes

 ** Description **   <a name="cloudfront-Type-OriginAccessControlConfig-Description"></a>
A description of the origin access control.
Type: String
Required: No

## See Also
<a name="API_OriginAccessControlConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginAccessControlConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginAccessControlConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginAccessControlConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

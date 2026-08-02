---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ResourceConfiguration.html
---

# ResourceConfiguration
<a name="API_ResourceConfiguration"></a>

Resource configuration for an input source. Provide exactly one field.

## Contents
<a name="API_ResourceConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cfnStackArn **   <a name="ngresiliencehub-Type-ResourceConfiguration-cfnStackArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** designFileS3Url **   <a name="ngresiliencehub-Type-ResourceConfiguration-designFileS3Url"></a>
S3 URL — virtual hosted-style or s3:// URI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `((https://([^/]+)\.s3[^/]*\.[^/]+)|(s3://([^/]+)))/\S{1,2000}`
Required: No

 ** eks **   <a name="ngresiliencehub-Type-ResourceConfiguration-eks"></a>
The Amazon EKS configuration for resource discovery.
Type: [EksSource](API_EksSource.md) object
Required: No

 ** resourceTags **   <a name="ngresiliencehub-Type-ResourceConfiguration-resourceTags"></a>
The resource tags for tag-based resource discovery.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** tfStateFileUrl **   <a name="ngresiliencehub-Type-ResourceConfiguration-tfStateFileUrl"></a>
S3 URL — virtual hosted-style or s3:// URI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `((https://([^/]+)\.s3[^/]*\.[^/]+)|(s3://([^/]+)))/\S{1,2000}`
Required: No

## See Also
<a name="API_ResourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ResourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ResourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ResourceConfiguration)

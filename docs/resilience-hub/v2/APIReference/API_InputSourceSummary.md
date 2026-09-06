---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_InputSourceSummary.html
---

# InputSourceSummary
<a name="API_InputSourceSummary"></a>

Contains summary information about an input source for a service.

## Contents
<a name="API_InputSourceSummary_Contents"></a>

 ** inputSourceId **   <a name="ngresiliencehub-Type-InputSourceSummary-inputSourceId"></a>
The unique identifier of the input source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`
Required: Yes

 ** cfnStackArn **   <a name="ngresiliencehub-Type-InputSourceSummary-cfnStackArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** createdAt **   <a name="ngresiliencehub-Type-InputSourceSummary-createdAt"></a>
The timestamp when the input source was created.
Type: Timestamp
Required: No

 ** designFileS3Url **   <a name="ngresiliencehub-Type-InputSourceSummary-designFileS3Url"></a>
S3 URL — virtual hosted-style or s3:// URI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `((https://([^/]+)\.s3[^/]*\.[^/]+)|(s3://([^/]+)))/\S{1,2000}`
Required: No

 ** eks **   <a name="ngresiliencehub-Type-InputSourceSummary-eks"></a>
The Amazon EKS configuration, if this input source uses EKS.
Type: [EksSource](API_EksSource.md) object
Required: No

 ** resourceTags **   <a name="ngresiliencehub-Type-InputSourceSummary-resourceTags"></a>
The resource tags used for discovery, if this input source uses tags.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** tfStateFileUrl **   <a name="ngresiliencehub-Type-InputSourceSummary-tfStateFileUrl"></a>
S3 URL — virtual hosted-style or s3:// URI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `((https://([^/]+)\.s3[^/]*\.[^/]+)|(s3://([^/]+)))/\S{1,2000}`
Required: No

 ** type **   <a name="ngresiliencehub-Type-InputSourceSummary-type"></a>
The type of the input source.
Type: String
Valid Values: `CFN_STACK | TAGS | EKS | TERRAFORM | DESIGN_FILE | MONITORING`
Required: No

## See Also
<a name="API_InputSourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/InputSourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/InputSourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/InputSourceSummary)

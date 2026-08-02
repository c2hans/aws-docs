---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_SourceCloudProperties.html
---

# SourceCloudProperties
<a name="API_SourceCloudProperties"></a>

Properties of the cloud environment where this Source Server originated from.

## Contents
<a name="API_SourceCloudProperties_Contents"></a>

 ** originAccountID **   <a name="drs-Type-SourceCloudProperties-originAccountID"></a>
AWS Account ID for an EC2-originated Source Server.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** originAvailabilityZone **   <a name="drs-Type-SourceCloudProperties-originAvailabilityZone"></a>
AWS Availability Zone for an EC2-originated Source Server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(us(-gov)?|ap|ca|cn|eu|eusc|sa|af|me|mx|il)-([a-z]{2}-)?(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-[0-9][a-z]`
Required: No

 ** originRegion **   <a name="drs-Type-SourceCloudProperties-originRegion"></a>
AWS Region for an EC2-originated Source Server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(us(-gov)?|ap|ca|cn|eu|eusc|sa|af|me|mx|il)-([a-z]{2}-)?(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-[0-9]`
Required: No

 ** sourceOutpostArn **   <a name="drs-Type-SourceCloudProperties-sourceOutpostArn"></a>
The ARN of the source Outpost
Type: String
Length Constraints: Minimum length of 20. Maximum length of 255.
Pattern: `arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}`
Required: No

## See Also
<a name="API_SourceCloudProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/SourceCloudProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/SourceCloudProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/SourceCloudProperties)

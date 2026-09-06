---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessGroup.html
---

# VerifiedAccessGroup
<a name="API_VerifiedAccessGroup"></a>

Describes a Verified Access group.

## Contents
<a name="API_VerifiedAccessGroup_Contents"></a>

 ** creationTime **
The creation time.
Type: String
Required: No

 ** deletionTime **
The deletion time.
Type: String
Required: No

 ** description **
A description for the AWS Verified Access group.
Type: String
Required: No

 ** lastUpdatedTime **
The last updated time.
Type: String
Required: No

 ** owner **
The AWS account number that owns the group.
Type: String
Required: No

 ** sseSpecification **
The options in use for server side encryption.
Type: [VerifiedAccessSseSpecificationResponse](API_VerifiedAccessSseSpecificationResponse.md) object
Required: No

 ** TagSet.N **
The tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** verifiedAccessGroupArn **
The ARN of the Verified Access group.
Type: String
Required: No

 ** verifiedAccessGroupId **
The ID of the Verified Access group.
Type: String
Required: No

 ** verifiedAccessInstanceId **
The ID of the AWS Verified Access instance.
Type: String
Required: No

## See Also
<a name="API_VerifiedAccessGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessGroup)

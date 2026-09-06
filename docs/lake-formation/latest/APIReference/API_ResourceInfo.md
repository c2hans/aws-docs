---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ResourceInfo.html
---

# ResourceInfo
<a name="API_ResourceInfo"></a>

A structure containing information about an AWS Lake Formation resource.

## Contents
<a name="API_ResourceInfo_Contents"></a>

 ** ExpectedResourceOwnerAccount **   <a name="lakeformation-Type-ResourceInfo-ExpectedResourceOwnerAccount"></a>
The AWS account that owns the AWS Glue tables associated with specific Amazon S3 locations.
Type: String
Pattern: `^\d{12}$`
Required: No

 ** HybridAccessEnabled **   <a name="lakeformation-Type-ResourceInfo-HybridAccessEnabled"></a>
 Indicates whether the data access of tables pointing to the location can be managed by both Lake Formation permissions as well as Amazon S3 bucket policies.
Type: Boolean
Required: No

 ** LastModified **   <a name="lakeformation-Type-ResourceInfo-LastModified"></a>
The date and time the resource was last modified.
Type: Timestamp
Required: No

 ** ResourceArn **   <a name="lakeformation-Type-ResourceInfo-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** RoleArn **   <a name="lakeformation-Type-ResourceInfo-RoleArn"></a>
The IAM role that registered a resource.
Type: String
Pattern: `arn:aws:iam::[0-9]*:role/.*`
Required: No

 ** VerificationStatus **   <a name="lakeformation-Type-ResourceInfo-VerificationStatus"></a>
Indicates whether the registered role has sufficient permissions to access registered Amazon S3 location. Verification Status can be one of the following:
+ VERIFIED - Registered role has sufficient permissions to access registered Amazon S3 location.
+ NOT\_VERIFIED - Registered role does not have sufficient permissions to access registered Amazon S3 location.
+ VERIFICATION\_FAILED - Unable to verify if the registered role can access the registered Amazon S3 location.
Type: String
Valid Values: `VERIFIED | VERIFICATION_FAILED | NOT_VERIFIED`
Required: No

 ** WithFederation **   <a name="lakeformation-Type-ResourceInfo-WithFederation"></a>
Whether or not the resource is a federated resource.
Type: Boolean
Required: No

 ** WithPrivilegedAccess **   <a name="lakeformation-Type-ResourceInfo-WithPrivilegedAccess"></a>
Grants the calling principal the permissions to perform all supported Lake Formation operations on the registered data location.
Type: Boolean
Required: No

## See Also
<a name="API_ResourceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ResourceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ResourceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ResourceInfo)

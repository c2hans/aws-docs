---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_MembershipDatasources.html
---

# MembershipDatasources
<a name="API_MembershipDatasources"></a>

Details on data source packages for members of the behavior graph.

## Contents
<a name="API_MembershipDatasources_Contents"></a>

 ** AccountId **   <a name="detective-Type-MembershipDatasources-AccountId"></a>
The account identifier of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: No

 ** DatasourcePackageIngestHistory **   <a name="detective-Type-MembershipDatasources-DatasourcePackageIngestHistory"></a>
Details on when a data source package was added to a behavior graph.
Type: String to string to [TimestampForCollection](API_TimestampForCollection.md) object map map
Valid Keys: `DETECTIVE_CORE | EKS_AUDIT | ASFF_SECURITYHUB_FINDING`
Valid Keys: `STARTED | STOPPED | DISABLED`
Required: No

 ** GraphArn **   <a name="detective-Type-MembershipDatasources-GraphArn"></a>
The ARN of the organization behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: No

## See Also
<a name="API_MembershipDatasources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/MembershipDatasources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/MembershipDatasources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/MembershipDatasources)

---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_IdentityUsage.html
---

# IdentityUsage
<a name="API_IdentityUsage"></a>

Usage information for the identity.

## Contents
<a name="API_IdentityUsage_Contents"></a>

 ** DatasetCount **   <a name="Cognito-Type-IdentityUsage-DatasetCount"></a>
Number of datasets for the identity.
Type: Integer
Required: No

 ** DataStorage **   <a name="Cognito-Type-IdentityUsage-DataStorage"></a>
Total data storage for this identity.
Type: Long
Required: No

 ** IdentityId **   <a name="Cognito-Type-IdentityUsage-IdentityId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: No

 ** IdentityPoolId **   <a name="Cognito-Type-IdentityUsage-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: No

 ** LastModifiedDate **   <a name="Cognito-Type-IdentityUsage-LastModifiedDate"></a>
Date on which the identity was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_IdentityUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/IdentityUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/IdentityUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/IdentityUsage)

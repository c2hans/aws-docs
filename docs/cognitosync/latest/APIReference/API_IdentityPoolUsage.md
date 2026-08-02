---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_IdentityPoolUsage.html
---

# IdentityPoolUsage
<a name="API_IdentityPoolUsage"></a>

Usage information for the identity pool.

## Contents
<a name="API_IdentityPoolUsage_Contents"></a>

 ** DataStorage **   <a name="Cognito-Type-IdentityPoolUsage-DataStorage"></a>
Data storage information for the identity pool.
Type: Long
Required: No

 ** IdentityPoolId **   <a name="Cognito-Type-IdentityPoolUsage-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: No

 ** LastModifiedDate **   <a name="Cognito-Type-IdentityPoolUsage-LastModifiedDate"></a>
Date on which the identity pool was last modified.
Type: Timestamp
Required: No

 ** SyncSessionsCount **   <a name="Cognito-Type-IdentityPoolUsage-SyncSessionsCount"></a>
Number of sync sessions for the identity pool.
Type: Long
Required: No

## See Also
<a name="API_IdentityPoolUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/IdentityPoolUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/IdentityPoolUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/IdentityPoolUsage)

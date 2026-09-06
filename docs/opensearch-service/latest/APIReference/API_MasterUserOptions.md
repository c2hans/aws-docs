---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_MasterUserOptions.html
---

# MasterUserOptions
<a name="API_MasterUserOptions"></a>

Credentials for the master user for a domain.

## Contents
<a name="API_MasterUserOptions_Contents"></a>

 ** MasterUserARN **   <a name="opensearchservice-Type-MasterUserOptions-MasterUserARN"></a>
Amazon Resource Name (ARN) for the master user. Only specify if `InternalUserDatabaseEnabled` is `false`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** MasterUserName **   <a name="opensearchservice-Type-MasterUserOptions-MasterUserName"></a>
User name for the master user. Only specify if `InternalUserDatabaseEnabled` is `true`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** MasterUserPassword **   <a name="opensearchservice-Type-MasterUserOptions-MasterUserPassword"></a>
Password for the master user. Only specify if `InternalUserDatabaseEnabled` is `true`.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 128.
Pattern: `.*`
Required: No

## See Also
<a name="API_MasterUserOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/MasterUserOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/MasterUserOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/MasterUserOptions)

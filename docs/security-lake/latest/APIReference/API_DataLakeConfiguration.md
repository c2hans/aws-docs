---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeConfiguration.html
---

# DataLakeConfiguration
<a name="API_DataLakeConfiguration"></a>

Provides details of Amazon Security Lake object.

## Contents
<a name="API_DataLakeConfiguration_Contents"></a>

 ** region **   <a name="securitylake-Type-DataLakeConfiguration-region"></a>
The AWS Regions where Security Lake is automatically enabled.
Type: String
Pattern: `(us(-gov)?|af|ap|ca|eu|me|sa)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-\d+`
Required: Yes

 ** encryptionConfiguration **   <a name="securitylake-Type-DataLakeConfiguration-encryptionConfiguration"></a>
Provides encryption details of Amazon Security Lake object.
Type: [DataLakeEncryptionConfiguration](API_DataLakeEncryptionConfiguration.md) object
Required: No

 ** lifecycleConfiguration **   <a name="securitylake-Type-DataLakeConfiguration-lifecycleConfiguration"></a>
Provides lifecycle details of Amazon Security Lake object.
Type: [DataLakeLifecycleConfiguration](API_DataLakeLifecycleConfiguration.md) object
Required: No

 ** replicationConfiguration **   <a name="securitylake-Type-DataLakeConfiguration-replicationConfiguration"></a>
Provides replication details of Amazon Security Lake object.
Type: [DataLakeReplicationConfiguration](API_DataLakeReplicationConfiguration.md) object
Required: No

## See Also
<a name="API_DataLakeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/DataLakeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/DataLakeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/DataLakeConfiguration)

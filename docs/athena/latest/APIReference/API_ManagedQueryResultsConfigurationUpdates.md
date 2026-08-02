---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ManagedQueryResultsConfigurationUpdates.html
---

# ManagedQueryResultsConfigurationUpdates
<a name="API_ManagedQueryResultsConfigurationUpdates"></a>

Updates the configuration for managed query results.

## Contents
<a name="API_ManagedQueryResultsConfigurationUpdates_Contents"></a>

 ** Enabled **   <a name="athena-Type-ManagedQueryResultsConfigurationUpdates-Enabled"></a>
If set to true, specifies that Athena manages query results in Athena owned storage.
Type: Boolean
Required: No

 ** EncryptionConfiguration **   <a name="athena-Type-ManagedQueryResultsConfigurationUpdates-EncryptionConfiguration"></a>
If you encrypt query and calculation results in Athena owned storage, this field indicates the encryption option (for example, SSE\_KMS or CSE\_KMS) and key information.
Type: [ManagedQueryResultsEncryptionConfiguration](API_ManagedQueryResultsEncryptionConfiguration.md) object
Required: No

 ** RemoveEncryptionConfiguration **   <a name="athena-Type-ManagedQueryResultsConfigurationUpdates-RemoveEncryptionConfiguration"></a>
If set to true, it removes workgroup from Athena owned storage. The existing query results are cleaned up after 24hrs. You must provide query results in location specified under `ResultConfiguration$OutputLocation`.
Type: Boolean
Required: No

## See Also
<a name="API_ManagedQueryResultsConfigurationUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ManagedQueryResultsConfigurationUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ManagedQueryResultsConfigurationUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ManagedQueryResultsConfigurationUpdates)

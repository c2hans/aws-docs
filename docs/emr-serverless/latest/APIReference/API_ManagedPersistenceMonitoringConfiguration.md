---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ManagedPersistenceMonitoringConfiguration.html
---

# ManagedPersistenceMonitoringConfiguration
<a name="API_ManagedPersistenceMonitoringConfiguration"></a>

The managed log persistence configuration for a job run.

## Contents
<a name="API_ManagedPersistenceMonitoringConfiguration_Contents"></a>

 ** enabled **   <a name="emrserverless-Type-ManagedPersistenceMonitoringConfiguration-enabled"></a>
Enables managed logging and defaults to true. If set to false, managed logging will be turned off.
Type: Boolean
Required: No

 ** encryptionKeyArn **   <a name="emrserverless-Type-ManagedPersistenceMonitoringConfiguration-encryptionKeyArn"></a>
The KMS key ARN to encrypt the logs stored in managed log persistence.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):kms:[a-zA-Z0-9\-]*:([0-9]{12}):key\/[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_ManagedPersistenceMonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/ManagedPersistenceMonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/ManagedPersistenceMonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/ManagedPersistenceMonitoringConfiguration)

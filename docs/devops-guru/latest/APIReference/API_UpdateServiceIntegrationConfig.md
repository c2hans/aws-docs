---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_UpdateServiceIntegrationConfig.html
---

# UpdateServiceIntegrationConfig
<a name="API_UpdateServiceIntegrationConfig"></a>

 Information about updating the integration status of an AWS service, such as AWS Systems Manager, with DevOps Guru.

## Contents
<a name="API_UpdateServiceIntegrationConfig_Contents"></a>

 ** KMSServerSideEncryption **   <a name="DevOpsGuru-Type-UpdateServiceIntegrationConfig-KMSServerSideEncryption"></a>
 Information about whether DevOps Guru is configured to encrypt server-side data using KMS.
Type: [KMSServerSideEncryptionIntegrationConfig](API_KMSServerSideEncryptionIntegrationConfig.md) object
Required: No

 ** LogsAnomalyDetection **   <a name="DevOpsGuru-Type-UpdateServiceIntegrationConfig-LogsAnomalyDetection"></a>
 Information about whether DevOps Guru is configured to perform log anomaly detection on Amazon CloudWatch log groups.
Type: [LogsAnomalyDetectionIntegrationConfig](API_LogsAnomalyDetectionIntegrationConfig.md) object
Required: No

 ** OpsCenter **   <a name="DevOpsGuru-Type-UpdateServiceIntegrationConfig-OpsCenter"></a>
 Information about whether DevOps Guru is configured to create an OpsItem in AWS Systems Manager OpsCenter for each created insight. You can use this to update the configuration.
Type: [OpsCenterIntegrationConfig](API_OpsCenterIntegrationConfig.md) object
Required: No

## See Also
<a name="API_UpdateServiceIntegrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/UpdateServiceIntegrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/UpdateServiceIntegrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/UpdateServiceIntegrationConfig)

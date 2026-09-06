---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ServiceIntegrationConfig.html
---

# ServiceIntegrationConfig
<a name="API_ServiceIntegrationConfig"></a>

 Information about the integration of DevOps Guru with another AWS service, such as AWS Systems Manager.

## Contents
<a name="API_ServiceIntegrationConfig_Contents"></a>

 ** KMSServerSideEncryption **   <a name="DevOpsGuru-Type-ServiceIntegrationConfig-KMSServerSideEncryption"></a>
 Information about whether DevOps Guru is configured to encrypt server-side data using KMS.
Type: [KMSServerSideEncryptionIntegration](API_KMSServerSideEncryptionIntegration.md) object
Required: No

 ** LogsAnomalyDetection **   <a name="DevOpsGuru-Type-ServiceIntegrationConfig-LogsAnomalyDetection"></a>
 Information about whether DevOps Guru is configured to perform log anomaly detection on Amazon CloudWatch log groups.
Type: [LogsAnomalyDetectionIntegration](API_LogsAnomalyDetectionIntegration.md) object
Required: No

 ** OpsCenter **   <a name="DevOpsGuru-Type-ServiceIntegrationConfig-OpsCenter"></a>
 Information about whether DevOps Guru is configured to create an OpsItem in AWS Systems Manager OpsCenter for each created insight.
Type: [OpsCenterIntegration](API_OpsCenterIntegration.md) object
Required: No

## See Also
<a name="API_ServiceIntegrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ServiceIntegrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ServiceIntegrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ServiceIntegrationConfig)

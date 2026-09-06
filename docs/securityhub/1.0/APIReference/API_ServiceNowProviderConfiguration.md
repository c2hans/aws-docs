---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ServiceNowProviderConfiguration.html
---

# ServiceNowProviderConfiguration
<a name="API_ServiceNowProviderConfiguration"></a>

The initial configuration settings required to establish an integration between Security Hub and ServiceNow ITSM.

## Contents
<a name="API_ServiceNowProviderConfiguration_Contents"></a>

 ** InstanceName **   <a name="securityhub-Type-ServiceNowProviderConfiguration-InstanceName"></a>
The instance name of ServiceNow ITSM.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** SecretArn **   <a name="securityhub-Type-ServiceNowProviderConfiguration-SecretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the ServiceNow credentials.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_ServiceNowProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ServiceNowProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ServiceNowProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ServiceNowProviderConfiguration)

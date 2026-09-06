---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CustomerProfilesIntegrationConfig.html
---

# CustomerProfilesIntegrationConfig
<a name="API_CustomerProfilesIntegrationConfig"></a>

Specifies the configuration for integrating with Customer Profiles. This configuration enables AWS Entity Resolution to send matched output directly to Customer Profiles instead of Amazon S3, creating a unified customer view by automatically updating customer profiles based on match clusters.

## Contents
<a name="API_CustomerProfilesIntegrationConfig_Contents"></a>

 ** domainArn **   <a name="API-Type-CustomerProfilesIntegrationConfig-domainArn"></a>
The Amazon Resource Name (ARN) of the Customer Profiles domain where the matched output will be sent.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):profile:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(domains/[a-zA-Z_0-9-]{1,255})`
Required: Yes

 ** objectTypeArn **   <a name="API-Type-CustomerProfilesIntegrationConfig-objectTypeArn"></a>
The Amazon Resource Name (ARN) of the Customer Profiles object type that defines the structure for the matched customer data.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):profile:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(domains/[a-zA-Z_0-9-]{1,255}/object-types/[a-zA-Z_0-9-]{1,255})`
Required: Yes

## See Also
<a name="API_CustomerProfilesIntegrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/CustomerProfilesIntegrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/CustomerProfilesIntegrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/CustomerProfilesIntegrationConfig)

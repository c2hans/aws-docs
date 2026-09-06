---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerServiceStateDetail.html
---

# ContainerServiceStateDetail
<a name="API_ContainerServiceStateDetail"></a>

Describes the current state of a container service.

## Contents
<a name="API_ContainerServiceStateDetail_Contents"></a>

 ** code **   <a name="Lightsail-Type-ContainerServiceStateDetail-code"></a>
The state code of the container service.
The following state codes are possible:
+ The following state codes are possible if your container service is in a `DEPLOYING` or `UPDATING` state:
  +  `CREATING_SYSTEM_RESOURCES` - The system resources for your container service are being created.
  +  `CREATING_NETWORK_INFRASTRUCTURE` - The network infrastructure for your container service are being created.
  +  `PROVISIONING_CERTIFICATE` - The SSL/TLS certificate for your container service is being created.
  +  `PROVISIONING_SERVICE` - Your container service is being provisioned.
  +  `CREATING_DEPLOYMENT` - Your deployment is being created on your container service.
  +  `EVALUATING_HEALTH_CHECK` - The health of your deployment is being evaluated.
  +  `ACTIVATING_DEPLOYMENT` - Your deployment is being activated.
+ The following state codes are possible if your container service is in a `PENDING` state:
  +  `CERTIFICATE_LIMIT_EXCEEDED` - The SSL/TLS certificate required for your container service exceeds the maximum number of certificates allowed for your account.
  +  `UNKNOWN_ERROR` - An error was experienced when your container service was being created.
Type: String
Valid Values: `CREATING_SYSTEM_RESOURCES | CREATING_NETWORK_INFRASTRUCTURE | PROVISIONING_CERTIFICATE | PROVISIONING_SERVICE | CREATING_DEPLOYMENT | EVALUATING_HEALTH_CHECK | ACTIVATING_DEPLOYMENT | CERTIFICATE_LIMIT_EXCEEDED | UNKNOWN_ERROR`
Required: No

 ** message **   <a name="Lightsail-Type-ContainerServiceStateDetail-message"></a>
A message that provides more information for the state code.
The state detail is populated only when a container service is in a `PENDING`, `DEPLOYING`, or `UPDATING` state.
Type: String
Required: No

## See Also
<a name="API_ContainerServiceStateDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ContainerServiceStateDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ContainerServiceStateDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ContainerServiceStateDetail)

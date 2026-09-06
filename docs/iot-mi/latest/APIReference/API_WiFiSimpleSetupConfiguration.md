---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_WiFiSimpleSetupConfiguration.html
---

# WiFiSimpleSetupConfiguration
<a name="API_WiFiSimpleSetupConfiguration"></a>

The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.

## Contents
<a name="API_WiFiSimpleSetupConfiguration_Contents"></a>

 ** EnableAsProvisionee **   <a name="managedintegrations-Type-WiFiSimpleSetupConfiguration-EnableAsProvisionee"></a>
Indicates whether the device can act as a provisionee in Wi-Fi Simple Setup, allowing it to be configured by other devices.
Type: Boolean
Required: No

 ** EnableAsProvisioner **   <a name="managedintegrations-Type-WiFiSimpleSetupConfiguration-EnableAsProvisioner"></a>
Indicates whether the device can act as a provisioner in Wi-Fi Simple Setup, allowing it to configure other devices.
Type: Boolean
Required: No

 ** TimeoutInMinutes **   <a name="managedintegrations-Type-WiFiSimpleSetupConfiguration-TimeoutInMinutes"></a>
The timeout duration in minutes for Wi-Fi Simple Setup. Valid range is 5 to 15 minutes.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 15.
Required: No

## See Also
<a name="API_WiFiSimpleSetupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/WiFiSimpleSetupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/WiFiSimpleSetupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/WiFiSimpleSetupConfiguration)

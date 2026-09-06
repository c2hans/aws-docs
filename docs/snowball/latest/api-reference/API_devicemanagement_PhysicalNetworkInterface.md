---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_PhysicalNetworkInterface.html
---

# PhysicalNetworkInterface
<a name="API_devicemanagement_PhysicalNetworkInterface"></a>

The details about the physical network interface for the device.

## Contents
<a name="API_devicemanagement_PhysicalNetworkInterface_Contents"></a>

 ** defaultGateway **   <a name="Snowball-Type-devicemanagement_PhysicalNetworkInterface-defaultGateway"></a>
The default gateway of the device.
Type: String
Required: No

 ** ipAddress **   <a name="Snowball-Type-devicemanagement_PhysicalNetworkInterface-ipAddress"></a>
The IP address of the device.
Type: String
Required: No

 ** ipAddressAssignment **   <a name="Snowball-Type-devicemanagement_PhysicalNetworkInterface-ipAddressAssignment"></a>
A value that describes whether the IP address is dynamic or persistent.
Type: String
Valid Values: `DHCP | STATIC`
Required: No

 ** macAddress **   <a name="Snowball-Type-devicemanagement_PhysicalNetworkInterface-macAddress"></a>
The MAC address of the device.
Type: String
Required: No

 ** netmask **   <a name="Snowball-Type-devicemanagement_PhysicalNetworkInterface-netmask"></a>
The netmask used to divide the IP address into subnets.
Type: String
Required: No

 ** physicalConnectorType **   <a name="Snowball-Type-devicemanagement_PhysicalNetworkInterface-physicalConnectorType"></a>
The physical connector type.
Type: String
Valid Values: `RJ45 | SFP_PLUS | QSFP | RJ45_2 | WIFI`
Required: No

 ** physicalNetworkInterfaceId **   <a name="Snowball-Type-devicemanagement_PhysicalNetworkInterface-physicalNetworkInterfaceId"></a>
The physical network interface ID.
Type: String
Required: No

## See Also
<a name="API_devicemanagement_PhysicalNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/PhysicalNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/PhysicalNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/PhysicalNetworkInterface)

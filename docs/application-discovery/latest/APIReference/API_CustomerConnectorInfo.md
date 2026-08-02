---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CustomerConnectorInfo.html
---

# CustomerConnectorInfo
<a name="API_CustomerConnectorInfo"></a>

Inventory data for installed discovery connectors.

## Contents
<a name="API_CustomerConnectorInfo_Contents"></a>

 ** activeConnectors **   <a name="DiscServ-Type-CustomerConnectorInfo-activeConnectors"></a>
Number of active discovery connectors.
Type: Integer
Required: Yes

 ** blackListedConnectors **   <a name="DiscServ-Type-CustomerConnectorInfo-blackListedConnectors"></a>
Number of blacklisted discovery connectors.
Type: Integer
Required: Yes

 ** healthyConnectors **   <a name="DiscServ-Type-CustomerConnectorInfo-healthyConnectors"></a>
Number of healthy discovery connectors.
Type: Integer
Required: Yes

 ** shutdownConnectors **   <a name="DiscServ-Type-CustomerConnectorInfo-shutdownConnectors"></a>
Number of discovery connectors with status SHUTDOWN,
Type: Integer
Required: Yes

 ** totalConnectors **   <a name="DiscServ-Type-CustomerConnectorInfo-totalConnectors"></a>
Total number of discovery connectors.
Type: Integer
Required: Yes

 ** unhealthyConnectors **   <a name="DiscServ-Type-CustomerConnectorInfo-unhealthyConnectors"></a>
Number of unhealthy discovery connectors.
Type: Integer
Required: Yes

 ** unknownConnectors **   <a name="DiscServ-Type-CustomerConnectorInfo-unknownConnectors"></a>
Number of unknown discovery connectors.
Type: Integer
Required: Yes

## See Also
<a name="API_CustomerConnectorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/CustomerConnectorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/CustomerConnectorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/CustomerConnectorInfo)

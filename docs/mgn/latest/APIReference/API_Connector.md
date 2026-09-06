---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_Connector.html
---

# Connector
<a name="API_Connector"></a>

## Contents
<a name="API_Connector_Contents"></a>

 ** arn **   <a name="mgn-Type-Connector-arn"></a>
Connector arn.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** connectorID **   <a name="mgn-Type-Connector-connectorID"></a>
Connector ID.
Type: String
Length Constraints: Fixed length of 27.
Pattern: `connector-[0-9a-zA-Z]{17}`
Required: No

 ** name **   <a name="mgn-Type-Connector-name"></a>
Connector name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** ssmCommandConfig **   <a name="mgn-Type-Connector-ssmCommandConfig"></a>
Connector SSM command config.
Type: [ConnectorSsmCommandConfig](API_ConnectorSsmCommandConfig.md) object
Required: No

 ** ssmInstanceID **   <a name="mgn-Type-Connector-ssmInstanceID"></a>
Connector SSM instance ID.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 20.
Pattern: `.*(^i-[0-9a-zA-Z]{17}$)|(^mi-[0-9a-zA-Z]{17}$).*`
Required: No

 ** tags **   <a name="mgn-Type-Connector-tags"></a>
Connector tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Connector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/Connector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/Connector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/Connector)

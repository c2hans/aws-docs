---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_EventIntegrationAssociation.html
---

# EventIntegrationAssociation
<a name="API_connect-app-integrations_EventIntegrationAssociation"></a>

The event integration association.

## Contents
<a name="API_connect-app-integrations_EventIntegrationAssociation_Contents"></a>

 ** ClientAssociationMetadata **   <a name="connect-Type-connect-app-integrations_EventIntegrationAssociation-ClientAssociationMetadata"></a>
The metadata associated with the client.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `.*\S.*`
Required: No

 ** ClientId **   <a name="connect-Type-connect-app-integrations_EventIntegrationAssociation-ClientId"></a>
The identifier for the client that is associated with the event integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** EventBridgeRuleName **   <a name="connect-Type-connect-app-integrations_EventIntegrationAssociation-EventBridgeRuleName"></a>
The name of the EventBridge rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

 ** EventIntegrationAssociationArn **   <a name="connect-Type-connect-app-integrations_EventIntegrationAssociation-EventIntegrationAssociationArn"></a>
The Amazon Resource Name (ARN) for the event integration association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** EventIntegrationAssociationId **   <a name="connect-Type-connect-app-integrations_EventIntegrationAssociation-EventIntegrationAssociationId"></a>
The identifier for the event integration association.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** EventIntegrationName **   <a name="connect-Type-connect-app-integrations_EventIntegrationAssociation-EventIntegrationName"></a>
The name of the event integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

## See Also
<a name="API_connect-app-integrations_EventIntegrationAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/EventIntegrationAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/EventIntegrationAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/EventIntegrationAssociation)

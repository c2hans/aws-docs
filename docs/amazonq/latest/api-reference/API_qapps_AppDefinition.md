---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_AppDefinition.html
---

# AppDefinition
<a name="API_qapps_AppDefinition"></a>

The definition of the Q App, specifying the cards and flow.

## Contents
<a name="API_qapps_AppDefinition_Contents"></a>

 ** appDefinitionVersion **   <a name="qbusiness-Type-qapps_AppDefinition-appDefinitionVersion"></a>
The version of the app definition schema or specification.
Type: String
Required: Yes

 ** cards **   <a name="qbusiness-Type-qapps_AppDefinition-cards"></a>
The cards that make up the Q App, such as text input, file upload, or query cards.
Type: Array of [Card](API_qapps_Card.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

 ** canEdit **   <a name="qbusiness-Type-qapps_AppDefinition-canEdit"></a>
A flag indicating whether the Q App's definition can be edited by the user.
Type: Boolean
Required: No

## See Also
<a name="API_qapps_AppDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/AppDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/AppDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/AppDefinition)

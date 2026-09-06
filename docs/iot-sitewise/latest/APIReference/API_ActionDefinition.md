---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ActionDefinition.html
---

# ActionDefinition
<a name="API_ActionDefinition"></a>

Contains a definition for an action.

## Contents
<a name="API_ActionDefinition_Contents"></a>

 ** actionDefinitionId **   <a name="iotsitewise-Type-ActionDefinition-actionDefinitionId"></a>
The ID of the action definition.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** actionName **   <a name="iotsitewise-Type-ActionDefinition-actionName"></a>
The name of the action definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** actionType **   <a name="iotsitewise-Type-ActionDefinition-actionType"></a>
The type of the action definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

## See Also
<a name="API_ActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ActionDefinition)

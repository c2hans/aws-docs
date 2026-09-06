---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TaskActionDefinition.html
---

# TaskActionDefinition
<a name="API_TaskActionDefinition"></a>

Information about the task action.

## Contents
<a name="API_TaskActionDefinition_Contents"></a>

 ** ContactFlowId **   <a name="connect-Type-TaskActionDefinition-ContactFlowId"></a>
The identifier of the flow.
Type: String
Length Constraints: Maximum length of 500.
Required: Yes

 ** Name **   <a name="connect-Type-TaskActionDefinition-Name"></a>
The name. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Connect Customer Administrators Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** Description **   <a name="connect-Type-TaskActionDefinition-Description"></a>
The description. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Connect Customer Administrators Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** References **   <a name="connect-Type-TaskActionDefinition-References"></a>
Information about the reference when the `referenceType` is `URL`. Otherwise, null. (Supports variable injection in the `Value` field.)
Type: String to [Reference](API_Reference.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_TaskActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TaskActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TaskActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TaskActionDefinition)

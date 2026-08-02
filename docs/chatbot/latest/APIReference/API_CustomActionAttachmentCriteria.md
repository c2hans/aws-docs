---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CustomActionAttachmentCriteria.html
---

# CustomActionAttachmentCriteria
<a name="API_CustomActionAttachmentCriteria"></a>

A criteria for when a button should be shown based on values in the notification

## Contents
<a name="API_CustomActionAttachmentCriteria_Contents"></a>

 ** Operator **   <a name="qdevinchatapps-Type-CustomActionAttachmentCriteria-Operator"></a>
The operation to perform on the named variable.
Type: String
Valid Values: `HAS_VALUE | EQUALS`
Required: Yes

 ** VariableName **   <a name="qdevinchatapps-Type-CustomActionAttachmentCriteria-VariableName"></a>
The name of the variable to operate on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

 ** Value **   <a name="qdevinchatapps-Type-CustomActionAttachmentCriteria-Value"></a>
A value that is compared with the actual value of the variable based on the behavior of the operator.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]+`
Required: No

## See Also
<a name="API_CustomActionAttachmentCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/CustomActionAttachmentCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/CustomActionAttachmentCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/CustomActionAttachmentCriteria)

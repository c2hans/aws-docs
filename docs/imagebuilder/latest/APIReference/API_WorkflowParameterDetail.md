---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowParameterDetail.html
---

# WorkflowParameterDetail
<a name="API_WorkflowParameterDetail"></a>

Defines a parameter that's used to provide configuration details for the workflow.

## Contents
<a name="API_WorkflowParameterDetail_Contents"></a>

 ** name **   <a name="imagebuilder-Type-WorkflowParameterDetail-name"></a>
The name of this input parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[^\x00]+`
Required: Yes

 ** type **   <a name="imagebuilder-Type-WorkflowParameterDetail-type"></a>
The type of input this parameter provides. The currently supported value is "string".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^string|integer|boolean|stringList$`
Required: Yes

 ** defaultValue **   <a name="imagebuilder-Type-WorkflowParameterDetail-defaultValue"></a>
The default value of this parameter if no input is provided.
Type: Array of strings
Length Constraints: Minimum length of 0.
Pattern: `[^\x00]*`
Required: No

 ** description **   <a name="imagebuilder-Type-WorkflowParameterDetail-description"></a>
Describes this parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\x00]+`
Required: No

## See Also
<a name="API_WorkflowParameterDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/WorkflowParameterDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/WorkflowParameterDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/WorkflowParameterDetail)

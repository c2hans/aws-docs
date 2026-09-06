---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowTypeInfo.html
---

# WorkflowTypeInfo
<a name="API_WorkflowTypeInfo"></a>

Contains information about a workflow type.

## Contents
<a name="API_WorkflowTypeInfo_Contents"></a>

 ** creationDate **   <a name="SWF-Type-WorkflowTypeInfo-creationDate"></a>
The date when this type was registered.
Type: Timestamp
Required: Yes

 ** status **   <a name="SWF-Type-WorkflowTypeInfo-status"></a>
The current status of the workflow type.
Type: String
Valid Values: `REGISTERED | DEPRECATED`
Required: Yes

 ** workflowType **   <a name="SWF-Type-WorkflowTypeInfo-workflowType"></a>
The workflow type this information is about.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

 ** deprecationDate **   <a name="SWF-Type-WorkflowTypeInfo-deprecationDate"></a>
If the type is in deprecated state, then it is set to the date when the type was deprecated.
Type: Timestamp
Required: No

 ** description **   <a name="SWF-Type-WorkflowTypeInfo-description"></a>
The description of the type registered through [RegisterWorkflowType](API_RegisterWorkflowType.md).
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_WorkflowTypeInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowTypeInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowTypeInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowTypeInfo)

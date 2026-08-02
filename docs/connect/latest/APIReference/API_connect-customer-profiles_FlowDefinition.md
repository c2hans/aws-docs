---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_FlowDefinition.html
---

# FlowDefinition
<a name="API_connect-customer-profiles_FlowDefinition"></a>

The configurations that control how Customer Profiles retrieves data from the source, Amazon AppFlow. Customer Profiles uses this information to create an AppFlow flow on behalf of customers.

## Contents
<a name="API_connect-customer-profiles_FlowDefinition_Contents"></a>

 ** FlowName **   <a name="connect-Type-connect-customer-profiles_FlowDefinition-FlowName"></a>
The specified name of the flow. Use underscores (\_) or hyphens (-) only. Spaces are not allowed.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: Yes

 ** KmsArn **   <a name="connect-Type-connect-customer-profiles_FlowDefinition-KmsArn"></a>
The Amazon Resource Name of the AWS Key Management Service (KMS) key you provide for encryption.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:.*:[0-9]+:.*`
Required: Yes

 ** SourceFlowConfig **   <a name="connect-Type-connect-customer-profiles_FlowDefinition-SourceFlowConfig"></a>
The configuration that controls how Customer Profiles retrieves data from the source.
Type: [SourceFlowConfig](API_connect-customer-profiles_SourceFlowConfig.md) object
Required: Yes

 ** Tasks **   <a name="connect-Type-connect-customer-profiles_FlowDefinition-Tasks"></a>
A list of tasks that Customer Profiles performs while transferring the data in the flow run.
Type: Array of [Task](API_connect-customer-profiles_Task.md) objects
Required: Yes

 ** TriggerConfig **   <a name="connect-Type-connect-customer-profiles_FlowDefinition-TriggerConfig"></a>
The trigger settings that determine how and when the flow runs.
Type: [TriggerConfig](API_connect-customer-profiles_TriggerConfig.md) object
Required: Yes

 ** Description **   <a name="connect-Type-connect-customer-profiles_FlowDefinition-Description"></a>
A description of the flow you want to create.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\w!@#\-.?,\s]*`
Required: No

## See Also
<a name="API_connect-customer-profiles_FlowDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/FlowDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/FlowDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/FlowDefinition)

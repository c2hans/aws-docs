---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_TemplateConfiguration.html
---

# TemplateConfiguration
<a name="API_TemplateConfiguration"></a>

The configuration details of a generated template.

## Contents
<a name="API_TemplateConfiguration_Contents"></a>

 ** DeletionPolicy **
The `DeletionPolicy` assigned to resources in the generated template. Supported values are:
+  `DELETE` - delete all resources when the stack is deleted.
+  `RETAIN` - retain all resources when the stack is deleted.
For more information, see [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html) in the * AWS CloudFormation User Guide*.
Type: String
Valid Values: `DELETE | RETAIN`
Required: No

 ** UpdateReplacePolicy **
The `UpdateReplacePolicy` assigned to resources in the generated template. Supported values are:
+  `DELETE` - delete all resources when the resource is replaced during an update operation.
+  `RETAIN` - retain all resources when the resource is replaced during an update operation.
For more information, see [UpdateReplacePolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html) in the * AWS CloudFormation User Guide*.
Type: String
Valid Values: `DELETE | RETAIN`
Required: No

## See Also
<a name="API_TemplateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TemplateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TemplateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TemplateConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

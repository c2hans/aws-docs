---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowVersion.html
---

# WorkflowVersion
<a name="API_WorkflowVersion"></a>

Contains details about this version of the workflow.

## Contents
<a name="API_WorkflowVersion_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-WorkflowVersion-arn"></a>
The Amazon Resource Name (ARN) of the workflow resource.
Type: String
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-WorkflowVersion-dateCreated"></a>
The timestamp when Image Builder created the workflow version.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-WorkflowVersion-description"></a>
Describes the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-WorkflowVersion-name"></a>
The name of the workflow.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** owner **   <a name="imagebuilder-Type-WorkflowVersion-owner"></a>
The owner of the workflow resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** type **   <a name="imagebuilder-Type-WorkflowVersion-type"></a>
The image creation stage that this workflow applies to. Image Builder currently supports build and test stage workflows.
Type: String
Valid Values: `BUILD | TEST | DISTRIBUTION`
Required: No

 ** version **   <a name="imagebuilder-Type-WorkflowVersion-version"></a>
The semantic version of the workflow resource. The format includes three nodes: <major>.<minor>.<patch>.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

## See Also
<a name="API_WorkflowVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/WorkflowVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/WorkflowVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/WorkflowVersion)

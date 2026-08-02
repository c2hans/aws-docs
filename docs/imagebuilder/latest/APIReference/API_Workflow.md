---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Workflow.html
---

# Workflow
<a name="API_Workflow"></a>

Defines a process that Image Builder uses to build and test images during the image creation process.

## Contents
<a name="API_Workflow_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-Workflow-arn"></a>
The Amazon Resource Name (ARN) of the workflow resource.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: No

 ** changeDescription **   <a name="imagebuilder-Type-Workflow-changeDescription"></a>
Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** data **   <a name="imagebuilder-Type-Workflow-data"></a>
Contains the YAML document content for the workflow.
Type: String
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-Workflow-dateCreated"></a>
The timestamp when Image Builder created the workflow resource.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-Workflow-description"></a>
The description of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** kmsKeyId **   <a name="imagebuilder-Type-Workflow-kmsKeyId"></a>
The KMS key identifier used to encrypt the workflow resource. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-Workflow-name"></a>
The name of the workflow resource.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** owner **   <a name="imagebuilder-Type-Workflow-owner"></a>
The owner of the workflow resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** parameters **   <a name="imagebuilder-Type-Workflow-parameters"></a>
An array of input parameters that that the image workflow uses to control actions or configure settings.
Type: Array of [WorkflowParameterDetail](API_WorkflowParameterDetail.md) objects
Required: No

 ** state **   <a name="imagebuilder-Type-Workflow-state"></a>
Describes the current status of the workflow and the reason for that status.
Type: [WorkflowState](API_WorkflowState.md) object
Required: No

 ** tags **   <a name="imagebuilder-Type-Workflow-tags"></a>
The tags that apply to the workflow resource
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** type **   <a name="imagebuilder-Type-Workflow-type"></a>
Specifies the image creation stage that the workflow applies to. Image Builder currently supports build and test workflows.
Type: String
Valid Values: `BUILD | TEST | DISTRIBUTION`
Required: No

 ** version **   <a name="imagebuilder-Type-Workflow-version"></a>
The workflow resource version. Workflow resources are immutable. To make a change, you can clone a workflow or create a new version.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

## See Also
<a name="API_Workflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/Workflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/Workflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/Workflow)

---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowSummary.html
---

# WorkflowSummary
<a name="API_WorkflowSummary"></a>

Contains metadata about the workflow resource.

## Contents
<a name="API_WorkflowSummary_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-WorkflowSummary-arn"></a>
The Amazon Resource Name (ARN) of the workflow resource.
Type: String
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/x\.x\.x$`
Required: No

 ** changeDescription **   <a name="imagebuilder-Type-WorkflowSummary-changeDescription"></a>
The change description for the current version of the workflow resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-WorkflowSummary-dateCreated"></a>
The original creation date of the workflow resource.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-WorkflowSummary-description"></a>
Describes the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-WorkflowSummary-name"></a>
The name of the workflow.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** owner **   <a name="imagebuilder-Type-WorkflowSummary-owner"></a>
The owner of the workflow resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** state **   <a name="imagebuilder-Type-WorkflowSummary-state"></a>
Describes the current state of the workflow resource.
Type: [WorkflowState](API_WorkflowState.md) object
Required: No

 ** tags **   <a name="imagebuilder-Type-WorkflowSummary-tags"></a>
Contains a list of tags that are defined for the workflow.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** type **   <a name="imagebuilder-Type-WorkflowSummary-type"></a>
The image creation stage that this workflow applies to. Image Builder currently supports build and test stage workflows.
Type: String
Valid Values: `BUILD | TEST | DISTRIBUTION`
Required: No

 ** version **   <a name="imagebuilder-Type-WorkflowSummary-version"></a>
The version of the workflow.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

## See Also
<a name="API_WorkflowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/WorkflowSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/WorkflowSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/WorkflowSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

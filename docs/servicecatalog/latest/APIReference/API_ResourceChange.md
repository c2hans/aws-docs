---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ResourceChange.html
---

# ResourceChange
<a name="API_ResourceChange"></a>

Information about a resource change that will occur when a plan is executed.

## Contents
<a name="API_ResourceChange_Contents"></a>

 ** Action **   <a name="servicecatalog-Type-ResourceChange-Action"></a>
The change action.
Type: String
Valid Values: `ADD | MODIFY | REMOVE`
Required: No

 ** Details **   <a name="servicecatalog-Type-ResourceChange-Details"></a>
Information about the resource changes.
Type: Array of [ResourceChangeDetail](API_ResourceChangeDetail.md) objects
Required: No

 ** LogicalResourceId **   <a name="servicecatalog-Type-ResourceChange-LogicalResourceId"></a>
The ID of the resource, as defined in the AWS CloudFormation template.
Type: String
Required: No

 ** PhysicalResourceId **   <a name="servicecatalog-Type-ResourceChange-PhysicalResourceId"></a>
The ID of the resource, if it was already created.
Type: String
Required: No

 ** Replacement **   <a name="servicecatalog-Type-ResourceChange-Replacement"></a>
If the change type is `Modify`, indicates whether the existing resource is deleted and replaced with a new one.
Type: String
Valid Values: `TRUE | FALSE | CONDITIONAL`
Required: No

 ** ResourceType **   <a name="servicecatalog-Type-ResourceChange-ResourceType"></a>
The type of resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Scope **   <a name="servicecatalog-Type-ResourceChange-Scope"></a>
The change scope.
Type: Array of strings
Valid Values: `PROPERTIES | METADATA | CREATIONPOLICY | UPDATEPOLICY | DELETIONPOLICY | TAGS`
Required: No

## See Also
<a name="API_ResourceChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ResourceChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ResourceChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ResourceChange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

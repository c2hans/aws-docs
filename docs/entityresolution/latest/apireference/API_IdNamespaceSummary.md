---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdNamespaceSummary.html
---

# IdNamespaceSummary
<a name="API_IdNamespaceSummary"></a>

A summary of ID namespaces.

## Contents
<a name="API_IdNamespaceSummary_Contents"></a>

 ** createdAt **   <a name="API-Type-IdNamespaceSummary-createdAt"></a>
The timestamp of when the ID namespace was created.
Type: Timestamp
Required: Yes

 ** idNamespaceArn **   <a name="API-Type-IdNamespaceSummary-idNamespaceArn"></a>
The Amazon Resource Name (ARN) of the ID namespace.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})`
Required: Yes

 ** idNamespaceName **   <a name="API-Type-IdNamespaceSummary-idNamespaceName"></a>
The name of the ID namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

 ** type **   <a name="API-Type-IdNamespaceSummary-type"></a>
The type of ID namespace. There are two types: `SOURCE` and `TARGET`.
The `SOURCE` contains configurations for `sourceId` data that will be processed in an ID mapping workflow.
The `TARGET` contains a configuration of `targetId` which all `sourceIds` will resolve to.
Type: String
Valid Values: `SOURCE | TARGET`
Required: Yes

 ** updatedAt **   <a name="API-Type-IdNamespaceSummary-updatedAt"></a>
The timestamp of when the ID namespace was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-IdNamespaceSummary-description"></a>
The description of the ID namespace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** idMappingWorkflowProperties **   <a name="API-Type-IdNamespaceSummary-idMappingWorkflowProperties"></a>
An object which defines any additional configurations required by the ID mapping workflow.
Type: Array of [IdNamespaceIdMappingWorkflowMetadata](API_IdNamespaceIdMappingWorkflowMetadata.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_IdNamespaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/IdNamespaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/IdNamespaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/IdNamespaceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

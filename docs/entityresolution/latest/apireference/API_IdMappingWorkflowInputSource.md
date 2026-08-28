---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingWorkflowInputSource.html
---

# IdMappingWorkflowInputSource
<a name="API_IdMappingWorkflowInputSource"></a>

An object containing `inputSourceARN`, `schemaName`, and `type`.

## Contents
<a name="API_IdMappingWorkflowInputSource_Contents"></a>

 ** inputSourceARN **   <a name="API-Type-IdMappingWorkflowInputSource-inputSourceARN"></a>
An AWS Glue table Amazon Resource Name (ARN) or a matching workflow ARN for the input source table.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})`
Required: Yes

 ** schemaName **   <a name="API-Type-IdMappingWorkflowInputSource-schemaName"></a>
The name of the schema to be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: No

 ** type **   <a name="API-Type-IdMappingWorkflowInputSource-type"></a>
The type of ID namespace. There are two types: `SOURCE` and `TARGET`.
The `SOURCE` contains configurations for `sourceId` data that will be processed in an ID mapping workflow.
The `TARGET` contains a configuration of `targetId` which all `sourceIds` will resolve to.
Type: String
Valid Values: `SOURCE | TARGET`
Required: No

## See Also
<a name="API_IdMappingWorkflowInputSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/IdMappingWorkflowInputSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/IdMappingWorkflowInputSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/IdMappingWorkflowInputSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

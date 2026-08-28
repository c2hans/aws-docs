---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_DocumentCustomOutputConfiguration.html
---

# DocumentCustomOutputConfiguration
<a name="API_data-automation_DocumentCustomOutputConfiguration"></a>

Custom output configuration for document processing.

## Contents
<a name="API_data-automation_DocumentCustomOutputConfiguration_Contents"></a>

 ** fallbackBlueprints **   <a name="bedrock-Type-data-automation_DocumentCustomOutputConfiguration-fallbackBlueprints"></a>
The fallback blueprints to use for document processing. This will be used in the case where the service cannot find a match between the document and your list of blueprints.
Type: Array of [BlueprintItem](API_data-automation_BlueprintItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_data-automation_DocumentCustomOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/DocumentCustomOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/DocumentCustomOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/DocumentCustomOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

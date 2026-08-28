---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_DeleteEntitiesInfo.html
---

# DeleteEntitiesInfo
<a name="API_data-automation_DeleteEntitiesInfo"></a>

Information about entities to delete.

## Contents
<a name="API_data-automation_DeleteEntitiesInfo_Contents"></a>

 ** entityIds **   <a name="bedrock-Type-data-automation_DeleteEntitiesInfo-entityIds"></a>
The entity IDs to delete.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

## See Also
<a name="API_data-automation_DeleteEntitiesInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/DeleteEntitiesInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/DeleteEntitiesInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/DeleteEntitiesInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

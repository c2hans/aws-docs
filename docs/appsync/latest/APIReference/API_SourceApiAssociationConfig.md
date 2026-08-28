---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_SourceApiAssociationConfig.html
---

# SourceApiAssociationConfig
<a name="API_SourceApiAssociationConfig"></a>

Describes properties used to specify configurations related to a source API.

## Contents
<a name="API_SourceApiAssociationConfig_Contents"></a>

 ** mergeType **   <a name="appsync-Type-SourceApiAssociationConfig-mergeType"></a>
The property that indicates which merging option is enabled in the source API association.
Valid merge types are `MANUAL_MERGE` (default) and `AUTO_MERGE`. Manual merges are the default behavior and require the user to trigger any changes from the source APIs to the merged API manually. Auto merges subscribe the merged API to the changes performed on the source APIs so that any change in the source APIs are also made to the merged API. Auto merges use `MergedApiExecutionRoleArn` to perform merge operations.
Type: String
Valid Values: `MANUAL_MERGE | AUTO_MERGE`
Required: No

## See Also
<a name="API_SourceApiAssociationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/SourceApiAssociationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/SourceApiAssociationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/SourceApiAssociationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

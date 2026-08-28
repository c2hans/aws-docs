---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_AttributeGroupSummary.html
---

# AttributeGroupSummary
<a name="API_app-registry_AttributeGroupSummary"></a>

Summary of a AWS Service Catalog AppRegistry attribute group.

## Contents
<a name="API_app-registry_AttributeGroupSummary_Contents"></a>

 ** arn **   <a name="servicecatalog-Type-app-registry_AttributeGroupSummary-arn"></a>
The Amazon resource name (ARN) that specifies the attribute group across services.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`
Required: No

 ** createdBy **   <a name="servicecatalog-Type-app-registry_AttributeGroupSummary-createdBy"></a>
The service principal that created the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!-)([a-z0-9-]+\.)+(aws\.internal|amazonaws\.com(\.cn)?)$`
Required: No

 ** creationTime **   <a name="servicecatalog-Type-app-registry_AttributeGroupSummary-creationTime"></a>
The ISO-8601 formatted timestamp of the moment the attribute group was created.
Type: Timestamp
Required: No

 ** description **   <a name="servicecatalog-Type-app-registry_AttributeGroupSummary-description"></a>
The description of the attribute group that the user provides.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** id **   <a name="servicecatalog-Type-app-registry_AttributeGroupSummary-id"></a>
The globally unique attribute group identifier of the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: No

 ** lastUpdateTime **   <a name="servicecatalog-Type-app-registry_AttributeGroupSummary-lastUpdateTime"></a>
The ISO-8601 formatted timestamp of the moment the attribute group was last updated. This time is the same as the creationTime for a newly created attribute group.
Type: Timestamp
Required: No

 ** name **   <a name="servicecatalog-Type-app-registry_AttributeGroupSummary-name"></a>
The name of the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: No

## See Also
<a name="API_app-registry_AttributeGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AttributeGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AttributeGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AttributeGroupSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

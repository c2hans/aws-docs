---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_AttributeGroup.html
---

# AttributeGroup
<a name="API_app-registry_AttributeGroup"></a>

Represents a AWS Service Catalog AppRegistry attribute group that is rich metadata which describes an application and its components.

## Contents
<a name="API_app-registry_AttributeGroup_Contents"></a>

 ** arn **   <a name="servicecatalog-Type-app-registry_AttributeGroup-arn"></a>
The Amazon resource name (ARN) that specifies the attribute group across services.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`
Required: No

 ** creationTime **   <a name="servicecatalog-Type-app-registry_AttributeGroup-creationTime"></a>
The ISO-8601 formatted timestamp of the moment the attribute group was created.
Type: Timestamp
Required: No

 ** description **   <a name="servicecatalog-Type-app-registry_AttributeGroup-description"></a>
The description of the attribute group that the user provides.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** id **   <a name="servicecatalog-Type-app-registry_AttributeGroup-id"></a>
The globally unique attribute group identifier of the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: No

 ** lastUpdateTime **   <a name="servicecatalog-Type-app-registry_AttributeGroup-lastUpdateTime"></a>
The ISO-8601 formatted timestamp of the moment the attribute group was last updated. This time is the same as the creationTime for a newly created attribute group.
Type: Timestamp
Required: No

 ** name **   <a name="servicecatalog-Type-app-registry_AttributeGroup-name"></a>
The name of the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: No

 ** tags **   <a name="servicecatalog-Type-app-registry_AttributeGroup-tags"></a>
Key-value pairs you can use to associate with the attribute group.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: No

## See Also
<a name="API_app-registry_AttributeGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AttributeGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AttributeGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AttributeGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

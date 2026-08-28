---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsItemRelatedItemsFilter.html
---

# OpsItemRelatedItemsFilter
<a name="API_OpsItemRelatedItemsFilter"></a>

Describes a filter for a specific list of related-item resources.

## Contents
<a name="API_OpsItemRelatedItemsFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-OpsItemRelatedItemsFilter-Key"></a>
The name of the filter key. Supported values include `ResourceUri`, `ResourceType`, or `AssociationId`.
Type: String
Valid Values: `ResourceType | AssociationId | ResourceUri`
Required: Yes

 ** Operator **   <a name="systemsmanager-Type-OpsItemRelatedItemsFilter-Operator"></a>
The operator used by the filter call. The only supported operator is `EQUAL`.
Type: String
Valid Values: `Equal`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-OpsItemRelatedItemsFilter-Values"></a>
The values for the filter.
Type: Array of strings
Required: Yes

## See Also
<a name="API_OpsItemRelatedItemsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsItemRelatedItemsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsItemRelatedItemsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsItemRelatedItemsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

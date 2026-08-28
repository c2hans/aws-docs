---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ComputationModelDataBindingUsageSummary.html
---

# ComputationModelDataBindingUsageSummary
<a name="API_ComputationModelDataBindingUsageSummary"></a>

A summary of how a specific data binding is used across computation models. This tracks dependencies between data sources and computation models, allowing you to understand the impact of changes to data sources.

## Contents
<a name="API_ComputationModelDataBindingUsageSummary_Contents"></a>

 ** computationModelIds **   <a name="iotsitewise-Type-ComputationModelDataBindingUsageSummary-computationModelIds"></a>
The list of computation model IDs that use this data binding. This allows identification of all computation models affected by changes to the referenced data source.
Type: Array of strings
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** matchedDataBinding **   <a name="iotsitewise-Type-ComputationModelDataBindingUsageSummary-matchedDataBinding"></a>
The data binding matched by the filter criteria. Contains details about specific data binding values used by the computation models.
Type: [MatchedDataBinding](API_MatchedDataBinding.md) object
Required: Yes

## See Also
<a name="API_ComputationModelDataBindingUsageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ComputationModelDataBindingUsageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ComputationModelDataBindingUsageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ComputationModelDataBindingUsageSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

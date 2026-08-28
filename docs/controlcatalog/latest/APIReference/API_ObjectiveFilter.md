---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ObjectiveFilter.html
---

# ObjectiveFilter
<a name="API_ObjectiveFilter"></a>

An optional filter that narrows the list of objectives to a specific domain.

## Contents
<a name="API_ObjectiveFilter_Contents"></a>

 ** Domains **   <a name="controlcatalog-Type-ObjectiveFilter-Domains"></a>
The domain that's used as filter criteria.
You can use this parameter to specify one domain ARN at a time. Passing multiple ARNs in the `ObjectiveFilter` isn’t supported.
Type: Array of [DomainResourceFilter](API_DomainResourceFilter.md) objects
Required: No

## See Also
<a name="API_ObjectiveFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ObjectiveFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ObjectiveFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ObjectiveFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controlcatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

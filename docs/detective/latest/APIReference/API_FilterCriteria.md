---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_FilterCriteria.html
---

# FilterCriteria
<a name="API_FilterCriteria"></a>

Details on the criteria used to define the filter for investigation results.

## Contents
<a name="API_FilterCriteria_Contents"></a>

 ** CreatedTime **   <a name="detective-Type-FilterCriteria-CreatedTime"></a>
Filter the investigation results based on when the investigation was created.
Type: [DateFilter](API_DateFilter.md) object
Required: No

 ** EntityArn **   <a name="detective-Type-FilterCriteria-EntityArn"></a>
Filter the investigation results based on the Amazon Resource Name (ARN) of the entity.
Type: [StringFilter](API_StringFilter.md) object
Required: No

 ** Severity **   <a name="detective-Type-FilterCriteria-Severity"></a>
Filter the investigation results based on the severity.
Type: [StringFilter](API_StringFilter.md) object
Required: No

 ** State **   <a name="detective-Type-FilterCriteria-State"></a>
Filter the investigation results based on the state.
Type: [StringFilter](API_StringFilter.md) object
Required: No

 ** Status **   <a name="detective-Type-FilterCriteria-Status"></a>
Filter the investigation results based on the status.
Type: [StringFilter](API_StringFilter.md) object
Required: No

## See Also
<a name="API_FilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/FilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/FilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/FilterCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

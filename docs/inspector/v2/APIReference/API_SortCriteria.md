---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_SortCriteria.html
---

# SortCriteria
<a name="API_SortCriteria"></a>

Details about the criteria used to sort finding results.

## Contents
<a name="API_SortCriteria_Contents"></a>

 ** field **   <a name="inspector2-Type-SortCriteria-field"></a>
The finding detail field by which results are sorted.
Type: String
Valid Values: `AWS_ACCOUNT_ID | FINDING_TYPE | SEVERITY | FIRST_OBSERVED_AT | LAST_OBSERVED_AT | FINDING_STATUS | RESOURCE_TYPE | ECR_IMAGE_PUSHED_AT | ECR_IMAGE_REPOSITORY_NAME | ECR_IMAGE_REGISTRY | NETWORK_PROTOCOL | COMPONENT_TYPE | VULNERABILITY_ID | VULNERABILITY_SOURCE | INSPECTOR_SCORE | VENDOR_SEVERITY | EPSS_SCORE`
Required: Yes

 ** sortOrder **   <a name="inspector2-Type-SortCriteria-sortOrder"></a>
The order by which findings are sorted.
Type: String
Valid Values: `ASC | DESC`
Required: Yes

## See Also
<a name="API_SortCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/SortCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/SortCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/SortCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

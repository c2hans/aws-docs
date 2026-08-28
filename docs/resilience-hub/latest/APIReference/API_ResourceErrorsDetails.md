---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ResourceErrorsDetails.html
---

# ResourceErrorsDetails
<a name="API_ResourceErrorsDetails"></a>

 A list of errors retrieving an application's resources.

## Contents
<a name="API_ResourceErrorsDetails_Contents"></a>

 ** hasMoreErrors **   <a name="resiliencehub-Type-ResourceErrorsDetails-hasMoreErrors"></a>
 This indicates if there are more errors not listed in the `resourceErrors` list.
Type: Boolean
Required: No

 ** resourceErrors **   <a name="resiliencehub-Type-ResourceErrorsDetails-resourceErrors"></a>
 A list of errors retrieving an application's resources.
Type: Array of [ResourceError](API_ResourceError.md) objects
Required: No

## See Also
<a name="API_ResourceErrorsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ResourceErrorsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ResourceErrorsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ResourceErrorsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ServiceActionDetail.html
---

# ServiceActionDetail
<a name="API_ServiceActionDetail"></a>

An object containing detailed information about the self-service action.

## Contents
<a name="API_ServiceActionDetail_Contents"></a>

 ** Definition **   <a name="servicecatalog-Type-ServiceActionDetail-Definition"></a>
A map that defines the self-service action.
Type: String to string map
Map Entries: Maximum number of 100 items.
Valid Keys: `Name | Version | AssumeRole | Parameters`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ServiceActionSummary **   <a name="servicecatalog-Type-ServiceActionDetail-ServiceActionSummary"></a>
Summary information about the self-service action.
Type: [ServiceActionSummary](API_ServiceActionSummary.md) object
Required: No

## See Also
<a name="API_ServiceActionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ServiceActionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ServiceActionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ServiceActionDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

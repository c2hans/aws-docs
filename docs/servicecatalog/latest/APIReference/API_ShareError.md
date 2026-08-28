---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ShareError.html
---

# ShareError
<a name="API_ShareError"></a>

Errors that occurred during the portfolio share operation.

## Contents
<a name="API_ShareError_Contents"></a>

 ** Accounts **   <a name="servicecatalog-Type-ShareError-Accounts"></a>
List of accounts impacted by the error.
Type: Array of strings
Pattern: `^[0-9]{12}$`
Required: No

 ** Error **   <a name="servicecatalog-Type-ShareError-Error"></a>
Error type that happened when processing the operation.
Type: String
Required: No

 ** Message **   <a name="servicecatalog-Type-ShareError-Message"></a>
Information about the error.
Type: String
Required: No

## See Also
<a name="API_ShareError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ShareError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ShareError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ShareError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

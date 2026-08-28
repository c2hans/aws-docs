---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ShareDetails.html
---

# ShareDetails
<a name="API_ShareDetails"></a>

Information about the portfolio share operation.

## Contents
<a name="API_ShareDetails_Contents"></a>

 ** ShareErrors **   <a name="servicecatalog-Type-ShareDetails-ShareErrors"></a>
List of errors.
Type: Array of [ShareError](API_ShareError.md) objects
Required: No

 ** SuccessfulShares **   <a name="servicecatalog-Type-ShareDetails-SuccessfulShares"></a>
List of accounts for whom the operation succeeded.
Type: Array of strings
Pattern: `^[0-9]{12}$`
Required: No

## See Also
<a name="API_ShareDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ShareDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ShareDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ShareDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

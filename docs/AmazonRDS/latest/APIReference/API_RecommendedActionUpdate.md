---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RecommendedActionUpdate.html
---

# RecommendedActionUpdate
<a name="API_RecommendedActionUpdate"></a>

The recommended status to update for the specified recommendation action ID.

## Contents
<a name="API_RecommendedActionUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ActionId **
A unique identifier of the updated recommendation action.
Type: String
Required: Yes

 ** Status **
The status of the updated recommendation action.
+  `applied`
+  `scheduled`
Type: String
Required: Yes

## See Also
<a name="API_RecommendedActionUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RecommendedActionUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RecommendedActionUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RecommendedActionUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

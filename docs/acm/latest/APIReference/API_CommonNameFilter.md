---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_CommonNameFilter.html
---

# CommonNameFilter
<a name="API_CommonNameFilter"></a>

Filters certificates by common name.

## Contents
<a name="API_CommonNameFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComparisonOperator **   <a name="ACM-Type-CommonNameFilter-ComparisonOperator"></a>
The comparison operator to use.
Type: String
Valid Values: `CONTAINS | EQUALS`
Required: Yes

 ** Value **   <a name="ACM-Type-CommonNameFilter-Value"></a>
The value to match against.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_CommonNameFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CommonNameFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CommonNameFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CommonNameFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

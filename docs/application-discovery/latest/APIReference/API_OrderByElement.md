---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_OrderByElement.html
---

# OrderByElement
<a name="API_OrderByElement"></a>

A field and direction for ordered output.

## Contents
<a name="API_OrderByElement_Contents"></a>

 ** fieldName **   <a name="DiscServ-Type-OrderByElement-fieldName"></a>
The field on which to order.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\s\S]*\S[\s\S]*`
Required: Yes

 ** sortOrder **   <a name="DiscServ-Type-OrderByElement-sortOrder"></a>
Ordering direction.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_OrderByElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/OrderByElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/OrderByElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/OrderByElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

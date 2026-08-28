---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PropertyPredicate.html
---

# PropertyPredicate
<a name="API_PropertyPredicate"></a>

Defines a property predicate.

## Contents
<a name="API_PropertyPredicate_Contents"></a>

 ** Comparator **   <a name="Glue-Type-PropertyPredicate-Comparator"></a>
The comparator used to compare this property to others.
Type: String
Valid Values: `EQUALS | GREATER_THAN | LESS_THAN | GREATER_THAN_EQUALS | LESS_THAN_EQUALS`
Required: No

 ** Key **   <a name="Glue-Type-PropertyPredicate-Key"></a>
The key of the property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Value **   <a name="Glue-Type-PropertyPredicate-Value"></a>
The value of the property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_PropertyPredicate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PropertyPredicate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PropertyPredicate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PropertyPredicate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

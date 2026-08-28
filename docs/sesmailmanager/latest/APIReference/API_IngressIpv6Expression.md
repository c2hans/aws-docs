---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressIpv6Expression.html
---

# IngressIpv6Expression
<a name="API_IngressIpv6Expression"></a>

The union type representing the allowed types for the left hand side of an IPv6 condition.

## Contents
<a name="API_IngressIpv6Expression_Contents"></a>

 ** Evaluate **   <a name="sesmailmanager-Type-IngressIpv6Expression-Evaluate"></a>
The left hand side argument of an IPv6 condition expression.
Type: [IngressIpv6ToEvaluate](API_IngressIpv6ToEvaluate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Operator **   <a name="sesmailmanager-Type-IngressIpv6Expression-Operator"></a>
The matching operator for an IPv6 condition expression.
Type: String
Valid Values: `CIDR_MATCHES | NOT_CIDR_MATCHES`
Required: Yes

 ** Values **   <a name="sesmailmanager-Type-IngressIpv6Expression-Values"></a>
The right hand side argument of an IPv6 condition expression.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 49.
Pattern: `(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))\/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])`
Required: Yes

## See Also
<a name="API_IngressIpv6Expression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressIpv6Expression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressIpv6Expression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressIpv6Expression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

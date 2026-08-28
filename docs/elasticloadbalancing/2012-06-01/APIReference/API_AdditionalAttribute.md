---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AdditionalAttribute.html
---

# AdditionalAttribute
<a name="API_AdditionalAttribute"></a>

Information about additional load balancer attributes.

## Contents
<a name="API_AdditionalAttribute_Contents"></a>

 ** Key **
The name of the attribute.
The following attribute is supported.
+  `elb.http.desyncmitigationmode` - Determines how the load balancer handles requests that might pose a security risk to your application. The possible values are `monitor`, `defensive`, and `strictest`. The default is `defensive`.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[a-zA-Z0-9.]+$`
Required: No

 ** Value **
This value of the attribute.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[a-zA-Z0-9.]+$`
Required: No

## See Also
<a name="API_AdditionalAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/AdditionalAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/AdditionalAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/AdditionalAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

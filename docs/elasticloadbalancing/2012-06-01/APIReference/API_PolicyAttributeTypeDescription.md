---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_PolicyAttributeTypeDescription.html
---

# PolicyAttributeTypeDescription
<a name="API_PolicyAttributeTypeDescription"></a>

Information about a policy attribute type.

## Contents
<a name="API_PolicyAttributeTypeDescription_Contents"></a>

 ** AttributeName **
The name of the attribute.
Type: String
Required: No

 ** AttributeType **
The type of the attribute. For example, `Boolean` or `Integer`.
Type: String
Required: No

 ** Cardinality **
The cardinality of the attribute.
Valid values:
+ ONE(1) : Single value required
+ ZERO\_OR\_ONE(0..1) : Up to one value is allowed
+ ZERO\_OR\_MORE(0..\*) : Optional. Multiple values are allowed
+ ONE\_OR\_MORE(1..\*0) : Required. Multiple values are allowed
Type: String
Required: No

 ** DefaultValue **
The default value of the attribute, if applicable.
Type: String
Required: No

 ** Description **
A description of the attribute.
Type: String
Required: No

## See Also
<a name="API_PolicyAttributeTypeDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/PolicyAttributeTypeDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/PolicyAttributeTypeDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/PolicyAttributeTypeDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

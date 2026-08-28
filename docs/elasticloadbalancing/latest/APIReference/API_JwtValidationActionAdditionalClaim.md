---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_JwtValidationActionAdditionalClaim.html
---

# JwtValidationActionAdditionalClaim
<a name="API_JwtValidationActionAdditionalClaim"></a>

Information about an additional claim to validate.

## Contents
<a name="API_JwtValidationActionAdditionalClaim_Contents"></a>

 ** Format **
The format of the claim value.
Type: String
Valid Values: `single-string | string-array | space-separated-values`
Required: Yes

 ** Name **
The name of the claim. You can't specify `exp`, `iss`, `nbf`, or `iat` because we validate them by default.
Type: String
Required: Yes

 ** Values.member.N **
The claim value. The maximum size of the list is 10. Each value can be up to 256 characters in length. If the format is `space-separated-values`, the values can't include spaces.
Type: Array of strings
Required: Yes

## See Also
<a name="API_JwtValidationActionAdditionalClaim_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/JwtValidationActionAdditionalClaim)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/JwtValidationActionAdditionalClaim)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/JwtValidationActionAdditionalClaim)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

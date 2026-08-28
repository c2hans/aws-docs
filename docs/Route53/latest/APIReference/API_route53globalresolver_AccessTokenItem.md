---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_AccessTokenItem.html
---

# AccessTokenItem
<a name="API_route53globalresolver_AccessTokenItem"></a>

Summary information about a token.

## Contents
<a name="API_route53globalresolver_AccessTokenItem_Contents"></a>

 ** arn **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessTokenItem-arn"></a>
The Amazon Resource Name (ARN) of the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
Required: Yes

 ** createdAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessTokenItem-createdAt"></a>
The date and time when the token was created.
Type: Timestamp
Required: Yes

 ** dnsViewId **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessTokenItem-dnsViewId"></a>
The ID of the DNS view associated with the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** expiresAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessTokenItem-expiresAt"></a>
The date and time when the token expires.
Type: Timestamp
Required: Yes

 ** globalResolverId **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessTokenItem-globalResolverId"></a>
The ID of the global resolver associated with the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessTokenItem-id"></a>
The unique identifier of the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessTokenItem-status"></a>
The current status of the token.
Type: String
Valid Values: `CREATING | OPERATIONAL | DELETING`
Required: Yes

 ** updatedAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessTokenItem-updatedAt"></a>
The date and time when the token was last updated.
Type: Timestamp
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessTokenItem-name"></a>
The name of the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

## See Also
<a name="API_route53globalresolver_AccessTokenItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/AccessTokenItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/AccessTokenItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/AccessTokenItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_AccessSourcesItem.html
---

# AccessSourcesItem
<a name="API_route53globalresolver_AccessSourcesItem"></a>

Summary information about an access source.

## Contents
<a name="API_route53globalresolver_AccessSourcesItem_Contents"></a>

 ** arn **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessSourcesItem-arn"></a>
The Amazon Resource Name (ARN) of the access source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
Required: Yes

 ** cidr **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessSourcesItem-cidr"></a>
The CIDR block that defines the IP address range for the access source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 43.
Required: Yes

 ** createdAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessSourcesItem-createdAt"></a>
The date and time when the access source was created.
Type: Timestamp
Required: Yes

 ** dnsViewId **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessSourcesItem-dnsViewId"></a>
The ID of the DNS view that the access source is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessSourcesItem-id"></a>
The unique identifier of the access source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** ipAddressType **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessSourcesItem-ipAddressType"></a>
The IP address type of the access source.
Type: String
Valid Values: `IPV4 | IPV6`
Required: Yes

 ** protocol **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessSourcesItem-protocol"></a>
The protocol used by the access source.
Type: String
Valid Values: `DO53 | DOH | DOT`
Required: Yes

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessSourcesItem-status"></a>
The current status of the access source.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`
Required: Yes

 ** updatedAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessSourcesItem-updatedAt"></a>
The date and time when the access source was last updated.
Type: Timestamp
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_AccessSourcesItem-name"></a>
The name of the access source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

## See Also
<a name="API_route53globalresolver_AccessSourcesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/AccessSourcesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/AccessSourcesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/AccessSourcesItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_TrafficPolicyInstance.html
---

# TrafficPolicyInstance
<a name="API_TrafficPolicyInstance"></a>

A complex type that contains settings for the new traffic policy instance.

## Contents
<a name="API_TrafficPolicyInstance_Contents"></a>

 ** HostedZoneId **   <a name="Route53-Type-TrafficPolicyInstance-HostedZoneId"></a>
The ID of the hosted zone that Amazon Route 53 created resource record sets in.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

 ** Id **   <a name="Route53-Type-TrafficPolicyInstance-Id"></a>
The ID that Amazon Route 53 assigned to the new traffic policy instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** Message **   <a name="Route53-Type-TrafficPolicyInstance-Message"></a>
If `State` is `Failed`, an explanation of the reason for the failure. If `State` is another value, `Message` is empty.
Type: String
Length Constraints: Maximum length of 1024.
Required: Yes

 ** Name **   <a name="Route53-Type-TrafficPolicyInstance-Name"></a>
The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance.
Type: String
Length Constraints: Maximum length of 1024.
Required: Yes

 ** State **   <a name="Route53-Type-TrafficPolicyInstance-State"></a>
The value of `State` is one of the following values:
Applied
Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Route 53 edge locations.
Creating
Route 53 is creating the resource record sets. Use `GetTrafficPolicyInstance` to confirm that the `CreateTrafficPolicyInstance` request completed successfully.
Failed
Route 53 wasn't able to create or update the resource record sets. When the value of `State` is `Failed`, see `Message` for an explanation of what caused the request to fail.
Type: String
Required: Yes

 ** TrafficPolicyId **   <a name="Route53-Type-TrafficPolicyInstance-TrafficPolicyId"></a>
The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** TrafficPolicyType **   <a name="Route53-Type-TrafficPolicyInstance-TrafficPolicyType"></a>
The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance.
Type: String
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`
Required: Yes

 ** TrafficPolicyVersion **   <a name="Route53-Type-TrafficPolicyInstance-TrafficPolicyVersion"></a>
The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** TTL **   <a name="Route53-Type-TrafficPolicyInstance-TTL"></a>
The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

## See Also
<a name="API_TrafficPolicyInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/TrafficPolicyInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/TrafficPolicyInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/TrafficPolicyInstance)

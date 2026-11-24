---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-security-posture.html
---

# Review security posture in API Portal

Each managed API has a **Security checklist** tab on its detail page (**API Portal**, **Managed APIs**, then choose an API). The checklist evaluates the API against a set of security postures. Each row shows a **Compliance status** of **Compliant**, **Non-compliant**, **Not applicable**, or **Insufficient data**, a **Reason**, and a **Last evaluated** time. Insufficient data means the posture couldn't be evaluated yet.

The postures that apply depend on the source service. Postures that don't describe the resource show Not applicable.

| Source service | Postures evaluated |
| --- | --- |
| API Gateway | Method authentication required, request validation enabled, API key required, stage throttling enabled (rate and burst limits set), stage response caching, stage AWS WAF web ACL associated, stage access logging enabled, private API resource policy configured, TLS 1.2 or later. |
| Application Load Balancer | AWS WAF web ACL associated with the load balancer, listener TLS 1.2 or later. |
| CloudFront | AWS WAF web ACL associated with the distribution, TLS 1.2 or later, no plaintext HTTP, access logging enabled, geo restriction configured. |

The **Reason** column explains the effect of a non-compliant item, for example that callers aren't identified and usage plan limits don't apply when no API key is required. After you change the resource, API Portal re-evaluates the posture when it next processes the resource's configuration; you can't trigger a re-evaluation on demand.

API Portal reports posture; it doesn't enforce it. AWS WAF is the enforcement layer. To protect an API that shows AWS WAF as disabled, associate a web ACL with its stage, load balancer, or distribution. For more information, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Security postures reference
<a name="apiportal-security-posture-reasons"></a>

API Portal evaluates the following postures from the AWS Config configuration items of each resource. Each finding has a posture ID, a status, and, when the posture isn't satisfied, a reason code. The AWS CLI and SDKs return these values in `GetManagedApi`.

| Status | Meaning |
| --- | --- |
| TRUE | The posture is satisfied (console: Compliant). |
| FALSE | The posture isn't satisfied (console: Non-compliant). See the reason code. |
| NOT\_APPLICABLE | The posture doesn't apply to this API, for example a caching check on a POST method, so it wasn't evaluated. |
| INSUFFICIENT\_DATA | No verdict could be reached, usually because the resource's configuration hasn't been read yet. |

### API Gateway REST API postures
<a name="apiportal-security-posture-reasons-apigw"></a>

| Posture (console name) | Satisfied when | Reason code | Remediation |
| --- | --- | --- | --- |
| APIGW\_METHOD\_AUTHENTICATION\_REQUIRED (Authentication) | The method's authorization type isn't NONE. OPTIONS methods are exempt. | AUTHENTICATION\_NOT\_CONFIGURED | Set an authorization type of AWS\_IAM, COGNITO\_USER\_POOLS, or CUSTOM, or attach an authorizer. |
| APIGW\_REQUEST\_VALIDATION\_ENABLED (Request validation) | A request validator is attached. Evaluated for POST, PUT, PATCH, and DELETE only. | REQUEST\_VALIDATION\_NOT\_ENABLED | Attach a request model and validator to methods that accept a body. |
| APIGW\_API\_KEY\_REQUIRED (API key required) | apiKeyRequired is true. OPTIONS methods are exempt. | API\_KEY\_NOT\_CONFIGURED | Require an API key on methods fronted by a usage plan. |
| APIGW\_STAGE\_THROTTLING\_ENABLED (Throttling) | The effective method settings have a rate limit and a burst limit greater than 0. | THROTTLING\_RATE\_LIMIT\_NOT\_SET, THROTTLING\_BURST\_LIMIT\_NOT\_SET | Set throttlingRateLimit and throttlingBurstLimit in the stage's method settings. |
| APIGW\_STAGE\_CACHING (API caching) | Caching is enabled for the method. Evaluated for GET and HEAD only. | RESPONSE\_CACHING\_NOT\_ENABLED | Enable caching in the stage's method settings where appropriate. |
| APIGW\_STAGE\_WAF\_ENABLED (WAF protection) | A web ACL is associated with the stage. | STAGE\_WAF\_NOT\_ASSOCIATED | Associate a AWS WAF web ACL with the stage. |
| APIGW\_STAGE\_ACCESS\_LOGGING (Logging) | The stage has an access log destination. | STAGE\_ACCESS\_LOGGING\_NOT\_ENABLED | Configure an access log destination on the stage. |
| APIGW\_PRIVATE\_RESOURCE\_POLICY (Resource policy) | A private REST API has a resource policy. Evaluated for private APIs only. | PRIVATE\_API\_RESOURCE\_POLICY\_MISSING | Attach a resource policy that restricts access to the intended VPC endpoints. |
| APIGW\_REST\_API\_TLS\_1\_2\_MINIMUM (Commercial-grade TLS) | The REST API's security policy is one of: SecurityPolicy\_TLS13\_1\_3\_2025\_09, SecurityPolicy\_TLS13\_1\_3\_FIPS\_2025\_09, SecurityPolicy\_TLS13\_1\_2\_FIPS\_PFS\_PQ\_2025\_09, SecurityPolicy\_TLS13\_1\_2\_PFS\_PQ\_2025\_09, SecurityPolicy\_TLS13\_1\_2\_FIPS\_PQ\_2025\_09, SecurityPolicy\_TLS13\_2025\_EDGE, SecurityPolicy\_TLS12\_PFS\_2025\_EDGE. | REST\_API\_TLS\_BELOW\_1\_2 | Change the REST API's security policy to one that meets the Commercial-grade TLS bar. |

### Application Load Balancer postures
<a name="apiportal-security-posture-reasons-alb"></a>

| Posture (console name) | Satisfied when | Reason code | Remediation |
| --- | --- | --- | --- |
| ALB\_INTERNET\_FACING\_REQUIRES\_WAF (WAF protection) | An internet-facing load balancer has a web ACL associated. Internal load balancers are exempt. | LOAD\_BALANCER\_WAF\_NOT\_ASSOCIATED | Associate a AWS WAF web ACL with the load balancer, or make it internal. |
| ALB\_LISTENER\_TLS\_1\_2\_MINIMUM (Commercial-grade TLS) | An HTTPS listener uses one of: ELBSecurityPolicy-TLS13-1-3-2021-06, ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04, ELBSecurityPolicy-TLS13-1-3-PQ-2025-09, ELBSecurityPolicy-TLS13-1-3-FIPS-PQ-2025-09, ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09, ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09, ELBSecurityPolicy-TLS13-1-2-PQ-2025-09, ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09, ELBSecurityPolicy-TLS13-1-3-RFC9151-FIPS-2023-07, ELBSecurityPolicy-TLS13-1-2-RFC9151-FIPS-2023-07, ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP1-FIPS-2023-07, ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07. | LISTENER\_TLS\_BELOW\_1\_2 | Change the listener's SSL policy to one that meets the Commercial-grade TLS bar. |

### CloudFront postures
<a name="apiportal-security-posture-reasons-cf"></a>

| Posture (console name) | Satisfied when | Reason code | Remediation |
| --- | --- | --- | --- |
| CLOUDFRONT\_TLS\_1\_2\_MINIMUM (Commercial-grade TLS) | The viewer certificate's minimum protocol version is TLSv1.2\_2025 or TLSv1.3\_2025. Distributions using the default CloudFront certificate are exempt, because CloudFront fixes their policy. | DISTRIBUTION\_TLS\_BELOW\_1\_2 | Use a custom certificate and set the security policy to TLSv1.2\_2025 or TLSv1.3\_2025. |
| CLOUDFRONT\_WAF\_ENABLED (WAF protection) | A web ACL is associated with the distribution. | DISTRIBUTION\_WAF\_NOT\_ASSOCIATED | Associate a AWS WAF web ACL with the distribution. |
| CLOUDFRONT\_HTTPS\_ONLY (HTTPS required) | The default cache behavior's viewer protocol policy is https-only or redirect-to-https. | DISTRIBUTION\_SERVES\_PLAINTEXT\_HTTP | Set the viewer protocol policy to https-only or redirect-to-https. |
| CLOUDFRONT\_LOGGING\_ENABLED (Logging) | Standard logging is enabled. | DISTRIBUTION\_ACCESS\_LOGGING\_NOT\_ENABLED | Enable standard access logging on the distribution. |
| CLOUDFRONT\_GEO\_RESTRICTION (Geo-restriction) | A geographic allowlist or blocklist is configured. | GEO\_RESTRICTION\_NOT\_CONFIGURED | Configure a geo-restriction if the service is limited to specific countries. |

The Commercial-grade TLS postures require TLS 1.2 or later with forward-secret (ECDHE) key exchange and no SHA-1 or SHA-224 in the handshake, matching the corresponding Security Hub CSPM controls. New reason codes may be added over time; treat any value you don't recognize as `UNKNOWN`.

## AWS WAF API Security findings
<a name="apiportal-security-posture-waf-api-security"></a>

When you add the AWS WAF API Security managed rule group to the web ACLs that protect your APIs, API Portal shows the threats that API Security detects for each managed API, so the view that shows an unprotected API also shows the activity against it. Associating a web ACL alone isn't enough; the API Security managed rule group must be enabled on it. API Portal shows events for the individual managed API (method and path); the AWS WAF console shows them for the protected resource as a whole. Each event names the detection and its confidence, for example a caller enumerating object IDs to read other users' records (broken object level authorization), a tampered or unsigned token in the `Authorization` header, credential stuffing, or reconnaissance such as probing for routes that your API doesn't serve. For more information, see [API Security](https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security.html) in the *AWS WAF Developer Guide*.

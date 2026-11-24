---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-api-security.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF API Security rule group

This section explains what the AWS WAF API Security managed rule group does.

VendorName: `AWS`, Name: `AWSManagedRulesAPISecurityRuleSet`, Version: `AWSManagedRulesAPISecurityRuleSet-V1-0`, WCU: 500

**Note**
This documentation covers the most recent static version release of this managed rule group. We report version changes in the changelog log at [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md). For information about other versions, use the API command [DescribeManagedRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_DescribeManagedRuleGroup.html).
The information that we publish for the rules in the AWS Managed Rules rule groups is intended to provide you with what you need to use the rules without giving bad actors what they need to circumvent the rules.
If you need more information than you find here, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/).

The AWS WAF API Security managed rule group labels and manages requests that abuse your APIs. It does this two ways: deterministic rules that decide on the contents of a single request, and behavioral rules, one for each detection at each confidence, that act on findings produced by scoring a client's activity across your endpoints against a learned baseline.

The deterministic rules identify issues that can be detected from a single request such as JSON Web Token attack constructs, where the token itself is evidence of an attack rather than of a misconfiguration, token posture observations and schema discovery. The behavioral detections cover threats such as object level authorization abuse, enumeration, credential stuffing from the `Authorization` header, and route and parameter fuzzing. Each behavioral finding requires several independent classes of evidence to agree before it emits, and emits at one of the confidence levels.

The rule group evaluates requests. It does not inspect the content of your application's responses at this time. The behavioral findings do take account of the status codes your application returns, such as a client's rate of denied or failed requests, as evidence about that client's requests.

## Considerations for using this rule group
<a name="aws-managed-rule-groups-api-security-using"></a>

This rule group requires no configuration of its own. You add it with a plain managed rule group reference statement, and tune it with rule action overrides and a scope-down statement. For guidance, see [AWS WAF API Security](waf-api-security.md).

This rule group is part of the intelligent threat mitigation protections in AWS WAF. For information, see [Intelligent threat mitigation in AWS WAF](waf-managed-protections.md).

**Note**
You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

To keep your costs down and to be sure you're managing your web traffic as you want, use this rule group in accordance with the guidance at [Best practices for intelligent threat mitigation in AWS WAF](waf-managed-protections-best-practices.md).

**Resource type support.** This rule group is supported for protection packs (web ACLs) that protect Amazon CloudFront distributions, Application Load Balancers, and Amazon API Gateway REST APIs. This rule group isn't available for use with AWS AppSync GraphQL APIs, Amazon Cognito user pools, AWS App Runner services, Amazon Bedrock AgentCore Gateways, AWS Verified Access instances or AWS Amplify apps at this time. If you try to associate a protection pack (web ACL) that uses this rule group with one of these resources, AWS WAF rejects the request with a `WAFInvalidOperationException` and the message "A web ACL that uses the AWSManagedRulesAPISecurityRuleSet managed rule group can only be associated with an Application Load Balancer, an Amazon API Gateway REST API or an Amazon CloudFront distribution. Choose a different web ACL, or remove the managed rule group from the web ACL."

**The behavioral detections need a baseline before they can fire.** The behavioral half of this rule group compares a client's activity against the normal pattern of activity for the endpoints it is using, and that pattern has to be learned first. AWS WAF learns a baseline for each protected resource and refreshes it automatically, at least every 12 hours and sooner on high-traffic resources. Plan for about a day of typical traffic before the first baseline is available, and expect the behavioral detections to become more accurate over the first one to two weeks. Traffic drops out of the baseline after about two weeks. An endpoint is modeled individually only once it receives enough successful requests over the trailing two weeks, so endpoints with very little traffic are not. The deterministic rules need no baseline and are effective from the first request. For deployment guidance, see [Testing and deploying AWS WAF API Security](waf-api-security-deploying.md).

**AWS WAF does not verify token signatures.** The deterministic rules in this rule group identify attack constructs in the *structure* of a JSON Web Token, such as an algorithm of `none`, an empty or degenerate signature, a key embedded in the token, or injection in a key identifier. They do not validate a signature against a key, so a token that is well formed and carries a signature that is simply wrong is not detected by this rule group. Validating signatures remains your application's responsibility. The rule group also does not inspect encrypted tokens, and reads tokens only from the `Authorization` header, so a token carried in a cookie value or in the request body is not inspected.

**Behavioral findings are probabilistic.** A behavioral finding means that a client's activity deviated from the established pattern for the endpoints it accessed, in a combination of evidence that the rule group could not explain through normal use. It does not mean an attack has been confirmed. Confidence reflects how much benign traffic the combination of evidence ruled out, rather than how closely the traffic resembled a known attack: high rules out the known benign explanations, medium leaves at least one fitting, and low rules out none. That is why only the high tier blocks by default. We continuously test and update our analysis methods to increase accuracy. Treat a finding as a risk indicator and validate the rule group's behavior against your own traffic in count mode before you enforce.

**High confidence also requires that AWS WAF can identify the caller.** AWS WAF identifies a client by its source IP address together with a hash of the request's authentication header. When a request carries no credential that AWS WAF can hash, the client is identified by source IP address alone, and a finding that would otherwise be high confidence is reported as medium instead. Requests from a client that does not authenticate therefore never reach the high tier, whatever the evidence.

Take this into account when you test. Traffic you generate yourself, from a script or a test host without your application's credentials, is identified by IP address alone and will not produce a high-confidence behavioral finding. Test with credentials your API accepts if you want to see the behavior your real clients will produce.

## Labels added by this rule group
<a name="aws-managed-rule-groups-api-security-labels"></a>

This managed rule group adds labels to the web requests that it evaluates, which are available to rules that run after this rule group in your protection pack (web ACL). AWS WAF also records the labels to Amazon CloudWatch metrics. For general information about labels and label metrics, see [Web request labeling in AWS WAF](waf-labels.md) and [Label metrics and dimensions](waf-metrics.md#waf-metrics-label).

This rule group does not use AWS WAF token management, so it adds no token labels and requires no application integration SDK. A reader arriving from the Bot Control or Fraud Control documentation should expect neither.

All labels begin with the rule group's namespace, `awswaf:managed:aws:api-security:`, and every detection label carries a stage as its first segment: `attack` for exploitation, `recon` for probing that has not exploited anything, and `warning` for a posture observation not attributable to an attacker. The `not_supported` label has no stage.

**The rule group's label families use different shapes after the stage, and a rule written against the wrong one never matches.** The identity labels are described in [Identity labels](#aws-managed-rule-groups-api-security-identity-labels); the two shapes a detection uses are these.

```text
behavioral    awswaf:managed:aws:api-security:<stage>:<finding>:<confidence>
deterministic awswaf:managed:aws:api-security:<stage>:<check>[:<location>]
```

A behavioral label always ends in a confidence, so you can match a stage and finding as a label prefix and catch all of its confidences in one rule. A deterministic label does not have confidence segment. Instead it names the specific check, and usually the part of the token it inspected, such as `jwt_header`, `jwt_payload` or `jwt_signature`. Some deterministic labels have no location segment: `warning:unsafe_method` and `recon:path_schema`.

**Labels.** Every deterministic rule adds exactly one label, and the following rules listing gives the label for each. The behavioral rules add none: they act on labels the behavioral analysis adds. **The rule group publishes more labels than its rules match.**

The deterministic rules contribute one label per rule. The rule group also publishes behavioral labels, and `not_supported` for requests the rule group does not send for behavioral analysis. Not every behavioral label occurs at every confidence.

### Identity labels
<a name="aws-managed-rule-groups-api-security-identity-labels"></a>

The identity labels attribute a conclusion to the client rather than to the request it sent, which is what makes them useful for a rule that should follow an actor across your endpoints. They are surface-scoped: every other label in this rule group describes one request against one endpoint.

A label attaches to the identity when that identity trips any endpoint-scoped detection, and it carries the tier of the detection that triggered it rather than a tier of its own. Route probing and credential stuffing are evaluated across the caller's activity on the whole protection pack (web ACL) rather than per endpoint, so they do not set these labels. Each label is held on a sliding window of about five minutes, which resets if the identity trips another detection and expires if it does not.

**Identity label meanings**

| Label | Meaning |
| --- | --- |
| `awswaf:managed:aws:api-security:recon:actor_identity:<high\|medium\|low>` | This identity tripped a `recon` stage detection somewhere on the protection pack (web ACL), at this tier. Carried on every later request from the identity until it expires |
| `awswaf:managed:aws:api-security:attack:actor_identity:<high\|medium\|low>` | This identity tripped an `attack` stage detection somewhere on the protection pack (web ACL), at this tier. Carried on every later request from the identity until it expires |

`APISecurityActorIdentityHigh` blocks every request that carries either identity label at high confidence. So once a caller trips a high-confidence detection on one endpoint, the rule group blocks its later requests to any endpoint on the protection pack (web ACL) until the label expires. `APISecurityActorIdentityMedium` and `APISecurityActorIdentityLow` count. A caller identified by IP address alone never reaches high confidence, so these rules never block it.

## API Security rules listing
<a name="aws-managed-rule-groups-api-security-rules"></a>

The deterministic rules decide on the contents of a single request and need no baseline. Most deterministic rules block by default. The token rules read the token from the `Authorization` header.

For the deterministic rules, the stage and the default action agree. All `attack` stage rules block, and all `warning` and `recon` stage rules count.

**Deterministic rules**

| Rule name | What it looks for | Default action | Label added |
| --- | --- | --- | --- |
| FixedAlgSignatureLengthMismatch\_JWT\_Signature | A signature whose length does not match the one its declared algorithm produces | Block | attack:fixed\_alg\_signature\_length\_mismatch:jwt\_signature |
| AlgNone\_JWT\_Header | A header `alg` of `none`, which tells the verifier the token is unsigned | Block | attack:alg\_none:jwt\_header |
| MissingAlg\_JWT\_Header | A token carrying a signature but no `alg` claim to verify it against | Block | attack:missing\_alg:jwt\_header |
| EmbeddedCertChain\_JWT\_Header | An `x5c` certificate chain embedded in the header, so the sender supplies the verification key | Block | attack:embedded\_cert\_chain:jwt\_header |
| EmbeddedJwk\_JWT\_Header | A `jwk` key embedded in the header, with the same effect | Block | attack:embedded\_jwk:jwt\_header |
| CommandInjection\_JWT | Shell metacharacters or command substitution in the `kid` header parameter or the `role` or `scope` claim | Block | attack:command\_injection:jwt |
| PathTraversal\_JWT\_Header | Path traversal sequences in the `kid`, aimed at the verifier's key lookup | Block | attack:path\_traversal:jwt\_header |
| SQLInjection\_JWT | SQL injection constructs in the `kid` header parameter or the `sub` claim | Block | attack:sql\_injection:jwt |
| RemoteCertUrl\_JWT\_Header | An `x5u` remote certificate URL, pointing the verifier at a key the sender controls | Block | attack:remote\_cert\_url:jwt\_header |
| RemoteJwkUrl\_JWT\_Header | A `jku` remote key-set URL, with the same effect | Block | attack:remote\_jwk\_url:jwt\_header |
| UnsignedToken\_JWT | A bearer token presented with no signature segment | Block | attack:unsigned\_token:jwt |
| InvalidFourSegmentCompact\_JWT | A compact-serialization token with four segments, which is not a valid JWS | Block | attack:invalid\_four\_segment\_compact:jwt |
| Log4j\_JWT\_Payload | A JNDI lookup expression in the `sub` or `resource` claim | Block | attack:log4j:jwt\_payload |
| Method\_Unsafe\_Method | A request using TRACE or TRACK | Count | warning:unsafe\_method |
| OversizedToken\_JWT | A bearer token beyond a size ceiling, which usually means claims are being carried that do not belong in a token | Count | warning:oversized\_token:jwt |
| AlgWhitespace\_JWT\_Header | Whitespace inside the `alg` value, used to slip past an exact-match allow list | Block | attack:alg\_whitespace:jwt\_header |
| EcdsaPsychicSignature\_JWT\_Signature | An ECDSA signature of all zeros, which some verifiers accept as valid | Block | attack:ecdsa\_psychic\_signature:jwt\_signature |
| UnregisteredAlg\_JWT\_Header | An `alg` value outside the registered algorithm set | Count | warning:unregistered\_alg:jwt\_header |
| MissingExpiry\_JWT\_Payload | A token with no `exp` claim, so it does not expire on its own | Count | warning:missing\_expiry:jwt\_payload |
| MissingIssuer\_JWT\_Payload | A token with no `iss` claim, so the verifier cannot confirm who issued it | Count | warning:missing\_issuer:jwt\_payload |
| PrivilegedClaim\_JWT\_Payload | A privileged value in a role, scope, subject, permissions, admin, superuser or groups claim | Count | warning:privileged\_claim:jwt\_payload |
| Path\_SchemaDiscovery\_UriPath | A request to a path that serves the API's own schema, specification or an interactive query console, or an environment or repository configuration file | Count | recon:path\_schema |
| UndersizedSignature\_JWT\_Signature | A signature shorter than any registered algorithm produces | Count | warning:undersized\_signature:jwt\_signature |
| CriticalExtension\_JWT\_Header | A `crit` header parameter, which asks the verifier to reject the token unless it understands an extension | Count | warning:critical\_extension:jwt\_header |
| CompressionInJws\_JWT\_Header | A `zip` header parameter on a signed token, which is not defined for JWS | Count | warning:compression\_in\_jws:jwt\_header |
| FarFutureExpiry\_JWT\_Payload | An `exp` claim set implausibly far into the future | Count | warning:far\_future\_expiry:jwt\_payload |
| NonCanonicalBase64Url\_JWT | A token whose segments are not canonical base64url, used to produce two readings of one token | Count | warning:non\_canonical\_base64\_url:jwt |

The behavioral rules provide one rule for each of the behavioral detections and one for the identity labels, at each of the confidence levels. Each matches the reconnaissance and attack labels of its detection at its own confidence, with these exceptions: the path fuzzing and args fuzzing rules match reconnaissance labels only, and the enumeration rules match reconnaissance labels only at low and medium confidence. Because each rule covers one detection at one confidence, you can override the action for one detection at one confidence, such as `APISecurityCredStuffingHigh`, without changing any other. The high-confidence rules block by default, and the medium and low ones count. High means the combination of evidence ruled out the known benign explanations, medium that at least one benign explanation still fits, and low that an anomaly is present that rules out no common benign flow.

These rules add no label of their own. They match labels that the behavioral analysis added earlier in the request, so there is no `awswaf:managed:aws:api-security:high` label for you to match in a rule of your own.

**Behavioral rules**

| Rule name | What it matches | Default action |
| --- | --- | --- |
| APISecurityObjectLevelLow | Object level authorization abuse at low confidence: `attack:object_level:low`, `recon:object_level:low` | Count |
| APISecurityObjectLevelMedium | Object level authorization abuse at medium confidence: `attack:object_level:medium`, `recon:object_level:medium` | Count |
| APISecurityObjectLevelHigh | Object level authorization abuse at high confidence: `attack:object_level:high`, `recon:object_level:high` | Block |
| APISecurityCredStuffingLow | Credential stuffing against the `Authorization` header at low confidence: `attack:cred_stuffing:low`, `recon:cred_stuffing:low` | Count |
| APISecurityCredStuffingMedium | Credential stuffing against the `Authorization` header at medium confidence: `attack:cred_stuffing:medium`, `recon:cred_stuffing:medium` | Count |
| APISecurityCredStuffingHigh | Credential stuffing against the `Authorization` header at high confidence: `attack:cred_stuffing:high`, `recon:cred_stuffing:high` | Block |
| APISecurityPathFuzzingLow | Hidden-route probing at low confidence: `recon:path_fuzzing:low` | Count |
| APISecurityPathFuzzingMedium | Hidden-route probing at medium confidence: `recon:path_fuzzing:medium` | Count |
| APISecurityPathFuzzingHigh | Hidden-route probing at high confidence: `recon:path_fuzzing:high` | Block |
| APISecurityArgsFuzzingLow | Parameter fuzzing at low confidence: `recon:args_fuzzing:low` | Count |
| APISecurityArgsFuzzingMedium | Parameter fuzzing at medium confidence: `recon:args_fuzzing:medium` | Count |
| APISecurityArgsFuzzingHigh | Parameter fuzzing at high confidence: `recon:args_fuzzing:high` | Block |
| APISecurityEnumerationLow | Enumeration at low confidence, reconnaissance stage only: `recon:enumeration:low` | Count |
| APISecurityEnumerationMedium | Enumeration at medium confidence, reconnaissance stage only: `recon:enumeration:medium` | Count |
| APISecurityEnumerationHigh | Enumeration at high confidence: `recon:enumeration:high`, `attack:enumeration:high` | Block |
| APISecurityActorIdentityLow | The identity labels at low confidence, carried by a caller that tripped a detection earlier: `attack:actor_identity:low`, `recon:actor_identity:low` | Count |
| APISecurityActorIdentityMedium | The identity labels at medium confidence, carried by a caller that tripped a detection earlier: `attack:actor_identity:medium`, `recon:actor_identity:medium` | Count |
| APISecurityActorIdentityHigh | The identity labels at high confidence, carried by a caller that tripped a detection earlier: `attack:actor_identity:high`, `recon:actor_identity:high` | Block |

Each label combines a stage, a detection, and a confidence level of high, medium, or low. Not every detection is reported at every stage or at every confidence level. The stage says how far the caller's activity has gone: `recon` for mapping or probing your API, and `attack` for stronger evidence of abuse, such as your API starting to refuse the caller's requests. The final column says what the rule group does with the label by default. Where it says label only, no rule in the rule group acts on the label; to act on it, add your own label match rule after the rule group.

**Behavioral detection labels**

| Label | Behavior it catches | Default action in this rule group |
| --- | --- | --- |
| `awswaf:managed:aws:api-security:recon:object_level:<high\|medium\|low>` | A caller walking object identifiers to harvest records that belong to other users | Block at high (`APISecurityObjectLevelHigh`). Count at medium and low |
| `awswaf:managed:aws:api-security:recon:enumeration:<high\|medium\|low>` | Systematically discovering valid identifiers | Block at high (`APISecurityEnumerationHigh`). Count at medium and low |
| `awswaf:managed:aws:api-security:recon:args_fuzzing:<high\|medium\|low>` | A caller adding URL parameters never seen on an endpoint, such as `?admin=true` or `?debug=1`, to find hidden features or weak input checks | Block at high (`APISecurityArgsFuzzingHigh`). Count at medium and low |
| `awswaf:managed:aws:api-security:recon:cred_stuffing:<high\|medium\|low>` | Credential stuffing and token guessing against credentials sent in the `Authorization` header | Block at high (`APISecurityCredStuffingHigh`). Count at medium and low |
| `awswaf:managed:aws:api-security:recon:path_fuzzing:<high\|medium\|low>` | A caller that keeps requesting routes never seen in normal traffic and keeps receiving errors | Block at high (`APISecurityPathFuzzingHigh`). Count at medium and low |
| `awswaf:managed:aws:api-security:attack:object_level:<high\|medium\|low>` | A caller walking object identifiers to harvest records that belong to other users | Block at high (`APISecurityObjectLevelHigh`). Count at medium and low |
| `awswaf:managed:aws:api-security:attack:enumeration:<high\|medium\|low>` | Systematically discovering valid identifiers | Block at high (`APISecurityEnumerationHigh`). **Label only** at medium and low: no rule in the rule group acts on it |
| `awswaf:managed:aws:api-security:attack:cred_stuffing:<high\|medium\|low>` | Credential stuffing and token guessing against credentials sent in the `Authorization` header | Block at high (`APISecurityCredStuffingHigh`). Count at medium and low |
| `awswaf:managed:aws:api-security:recon:actor_identity:<high\|medium\|low>` | This identity tripped a `recon` stage detection somewhere on the protection pack (web ACL), at this tier. Carried on every later request from the identity until it expires | Block at high (`APISecurityActorIdentityHigh`). Count at medium and low |
| `awswaf:managed:aws:api-security:attack:actor_identity:<high\|medium\|low>` | This identity tripped an `attack` stage detection somewhere on the protection pack (web ACL), at this tier. Carried on every later request from the identity until it expires | Block at high (`APISecurityActorIdentityHigh`). Count at medium and low |

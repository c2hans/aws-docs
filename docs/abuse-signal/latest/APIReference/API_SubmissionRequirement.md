---
source_url: https://docs.aws.amazon.com/abuse-signal/latest/APIReference/API_SubmissionRequirement.html
---

# SubmissionRequirement

Describes one specific submission requirement that a well-formed report did not meet. The service returns this structure in the `unmetRequirements` list of a `SubmissionRequirementException` (HTTP 422).

## Contents
<a name="API_SubmissionRequirement_Contents"></a>

 ** message **   <a name="abusesignal-Type-SubmissionRequirement-message"></a>
A detailed, human-readable description of the unmet submission requirement.
Type: String
Required: Yes

 ** path **   <a name="abusesignal-Type-SubmissionRequirement-path"></a>
A JSON Pointer expression to the report member that did not meet the requirement. An empty string refers to the report as a whole.
Type: String
Required: Yes

 ** code **   <a name="abusesignal-Type-SubmissionRequirement-code"></a>
A stable, dot-namespaced identifier for the submission requirement that the report did not meet (for example, `rule.timestamp.too_old`). The set of codes is append-only, so treat an unrecognized value as opaque. This value is absent when the requirement that the report did not meet does not publish an identifier.
The service checks the following submission requirements:
+  `rule.source_identifier.too_long` (`source_identifier`) – The value exceeds the maximum accepted length of 253 characters (the DNS hostname limit).
+  `rule.source_identifier.forbidden_characters` (`source_identifier`) – The value contains characters that are never valid in an address (`{`, `}`, `*`, or ```). These are common template-injection and command-injection markers.
+  `rule.source_identifier.malformed` (`source_identifier`) – The value is not a valid IPv4 address, IPv6 address, URL, or domain name.
+  `rule.timestamp.unparseable` (`timestamp`) – The value could not be parsed as an RFC 3339 date-time.
+  `rule.timestamp.in_future` (`timestamp`) – The value is dated further into the future than the accepted clock-skew tolerance (a default of 1 hour).
+  `rule.timestamp.too_old` (`timestamp`) – The value predates the submission lookback window (a default of 90 days). For content that is still accessible, set `timestamp` to the time you most recently observed it.
+  `rule.evidence.content_type_mismatch` (`evidence`) – The decoded payload of an evidence item does not match its declared `content_type`. The `path` identifies the item, for example `/evidence/0`.
Submission requirement thresholds are configuration-driven and can change over time. The set of codes is append-only, so treat an unrecognized code as opaque.
Type: String
Required: No

## See Also
<a name="API_SubmissionRequirement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/abuse-signal-2026-01-12/SubmissionRequirement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/abuse-signal-2026-01-12/SubmissionRequirement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/abuse-signal-2026-01-12/SubmissionRequirement)

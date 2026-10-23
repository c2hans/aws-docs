---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_PrevalidationSignal.html
---

# PrevalidationSignal
<a name="API_PrevalidationSignal"></a>

One producer's conclusion about one subject on one scoring dimension.

## Contents
<a name="API_PrevalidationSignal_Contents"></a>

 ** computed **   <a name="continuum-Type-PrevalidationSignal-computed"></a>
Deterministic values the producer computed from its assessment, as distinct from the assessment itself.
Type: [SignalComputation](API_SignalComputation.md) object
Required: No

 ** conclusion **   <a name="continuum-Type-PrevalidationSignal-conclusion"></a>
The conclusion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** confidence **   <a name="continuum-Type-PrevalidationSignal-confidence"></a>
The confidence.
Type: Double
Required: No

 ** confidenceReasoning **   <a name="continuum-Type-PrevalidationSignal-confidenceReasoning"></a>
A producer's structured rationale for a signal's confidence.
Type: [SignalConfidenceReasoning](API_SignalConfidenceReasoning.md) object
Required: No

 ** dimension **   <a name="continuum-Type-PrevalidationSignal-dimension"></a>
The dimension.
Type: String
Valid Values: `EXPLOITABILITY | BLAST_RADIUS | NETWORK_EXPOSURE | PRECONDITION | CODE_CONTEXT | LIKELIHOOD_ASSESSMENT | IMPACT_ASSESSMENT`
Required: No

 ** exploitability **   <a name="continuum-Type-PrevalidationSignal-exploitability"></a>
What validation established about exploitability, as summarized onto the scoring signal derived from it.
Type: [SignalExploitability](API_SignalExploitability.md) object
Required: No

 ** impactDimensions **   <a name="continuum-Type-PrevalidationSignal-impactDimensions"></a>
The three impact dimensions an impact signal assessed. The computed impact band is derived from attackerGains and blastRadius, then shifted by targetValue.
Type: [SignalImpactDimensions](API_SignalImpactDimensions.md) object
Required: No

 ** preconditions **   <a name="continuum-Type-PrevalidationSignal-preconditions"></a>
The four preconditions a likelihood signal assessed.
Type: [SignalPreconditions](API_SignalPreconditions.md) object
Required: No

 ** producerId **   <a name="continuum-Type-PrevalidationSignal-producerId"></a>
The identifier of the producer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_.-]{0,127}`
Required: No

 ** producerVersion **   <a name="continuum-Type-PrevalidationSignal-producerVersion"></a>
The producer Version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** signalStrength **   <a name="continuum-Type-PrevalidationSignal-signalStrength"></a>
The signal Strength.
Type: String
Valid Values: `NONE | WEAK | MODERATE | STRONG`
Required: No

 ** subjectRef **   <a name="continuum-Type-PrevalidationSignal-subjectRef"></a>
The subject Ref.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_PrevalidationSignal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/PrevalidationSignal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/PrevalidationSignal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/PrevalidationSignal)

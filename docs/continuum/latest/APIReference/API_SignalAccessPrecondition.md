---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_SignalAccessPrecondition.html
---

# SignalAccessPrecondition
<a name="API_SignalAccessPrecondition"></a>

The assessed access-level precondition with the basis behind it.

## Contents
<a name="API_SignalAccessPrecondition_Contents"></a>

 ** basis **   <a name="continuum-Type-SignalAccessPrecondition-basis"></a>
The basis.
Type: String
Valid Values: `CODE | GRAPH | FINDING | INFERRED | NO_EVIDENCE_DEFAULT`
Required: No

 ** missingInfo **   <a name="continuum-Type-SignalAccessPrecondition-missingInfo"></a>
The missing Info.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** reason **   <a name="continuum-Type-SignalAccessPrecondition-reason"></a>
The reason.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** value **   <a name="continuum-Type-SignalAccessPrecondition-value"></a>
The value.
Type: String
Valid Values: `NONE | ANY_AUTHENTICATED | PRIVILEGED`
Required: No

## See Also
<a name="API_SignalAccessPrecondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/SignalAccessPrecondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/SignalAccessPrecondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/SignalAccessPrecondition)

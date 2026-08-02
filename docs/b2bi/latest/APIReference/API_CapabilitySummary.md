---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CapabilitySummary.html
---

# CapabilitySummary
<a name="API_CapabilitySummary"></a>

Returns the capability summary details. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

## Contents
<a name="API_CapabilitySummary_Contents"></a>

 ** capabilityId **   <a name="b2bi-Type-CapabilitySummary-capabilityId"></a>
Returns a system-assigned unique identifier for the capability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** createdAt **   <a name="b2bi-Type-CapabilitySummary-createdAt"></a>
Returns a timestamp for creation date and time of the capability.
Type: Timestamp
Required: Yes

 ** name **   <a name="b2bi-Type-CapabilitySummary-name"></a>
The display name of the capability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Required: Yes

 ** type **   <a name="b2bi-Type-CapabilitySummary-type"></a>
Returns the type of the capability. Currently, only `edi` is supported.
Type: String
Valid Values: `edi`
Required: Yes

 ** modifiedAt **   <a name="b2bi-Type-CapabilitySummary-modifiedAt"></a>
Returns a timestamp that identifies the most recent date and time that the capability was modified.
Type: Timestamp
Required: No

## See Also
<a name="API_CapabilitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/CapabilitySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/CapabilitySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/CapabilitySummary)

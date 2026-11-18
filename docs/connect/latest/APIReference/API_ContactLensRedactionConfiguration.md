---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactLensRedactionConfiguration.html
---

# ContactLensRedactionConfiguration
<a name="API_ContactLensRedactionConfiguration"></a>

The redaction configuration for conversational analytics transcripts.

## Contents
<a name="API_ContactLensRedactionConfiguration_Contents"></a>

 ** Behavior **   <a name="connect-Type-ContactLensRedactionConfiguration-Behavior"></a>
Specifies whether redaction is enabled for sensitive data, such as personal information, in the conversational analytics output. Valid values:
+  `Enable` – Redaction is applied according to the other values in this object.
+  `Disable` – Redaction is not applied, and all other values in this object are ignored.
Type: String
Required: No

 ** Entities **   <a name="connect-Type-ContactLensRedactionConfiguration-Entities"></a>
The entity types to redact from the transcript (for example, `NAME`, `EMAIL`, `ADDRESS`).
Type: Array of strings
Required: No

 ** MaskMode **   <a name="connect-Type-ContactLensRedactionConfiguration-MaskMode"></a>
How sensitive information is masked in the transcript. Valid values:
+  `PII` – All redacted entities are replaced with the `[PII]` string.
+  `EntityType` – All redacted entities are replaced with the label of the entity. For example, when the `EMAIL` entity is configured for redaction, emails in the transcript are replaced with the `[EMAIL]` string.
Type: String
Required: No

 ** Policy **   <a name="connect-Type-ContactLensRedactionConfiguration-Policy"></a>
The redaction policy that determines which versions of the transcript are stored. Valid values:
+  `None` – No redaction is applied.
+  `RedactedOnly` – Only the redacted transcript is stored.
+  `RedactedAndOriginal` – Both the redacted and the original transcript are stored.
Type: String
Required: No

## See Also
<a name="API_ContactLensRedactionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactLensRedactionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactLensRedactionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactLensRedactionConfiguration)

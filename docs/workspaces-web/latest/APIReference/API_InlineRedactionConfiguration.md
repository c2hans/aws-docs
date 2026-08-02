---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_InlineRedactionConfiguration.html
---

# InlineRedactionConfiguration
<a name="API_InlineRedactionConfiguration"></a>

The configuration for in-session inline redaction.

## Contents
<a name="API_InlineRedactionConfiguration_Contents"></a>

 ** inlineRedactionPatterns **   <a name="workspacesweb-Type-InlineRedactionConfiguration-inlineRedactionPatterns"></a>
The inline redaction patterns to be enabled for the inline redaction configuration.
Type: Array of [InlineRedactionPattern](API_InlineRedactionPattern.md) objects
Array Members: Minimum number of 0 items. Maximum number of 150 items.
Required: Yes

 ** globalConfidenceLevel **   <a name="workspacesweb-Type-InlineRedactionConfiguration-globalConfidenceLevel"></a>
The global confidence level for the inline redaction configuration. This indicates the certainty of data type matches in the redaction process. Confidence level 3 means high confidence, and requires a formatted text pattern match in order for content to be redacted. Confidence level 2 means medium confidence, and redaction considers both formatted and unformatted text, and adds keyword associate to the logic. Confidence level 1 means low confidence, and redaction is enforced for both formatted pattern \+ unformatted pattern without keyword. This is applied to patterns that do not have a pattern-level confidence level. Defaults to confidence level 2.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3.
Required: No

 ** globalEnforcedUrls **   <a name="workspacesweb-Type-InlineRedactionConfiguration-globalEnforcedUrls"></a>
The global enforced URL configuration for the inline redaction configuration. This is applied to patterns that do not have a pattern-level enforced URL list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `((([a-zA-Z][a-zA-Z0-9+.-]*):\/\/(\*|[\w%._\-\+~#=@]+)?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?)|(\*|[\w%._\-\+~#=@]+\.[\w%._\-\+~#=@]+)(?::(\d{1,5}))?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?|(([a-zA-Z][a-zA-Z0-9+.-]*):(\/\/)?\*))`
Required: No

 ** globalExemptUrls **   <a name="workspacesweb-Type-InlineRedactionConfiguration-globalExemptUrls"></a>
The global exempt URL configuration for the inline redaction configuration. This is applied to patterns that do not have a pattern-level exempt URL list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `((([a-zA-Z][a-zA-Z0-9+.-]*):\/\/(\*|[\w%._\-\+~#=@]+)?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?)|(\*|[\w%._\-\+~#=@]+\.[\w%._\-\+~#=@]+)(?::(\d{1,5}))?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?|(([a-zA-Z][a-zA-Z0-9+.-]*):(\/\/)?\*))`
Required: No

## See Also
<a name="API_InlineRedactionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/InlineRedactionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/InlineRedactionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/InlineRedactionConfiguration)

---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_InlineRedactionPattern.html
---

# InlineRedactionPattern
<a name="API_InlineRedactionPattern"></a>

The set of patterns that determine the data types redacted in session.

## Contents
<a name="API_InlineRedactionPattern_Contents"></a>

 ** redactionPlaceHolder **   <a name="workspacesweb-Type-InlineRedactionPattern-redactionPlaceHolder"></a>
The redaction placeholder that will replace the redacted text in session for the inline redaction pattern.
Type: [RedactionPlaceHolder](API_RedactionPlaceHolder.md) object
Required: Yes

 ** builtInPatternId **   <a name="workspacesweb-Type-InlineRedactionPattern-builtInPatternId"></a>
The built-in pattern from the list of preconfigured patterns. Either a customPattern or builtInPatternId is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[_\-\d\w]+`
Required: No

 ** confidenceLevel **   <a name="workspacesweb-Type-InlineRedactionPattern-confidenceLevel"></a>
The confidence level for inline redaction pattern. This indicates the certainty of data type matches in the redaction process. Confidence level 3 means high confidence, and requires a formatted text pattern match in order for content to be redacted. Confidence level 2 means medium confidence, and redaction considers both formatted and unformatted text, and adds keyword associate to the logic. Confidence level 1 means low confidence, and redaction is enforced for both formatted pattern \+ unformatted pattern without keyword. This overrides the global confidence level.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3.
Required: No

 ** customPattern **   <a name="workspacesweb-Type-InlineRedactionPattern-customPattern"></a>
>The configuration for a custom pattern. Either a customPattern or builtInPatternId is required.
Type: [CustomPattern](API_CustomPattern.md) object
Required: No

 ** enforcedUrls **   <a name="workspacesweb-Type-InlineRedactionPattern-enforcedUrls"></a>
The enforced URL configuration for the inline redaction pattern. This will override the global enforced URL configuration.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `((([a-zA-Z][a-zA-Z0-9+.-]*):\/\/(\*|[\w%._\-\+~#=@]+)?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?)|(\*|[\w%._\-\+~#=@]+\.[\w%._\-\+~#=@]+)(?::(\d{1,5}))?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?|(([a-zA-Z][a-zA-Z0-9+.-]*):(\/\/)?\*))`
Required: No

 ** exemptUrls **   <a name="workspacesweb-Type-InlineRedactionPattern-exemptUrls"></a>
The exempt URL configuration for the inline redaction pattern. This will override the global exempt URL configuration for the inline redaction pattern.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `((([a-zA-Z][a-zA-Z0-9+.-]*):\/\/(\*|[\w%._\-\+~#=@]+)?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?)|(\*|[\w%._\-\+~#=@]+\.[\w%._\-\+~#=@]+)(?::(\d{1,5}))?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?|(([a-zA-Z][a-zA-Z0-9+.-]*):(\/\/)?\*))`
Required: No

## See Also
<a name="API_InlineRedactionPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/InlineRedactionPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/InlineRedactionPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/InlineRedactionPattern)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

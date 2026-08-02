---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_IssueLocation.html
---

# IssueLocation
<a name="API_IssueLocation"></a>

Specifies the location of an identified issue within the bot configuration.

## Contents
<a name="API_IssueLocation_Contents"></a>

 ** botLocale **   <a name="lexv2-Type-IssueLocation-botLocale"></a>
The locale identifier where the issue was found.
Type: String
Required: No

 ** intentId **   <a name="lexv2-Type-IssueLocation-intentId"></a>
The intent identifier where the issue was found, if applicable.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** slotId **   <a name="lexv2-Type-IssueLocation-slotId"></a>
The slot identifier where the issue was found, if applicable.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

## See Also
<a name="API_IssueLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/IssueLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/IssueLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/IssueLocation)

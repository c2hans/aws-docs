---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateConnectionBasicAuthRequestParameters.html
---

# CreateConnectionBasicAuthRequestParameters
<a name="API_CreateConnectionBasicAuthRequestParameters"></a>

Contains the Basic authorization parameters to use for the connection.

## Contents
<a name="API_CreateConnectionBasicAuthRequestParameters_Contents"></a>

 ** Password **   <a name="eventbridge-Type-CreateConnectionBasicAuthRequestParameters-Password"></a>
The password associated with the user name to use for Basic authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[ \t]*[^\x00-\x1F:\x7F]+([ \t]+[^\x00-\x1F:\x7F]+)*[ \t]*$`
Required: Yes

 ** Username **   <a name="eventbridge-Type-CreateConnectionBasicAuthRequestParameters-Username"></a>
The user name to use for Basic authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[ \t]*[^\x00-\x1F:\x7F]+([ \t]+[^\x00-\x1F:\x7F]+)*[ \t]*$`
Required: Yes

## See Also
<a name="API_CreateConnectionBasicAuthRequestParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CreateConnectionBasicAuthRequestParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CreateConnectionBasicAuthRequestParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CreateConnectionBasicAuthRequestParameters)

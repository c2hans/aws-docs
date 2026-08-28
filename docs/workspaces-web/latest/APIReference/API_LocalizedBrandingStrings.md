---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_LocalizedBrandingStrings.html
---

# LocalizedBrandingStrings
<a name="API_LocalizedBrandingStrings"></a>

Localized text strings for a specific language that customize the web portal.

## Contents
<a name="API_LocalizedBrandingStrings_Contents"></a>

 ** browserTabTitle **   <a name="workspacesweb-Type-LocalizedBrandingStrings-browserTabTitle"></a>
The text displayed in the browser tab title.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 25.
Pattern: `[^<>&'`~\\]*`
Required: Yes

 ** welcomeText **   <a name="workspacesweb-Type-LocalizedBrandingStrings-welcomeText"></a>
The welcome text displayed on the sign-in page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Pattern: `[^<>&'`~\\]*`
Required: Yes

 ** contactButtonText **   <a name="workspacesweb-Type-LocalizedBrandingStrings-contactButtonText"></a>
The text displayed on the contact button. This field is optional and defaults to "Contact us".
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[^<>&'`~\\]*`
Required: No

 ** contactLink **   <a name="workspacesweb-Type-LocalizedBrandingStrings-contactLink"></a>
A contact link URL. The URL must start with `https://` or `mailto:`. If not provided, the contact button will be hidden from the web portal screen.
Type: String
Pattern: `(https://|mailto:).*`
Required: No

 ** loadingText **   <a name="workspacesweb-Type-LocalizedBrandingStrings-loadingText"></a>
The text displayed during session loading. This field is optional and defaults to "Loading your session".
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `[^<>&'`~\\]*`
Required: No

 ** loginButtonText **   <a name="workspacesweb-Type-LocalizedBrandingStrings-loginButtonText"></a>
The text displayed on the login button. This field is optional and defaults to "Sign In".
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[^<>&'`~\\]*`
Required: No

 ** loginDescription **   <a name="workspacesweb-Type-LocalizedBrandingStrings-loginDescription"></a>
The description text for the login section. This field is optional and defaults to "Sign in to your session".
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Pattern: `[^<>&'`~\\]*`
Required: No

 ** loginTitle **   <a name="workspacesweb-Type-LocalizedBrandingStrings-loginTitle"></a>
The title text for the login section. This field is optional and defaults to "Sign In".
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^<>&'`~\\]*`
Required: No

## See Also
<a name="API_LocalizedBrandingStrings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/LocalizedBrandingStrings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/LocalizedBrandingStrings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/LocalizedBrandingStrings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

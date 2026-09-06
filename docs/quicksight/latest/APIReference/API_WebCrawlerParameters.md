---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_WebCrawlerParameters.html
---

# WebCrawlerParameters
<a name="API_WebCrawlerParameters"></a>

The parameters for a web crawler data source.

## Contents
<a name="API_WebCrawlerParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** WebCrawlerAuthType **   <a name="QS-Type-WebCrawlerParameters-WebCrawlerAuthType"></a>
The authentication type for the web crawler. The type can be one of the following:
+  `NO_AUTH`: No authentication required.
+  `BASIC_AUTH`: Basic authentication using username and password.
+  `SAML`: SAML-based authentication.
+  `FORM`: Form-based authentication.
Type: String
Valid Values: `NO_AUTH | BASIC_AUTH | FORM | SAML`
Required: Yes

 ** LoginPageUrl **   <a name="QS-Type-WebCrawlerParameters-LoginPageUrl"></a>
The URL of the login page for the web crawler to authenticate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PasswordButtonXpath **   <a name="QS-Type-WebCrawlerParameters-PasswordButtonXpath"></a>
The XPath expression for locating the password submit button on the login page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PasswordFieldXpath **   <a name="QS-Type-WebCrawlerParameters-PasswordFieldXpath"></a>
The XPath expression for locating the password field on the login page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** UsernameButtonXpath **   <a name="QS-Type-WebCrawlerParameters-UsernameButtonXpath"></a>
The XPath expression for locating the username submit button on the login page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** UsernameFieldXpath **   <a name="QS-Type-WebCrawlerParameters-UsernameFieldXpath"></a>
The XPath expression for locating the username field on the login page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** WebProxyHostName **   <a name="QS-Type-WebCrawlerParameters-WebProxyHostName"></a>
The hostname of the web proxy server for the web crawler.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** WebProxyPortNumber **   <a name="QS-Type-WebCrawlerParameters-WebProxyPortNumber"></a>
The port number of the web proxy server for the web crawler.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_WebCrawlerParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/WebCrawlerParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/WebCrawlerParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/WebCrawlerParameters)

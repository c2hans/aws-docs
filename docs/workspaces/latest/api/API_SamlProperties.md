---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_SamlProperties.html
---

# SamlProperties
<a name="API_SamlProperties"></a>

Describes the enablement status, user access URL, and relay state parameter name that are used for configuring federation with an SAML 2.0 identity provider.

## Contents
<a name="API_SamlProperties_Contents"></a>

 ** RelayStateParameterName **   <a name="WorkSpaces-Type-SamlProperties-RelayStateParameterName"></a>
The relay state parameter name supported by the SAML 2.0 identity provider (IdP). When the end user is redirected to the user access URL from the WorkSpaces client application, this relay state parameter name is appended as a query parameter to the URL along with the relay state endpoint to return the user to the client application session.
To use SAML 2.0 authentication with WorkSpaces, the IdP must support IdP-initiated deep linking for the relay state URL. Consult your IdP documentation for more information.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Status **   <a name="WorkSpaces-Type-SamlProperties-Status"></a>
Indicates the status of SAML 2.0 authentication. These statuses include the following.
+ If the setting is `DISABLED`, end users will be directed to login with their directory credentials.
+ If the setting is `ENABLED`, end users will be directed to login via the user access URL. Users attempting to connect to WorkSpaces from a client application that does not support SAML 2.0 authentication will not be able to connect.
+ If the setting is `ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK`, end users will be directed to login via the user access URL on supported client applications, but will not prevent clients that do not support SAML 2.0 authentication from connecting as if SAML 2.0 authentication was disabled.
Type: String
Valid Values: `DISABLED | ENABLED | ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK`
Required: No

 ** UserAccessUrl **   <a name="WorkSpaces-Type-SamlProperties-UserAccessUrl"></a>
The SAML 2.0 identity provider (IdP) user access URL is the URL a user would navigate to in their web browser in order to federate from the IdP and directly access the application, without any SAML 2.0 service provider (SP) bindings.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 200.
Pattern: `^(http|https)\://\S+$`
Required: No

## See Also
<a name="API_SamlProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/SamlProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/SamlProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/SamlProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

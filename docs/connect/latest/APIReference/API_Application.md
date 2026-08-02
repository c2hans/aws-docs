---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Application.html
---

# Application
<a name="API_Application"></a>

This API is in preview release for Connect Customer and is subject to change.

A third-party application's metadata.

## Contents
<a name="API_Application_Contents"></a>

 ** ApplicationPermissions **   <a name="connect-Type-Application-ApplicationPermissions"></a>
The permissions that the agent is granted on the application. For third-party applications, only the `ACCESS` permission is supported. For MCP Servers, the permissions are tool Identifiers accepted by MCP Server.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Namespace **   <a name="connect-Type-Application-Namespace"></a>
Namespace of the application that you want to give access to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Type **   <a name="connect-Type-Application-Type"></a>
 Type of Application.
Type: String
Valid Values: `MCP | THIRD_PARTY_APPLICATION`
Required: No

## See Also
<a name="API_Application_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Application)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Application)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Application)

---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ConnectClientAddIn.html
---

# ConnectClientAddIn
<a name="API_ConnectClientAddIn"></a>

Describes an Connect Customer client add-in.

## Contents
<a name="API_ConnectClientAddIn_Contents"></a>

 ** AddInId **   <a name="WorkSpaces-Type-ConnectClientAddIn-AddInId"></a>
The client add-in identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** Name **   <a name="WorkSpaces-Type-ConnectClientAddIn-Name"></a>
The name of the client add in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^.*$`
Required: No

 ** ResourceId **   <a name="WorkSpaces-Type-ConnectClientAddIn-ResourceId"></a>
The directory identifier for which the client add-in is configured.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: No

 ** URL **   <a name="WorkSpaces-Type-ConnectClientAddIn-URL"></a>
The endpoint URL of the client add-in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(http|https)\://\S+`
Required: No

## See Also
<a name="API_ConnectClientAddIn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ConnectClientAddIn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ConnectClientAddIn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ConnectClientAddIn)

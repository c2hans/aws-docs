---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_User.html
---

# User
<a name="API_User"></a>

A structure that specifies one user or group in the workspace.

## Contents
<a name="API_User_Contents"></a>

 ** id **   <a name="ManagedGrafana-Type-User-id"></a>
The ID of the user or group.
Pattern: `^([0-9a-fA-F]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Required: Yes

 ** type **   <a name="ManagedGrafana-Type-User-type"></a>
Specifies whether this is a single user or a group.
Type: String
Valid Values: `SSO_USER | SSO_GROUP`
Required: Yes

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/User)

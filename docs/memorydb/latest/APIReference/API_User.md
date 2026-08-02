---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_User.html
---

# User
<a name="API_User"></a>

You create users and assign them specific permissions by using an access string. You assign the users to Access Control Lists aligned with a specific role (administrators, human resources) that are then deployed to one or more MemoryDB clusters.

## Contents
<a name="API_User_Contents"></a>

 ** AccessString **   <a name="MemoryDB-Type-User-AccessString"></a>
Access permissions string used for this user.
Type: String
Required: No

 ** ACLNames **   <a name="MemoryDB-Type-User-ACLNames"></a>
The names of the Access Control Lists to which the user belongs
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

 ** ARN **   <a name="MemoryDB-Type-User-ARN"></a>
The Amazon Resource Name (ARN) of the user.
Type: String
Required: No

 ** Authentication **   <a name="MemoryDB-Type-User-Authentication"></a>
Denotes whether the user requires a password to authenticate.
Type: [Authentication](API_Authentication.md) object
Required: No

 ** MinimumEngineVersion **   <a name="MemoryDB-Type-User-MinimumEngineVersion"></a>
The minimum engine version supported for the user
Type: String
Required: No

 ** Name **   <a name="MemoryDB-Type-User-Name"></a>
The name of the user
Type: String
Required: No

 ** Status **   <a name="MemoryDB-Type-User-Status"></a>
Indicates the user status. Can be "active", "modifying" or "deleting".
Type: String
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/User)

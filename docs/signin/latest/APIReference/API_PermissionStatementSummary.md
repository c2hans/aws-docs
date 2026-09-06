---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_PermissionStatementSummary.html
---

# PermissionStatementSummary
<a name="API_PermissionStatementSummary"></a>

Summary information for a permission statement in the AWS Sign-In resource-based policy.

## Contents
<a name="API_PermissionStatementSummary_Contents"></a>

 ** sid **   <a name="signin-Type-PermissionStatementSummary-sid"></a>
The unique identifier of the permission statement.
Type: String
Pattern: `[A-Za-z0-9+/]{64}=?`
Required: Yes

 ** condition **   <a name="signin-Type-PermissionStatementSummary-condition"></a>
The condition block that defines under what conditions this statement applies.
Type: String to string to array of strings map map
Required: No

## See Also
<a name="API_PermissionStatementSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/PermissionStatementSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/PermissionStatementSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/PermissionStatementSummary)

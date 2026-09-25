---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AccountFilter.html
---

# AccountFilter
<a name="API_AccountFilter"></a>

Determines which accounts are in scope. Exactly one of `includeAll`, `include`, or `exclude` is set.

## Contents
<a name="API_AccountFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** exclude **   <a name="networksecuritymanager-Type-AccountFilter-exclude"></a>
Excludes the specified accounts and organizational units. All others are in scope.
Type: [AccountSet](API_AccountSet.md) object
Required: No

 ** include **   <a name="networksecuritymanager-Type-AccountFilter-include"></a>
Includes only the specified accounts and organizational units.
Type: [AccountSet](API_AccountSet.md) object
Required: No

 ** includeAll **   <a name="networksecuritymanager-Type-AccountFilter-includeAll"></a>
Includes all accounts. No account filtering is applied.
Type: Structure
Required: No

## See Also
<a name="API_AccountFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AccountFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AccountFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AccountFilter)

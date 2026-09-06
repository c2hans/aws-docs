---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Target.html
---

# Target
<a name="API_Target"></a>

 The target account, organizational unit, or the root that is associated with an AWS Security Hub CSPM configuration. The configuration can be a configuration policy or self-managed behavior.

## Contents
<a name="API_Target_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AccountId **   <a name="securityhub-Type-Target-AccountId"></a>
 The AWS account ID of the target account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OrganizationalUnitId **   <a name="securityhub-Type-Target-OrganizationalUnitId"></a>
 The organizational unit ID of the target organizational unit.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RootId **   <a name="securityhub-Type-Target-RootId"></a>
 The ID of the organization root.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Target_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Target)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Target)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Target)

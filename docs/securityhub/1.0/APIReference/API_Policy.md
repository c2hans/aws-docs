---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Policy.html
---

# Policy
<a name="API_Policy"></a>

 An object that defines how AWS Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls).

## Contents
<a name="API_Policy_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** SecurityHub **   <a name="securityhub-Type-Policy-SecurityHub"></a>
 The AWS service that the configuration policy applies to.
Type: [SecurityHubPolicy](API_SecurityHubPolicy.md) object
Required: No

## See Also
<a name="API_Policy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Policy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Policy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Policy)

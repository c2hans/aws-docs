---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_UserContext.html
---

# UserContext
<a name="API_UserContext"></a>

Details for user initiating insights job

## Contents
<a name="API_UserContext_Contents"></a>

 ** role **   <a name="connecthealth-Type-UserContext-role"></a>

Type: String
Valid Values: `CLINICIAN`
Required: Yes

 ** userId **   <a name="connecthealth-Type-UserContext-userId"></a>
Unique identifier of the user
Type: String
Pattern: `.*[\s\S]*\S[\s\S]*.*`
Required: Yes

 ** specialty **   <a name="connecthealth-Type-UserContext-specialty"></a>

Type: String
Valid Values: `PRIMARY_CARE`
Required: No

## See Also
<a name="API_UserContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/UserContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/UserContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/UserContext)

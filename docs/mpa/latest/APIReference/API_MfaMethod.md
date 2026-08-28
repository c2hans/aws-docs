---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_MfaMethod.html
---

# MfaMethod
<a name="API_MfaMethod"></a>

MFA configuration and sycnronization status for an approver

## Contents
<a name="API_MfaMethod_Contents"></a>

 ** SyncStatus **   <a name="mpa-Type-MfaMethod-SyncStatus"></a>
Indicates if the approver's MFA device is in-sync with the Identity Source
Type: String
Valid Values: `IN_SYNC | OUT_OF_SYNC`
Required: Yes

 ** Type **   <a name="mpa-Type-MfaMethod-Type"></a>
The type of MFA configuration used by the approver
Type: String
Valid Values: `EMAIL_OTP`
Required: Yes

## See Also
<a name="API_MfaMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/MfaMethod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/MfaMethod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/MfaMethod)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

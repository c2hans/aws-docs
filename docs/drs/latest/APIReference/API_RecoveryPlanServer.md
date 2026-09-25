---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryPlanServer.html
---

# RecoveryPlanServer
<a name="API_RecoveryPlanServer"></a>

A server associated with a Recovery Plan Step.

## Contents
<a name="API_RecoveryPlanServer_Contents"></a>

 ** serverArn **   <a name="drs-Type-RecoveryPlanServer-serverArn"></a>
The ARN of the source server.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:[0-9a-zA-Z_-]+:){3}([0-9]{12,}):source-server/(s-[0-9a-zA-Z]{17})`
Required: Yes

 ** impactLevel **   <a name="drs-Type-RecoveryPlanServer-impactLevel"></a>
The impact level of a server within a Recovery Plan step. `CRITICAL` means the step fails if this server fails. `OPTIONAL` means the step continues even if this server fails.
Type: String
Valid Values: `CRITICAL | OPTIONAL`
Required: No

## See Also
<a name="API_RecoveryPlanServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryPlanServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryPlanServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryPlanServer)

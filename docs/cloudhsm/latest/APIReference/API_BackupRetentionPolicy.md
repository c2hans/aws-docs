---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_BackupRetentionPolicy.html
---

# BackupRetentionPolicy
<a name="API_BackupRetentionPolicy"></a>

A policy that defines the number of days to retain backups.

## Contents
<a name="API_BackupRetentionPolicy_Contents"></a>

 ** Type **   <a name="CloudHSMV2-Type-BackupRetentionPolicy-Type"></a>
The type of backup retention policy. For the `DAYS` type, the value is the number of days to retain backups.
Type: String
Valid Values: `DAYS`
Required: No

 ** Value **   <a name="CloudHSMV2-Type-BackupRetentionPolicy-Value"></a>
Use a value between 7 - 379.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3.
Pattern: `[0-9]+`
Required: No

## See Also
<a name="API_BackupRetentionPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/BackupRetentionPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/BackupRetentionPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/BackupRetentionPolicy)

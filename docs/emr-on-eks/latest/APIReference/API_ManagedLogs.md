---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ManagedLogs.html
---

# ManagedLogs
<a name="API_ManagedLogs"></a>

The entity that provides configuration control over managed logs.

## Contents
<a name="API_ManagedLogs_Contents"></a>

 ** allowAWSToRetainLogs **   <a name="emroneks-Type-ManagedLogs-allowAWSToRetainLogs"></a>
Determines whether AWS can retain logs.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** encryptionKeyArn **   <a name="emroneks-Type-ManagedLogs-encryptionKeyArn"></a>
The Amazon resource name (ARN) of the encryption key for logs.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `^(arn:(aws[a-zA-Z0-9-]*):kms:.+:(\d{12})?:key\/[(0-9a-zA-Z)-?]+|\$\{[a-zA-Z]\w*\})$`
Required: No

## See Also
<a name="API_ManagedLogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ManagedLogs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ManagedLogs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ManagedLogs)

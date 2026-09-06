---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ManagedS3BackupAccess.html
---

# ManagedS3BackupAccess
<a name="API_ManagedS3BackupAccess"></a>

The configuration for managed Amazon S3 backup access from the ODB network.

## Contents
<a name="API_ManagedS3BackupAccess_Contents"></a>

 ** ipv4Addresses **   <a name="odb-Type-ManagedS3BackupAccess-ipv4Addresses"></a>
The IPv4 addresses for the managed Amazon S3 backup access.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** status **   <a name="odb-Type-ManagedS3BackupAccess-status"></a>
The status of the managed Amazon S3 backup access.
Type: String
Valid Values: `ENABLED | ENABLING | DISABLED | DISABLING`
Required: No

## See Also
<a name="API_ManagedS3BackupAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ManagedS3BackupAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ManagedS3BackupAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ManagedS3BackupAccess)

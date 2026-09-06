---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_EfsStorageConfiguration.html
---

# EfsStorageConfiguration
<a name="API_EfsStorageConfiguration"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Defines the storage configuration for an Amazon EFS file system.

## Contents
<a name="API_EfsStorageConfiguration_Contents"></a>

 ** file-system-id **   <a name="m2-Type-EfsStorageConfiguration-file-system-id"></a>
The file system identifier.
Type: String
Pattern: `\S{1,200}`
Required: Yes

 ** mount-point **   <a name="m2-Type-EfsStorageConfiguration-mount-point"></a>
The mount point for the file system.
Type: String
Pattern: `\S{1,200}`
Required: Yes

## See Also
<a name="API_EfsStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/EfsStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/EfsStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/EfsStorageConfiguration)

---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_UpdateProviderConfiguration.html
---

# UpdateProviderConfiguration
<a name="API_UpdateProviderConfiguration"></a>

The update Provider Configuration.

## Contents
<a name="API_UpdateProviderConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3 **   <a name="continuum-Type-UpdateProviderConfiguration-s3"></a>
Replacement credentials for a customer-managed S3 integration. The bucket cannot be changed.
Type: [UpdateS3Configuration](API_UpdateS3Configuration.md) object
Required: No

## See Also
<a name="API_UpdateProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/UpdateProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/UpdateProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/UpdateProviderConfiguration)

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedQueryOutputConfiguration.html
---

# ProtectedQueryOutputConfiguration
<a name="API_ProtectedQueryOutputConfiguration"></a>

Contains configuration details for protected query output.

## Contents
<a name="API_ProtectedQueryOutputConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** distribute **   <a name="API-Type-ProtectedQueryOutputConfiguration-distribute"></a>
 Required configuration for a protected query with a `distribute` output type.
Type: [ProtectedQueryDistributeOutputConfiguration](API_ProtectedQueryDistributeOutputConfiguration.md) object
Required: No

 ** intermediateTable **   <a name="API-Type-ProtectedQueryOutputConfiguration-intermediateTable"></a>
The intermediate table output configuration, present when the protected query was triggered by a populate operation.
Type: [IntermediateTableOutputConfiguration](API_IntermediateTableOutputConfiguration.md) object
Required: No

 ** member **   <a name="API-Type-ProtectedQueryOutputConfiguration-member"></a>
 Required configuration for a protected query with a `member` output type.
Type: [ProtectedQueryMemberOutputConfiguration](API_ProtectedQueryMemberOutputConfiguration.md) object
Required: No

 ** s3 **   <a name="API-Type-ProtectedQueryOutputConfiguration-s3"></a>
Required configuration for a protected query with an `s3` output type.
Type: [ProtectedQueryS3OutputConfiguration](API_ProtectedQueryS3OutputConfiguration.md) object
Required: No

## See Also
<a name="API_ProtectedQueryOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedQueryOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedQueryOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedQueryOutputConfiguration)

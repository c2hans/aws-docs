---
source_url: https://docs.aws.amazon.com/account-access-runtime/latest/APIReference/API_ProgrammaticAccessDetails.html
---

# ProgrammaticAccessDetails
<a name="API_ProgrammaticAccessDetails"></a>

A set of temporary AWS credentials for programmatic access. Treat these values as sensitive.

## Contents
<a name="API_ProgrammaticAccessDetails_Contents"></a>

 ** accessKeyId **   <a name="accountaccessruntime-Type-ProgrammaticAccessDetails-accessKeyId"></a>
The access key ID for the temporary credentials.
Type: String
Required: Yes

 ** expiresAt **   <a name="accountaccessruntime-Type-ProgrammaticAccessDetails-expiresAt"></a>
The date and time when the temporary credentials expire, after which they can no longer be used.
Type: Timestamp
Required: Yes

 ** secretAccessKey **   <a name="accountaccessruntime-Type-ProgrammaticAccessDetails-secretAccessKey"></a>
The secret access key for the temporary credentials. Treat this value as a secret.
Type: String
Required: Yes

 ** sessionToken **   <a name="accountaccessruntime-Type-ProgrammaticAccessDetails-sessionToken"></a>
The session token that you must include along with the access key ID and secret access key when you make requests with the temporary credentials.
Type: String
Required: Yes

## See Also
<a name="API_ProgrammaticAccessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-runtime-2018-05-10/ProgrammaticAccessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-runtime-2018-05-10/ProgrammaticAccessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-runtime-2018-05-10/ProgrammaticAccessDetails)

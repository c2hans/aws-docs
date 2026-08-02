---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_ServerSideEncryptionUpdateDetails.html
---

# ServerSideEncryptionUpdateDetails
<a name="API_connect-voice-id_ServerSideEncryptionUpdateDetails"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Details about the most recent server-side encryption configuration update. When the server-side encryption configuration is changed, dependency on the old KMS key is removed through an asynchronous process. When this update is complete, the domain’s data can only be accessed using the new KMS key.

## Contents
<a name="API_connect-voice-id_ServerSideEncryptionUpdateDetails_Contents"></a>

 ** Message **   <a name="connect-Type-connect-voice-id_ServerSideEncryptionUpdateDetails-Message"></a>
Message explaining the current UpdateStatus. When the UpdateStatus is FAILED, this message explains the cause of the failure.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** OldKmsKeyId **   <a name="connect-Type-connect-voice-id_ServerSideEncryptionUpdateDetails-OldKmsKeyId"></a>
The previous KMS key ID the domain was encrypted with, before ServerSideEncryptionConfiguration was updated to a new KMS key ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** UpdateStatus **   <a name="connect-Type-connect-voice-id_ServerSideEncryptionUpdateDetails-UpdateStatus"></a>
Status of the server-side encryption update. During an update, if there is an issue with the domain's current or old KMS key ID, such as an inaccessible or disabled key, then the status is FAILED. In order to resolve this, the key needs to be made accessible, and then an UpdateDomain call with the existing server-side encryption configuration will re-attempt this update process.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED`
Required: No

## See Also
<a name="API_connect-voice-id_ServerSideEncryptionUpdateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/ServerSideEncryptionUpdateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/ServerSideEncryptionUpdateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/ServerSideEncryptionUpdateDetails)

---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportServerSideEncryption.html
---

# ExportServerSideEncryption
<a name="API_ExportServerSideEncryption"></a>

Encryption configuration of the export job. Includes the encryption type in addition to the AWS KMS key. The KMS key is only necessary if you chose the KMS encryption type.

## Contents
<a name="API_ExportServerSideEncryption_Contents"></a>

 ** Type **   <a name="dataexchange-Type-ExportServerSideEncryption-Type"></a>
The type of server side encryption used for encrypting the objects in Amazon S3.
Type: String
Valid Values: `aws:kms | AES256`
Required: Yes

 ** KmsKeyArn **   <a name="dataexchange-Type-ExportServerSideEncryption-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key you want to use to encrypt the Amazon S3 objects. This parameter is required if you choose aws:kms as an encryption type.
Type: String
Required: No

## See Also
<a name="API_ExportServerSideEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ExportServerSideEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ExportServerSideEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ExportServerSideEncryption)

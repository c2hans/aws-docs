---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_FsxOntapConfiguration.html
---

# FsxOntapConfiguration
<a name="API_FsxOntapConfiguration"></a>

FSx for ONTAP storage configuration.

## Contents
<a name="API_FsxOntapConfiguration_Contents"></a>

 ** credentialsSecretArn **   <a name="mgn-Type-FsxOntapConfiguration-credentialsSecretArn"></a>
FSx ONTAP configuration credentials secret ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `arn:[\w-]+:secretsmanager:([a-z]{2}-(gov-)?[a-z]+-\d{1})?:(\d{12})?:secret:(.+)`
Required: Yes

 ** storageVirtualMachineId **   <a name="mgn-Type-FsxOntapConfiguration-storageVirtualMachineId"></a>
FSx ONTAP configuration storage virtual machine ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `(svm-[0-9a-f]{17,})`
Required: Yes

## See Also
<a name="API_FsxOntapConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/FsxOntapConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/FsxOntapConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/FsxOntapConfiguration)

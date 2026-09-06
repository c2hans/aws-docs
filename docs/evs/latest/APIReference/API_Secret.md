---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_Secret.html
---

# Secret
<a name="API_Secret"></a>

A managed secret that contains the credentials for installing vCenter Server, NSX, and SDDC Manager. During environment creation, the Amazon EVS control plane uses AWS Secrets Manager to create, encrypt, validate, and store secrets. If you choose to delete your environment, Amazon EVS also deletes the secrets that are associated with your environment. Amazon EVS does not provide managed rotation of secrets. We recommend that you rotate secrets regularly to ensure that secrets are not long-lived.

## Contents
<a name="API_Secret_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** secretArn **   <a name="evs-Type-Secret-secretArn"></a>
 The Amazon Resource Name (ARN) of the secret.
Type: String
Required: No

## See Also
<a name="API_Secret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/Secret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/Secret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/Secret)

---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscribedIamPrincipal.html
---

# SubscribedIamPrincipal
<a name="API_SubscribedIamPrincipal"></a>

The IAM principal that subscribes to the asset.

## Contents
<a name="API_SubscribedIamPrincipal_Contents"></a>

 ** principalArn **   <a name="datazone-Type-SubscribedIamPrincipal-principalArn"></a>
The ARN of the subscribed IAM principal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|user)(/[\w+=,.@-]*)*/[\w+=,.@-]+`
Required: No

## See Also
<a name="API_SubscribedIamPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscribedIamPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscribedIamPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscribedIamPrincipal)

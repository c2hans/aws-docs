---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_ValidationExceptionField.html
---

# ValidationExceptionField
<a name="API_ValidationExceptionField"></a>

Returns information about a field passed inside a request that resulted in an exception. For example, the request has failed because you passed an instance of IAM Identity Center without an organization.

## Contents
<a name="API_ValidationExceptionField_Contents"></a>

 ** message **   <a name="signin-Type-ValidationExceptionField-message"></a>
Message describing why the field failed validation.
Type: String
Required: Yes

 ** name **   <a name="signin-Type-ValidationExceptionField-name"></a>
The name of the field which failed the validation. For example, `NOT_ORG_BASED_INSTANCE`.
Type: String
Required: Yes

## See Also
<a name="API_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/ValidationExceptionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/ValidationExceptionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/ValidationExceptionField)

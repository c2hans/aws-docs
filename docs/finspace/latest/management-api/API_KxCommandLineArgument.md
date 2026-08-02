---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxCommandLineArgument.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxCommandLineArgument
<a name="API_KxCommandLineArgument"></a>

Defines the key-value pairs to make them available inside the cluster. Duplicate keys are not allowed. To send a list of values for the same command line argument (key), use a space delimited list of values for the key.

## Contents
<a name="API_KxCommandLineArgument_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** key **   <a name="finspace-Type-KxCommandLineArgument-key"></a>
The name of the key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?![Aa][Ww][Ss])(s|([a-zA-Z][a-zA-Z0-9_]+))|(AWS_ZIP_DEFAULT)`
Required: No

 ** value **   <a name="finspace-Type-KxCommandLineArgument-value"></a>
The value of the key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[a-zA-Z0-9_:./,; ]+$`
Required: No

## See Also
<a name="API_KxCommandLineArgument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxCommandLineArgument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxCommandLineArgument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxCommandLineArgument)

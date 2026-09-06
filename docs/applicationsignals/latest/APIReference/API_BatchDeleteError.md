---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchDeleteError.html
---

# BatchDeleteError
<a name="API_BatchDeleteError"></a>

Represents an error that occurred when attempting to delete a configuration.

## Contents
<a name="API_BatchDeleteError_Contents"></a>

 ** Code **   <a name="applicationsignals-Type-BatchDeleteError-Code"></a>
The error code indicating the type of failure.
Type: String
Valid Values: `ResourceNotFoundException | AccessDeniedException | InternalServiceException`
Required: Yes

 ** Message **   <a name="applicationsignals-Type-BatchDeleteError-Message"></a>
A descriptive error message.
Type: String
Required: Yes

 ** ResourceArn **   <a name="applicationsignals-Type-BatchDeleteError-ResourceArn"></a>
The ARN of the configuration that failed to delete.
Type: String
Required: Yes

## See Also
<a name="API_BatchDeleteError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/BatchDeleteError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/BatchDeleteError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/BatchDeleteError)

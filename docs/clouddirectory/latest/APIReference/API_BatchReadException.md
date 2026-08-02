---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchReadException.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchReadException
<a name="API_BatchReadException"></a>

The batch read exception structure, which contains the exception type and message.

## Contents
<a name="API_BatchReadException_Contents"></a>

 ** Message **   <a name="amazoncds-Type-BatchReadException-Message"></a>
An exception message that is associated with the failure.
Type: String
Required: No

 ** Type **   <a name="amazoncds-Type-BatchReadException-Type"></a>
A type of exception, such as `InvalidArnException`.
Type: String
Valid Values: `ValidationException | InvalidArnException | ResourceNotFoundException | InvalidNextTokenException | AccessDeniedException | NotNodeException | FacetValidationException | CannotListParentOfRootException | NotIndexException | NotPolicyException | DirectoryNotEnabledException | LimitExceededException | InternalServiceException`
Required: No

## See Also
<a name="API_BatchReadException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchReadException)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchReadException)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchReadException)

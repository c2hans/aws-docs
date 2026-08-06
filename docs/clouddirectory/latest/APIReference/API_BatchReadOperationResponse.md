---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchReadOperationResponse.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchReadOperationResponse
<a name="API_BatchReadOperationResponse"></a>

Represents the output of a `BatchRead` response operation.

## Contents
<a name="API_BatchReadOperationResponse_Contents"></a>

 ** ExceptionResponse **   <a name="amazoncds-Type-BatchReadOperationResponse-ExceptionResponse"></a>
Identifies which operation in a batch has failed.
Type: [BatchReadException](API_BatchReadException.md) object
Required: No

 ** SuccessfulResponse **   <a name="amazoncds-Type-BatchReadOperationResponse-SuccessfulResponse"></a>
Identifies which operation in a batch has succeeded.
Type: [BatchReadSuccessfulResponse](API_BatchReadSuccessfulResponse.md) object
Required: No

## See Also
<a name="API_BatchReadOperationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchReadOperationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchReadOperationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchReadOperationResponse)

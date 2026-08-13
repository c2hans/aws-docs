---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchDescribeUserLimitsError.html
---

# BatchDescribeUserLimitsError
<a name="API_BatchDescribeUserLimitsError"></a>

Information about a user whose limits could not be described in a batch operation.

## Contents
<a name="API_BatchDescribeUserLimitsError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** errorCode **   <a name="QS-Type-BatchDescribeUserLimitsError-errorCode"></a>
The error code for the failure.
Type: String
Required: Yes

 ** message **   <a name="QS-Type-BatchDescribeUserLimitsError-message"></a>
The error message for the failure.
Type: String
Required: Yes

 ** namespace **   <a name="QS-Type-BatchDescribeUserLimitsError-namespace"></a>
The namespace of the user that failed.
Type: String
Required: No

 ** userArn **   <a name="QS-Type-BatchDescribeUserLimitsError-userArn"></a>
The ARN of the user that failed.
Type: String
Required: No

 ** userName **   <a name="QS-Type-BatchDescribeUserLimitsError-userName"></a>
The name of the user that failed.
Type: String
Required: No

## See Also
<a name="API_BatchDescribeUserLimitsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BatchDescribeUserLimitsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BatchDescribeUserLimitsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BatchDescribeUserLimitsError)

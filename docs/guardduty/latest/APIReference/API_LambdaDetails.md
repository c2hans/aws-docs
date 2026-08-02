---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_LambdaDetails.html
---

# LambdaDetails
<a name="API_LambdaDetails"></a>

Information about the Lambda function involved in the finding.

## Contents
<a name="API_LambdaDetails_Contents"></a>

 ** description **   <a name="guardduty-Type-LambdaDetails-description"></a>
Description of the Lambda function.
Type: String
Required: No

 ** functionArn **   <a name="guardduty-Type-LambdaDetails-functionArn"></a>
Amazon Resource Name (ARN) of the Lambda function.
Type: String
Required: No

 ** functionName **   <a name="guardduty-Type-LambdaDetails-functionName"></a>
Name of the Lambda function.
Type: String
Required: No

 ** functionVersion **   <a name="guardduty-Type-LambdaDetails-functionVersion"></a>
The version of the Lambda function.
Type: String
Required: No

 ** lastModifiedAt **   <a name="guardduty-Type-LambdaDetails-lastModifiedAt"></a>
The timestamp when the Lambda function was last modified. This field is in the UTC date string format `(2023-03-22T19:37:20.168Z)`.
Type: Timestamp
Required: No

 ** revisionId **   <a name="guardduty-Type-LambdaDetails-revisionId"></a>
The revision ID of the Lambda function version.
Type: String
Required: No

 ** role **   <a name="guardduty-Type-LambdaDetails-role"></a>
The execution role of the Lambda function.
Type: String
Required: No

 ** tags **   <a name="guardduty-Type-LambdaDetails-tags"></a>
A list of tags attached to this resource, listed in the format of `key`:`value` pair.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcConfig **   <a name="guardduty-Type-LambdaDetails-vpcConfig"></a>
Amazon Virtual Private Cloud configuration details associated with your Lambda function.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_LambdaDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/LambdaDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/LambdaDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/LambdaDetails)

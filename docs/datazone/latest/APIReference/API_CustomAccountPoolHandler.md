---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CustomAccountPoolHandler.html
---

# CustomAccountPoolHandler
<a name="API_CustomAccountPoolHandler"></a>

The custom AWS Lambda handler within an account pool.

## Contents
<a name="API_CustomAccountPoolHandler_Contents"></a>

 ** lambdaFunctionArn **   <a name="datazone-Type-CustomAccountPoolHandler-lambdaFunctionArn"></a>
The ARN of the AWS Lambda function for the custom AWS Lambda handler.
Type: String
Pattern: `arn:(?:aws|aws-cn|aws-us-gov):lambda:(?:[a-z]{2}(?:-gov)?-[a-z]+-\d{1,}):(\d{12}):function:[a-zA-Z0-9-_]+(?::[a-zA-Z0-9-_]+)?(?:\$[\w-]+)?`
Required: Yes

 ** lambdaExecutionRoleArn **   <a name="datazone-Type-CustomAccountPoolHandler-lambdaExecutionRoleArn"></a>
The ARN of the IAM role that enables Amazon SageMaker Unified Studio to invoke the AWS Lambda funtion if the account source is the custom account pool handler.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]*`
Required: No

## See Also
<a name="API_CustomAccountPoolHandler_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CustomAccountPoolHandler)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CustomAccountPoolHandler)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CustomAccountPoolHandler)

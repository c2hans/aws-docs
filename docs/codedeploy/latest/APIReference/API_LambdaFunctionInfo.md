---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_LambdaFunctionInfo.html
---

# LambdaFunctionInfo
<a name="API_LambdaFunctionInfo"></a>

 Information about a Lambda function specified in a deployment.

## Contents
<a name="API_LambdaFunctionInfo_Contents"></a>

 ** currentVersion **   <a name="CodeDeploy-Type-LambdaFunctionInfo-currentVersion"></a>
 The version of a Lambda function that production traffic points to.
Type: String
Required: No

 ** functionAlias **   <a name="CodeDeploy-Type-LambdaFunctionInfo-functionAlias"></a>
 The alias of a Lambda function. For more information, see [AWS Lambda Function Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html) in the * AWS Lambda Developer Guide*.
Type: String
Required: No

 ** functionName **   <a name="CodeDeploy-Type-LambdaFunctionInfo-functionName"></a>
 The name of a Lambda function.
Type: String
Required: No

 ** targetVersion **   <a name="CodeDeploy-Type-LambdaFunctionInfo-targetVersion"></a>
 The version of a Lambda function that production traffic points to after the Lambda function is deployed.
Type: String
Required: No

 ** targetVersionWeight **   <a name="CodeDeploy-Type-LambdaFunctionInfo-targetVersionWeight"></a>
 The percentage of production traffic that the target version of a Lambda function receives.
Type: Double
Required: No

## See Also
<a name="API_LambdaFunctionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/LambdaFunctionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/LambdaFunctionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/LambdaFunctionInfo)

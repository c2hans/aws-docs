---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ServerlessFunction.html
---

# ServerlessFunction
<a name="API_ServerlessFunction"></a>

Contains details about a serverless function involved in a finding.

## Contents
<a name="API_ServerlessFunction_Contents"></a>

 ** architectures **   <a name="inspector2-Type-ServerlessFunction-architectures"></a>
The architectures of the serverless function.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `X86_64 | ARM64`
Required: No

 ** codeDigest **   <a name="inspector2-Type-ServerlessFunction-codeDigest"></a>
The code digest of the serverless function.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** executionRole **   <a name="inspector2-Type-ServerlessFunction-executionRole"></a>
The execution role of the serverless function.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** lastModifiedAt **   <a name="inspector2-Type-ServerlessFunction-lastModifiedAt"></a>
The date and time the serverless function was last modified.
Type: Timestamp
Required: No

 ** layers **   <a name="inspector2-Type-ServerlessFunction-layers"></a>
The layers of the serverless function.
Type: Array of strings
Pattern: `arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+:[0-9]+`
Required: No

 ** networkId **   <a name="inspector2-Type-ServerlessFunction-networkId"></a>
The network ID associated with the serverless function.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** packageType **   <a name="inspector2-Type-ServerlessFunction-packageType"></a>
The package type of the serverless function.
Type: String
Valid Values: `IMAGE | ZIP`
Required: No

 ** runtime **   <a name="inspector2-Type-ServerlessFunction-runtime"></a>
The runtime of the serverless function.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** securityGroupIds **   <a name="inspector2-Type-ServerlessFunction-securityGroupIds"></a>
The security group IDs associated with the serverless function.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1.
Required: No

 ** serverlessFunctionName **   <a name="inspector2-Type-ServerlessFunction-serverlessFunctionName"></a>
The name of the serverless function.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** subnetIds **   <a name="inspector2-Type-ServerlessFunction-subnetIds"></a>
The subnet IDs associated with the serverless function.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Length Constraints: Minimum length of 1.
Required: No

 ** version **   <a name="inspector2-Type-ServerlessFunction-version"></a>
The version of the serverless function.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ServerlessFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ServerlessFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ServerlessFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ServerlessFunction)

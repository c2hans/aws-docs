---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceState.html
---

# ResourceState
<a name="API_ResourceState"></a>

Details the state of Amazon Inspector for each resource type Amazon Inspector scans.

## Contents
<a name="API_ResourceState_Contents"></a>

 ** ec2 **   <a name="inspector2-Type-ResourceState-ec2"></a>
An object detailing the state of Amazon Inspector scanning for Amazon EC2 resources.
Type: [State](API_State.md) object
Required: Yes

 ** ecr **   <a name="inspector2-Type-ResourceState-ecr"></a>
An object detailing the state of Amazon Inspector scanning for Amazon ECR resources.
Type: [State](API_State.md) object
Required: Yes

 ** codeRepository **   <a name="inspector2-Type-ResourceState-codeRepository"></a>
An object that described the state of Amazon Inspector scans for an account.
Type: [State](API_State.md) object
Required: No

 ** lambda **   <a name="inspector2-Type-ResourceState-lambda"></a>
An object that described the state of Amazon Inspector scans for an account.
Type: [State](API_State.md) object
Required: No

 ** lambdaCode **   <a name="inspector2-Type-ResourceState-lambdaCode"></a>
An object that described the state of Amazon Inspector scans for an account.
Type: [State](API_State.md) object
Required: No

## See Also
<a name="API_ResourceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ResourceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ResourceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ResourceState)

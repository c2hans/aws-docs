---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_OperatorResponse.html
---

# OperatorResponse
<a name="API_OperatorResponse"></a>

Describes whether the resource is managed by a service provider and, if so, describes the service provider that manages it.

## Contents
<a name="API_OperatorResponse_Contents"></a>

 ** hiddenByDefault **
If `true`, the resource is hidden by default based on the managed resource visibility settings for the account.
Type: Boolean
Required: No

 ** managed **
If `true`, the resource is managed by a service provider.
Type: Boolean
Required: No

 ** principal **
If `managed` is `true`, then the principal is returned. The principal is the service provider that manages the resource.
Type: String
Required: No

## See Also
<a name="API_OperatorResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/OperatorResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/OperatorResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/OperatorResponse)

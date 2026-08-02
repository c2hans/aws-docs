---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetVerifiedAccessGroupPolicy.html
---

# GetVerifiedAccessGroupPolicy
<a name="API_GetVerifiedAccessGroupPolicy"></a>

Shows the contents of the Verified Access policy associated with the group.

## Request Parameters
<a name="API_GetVerifiedAccessGroupPolicy_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VerifiedAccessGroupId**
The ID of the Verified Access group.
Type: String
Required: Yes

## Response Elements
<a name="API_GetVerifiedAccessGroupPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **policyDocument**
The Verified Access policy document.
Type: String

 **policyEnabled**
The status of the Verified Access policy.
Type: Boolean

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetVerifiedAccessGroupPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetVerifiedAccessGroupPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetVerifiedAccessGroupPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetVerifiedAccessGroupPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetVerifiedAccessGroupPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetVerifiedAccessGroupPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetVerifiedAccessGroupPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetVerifiedAccessGroupPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetVerifiedAccessGroupPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetVerifiedAccessGroupPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetVerifiedAccessGroupPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetVerifiedAccessGroupPolicy)

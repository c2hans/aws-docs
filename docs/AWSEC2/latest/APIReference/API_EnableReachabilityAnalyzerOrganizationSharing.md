---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableReachabilityAnalyzerOrganizationSharing.html
---

# EnableReachabilityAnalyzerOrganizationSharing
<a name="API_EnableReachabilityAnalyzerOrganizationSharing"></a>

Establishes a trust relationship between Reachability Analyzer and AWS Organizations. This operation must be performed by the management account for the organization.

After you establish a trust relationship, a user in the management account or a delegated administrator account can run a cross-account analysis using resources from the member accounts.

## Request Parameters
<a name="API_EnableReachabilityAnalyzerOrganizationSharing_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_EnableReachabilityAnalyzerOrganizationSharing_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **returnValue**
Returns `true` if the request succeeds; otherwise, returns an error.
Type: Boolean

## Errors
<a name="API_EnableReachabilityAnalyzerOrganizationSharing_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_EnableReachabilityAnalyzerOrganizationSharing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableReachabilityAnalyzerOrganizationSharing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableReachabilityAnalyzerOrganizationSharing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableReachabilityAnalyzerOrganizationSharing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableReachabilityAnalyzerOrganizationSharing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableReachabilityAnalyzerOrganizationSharing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableReachabilityAnalyzerOrganizationSharing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableReachabilityAnalyzerOrganizationSharing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableReachabilityAnalyzerOrganizationSharing)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableReachabilityAnalyzerOrganizationSharing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableReachabilityAnalyzerOrganizationSharing)

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartNetworkInsightsAnalysis.html
---

# StartNetworkInsightsAnalysis
<a name="API_StartNetworkInsightsAnalysis"></a>

Starts analyzing the specified path. If the path is reachable, the operation returns the shortest feasible path.

## Request Parameters
<a name="API_StartNetworkInsightsAnalysis_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AdditionalAccount.N**
The member accounts that contain resources that the path can traverse.
Type: Array of strings
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [How to ensure idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FilterInArn.N**
The Amazon Resource Names (ARN) of the resources that the path must traverse.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 **FilterOutArn.N**
The Amazon Resource Names (ARN) of the resources that the path will ignore.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 **NetworkInsightsPathId**
The ID of the path.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_StartNetworkInsightsAnalysis_ResponseElements"></a>

The following elements are returned by the service.

 **networkInsightsAnalysis**
Information about the network insights analysis.
Type: [NetworkInsightsAnalysis](API_NetworkInsightsAnalysis.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_StartNetworkInsightsAnalysis_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_StartNetworkInsightsAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/StartNetworkInsightsAnalysis)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/StartNetworkInsightsAnalysis)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/StartNetworkInsightsAnalysis)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/StartNetworkInsightsAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/StartNetworkInsightsAnalysis)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/StartNetworkInsightsAnalysis)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/StartNetworkInsightsAnalysis)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/StartNetworkInsightsAnalysis)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/StartNetworkInsightsAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/StartNetworkInsightsAnalysis)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelDeclarativePoliciesReport.html
---

# CancelDeclarativePoliciesReport
<a name="API_CancelDeclarativePoliciesReport"></a>

Cancels the generation of an account status report.

You can only cancel a report while it has the `running` status. Reports with other statuses (`complete`, `cancelled`, or `error`) can't be canceled.

For more information, see [Generating the account status report for declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_status-report.html) in the * AWS Organizations User Guide*.

## Request Parameters
<a name="API_CancelDeclarativePoliciesReport_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ReportId**
The ID of the report.
Type: String
Required: Yes

## Response Elements
<a name="API_CancelDeclarativePoliciesReport_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_CancelDeclarativePoliciesReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CancelDeclarativePoliciesReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CancelDeclarativePoliciesReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CancelDeclarativePoliciesReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CancelDeclarativePoliciesReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CancelDeclarativePoliciesReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CancelDeclarativePoliciesReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CancelDeclarativePoliciesReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CancelDeclarativePoliciesReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CancelDeclarativePoliciesReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CancelDeclarativePoliciesReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CancelDeclarativePoliciesReport)

---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_UpdateEnrollmentStatus.html
---

# UpdateEnrollmentStatus
<a name="API_UpdateEnrollmentStatus"></a>

Updates the enrollment (opt in and opt out) status of an account to the AWS Compute Optimizer service.

If the account is a management account of an organization, this action can also be used to enroll member accounts of the organization.

You must have the appropriate permissions to opt in to Compute Optimizer, to view its recommendations, and to opt out. For more information, see [Controlling access with AWS Identity and Access Management](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html) in the * AWS Compute Optimizer User Guide*.

When you opt in, Compute Optimizer automatically creates a service-linked role in your account to access its data. For more information, see [Using Service-Linked Roles for AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/using-service-linked-roles.html) in the * AWS Compute Optimizer User Guide*.

## Request Syntax
<a name="API_UpdateEnrollmentStatus_RequestSyntax"></a>

```
{
   "includeMemberAccounts": {{boolean}},
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateEnrollmentStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [includeMemberAccounts](#API_UpdateEnrollmentStatus_RequestSyntax) **   <a name="computeoptimizer-UpdateEnrollmentStatus-request-includeMemberAccounts"></a>
Indicates whether to enroll member accounts of the organization if the account is the management account of an organization.
Type: Boolean
Required: No

 ** [status](#API_UpdateEnrollmentStatus_RequestSyntax) **   <a name="computeoptimizer-UpdateEnrollmentStatus-request-status"></a>
The new enrollment status of the account.
The following status options are available:
+  `Active` - Opts in your account to the Compute Optimizer service. Compute Optimizer begins analyzing the configuration and utilization metrics of your AWS resources after you opt in. For more information, see [Metrics analyzed by AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html) in the * AWS Compute Optimizer User Guide*.
+  `Inactive` - Opts out your account from the Compute Optimizer service. Your account's recommendations and related metrics data will be deleted from Compute Optimizer after you opt out.
The `Pending` and `Failed` options cannot be used to update the enrollment status of an account. They are returned in the response of a request to update the enrollment status of an account.
Type: String
Valid Values: `Active | Inactive | Pending | Failed`
Required: Yes

## Response Syntax
<a name="API_UpdateEnrollmentStatus_ResponseSyntax"></a>

```
{
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_UpdateEnrollmentStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_UpdateEnrollmentStatus_ResponseSyntax) **   <a name="computeoptimizer-UpdateEnrollmentStatus-response-status"></a>
The enrollment status of the account.
Type: String
Valid Values: `Active | Inactive | Pending | Failed`

 ** [statusReason](#API_UpdateEnrollmentStatus_ResponseSyntax) **   <a name="computeoptimizer-UpdateEnrollmentStatus-response-statusReason"></a>
The reason for the enrollment status of the account. For example, an account might show a status of `Pending` because member accounts of an organization require more time to be enrolled in the service.
Type: String

## Errors
<a name="API_UpdateEnrollmentStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal error has occurred. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterValueException **
The value supplied for the input parameter is out of range or not valid.
HTTP Status Code: 400

 ** MissingAuthenticationToken **
The request must contain either a valid (registered) AWS access key ID or X.509 certificate.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed due to a temporary failure of the server.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_UpdateEnrollmentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/UpdateEnrollmentStatus)

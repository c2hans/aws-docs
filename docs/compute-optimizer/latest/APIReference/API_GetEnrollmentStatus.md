---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEnrollmentStatus.html
---

# GetEnrollmentStatus
<a name="API_GetEnrollmentStatus"></a>

Returns the enrollment (opt in) status of an account to the AWS Compute Optimizer service.

If the account is the management account of an organization, this action also confirms the enrollment status of member accounts of the organization. Use the [GetEnrollmentStatusesForOrganization](API_GetEnrollmentStatusesForOrganization.md) action to get detailed information about the enrollment status of member accounts of an organization.

## Response Syntax
<a name="API_GetEnrollmentStatus_ResponseSyntax"></a>

```
{
   "lastUpdatedTimestamp": number,
   "memberAccountsEnrolled": boolean,
   "numberOfMemberAccountsOptedIn": number,
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_GetEnrollmentStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lastUpdatedTimestamp](#API_GetEnrollmentStatus_ResponseSyntax) **   <a name="computeoptimizer-GetEnrollmentStatus-response-lastUpdatedTimestamp"></a>
The Unix epoch timestamp, in seconds, of when the account enrollment status was last updated.
Type: Timestamp

 ** [memberAccountsEnrolled](#API_GetEnrollmentStatus_ResponseSyntax) **   <a name="computeoptimizer-GetEnrollmentStatus-response-memberAccountsEnrolled"></a>
Confirms the enrollment status of member accounts of the organization, if the account is a management account of an organization.
Type: Boolean

 ** [numberOfMemberAccountsOptedIn](#API_GetEnrollmentStatus_ResponseSyntax) **   <a name="computeoptimizer-GetEnrollmentStatus-response-numberOfMemberAccountsOptedIn"></a>
The count of organization member accounts that are opted in to the service, if your account is an organization management account.
Type: Integer

 ** [status](#API_GetEnrollmentStatus_ResponseSyntax) **   <a name="computeoptimizer-GetEnrollmentStatus-response-status"></a>
The enrollment status of the account.
Type: String
Valid Values: `Active | Inactive | Pending | Failed`

 ** [statusReason](#API_GetEnrollmentStatus_ResponseSyntax) **   <a name="computeoptimizer-GetEnrollmentStatus-response-statusReason"></a>
The reason for the enrollment status of the account.
For example, an account might show a status of `Pending` because member accounts of an organization require more time to be enrolled in the service.
Type: String

## Errors
<a name="API_GetEnrollmentStatus_Errors"></a>

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
<a name="API_GetEnrollmentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetEnrollmentStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetEnrollmentStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetEnrollmentStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetEnrollmentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetEnrollmentStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetEnrollmentStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetEnrollmentStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetEnrollmentStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetEnrollmentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetEnrollmentStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

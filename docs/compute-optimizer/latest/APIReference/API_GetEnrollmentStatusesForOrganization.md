---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEnrollmentStatusesForOrganization.html
---

# GetEnrollmentStatusesForOrganization
<a name="API_GetEnrollmentStatusesForOrganization"></a>

Returns the AWS Compute Optimizer enrollment (opt-in) status of organization member accounts, if your account is an organization management account.

To get the enrollment status of standalone accounts, use the [GetEnrollmentStatus](API_GetEnrollmentStatus.md) action.

## Request Syntax
<a name="API_GetEnrollmentStatusesForOrganization_RequestSyntax"></a>

```
{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEnrollmentStatusesForOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filters](#API_GetEnrollmentStatusesForOrganization_RequestSyntax) **   <a name="computeoptimizer-GetEnrollmentStatusesForOrganization-request-filters"></a>
An array of objects to specify a filter that returns a more specific list of account enrollment statuses.
Type: Array of [EnrollmentFilter](API_EnrollmentFilter.md) objects
Required: No

 ** [maxResults](#API_GetEnrollmentStatusesForOrganization_RequestSyntax) **   <a name="computeoptimizer-GetEnrollmentStatusesForOrganization-request-maxResults"></a>
The maximum number of account enrollment statuses to return with a single request. You can specify up to 100 statuses to return with each request.
To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetEnrollmentStatusesForOrganization_RequestSyntax) **   <a name="computeoptimizer-GetEnrollmentStatusesForOrganization-request-nextToken"></a>
The token to advance to the next page of account enrollment statuses.
Type: String
Required: No

## Response Syntax
<a name="API_GetEnrollmentStatusesForOrganization_ResponseSyntax"></a>

```
{
   "accountEnrollmentStatuses": [
      {
         "accountId": "string",
         "lastUpdatedTimestamp": number,
         "status": "string",
         "statusReason": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetEnrollmentStatusesForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountEnrollmentStatuses](#API_GetEnrollmentStatusesForOrganization_ResponseSyntax) **   <a name="computeoptimizer-GetEnrollmentStatusesForOrganization-response-accountEnrollmentStatuses"></a>
An array of objects that describe the enrollment statuses of organization member accounts.
Type: Array of [AccountEnrollmentStatus](API_AccountEnrollmentStatus.md) objects

 ** [nextToken](#API_GetEnrollmentStatusesForOrganization_ResponseSyntax) **   <a name="computeoptimizer-GetEnrollmentStatusesForOrganization-response-nextToken"></a>
The token to use to advance to the next page of account enrollment statuses.
This value is null when there are no more pages of account enrollment statuses to return.
Type: String

## Errors
<a name="API_GetEnrollmentStatusesForOrganization_Errors"></a>

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
<a name="API_GetEnrollmentStatusesForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetEnrollmentStatusesForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetEnrollmentStatusesForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetEnrollmentStatusesForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetEnrollmentStatusesForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetEnrollmentStatusesForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetEnrollmentStatusesForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetEnrollmentStatusesForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetEnrollmentStatusesForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetEnrollmentStatusesForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetEnrollmentStatusesForOrganization)

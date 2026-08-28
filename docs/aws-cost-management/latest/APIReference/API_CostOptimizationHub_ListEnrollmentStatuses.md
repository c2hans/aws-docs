---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListEnrollmentStatuses.html
---

# ListEnrollmentStatuses
<a name="API_CostOptimizationHub_ListEnrollmentStatuses"></a>

Retrieves the enrollment status for an account. It can also return the list of accounts that are enrolled under the organization.

## Request Syntax
<a name="API_CostOptimizationHub_ListEnrollmentStatuses_RequestSyntax"></a>

```
{
   "accountId": "{{string}}",
   "includeOrganizationInfo": {{boolean}},
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_CostOptimizationHub_ListEnrollmentStatuses_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountId](#API_CostOptimizationHub_ListEnrollmentStatuses_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEnrollmentStatuses-request-accountId"></a>
The account ID of a member account in the organization.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [includeOrganizationInfo](#API_CostOptimizationHub_ListEnrollmentStatuses_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEnrollmentStatuses-request-includeOrganizationInfo"></a>
Indicates whether to return the enrollment status for the organization.
Type: Boolean
Required: No

 ** [maxResults](#API_CostOptimizationHub_ListEnrollmentStatuses_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEnrollmentStatuses-request-maxResults"></a>
The maximum number of objects that are returned for the request.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [nextToken](#API_CostOptimizationHub_ListEnrollmentStatuses_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEnrollmentStatuses-request-nextToken"></a>
The token to retrieve the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_CostOptimizationHub_ListEnrollmentStatuses_ResponseSyntax"></a>

```
{
   "includeMemberAccounts": boolean,
   "items": [
      {
         "accountId": "string",
         "createdTimestamp": number,
         "lastUpdatedTimestamp": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_CostOptimizationHub_ListEnrollmentStatuses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [includeMemberAccounts](#API_CostOptimizationHub_ListEnrollmentStatuses_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEnrollmentStatuses-response-includeMemberAccounts"></a>
The enrollment status of all member accounts in the organization if the account is the management account or delegated administrator.
Type: Boolean

 ** [items](#API_CostOptimizationHub_ListEnrollmentStatuses_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEnrollmentStatuses-response-items"></a>
The enrollment status of a specific account ID, including creation and last updated timestamps.
Type: Array of [AccountEnrollmentStatus](API_CostOptimizationHub_AccountEnrollmentStatus.md) objects

 ** [nextToken](#API_CostOptimizationHub_ListEnrollmentStatuses_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEnrollmentStatuses-response-nextToken"></a>
The token to retrieve the next set of results.
Type: String

## Errors
<a name="API_CostOptimizationHub_ListEnrollmentStatuses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
HTTP Status Code: 400

 ** InternalServerException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fields **
The list of fields that are invalid.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_CostOptimizationHub_ListEnrollmentStatuses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cost-optimization-hub-2022-07-26/ListEnrollmentStatuses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cost-optimization-hub-2022-07-26/ListEnrollmentStatuses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/ListEnrollmentStatuses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cost-optimization-hub-2022-07-26/ListEnrollmentStatuses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/ListEnrollmentStatuses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cost-optimization-hub-2022-07-26/ListEnrollmentStatuses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cost-optimization-hub-2022-07-26/ListEnrollmentStatuses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cost-optimization-hub-2022-07-26/ListEnrollmentStatuses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cost-optimization-hub-2022-07-26/ListEnrollmentStatuses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/ListEnrollmentStatuses)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

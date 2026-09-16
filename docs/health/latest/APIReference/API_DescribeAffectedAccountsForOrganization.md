---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedAccountsForOrganization.html
---

# DescribeAffectedAccountsForOrganization
<a name="API_DescribeAffectedAccountsForOrganization"></a>

Returns a list of accounts in the organization from AWS Organizations that are affected by the provided event. For more information about the different types of AWS Health events, see [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html).

Before you can call this operation, you must first enable AWS Health to work with AWS Organizations. To do this, call the [EnableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html) operation from your organization's management account.

**Note**
This API operation uses pagination. Specify the `nextToken` parameter in the next request to return more results.

## Request Syntax
<a name="API_DescribeAffectedAccountsForOrganization_RequestSyntax"></a>

```
{
   "eventArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAffectedAccountsForOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [eventArn](#API_DescribeAffectedAccountsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeAffectedAccountsForOrganization-request-eventArn"></a>
The unique identifier for the event. The event ARN has the `arn:aws:health:event-region::event/SERVICE/EVENT_TYPE_CODE/EVENT_TYPE_PLUS_ID ` format.
For example, an event ARN might look like the following:
 `arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: Yes

 ** [maxResults](#API_DescribeAffectedAccountsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeAffectedAccountsForOrganization-request-maxResults"></a>
The maximum number of items to return in one batch, between 10 and 100, inclusive.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeAffectedAccountsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeAffectedAccountsForOrganization-request-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`
Required: No

## Response Syntax
<a name="API_DescribeAffectedAccountsForOrganization_ResponseSyntax"></a>

```
{
   "affectedAccounts": [ "string" ],
   "eventScopeCode": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAffectedAccountsForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [affectedAccounts](#API_DescribeAffectedAccountsForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeAffectedAccountsForOrganization-response-affectedAccounts"></a>
A JSON set of elements of the affected accounts.
Type: Array of strings
Length Constraints: Maximum length of 12.
Pattern: `^\S+$`

 ** [eventScopeCode](#API_DescribeAffectedAccountsForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeAffectedAccountsForOrganization-response-eventScopeCode"></a>
This parameter specifies if the AWS Health event is a public AWS service event or an account-specific event.
+ If the `eventScopeCode` value is `PUBLIC`, then the `affectedAccounts` value is always empty.
+ If the `eventScopeCode` value is `ACCOUNT_SPECIFIC`, then the `affectedAccounts` value lists the affected AWS accounts in your organization. For example, if an event affects a service such as Amazon Elastic Compute Cloud and you have AWS accounts that use that service, those account IDs appear in the response.
+ If the `eventScopeCode` value is `NONE`, then the `eventArn` that you specified in the request is invalid or doesn't exist.
Type: String
Valid Values: `PUBLIC | ACCOUNT_SPECIFIC | NONE`

 ** [nextToken](#API_DescribeAffectedAccountsForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeAffectedAccountsForOrganization-response-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`

## Errors
<a name="API_DescribeAffectedAccountsForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPaginationToken **
The specified pagination token (`nextToken`) is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAffectedAccountsForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeAffectedAccountsForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeAffectedAccountsForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeAffectedAccountsForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeAffectedAccountsForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeAffectedAccountsForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeAffectedAccountsForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeAffectedAccountsForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeAffectedAccountsForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeAffectedAccountsForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeAffectedAccountsForOrganization)

---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html
---

# DescribeAffectedEntitiesForOrganization
<a name="API_DescribeAffectedEntitiesForOrganization"></a>

Returns a list of entities that have been affected by one or more events for one or more accounts in your organization in AWS Organizations, based on the filter criteria. Entities can refer to individual customer resources, groups of customer resources, or any other construct, depending on the AWS service.

At least one event Amazon Resource Name (ARN) and account ID are required.

Before you can call this operation, you must first enable AWS Health to work with AWS Organizations. To do this, call the [EnableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html) operation from your organization's management account.

**Note**
This API operation uses pagination. Specify the `nextToken` parameter in the next request to return more results.
This operation doesn't support resource-level permissions. You can't use this operation to allow or deny access to specific AWS Health events. For more information, see [Resource- and action-based conditions](https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions) in the * AWS Health User Guide*.

## Request Syntax
<a name="API_DescribeAffectedEntitiesForOrganization_RequestSyntax"></a>

```
{
   "locale": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "organizationEntityAccountFilters": [
      {
         "awsAccountId": "{{string}}",
         "eventArn": "{{string}}",
         "statusCodes": [ "{{string}}" ]
      }
   ],
   "organizationEntityFilters": [
      {
         "awsAccountId": "{{string}}",
         "eventArn": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_DescribeAffectedEntitiesForOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [locale](#API_DescribeAffectedEntitiesForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeAffectedEntitiesForOrganization-request-locale"></a>
The locale (language) to return information in. English (en) is the default and the only supported value at this time.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `.{2,256}`
Required: No

 ** [maxResults](#API_DescribeAffectedEntitiesForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeAffectedEntitiesForOrganization-request-maxResults"></a>
The maximum number of items to return in one batch, between 1 and 100, inclusive.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeAffectedEntitiesForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeAffectedEntitiesForOrganization-request-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`
Required: No

 ** [organizationEntityAccountFilters](#API_DescribeAffectedEntitiesForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeAffectedEntitiesForOrganization-request-organizationEntityAccountFilters"></a>
A JSON set of elements including the `awsAccountId`, `eventArn` and a set of `statusCodes`.
Type: Array of [EntityAccountFilter](API_EntityAccountFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [organizationEntityFilters](#API_DescribeAffectedEntitiesForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeAffectedEntitiesForOrganization-request-organizationEntityFilters"></a>
 *This parameter has been deprecated.*
A JSON set of elements including the `awsAccountId` and the `eventArn`.
Type: Array of [EventAccountFilter](API_EventAccountFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## Response Syntax
<a name="API_DescribeAffectedEntitiesForOrganization_ResponseSyntax"></a>

```
{
   "entities": [
      {
         "awsAccountId": "string",
         "entityArn": "string",
         "entityMetadata": {
            "string" : "string"
         },
         "entityUrl": "string",
         "entityValue": "string",
         "eventArn": "string",
         "lastUpdatedTime": number,
         "statusCode": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "failedSet": [
      {
         "awsAccountId": "string",
         "errorMessage": "string",
         "errorName": "string",
         "eventArn": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAffectedEntitiesForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entities](#API_DescribeAffectedEntitiesForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeAffectedEntitiesForOrganization-response-entities"></a>
A JSON set of elements including the `awsAccountId` and its `entityArn`, `entityValue` and its `entityArn`, `lastUpdatedTime`, and `statusCode`.
Type: Array of [AffectedEntity](API_AffectedEntity.md) objects

 ** [failedSet](#API_DescribeAffectedEntitiesForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeAffectedEntitiesForOrganization-response-failedSet"></a>
A JSON set of elements of the failed response, including the `awsAccountId`, `errorMessage`, `errorName`, and `eventArn`.
Type: Array of [OrganizationAffectedEntitiesErrorItem](API_OrganizationAffectedEntitiesErrorItem.md) objects

 ** [nextToken](#API_DescribeAffectedEntitiesForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeAffectedEntitiesForOrganization-response-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`

## Errors
<a name="API_DescribeAffectedEntitiesForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPaginationToken **
The specified pagination token (`nextToken`) is not valid.
HTTP Status Code: 400

 ** UnsupportedLocale **
The specified locale is not supported.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAffectedEntitiesForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeAffectedEntitiesForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeAffectedEntitiesForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeAffectedEntitiesForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeAffectedEntitiesForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeAffectedEntitiesForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeAffectedEntitiesForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeAffectedEntitiesForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeAffectedEntitiesForOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeAffectedEntitiesForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeAffectedEntitiesForOrganization)

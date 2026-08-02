---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html
---

# DescribeEventDetailsForOrganization
<a name="API_DescribeEventDetailsForOrganization"></a>

Returns detailed information about one or more specified events for one or more AWS accounts in your organization. This information includes standard event data (such as the AWS Region and service), an event description, and (depending on the event) possible metadata. This operation doesn't return affected entities, such as the resources related to the event. To return affected entities, use the [DescribeAffectedEntitiesForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html) operation.

**Note**
Before you can call this operation, you must first enable AWS Health to work with AWS Organizations. To do this, call the [EnableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html) operation from your organization's management account.

When you call the `DescribeEventDetailsForOrganization` operation, specify the `organizationEventDetailFilters` object in the request. Depending on the AWS Health event type, note the following differences:
+ To return event details for a public event, you must specify a null value for the `awsAccountId` parameter. If you specify an account ID for a public event, AWS Health returns an error message because public events aren't specific to an account.
+ To return event details for an event that is specific to an account in your organization, you must specify the `awsAccountId` parameter in the request. If you don't specify an account ID, AWS Health returns an error message because the event is specific to an account in your organization.

For more information, see [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html).

**Note**
This operation doesn't support resource-level permissions. You can't use this operation to allow or deny access to specific AWS Health events. For more information, see [Resource- and action-based conditions](https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions) in the * AWS Health User Guide*.

## Request Syntax
<a name="API_DescribeEventDetailsForOrganization_RequestSyntax"></a>

```
{
   "locale": "{{string}}",
   "organizationEventDetailFilters": [
      {
         "awsAccountId": "{{string}}",
         "eventArn": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_DescribeEventDetailsForOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [locale](#API_DescribeEventDetailsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeEventDetailsForOrganization-request-locale"></a>
The locale (language) to return information in. English (en) is the default and the only supported value at this time.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `.{2,256}`
Required: No

 ** [organizationEventDetailFilters](#API_DescribeEventDetailsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeEventDetailsForOrganization-request-organizationEventDetailFilters"></a>
A set of JSON elements that includes the `awsAccountId` and the `eventArn`.
Type: Array of [EventAccountFilter](API_EventAccountFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_DescribeEventDetailsForOrganization_ResponseSyntax"></a>

```
{
   "failedSet": [
      {
         "awsAccountId": "string",
         "errorMessage": "string",
         "errorName": "string",
         "eventArn": "string"
      }
   ],
   "successfulSet": [
      {
         "awsAccountId": "string",
         "event": {
            "actionability": "string",
            "arn": "string",
            "availabilityZone": "string",
            "endTime": number,
            "eventScopeCode": "string",
            "eventTypeCategory": "string",
            "eventTypeCode": "string",
            "lastUpdatedTime": number,
            "personas": [ "string" ],
            "region": "string",
            "service": "string",
            "startTime": number,
            "statusCode": "string"
         },
         "eventDescription": {
            "latestDescription": "string"
         },
         "eventMetadata": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEventDetailsForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedSet](#API_DescribeEventDetailsForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeEventDetailsForOrganization-response-failedSet"></a>
Error messages for any events that could not be retrieved.
Type: Array of [OrganizationEventDetailsErrorItem](API_OrganizationEventDetailsErrorItem.md) objects

 ** [successfulSet](#API_DescribeEventDetailsForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeEventDetailsForOrganization-response-successfulSet"></a>
Information about the events that could be retrieved.
Type: Array of [OrganizationEventDetails](API_OrganizationEventDetails.md) objects

## Errors
<a name="API_DescribeEventDetailsForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UnsupportedLocale **
The specified locale is not supported.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEventDetailsForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeEventDetailsForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeEventDetailsForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeEventDetailsForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeEventDetailsForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeEventDetailsForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeEventDetailsForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeEventDetailsForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeEventDetailsForOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeEventDetailsForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeEventDetailsForOrganization)

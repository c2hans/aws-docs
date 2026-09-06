---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html
---

# DescribeEventDetails
<a name="API_DescribeEventDetails"></a>

Returns detailed information about one or more specified events. Information includes standard event data (AWS Region, service, and so on, as returned by [DescribeEvents](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEvents.html)), a detailed event description, and possible additional metadata that depends upon the nature of the event. Affected entities are not included. To retrieve the entities, use the [DescribeAffectedEntities](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html) operation.

If a specified event can't be retrieved, an error message is returned for that event.

**Note**
This operation supports resource-level permissions. You can use this operation to allow or deny access to specific AWS Health events. For more information, see [Resource- and action-based conditions](https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions) in the * AWS Health User Guide*.

## Request Syntax
<a name="API_DescribeEventDetails_RequestSyntax"></a>

```
{
   "eventArns": [ "{{string}}" ],
   "locale": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEventDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [eventArns](#API_DescribeEventDetails_RequestSyntax) **   <a name="AWSHealth-DescribeEventDetails-request-eventArns"></a>
A list of event ARNs (unique identifiers). For example: `"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: Yes

 ** [locale](#API_DescribeEventDetails_RequestSyntax) **   <a name="AWSHealth-DescribeEventDetails-request-locale"></a>
The locale (language) to return information in. English (en) is the default and the only supported value at this time.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `.{2,256}`
Required: No

## Response Syntax
<a name="API_DescribeEventDetails_ResponseSyntax"></a>

```
{
   "failedSet": [
      {
         "errorMessage": "string",
         "errorName": "string",
         "eventArn": "string"
      }
   ],
   "successfulSet": [
      {
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
<a name="API_DescribeEventDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedSet](#API_DescribeEventDetails_ResponseSyntax) **   <a name="AWSHealth-DescribeEventDetails-response-failedSet"></a>
Error messages for any events that could not be retrieved.
Type: Array of [EventDetailsErrorItem](API_EventDetailsErrorItem.md) objects

 ** [successfulSet](#API_DescribeEventDetails_ResponseSyntax) **   <a name="AWSHealth-DescribeEventDetails-response-successfulSet"></a>
Information about the events that could be retrieved.
Type: Array of [EventDetails](API_EventDetails.md) objects

## Errors
<a name="API_DescribeEventDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UnsupportedLocale **
The specified locale is not supported.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeEventDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeEventDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeEventDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeEventDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeEventDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeEventDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeEventDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeEventDetails)

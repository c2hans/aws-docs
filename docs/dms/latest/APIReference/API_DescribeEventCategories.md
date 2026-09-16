---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEventCategories.html
---

# DescribeEventCategories
<a name="API_DescribeEventCategories"></a>

Lists categories for all event source types, or, if specified, for a specified source type. You can see a list of the event categories and source types in [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the * AWS Database Migration Service User Guide.*

## Request Syntax
<a name="API_DescribeEventCategories_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "SourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEventCategories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeEventCategories_RequestSyntax) **   <a name="DMS-DescribeEventCategories-request-Filters"></a>
Filters applied to the event categories.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [SourceType](#API_DescribeEventCategories_RequestSyntax) **   <a name="DMS-DescribeEventCategories-request-SourceType"></a>
 The type of AWS DMS resource that generates events.
Valid values: replication-instance \| replication-task
Type: String
Required: No

## Response Syntax
<a name="API_DescribeEventCategories_ResponseSyntax"></a>

```
{
   "EventCategoryGroupList": [
      {
         "EventCategories": [ "string" ],
         "SourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEventCategories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventCategoryGroupList](#API_DescribeEventCategories_ResponseSyntax) **   <a name="DMS-DescribeEventCategories-response-EventCategoryGroupList"></a>
A list of event categories.
Type: Array of [EventCategoryGroup](API_EventCategoryGroup.md) objects

## Errors
<a name="API_DescribeEventCategories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeEventCategories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeEventCategories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeEventCategories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeEventCategories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeEventCategories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeEventCategories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeEventCategories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeEventCategories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeEventCategories)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeEventCategories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeEventCategories)

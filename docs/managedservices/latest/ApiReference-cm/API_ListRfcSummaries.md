---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListRfcSummaries.html
---

# ListRfcSummaries
<a name="API_ListRfcSummaries"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Returns summaries of Request for Change (RFCs) that meet the specified criteria.

## Request Syntax
<a name="API_ListRfcSummaries_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Attribute": "{{string}}",
         "Condition": "{{string}}",
         "Value": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Locale": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RequestedEndTimeRange": {
      "EndTime": "{{string}}",
      "StartTime": "{{string}}"
   },
   "RequestedStartTimeRange": {
      "EndTime": "{{string}}",
      "StartTime": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListRfcSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListRfcSummaries_RequestSyntax) **   <a name="amscm-ListRfcSummaries-request-Filters"></a>
You can Filter results based on an Attribute and Value combined in a logical AND operation, or based on an Attribute, a Condition, and Values.
The following are the valid filter attributes:
ActualEndTime
+ Valid Values: Any string representing an ISO8601 datetime (e.g., “20170101T000000Z”).
+ Valid Conditions: Before, After, Between
+ Default Condition: None
+ Notes: The Before or After condition only accepts one value in the Values field. The Between condition must have exactly two values in the Values field, where the first value should represent a date that happens before the second value.
ActualStartTime
+ Valid Values: Any string representing an ISO8601 datetime (e.g., “20170101T000000Z”).
+ Valid Conditions: Before, After, Between
+ Default Condition: None
+ Notes: The Before or After condition only accepts one value in the Values field. The Between condition must have exactly two values in the Values field, where the first value should represent a date that happens before the second value.
AutomationStatusId
+ Valid Values: Manual, Automated
+ Valid Conditions: Equals
+ Default Condition: Equals
+ Notes: There are only two automation statuses.
ChangeTypeId
+ Valid Values: Any valid change type ID; for example, ct-123h45t6uz7jl.
+ Valid Conditions: Equals
+ Default Condition: Equals
+ Notes: [Finding a change type, using the query option](https://docs.aws.amazon.com/managedservices/latest/userguide/ug-find-ct-ex-section.html) in the *AMS User Guide*.
ChangeTypeVersion
+ Valid Values: Any valid change type ID; for example, 1.0.
+ Valid Conditions: Equals
+ Default Condition: Equals
+ Notes: [Finding a change type, using the query option](https://docs.aws.amazon.com/managedservices/latest/userguide/ug-find-ct-ex-section.html) in the *AMS User Guide*.
CreatedBy
+ Valid Values: Any string (maximum allowed length is 2048 characters).
+ Valid Conditions: Contains
+ Default Condition: Contains
+ Notes: The `CreatedBy` field of the RFC contains the ARN of the user who created it.
CreatedTime
+ Valid Values: Any string representing an ISO8601 datetime (e.g., “20170101T000000Z”).
+ Valid Conditions: Before, After, Between
+ Default Condition: None
+ Notes: The Before or After condition only accepts one value in the Values field. The Between condition must have exactly two values in the Values field, where the first value should represent a date that happens before the second value.
LastModifiedTime
+ Valid Values: Any string representing an ISO8601 datetime (e.g., “20170101T000000Z”).
+ Valid Conditions: Before, After, Between
+ Default Condition: None
+ Notes: The Before or After condition only accepts one value in the Values field. The Between condition must have exactly two values in the Values field, where the first value should represent a date that happens before the second value.
LastSubmittedTime
+ Valid Values: Any string representing an ISO8601 datetime (e.g., “20170101T000000Z”).
+ Valid Conditions: Before, After, Between
+ Default Condition: None
+ Notes: The Before or After condition only accepts one value in the Values field. The Between condition must have exactly two values in the Values field, where the first value should represent a date that happens before the second value.
RequestedEndTime
+ Valid Values: Any string representing an ISO8601 datetime (e.g., “20170101T000000Z”).
+ Valid Conditions: Before, After, Between
+ Default Condition: None
+ Notes:The Before or After condition only accepts one value in the Values field. The Between condition must have exactly two values in the Values field, where the first value should represent a date that happens before the second value.
RequestedStartTime
+ Valid Values: Any string representing an ISO8601 datetime (e.g., “20170101T000000Z”).
+ Valid Conditions: Before, After, Between
+ Default Condition: None
+ Notes: The Before or After condition only accepts one value in the Values field. The Between condition must have exactly two values in the Values field, where the first value should represent a date that happens before the second value.
RfcStatusId
+ Valid Values: Canceled, Editing, Failure, InProgress, PendingApproval, Rejected, Scheduled, Success
+ Valid Conditions: Equals
+ Default Condition: Equals
+ Notes: Refresh the RFC list in the AMS console or run [GetRfc](API_GetRfc.md).
Title
+ Valid Values: Any valid RFC title.
+ Valid Conditions: Contains
+ Default Condition: Contains
+ Notes: Regular expressions in each individual field are not supported. Case insensitive search.
For more information about the filter attributes and examples, see [Finding RFCs](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-rfc-find-col.html) in the *AMS User Guide*.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Locale](#API_ListRfcSummaries_RequestSyntax) **   <a name="amscm-ListRfcSummaries-request-Locale"></a>
The locale (language) to return information in. The default is English. **Note:** For future use; not currently implemented.
Type: String
Required: No

 ** [MaxResults](#API_ListRfcSummaries_RequestSyntax) **   <a name="amscm-ListRfcSummaries-request-MaxResults"></a>
The maximum number of items to return in one batch. Valid values are 20-100.
Type: Integer
Required: No

 ** [NextToken](#API_ListRfcSummaries_RequestSyntax) **   <a name="amscm-ListRfcSummaries-request-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String
Required: No

 ** [RequestedEndTimeRange](#API_ListRfcSummaries_RequestSyntax) **   <a name="amscm-ListRfcSummaries-request-RequestedEndTimeRange"></a>
 *This parameter has been deprecated.*
The span of time during which you want the change to end.
Type: [TimeRange](API_TimeRange.md) object
Required: No

 ** [RequestedStartTimeRange](#API_ListRfcSummaries_RequestSyntax) **   <a name="amscm-ListRfcSummaries-request-RequestedStartTimeRange"></a>
 *This parameter has been deprecated.*
The span of time during which you want the change to start.
Type: [TimeRange](API_TimeRange.md) object
Required: No

## Response Syntax
<a name="API_ListRfcSummaries_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RfcSummaries": [
      {
         "ActionState": {
            "Id": "string",
            "Name": "string"
         },
         "ActualExecutionTimeRange": {
            "EndTime": "string",
            "StartTime": "string"
         },
         "ApprovalState": {
            "AwsApprovalStatus": {
               "Id": "string",
               "Name": "string"
            },
            "CustomerApprovalStatus": {
               "Id": "string",
               "Name": "string"
            }
         },
         "AutomationStatus": {
            "Id": "string",
            "Name": "string"
         },
         "ChangeTypeId": "string",
         "ChangeTypeVersion": "string",
         "CreatedBy": "string",
         "CreatedTime": "string",
         "LastCorrespondenceTime": "string",
         "LastModifiedTime": "string",
         "LastSubmittedTime": "string",
         "RequestedExecutionTimeRange": {
            "EndTime": "string",
            "StartTime": "string"
         },
         "RfcId": "string",
         "Status": {
            "Id": "string",
            "Name": "string"
         },
         "Title": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRfcSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRfcSummaries_ResponseSyntax) **   <a name="amscm-ListRfcSummaries-response-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String

 ** [RfcSummaries](#API_ListRfcSummaries_ResponseSyntax) **   <a name="amscm-ListRfcSummaries-response-RfcSummaries"></a>
The summaries of RFCs that meet the specified criteria.
Type: Array of [RfcSummary](API_RfcSummary.md) objects

## Errors
<a name="API_ListRfcSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

## Examples
<a name="API_ListRfcSummaries_Examples"></a>

### Sample Request Using the CreatedBy Filter Attribute
<a name="API_ListRfcSummaries_Example_1"></a>

The following is an example request using the `CreatedBy` filter attribute.

```
{
  "Operation": "com.amazonaws.services.managedservices.cm.model#ListRfcSummaries",
  "Service": "com.amazonaws.services.managedservices.cm.model#AWSEnergonService",
  "Input": {
    "Filters": [
      {
        "Attribute": "CreatedBy",
        "Values": [
          "John", "Mary"
        ],
        "Condition": "Contains"
      }
    ]
  }
}
```

### Sample Response Using the CreatedBy Filter Attribute
<a name="API_ListRfcSummaries_Example_2"></a>

The following is an example response from the request using the `CreatedBy` filter attribute.

```
{
  "Output": {
    "__type": "com.amazonaws.services.managedservices.cm.model#ListRfcSummariesResponse",
    "NextToken": null,
    "RfcSummaries": [
      {
        "ActionState": {
          "Id": "NotApplicable",
          "Name": "NotApplicable"
        },
        "ActualExecutionTimeRange": {
          "EndTime": null,
          "StartTime": null
        },
        "AutomationStatus": {
          "Id": "Automated",
          "Name": "Automated"
        },
        "ChangeTypeId": "ct-3izj492hm8s02",
        "ChangeTypeVersion": "4.0",
        "CreatedBy": "arn:aws:sts::123456789012:assumed-role/FullAccess/John-Isengard",
        "CreatedTime": "20191025T232624Z",
        "LastCorrespondenceTime": null,
        "LastModifiedTime": "20191025T232624Z",
        "LastSubmittedTime": null,
        "RequestedExecutionTimeRange": {
          "EndTime": null,
          "StartTime": null
        },
        "RfcId": "14b7029f-0a16-a83e-09d6-cd4fc9598ba9",
        "Status": {
          "Id": "Editing",
          "Name": "Editing"
        },
        "Title": "test"
      },
      {
        "ActionState": {
          "Id": "NotApplicable",
          "Name": "NotApplicable"
        },
        "ActualExecutionTimeRange": {
          "EndTime": "20191017T184158Z",
          "StartTime": "20191017T184135Z"
        },
        "AutomationStatus": {
          "Id": "Automated",
          "Name": "Automated"
        },
        "ChangeTypeId": "ct-3izj492hm8s02",
        "ChangeTypeVersion": "2.0",
        "CreatedBy": "arn:aws:sts::111122223333:assumed-role/PowerUserAccess/Mary-Isengard",
        "CreatedTime": "20191017T183530Z",
        "LastCorrespondenceTime": null,
        "LastModifiedTime": "20191017T184158Z",
        "LastSubmittedTime": "20191017T183604Z",
        "RequestedExecutionTimeRange": {
          "EndTime": null,
          "StartTime": null
        },
        "RfcId": "32b6ed80-6efd-b096-9a2b-ff273c3a52f6",
        "Status": {
          "Id": "Success",
          "Name": "Success"
        },
        "Title": "testExecutionResponse"
      }
    ]
  }
}
```

## See Also
<a name="API_ListRfcSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/ListRfcSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/ListRfcSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/ListRfcSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/ListRfcSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/ListRfcSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/ListRfcSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/ListRfcSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/ListRfcSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/ListRfcSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/ListRfcSummaries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

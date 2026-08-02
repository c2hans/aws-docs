---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetOpsSummary.html
---

# GetOpsSummary
<a name="API_GetOpsSummary"></a>

View a summary of operations metadata (OpsData) based on specified filters and aggregators. OpsData can include information about AWS Systems Manager OpsCenter operational workitems (OpsItems) as well as information about any AWS resource or service configured to report OpsData to AWS Systems Manager Explorer.

## Request Syntax
<a name="API_GetOpsSummary_RequestSyntax"></a>

```
{
   "Aggregators": [
      {
         "Aggregators": [
            "OpsAggregator"
         ],
         "AggregatorType": "{{string}}",
         "AttributeName": "{{string}}",
         "Filters": [
            {
               "Key": "{{string}}",
               "Type": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ],
         "TypeName": "{{string}}",
         "Values": {
            "{{string}}" : "{{string}}"
         }
      }
   ],
   "Filters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResultAttributes": [
      {
         "TypeName": "{{string}}"
      }
   ],
   "SyncName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetOpsSummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Aggregators](#API_GetOpsSummary_RequestSyntax) **   <a name="systemsmanager-GetOpsSummary-request-Aggregators"></a>
Optional aggregators that return counts of OpsData based on one or more expressions.
Type: Array of [OpsAggregator](API_OpsAggregator.md) objects
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Required: No

 ** [Filters](#API_GetOpsSummary_RequestSyntax) **   <a name="systemsmanager-GetOpsSummary-request-Filters"></a>
Optional filters used to scope down the returned OpsData.
Type: Array of [OpsFilter](API_OpsFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_GetOpsSummary_RequestSyntax) **   <a name="systemsmanager-GetOpsSummary-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_GetOpsSummary_RequestSyntax) **   <a name="systemsmanager-GetOpsSummary-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

 ** [ResultAttributes](#API_GetOpsSummary_RequestSyntax) **   <a name="systemsmanager-GetOpsSummary-request-ResultAttributes"></a>
The OpsData data type to return.
Type: Array of [OpsResultAttribute](API_OpsResultAttribute.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [SyncName](#API_GetOpsSummary_RequestSyntax) **   <a name="systemsmanager-GetOpsSummary-request-SyncName"></a>
Specify the name of a resource data sync to get.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_GetOpsSummary_ResponseSyntax"></a>

```
{
   "Entities": [
      {
         "Data": {
            "string" : {
               "CaptureTime": "string",
               "Content": [
                  {
                     "string" : "string"
                  }
               ]
            }
         },
         "Id": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetOpsSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entities](#API_GetOpsSummary_ResponseSyntax) **   <a name="systemsmanager-GetOpsSummary-response-Entities"></a>
The list of aggregated details and filtered OpsData.
Type: Array of [OpsEntity](API_OpsEntity.md) objects

 ** [NextToken](#API_GetOpsSummary_ResponseSyntax) **   <a name="systemsmanager-GetOpsSummary-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

## Errors
<a name="API_GetOpsSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidAggregatorException **
The specified aggregator isn't valid for the group type. Verify that the aggregator you provided is supported.
HTTP Status Code: 400

 ** InvalidFilter **
The filter name isn't valid. Verify that you entered the correct name and try again.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

 ** InvalidTypeNameException **
The parameter type name isn't valid.
HTTP Status Code: 400

 ** ResourceDataSyncNotFoundException **
The specified sync name wasn't found.
HTTP Status Code: 400

## Examples
<a name="API_GetOpsSummary_Examples"></a>

### Example
<a name="API_GetOpsSummary_Example_1"></a>

This example illustrates one usage of GetOpsSummary.

#### Sample Request
<a name="API_GetOpsSummary_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetOpsSummary
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240330T152044Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240330/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2
```

#### Sample Response
<a name="API_GetOpsSummary_Example_1_Response"></a>

```
{
    "Entities": [
        {
            "Data": {
                "AWS:OpsItem": {
                    "CaptureTime": "2024-02-26T05:59:57.430Z",
                    "Content": [
                        {
                            "AccountId": "111122223333",
                            "Category": "Availability",
                            "CreatedBy": "arn:aws:sts::111122223333:assumed-role/OpsCenterRole/af3935bb93783f02aeea51784EXAMPLE",
                            "CreatedTime": "2024-02-26T07:18:37.193Z",
                            "Description": "CloudWatch Event Rule SSMOpsItems-SSM-maintenance-window-execution-failed was triggered. Your SSM Maintenance Window execution has failed. See below for more details.",
                            "LastModifiedBy": "arn:aws:sts::111122223333:assumed-role/OpsCenterRole/af3935bb93783f02aeea51784EXAMPLE",
                            "LastModifiedTime": "2024-02-26T07:18:37.193Z",
                            "Notifications": "",
                            "OperationalData": "{\"/aws/resources\":{\"type\":\"SearchableString\",\"value\":\"[{\\\"arn\\\":\\\"arn:aws:ssm:us-east-2:111122223333:maintenancewindow/mw-0e357ebdc6EXAMPLE\\\"}]\"},\"/aws/dedup\":{\"type\":\"SearchableString\",\"value\":\"{\\\"dedupString\\\":\\\"SSMOpsItems-SSM-maintenance-window-execution-failed\\\"}\"}}",
                            "OpsItemId": "oi-f99f2EXAMPLE",
                            "RelatedItems": "",
                            "Severity": "3",
                            "Source": "SSM",
                            "Status": "Open",
                            "Title": "SSM Maintenance Window execution failed"
                        }
                    ]
                }
            },
            "Id": "oi-f99f2EXAMPLE"
        },---truncated---
    ]
}
```

## See Also
<a name="API_GetOpsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetOpsSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetOpsSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetOpsSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetOpsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetOpsSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetOpsSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetOpsSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetOpsSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetOpsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetOpsSummary)

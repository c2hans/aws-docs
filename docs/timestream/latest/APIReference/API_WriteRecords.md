---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_WriteRecords.html
---

# WriteRecords
<a name="API_WriteRecords"></a>

Enables you to write your time-series data into Timestream. You can specify a single data point or a batch of data points to be inserted into the system. Timestream offers you a flexible schema that auto detects the column names and data types for your Timestream tables based on the dimension names and data types of the data points you specify when invoking writes into the database.

Timestream supports eventual consistency read semantics. This means that when you query data immediately after writing a batch of data into Timestream, the query results might not reflect the results of a recently completed write operation. The results may also include some stale data. If you repeat the query request after a short time, the results should return the latest data. [Service quotas apply](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html).

See [code sample](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.write.html) for details.

 **Upserts**

You can use the `Version` parameter in a `WriteRecords` request to update data points. Timestream tracks a version number with each record. `Version` defaults to `1` when it's not specified for the record in the request. Timestream updates an existing record’s measure value along with its `Version` when it receives a write request with a higher `Version` number for that record. When it receives an update request where the measure value is the same as that of the existing record, Timestream still updates `Version`, if it is greater than the existing value of `Version`. You can update a data point as many times as desired, as long as the value of `Version` continuously increases.

 For example, suppose you write a new record without indicating `Version` in the request. Timestream stores this record, and set `Version` to `1`. Now, suppose you try to update this record with a `WriteRecords` request of the same record with a different measure value but, like before, do not provide `Version`. In this case, Timestream will reject this update with a `RejectedRecordsException` since the updated record’s version is not greater than the existing value of Version.

However, if you were to resend the update request with `Version` set to `2`, Timestream would then succeed in updating the record’s value, and the `Version` would be set to `2`. Next, suppose you sent a `WriteRecords` request with this same record and an identical measure value, but with `Version` set to `3`. In this case, Timestream would only update `Version` to `3`. Any further updates would need to send a version number greater than `3`, or the update requests would receive a `RejectedRecordsException`.

## Request Syntax
<a name="API_WriteRecords_RequestSyntax"></a>

```
{
   "CommonAttributes": {
      "Dimensions": [
         {
            "DimensionValueType": "{{string}}",
            "Name": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "MeasureName": "{{string}}",
      "MeasureValue": "{{string}}",
      "MeasureValues": [
         {
            "Name": "{{string}}",
            "Type": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "MeasureValueType": "{{string}}",
      "Time": "{{string}}",
      "TimeUnit": "{{string}}",
      "Version": {{number}}
   },
   "DatabaseName": "{{string}}",
   "Records": [
      {
         "Dimensions": [
            {
               "DimensionValueType": "{{string}}",
               "Name": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "MeasureName": "{{string}}",
         "MeasureValue": "{{string}}",
         "MeasureValues": [
            {
               "Name": "{{string}}",
               "Type": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "MeasureValueType": "{{string}}",
         "Time": "{{string}}",
         "TimeUnit": "{{string}}",
         "Version": {{number}}
      }
   ],
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_WriteRecords_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CommonAttributes](#API_WriteRecords_RequestSyntax) **   <a name="timestream-WriteRecords-request-CommonAttributes"></a>
A record that contains the common measure, dimension, time, and version attributes shared across all the records in the request. The measure and dimension attributes specified will be merged with the measure and dimension attributes in the records object when the data is written into Timestream. Dimensions may not overlap, or a `ValidationException` will be thrown. In other words, a record must contain dimensions with unique names.
Type: [Record](API_Record.md) object
Required: No

 ** [DatabaseName](#API_WriteRecords_RequestSyntax) **   <a name="timestream-WriteRecords-request-DatabaseName"></a>
The name of the Timestream database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Required: Yes

 ** [Records](#API_WriteRecords_RequestSyntax) **   <a name="timestream-WriteRecords-request-Records"></a>
An array of records that contain the unique measure, dimension, time, and version attributes for each time-series data point.
Type: Array of [Record](API_Record.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [TableName](#API_WriteRecords_RequestSyntax) **   <a name="timestream-WriteRecords-request-TableName"></a>
The name of the Timestream table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_WriteRecords_ResponseSyntax"></a>

```
{
   "RecordsIngested": {
      "MagneticStore": number,
      "MemoryStore": number,
      "Total": number
   }
}
```

## Response Elements
<a name="API_WriteRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RecordsIngested](#API_WriteRecords_ResponseSyntax) **   <a name="timestream-WriteRecords-response-RecordsIngested"></a>
Information on the records ingested by this request.
Type: [RecordsIngested](API_RecordsIngested.md) object

## Errors
<a name="API_WriteRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
 Timestream was unable to fully process this request because of an internal server error.
HTTP Status Code: 500

 ** InvalidEndpointException **
The requested endpoint was not valid.
HTTP Status Code: 400

 ** RejectedRecordsException **
 WriteRecords would throw this exception in the following cases:
+ Records with duplicate data where there are multiple records with the same dimensions, timestamps, and measure names but:
  + Measure values are different
  + Version is not present in the request *or* the value of version in the new record is equal to or lower than the existing value

   In this case, if Timestream rejects data, the `ExistingVersion` field in the `RejectedRecords` response will indicate the current record’s version. To force an update, you can resend the request with a version for the record set to a value greater than the `ExistingVersion`.
+  Records with timestamps that lie outside the retention duration of the memory store.
+  Records with dimensions or measures that exceed the Timestream defined limits.
 For more information, see [Quotas](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html) in the Amazon Timestream Developer Guide.
 ** RejectedRecords **

HTTP Status Code: 400

 ** ResourceNotFoundException **
The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.
HTTP Status Code: 400

 ** ThrottlingException **
 Too many requests were made by a user and they exceeded the service quotas. The request was throttled.
HTTP Status Code: 400

 ** ValidationException **
 An invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_WriteRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-write-2018-11-01/WriteRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-write-2018-11-01/WriteRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/WriteRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-write-2018-11-01/WriteRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/WriteRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-write-2018-11-01/WriteRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-write-2018-11-01/WriteRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-write-2018-11-01/WriteRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/timestream-write-2018-11-01/WriteRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/WriteRecords)

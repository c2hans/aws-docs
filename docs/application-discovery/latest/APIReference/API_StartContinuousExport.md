---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartContinuousExport.html
---

# StartContinuousExport
<a name="API_StartContinuousExport"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Start the continuous flow of agent's discovered data into Amazon Athena.

## Response Syntax
<a name="API_StartContinuousExport_ResponseSyntax"></a>

```
{
   "dataSource": "string",
   "exportId": "string",
   "s3Bucket": "string",
   "schemaStorageConfig": {
      "string" : "string"
   },
   "startTime": number
}
```

## Response Elements
<a name="API_StartContinuousExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataSource](#API_StartContinuousExport_ResponseSyntax) **   <a name="DiscServ-StartContinuousExport-response-dataSource"></a>
The type of data collector used to gather this data (currently only offered for AGENT).
Type: String
Valid Values: `AGENT`

 ** [exportId](#API_StartContinuousExport_ResponseSyntax) **   <a name="DiscServ-StartContinuousExport-response-exportId"></a>
The unique ID assigned to this export.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`

 ** [s3Bucket](#API_StartContinuousExport_ResponseSyntax) **   <a name="DiscServ-StartContinuousExport-response-s3Bucket"></a>
The name of the s3 bucket where the export data parquet files are stored.
Type: String

 ** [schemaStorageConfig](#API_StartContinuousExport_ResponseSyntax) **   <a name="DiscServ-StartContinuousExport-response-schemaStorageConfig"></a>
A dictionary which describes how the data is stored.
+  `databaseName` - the name of the Glue database used to store the schema.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 252.
Value Length Constraints: Maximum length of 10000.
Value Pattern: `[\s\S]*`

 ** [startTime](#API_StartContinuousExport_ResponseSyntax) **   <a name="DiscServ-StartContinuousExport-response-startTime"></a>
The timestamp representing when the continuous export was started.
Type: Timestamp

## Errors
<a name="API_StartContinuousExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** ConflictErrorException **
Conflict error.
HTTP Status Code: 400

 ** HomeRegionNotSetException **
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
The home Region is not set. Set the home Region to continue.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters are not valid. Verify the parameters and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** OperationNotPermittedException **
This operation is not permitted.
HTTP Status Code: 400

 ** ResourceInUseException **
This issue occurs when the same `clientRequestToken` is used with the `StartImportTask` action, but with different parameters. For example, you use the same request token but have two different import URLs, you can encounter this issue. If the import tasks are meant to be different, use a different `clientRequestToken`, and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_StartContinuousExport_Examples"></a>

### Start a continuous export
<a name="API_StartContinuousExport_Example_1"></a>

The following example shows the response of starting a continuous export.

#### Sample Response
<a name="API_StartContinuousExport_Example_1_Response"></a>

```
{
    "startTime": 1531247730.19,
    "dataSource": "AGENT",
    "schemaStorageConfig": {
        "databaseName": "application_discovery_service_database"
    },
    "exportId": "continuous-export-181b77c3-7jf3-4610-924e-7acafe5bbc59",
    "s3Bucket": "aws-application-discovery-service-92costafer5c9vn0qjane94mi"
}
```

## See Also
<a name="API_StartContinuousExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/StartContinuousExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/StartContinuousExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/StartContinuousExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/StartContinuousExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/StartContinuousExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/StartContinuousExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/StartContinuousExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/StartContinuousExport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/StartContinuousExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/StartContinuousExport)

---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetDataSource.html
---

# GetDataSource
<a name="API_GetDataSource"></a>

Returns a `DataSource` that includes metadata and data file information, as well as the current status of the `DataSource`.

 `GetDataSource` provides results in normal or verbose format. The verbose format adds the schema description and the list of files pointed to by the DataSource to the normal format.

## Request Syntax
<a name="API_GetDataSource_RequestSyntax"></a>

```
{
   "DataSourceId": "{{string}}",
   "Verbose": {{boolean}}
}
```

## Request Parameters
<a name="API_GetDataSource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataSourceId](#API_GetDataSource_RequestSyntax) **   <a name="amazonml-GetDataSource-request-DataSourceId"></a>
The ID assigned to the `DataSource` at creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Verbose](#API_GetDataSource_RequestSyntax) **   <a name="amazonml-GetDataSource-request-Verbose"></a>
Specifies whether the `GetDataSource` operation should return `DataSourceSchema`.
If true, `DataSourceSchema` is returned.
If false, `DataSourceSchema` is not returned.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetDataSource_ResponseSyntax"></a>

```
{
   "ComputeStatistics": boolean,
   "ComputeTime": number,
   "CreatedAt": number,
   "CreatedByIamUser": "string",
   "DataLocationS3": "string",
   "DataRearrangement": "string",
   "DataSizeInBytes": number,
   "DataSourceId": "string",
   "DataSourceSchema": "string",
   "FinishedAt": number,
   "LastUpdatedAt": number,
   "LogUri": "string",
   "Message": "string",
   "Name": "string",
   "NumberOfFiles": number,
   "RDSMetadata": {
      "Database": {
         "DatabaseName": "string",
         "InstanceIdentifier": "string"
      },
      "DatabaseUserName": "string",
      "DataPipelineId": "string",
      "ResourceRole": "string",
      "SelectSqlQuery": "string",
      "ServiceRole": "string"
   },
   "RedshiftMetadata": {
      "DatabaseUserName": "string",
      "RedshiftDatabase": {
         "ClusterIdentifier": "string",
         "DatabaseName": "string"
      },
      "SelectSqlQuery": "string"
   },
   "RoleARN": "string",
   "StartedAt": number,
   "Status": "string"
}
```

## Response Elements
<a name="API_GetDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComputeStatistics](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-ComputeStatistics"></a>
 The parameter is `true` if statistics need to be generated from the observation data.
Type: Boolean

 ** [ComputeTime](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-ComputeTime"></a>
The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the `DataSource`, normalized and scaled on computation resources. `ComputeTime` is only available if the `DataSource` is in the `COMPLETED` state and the `ComputeStatistics` is set to true.
Type: Long

 ** [CreatedAt](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-CreatedAt"></a>
The time that the `DataSource` was created. The time is expressed in epoch time.
Type: Timestamp

 ** [CreatedByIamUser](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-CreatedByIamUser"></a>
The AWS user account from which the `DataSource` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
Type: String
Pattern: `arn:aws:iam::[0-9]+:((user/.+)|(root))`

 ** [DataLocationS3](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-DataLocationS3"></a>
The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`

 ** [DataRearrangement](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-DataRearrangement"></a>
A JSON string that represents the splitting and rearrangement requirement used when this `DataSource` was created.
Type: String

 ** [DataSizeInBytes](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-DataSizeInBytes"></a>
The total size of observations in the data files.
Type: Long

 ** [DataSourceId](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-DataSourceId"></a>
The ID assigned to the `DataSource` at creation. This value should be identical to the value of the `DataSourceId` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [DataSourceSchema](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-DataSourceSchema"></a>
The schema used by all of the data files of this `DataSource`.
 **Note:** This parameter is provided as part of the verbose format.
Type: String
Length Constraints: Maximum length of 131071.

 ** [FinishedAt](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-FinishedAt"></a>
The epoch time when Amazon Machine Learning marked the `DataSource` as `COMPLETED` or `FAILED`. `FinishedAt` is only available when the `DataSource` is in the `COMPLETED` or `FAILED` state.
Type: Timestamp

 ** [LastUpdatedAt](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-LastUpdatedAt"></a>
The time of the most recent edit to the `DataSource`. The time is expressed in epoch time.
Type: Timestamp

 ** [LogUri](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-LogUri"></a>
A link to the file containing logs of `CreateDataSourceFrom*` operations.
Type: String

 ** [Message](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-Message"></a>
The user-supplied description of the most recent details about creating the `DataSource`.
Type: String
Length Constraints: Maximum length of 10240.

 ** [Name](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-Name"></a>
A user-supplied name or description of the `DataSource`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`

 ** [NumberOfFiles](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-NumberOfFiles"></a>
The number of data files referenced by the `DataSource`.
Type: Long

 ** [RDSMetadata](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-RDSMetadata"></a>
The datasource details that are specific to Amazon RDS.
Type: [RDSMetadata](API_RDSMetadata.md) object

 ** [RedshiftMetadata](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-RedshiftMetadata"></a>
Describes the `DataSource` details specific to Amazon Redshift.
Type: [RedshiftMetadata](API_RedshiftMetadata.md) object

 ** [RoleARN](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-RoleARN"></a>
The Amazon Resource Name (ARN) of an [AWS IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts), such as the following: arn:aws:iam::account:role/rolename.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 110.

 ** [StartedAt](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-StartedAt"></a>
The epoch time when Amazon Machine Learning marked the `DataSource` as `INPROGRESS`. `StartedAt` isn't available if the `DataSource` is in the `PENDING` state.
Type: Timestamp

 ** [Status](#API_GetDataSource_ResponseSyntax) **   <a name="amazonml-GetDataSource-response-Status"></a>
The current status of the `DataSource`. This element can have one of the following values:
+  `PENDING` - Amazon ML submitted a request to create a `DataSource`.
+  `INPROGRESS` - The creation process is underway.
+  `FAILED` - The request to create a `DataSource` did not run to completion. It is not usable.
+  `COMPLETED` - The creation process completed successfully.
+  `DELETED` - The `DataSource` is marked as deleted. It is not usable.
Type: String
Valid Values: `PENDING | INPROGRESS | FAILED | COMPLETED | DELETED`

## Errors
<a name="API_GetDataSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred when trying to process a request.
HTTP Status Code: 500

 ** InvalidInputException **
An error on the client occurred. Typically, the cause is an invalid input value.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource cannot be located.
HTTP Status Code: 400

## Examples
<a name="API_GetDataSource_Examples"></a>

### The following is a sample request and response of the GetDataSource operation.
<a name="API_GetDataSource_Example_1"></a>

This example illustrates one usage of GetDataSource.

#### Sample Request
<a name="API_GetDataSource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.GetDataSource
{"DataSourceId": "17SdAv6WC6r5vACAxF7U", "Verbose": true}
```

#### Sample Response
<a name="API_GetDataSource_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  {
    "CreatedAt":141045168.275,
    "CreatedByIamUser":"arn:aws:iam::<awsAccountId>:user/testuser",
    "DataLocationS3":"s3://eml-test-EXAMPLE /data.csv",
    "DataRearrangement": "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}",
    "DataSizeInBytes":0,"DataSourceId":"17SdAv6WC6r5vACAxF7U",
    "DataSourceSchema":"
    {
      \"version\":\"1.0\",
      \"recordAnnotationFieldName\":null,
      \"recordWeightFieldName\":\"weight\",
      \"targetFieldName\":\"label\",
      \"dataFormat\":\"CSV\",
      \"dataFileContainsHeader\":false,
      \"attributes\":
      [
        {\"attributeName\":\"obsId\",\"attributeType\":\"NUMERIC\"},
        {\"attributeName\":\"label\",\"attributeType\":\"BINARY\"},
        {\"attributeName\":\"weight\",\"attributeType\":\"NUMERIC\"},
        {\"attributeName\":\"x\",\"attributeType\":\"TEXT\"}
      ],
      \"excludedAttributeNames\":[]
    }",
    "DataStatisticsStatus":"COMPLETED",
    "LastUpdatedAt":141045168.275,
    "LogUri": "https://s3bucket/locationToLogs/logname.tar.gz",
    "Name":"EXAMPLE",
    "Status":"COMPLETED",
    "ComputeTime":"185200",
    "FinishedAt":141045168.275,
    "StartedAt":141045168.275
  }
}
```

## See Also
<a name="API_GetDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/GetDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/GetDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/GetDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/GetDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/GetDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/GetDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/GetDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/GetDataSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/GetDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/GetDataSource)

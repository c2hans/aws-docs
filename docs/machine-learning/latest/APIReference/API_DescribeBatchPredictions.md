---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeBatchPredictions.html
---

# DescribeBatchPredictions
<a name="API_DescribeBatchPredictions"></a>

Returns a list of `BatchPrediction` operations that match the search criteria in the request.

## Request Syntax
<a name="API_DescribeBatchPredictions_RequestSyntax"></a>

```
{
   "EQ": "{{string}}",
   "FilterVariable": "{{string}}",
   "GE": "{{string}}",
   "GT": "{{string}}",
   "LE": "{{string}}",
   "Limit": {{number}},
   "LT": "{{string}}",
   "NE": "{{string}}",
   "NextToken": "{{string}}",
   "Prefix": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBatchPredictions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EQ](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-EQ"></a>
The equal to operator. The `BatchPrediction` results will have `FilterVariable` values that exactly match the value specified with `EQ`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [FilterVariable](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-FilterVariable"></a>
Use one of the following variables to filter a list of `BatchPrediction`:
+  `CreatedAt` - Sets the search criteria to the `BatchPrediction` creation date.
+  `Status` - Sets the search criteria to the `BatchPrediction` status.
+  `Name` - Sets the search criteria to the contents of the `BatchPrediction` ** ** `Name`.
+  `IAMUser` - Sets the search criteria to the user account that invoked the `BatchPrediction` creation.
+  `MLModelId` - Sets the search criteria to the `MLModel` used in the `BatchPrediction`.
+  `DataSourceId` - Sets the search criteria to the `DataSource` used in the `BatchPrediction`.
+  `DataURI` - Sets the search criteria to the data file(s) used in the `BatchPrediction`. The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
Type: String
Valid Values: `CreatedAt | LastUpdatedAt | Status | Name | IAMUser | MLModelId | DataSourceId | DataURI`
Required: No

 ** [GE](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-GE"></a>
The greater than or equal to operator. The `BatchPrediction` results will have `FilterVariable` values that are greater than or equal to the value specified with `GE`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [GT](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-GT"></a>
The greater than operator. The `BatchPrediction` results will have `FilterVariable` values that are greater than the value specified with `GT`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [LE](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-LE"></a>
The less than or equal to operator. The `BatchPrediction` results will have `FilterVariable` values that are less than or equal to the value specified with `LE`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [Limit](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-Limit"></a>
The number of pages of information to include in the result. The range of acceptable values is `1` through `100`. The default value is `100`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [LT](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-LT"></a>
The less than operator. The `BatchPrediction` results will have `FilterVariable` values that are less than the value specified with `LT`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [NE](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-NE"></a>
The not equal to operator. The `BatchPrediction` results will have `FilterVariable` values not equal to the value specified with `NE`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [NextToken](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-NextToken"></a>
An ID of the page in the paginated results.
Type: String
Required: No

 ** [Prefix](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-Prefix"></a>
A string that is found at the beginning of a variable, such as `Name` or `Id`.
For example, a `Batch Prediction` operation could have the `Name` `2014-09-09-HolidayGiftMailer`. To search for this `BatchPrediction`, select `Name` for the `FilterVariable` and any of the following strings for the `Prefix`:
+ 2014-09
+ 2014-09-09
+ 2014-09-09-Holiday
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [SortOrder](#API_DescribeBatchPredictions_RequestSyntax) **   <a name="amazonml-DescribeBatchPredictions-request-SortOrder"></a>
A two-value parameter that determines the sequence of the resulting list of `MLModel`s.
+  `asc` - Arranges the list in ascending order (A-Z, 0-9).
+  `dsc` - Arranges the list in descending order (Z-A, 9-0).
Results are sorted by `FilterVariable`.
Type: String
Valid Values: `asc | dsc`
Required: No

## Response Syntax
<a name="API_DescribeBatchPredictions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Results": [
      {
         "BatchPredictionDataSourceId": "string",
         "BatchPredictionId": "string",
         "ComputeTime": number,
         "CreatedAt": number,
         "CreatedByIamUser": "string",
         "FinishedAt": number,
         "InputDataLocationS3": "string",
         "InvalidRecordCount": number,
         "LastUpdatedAt": number,
         "Message": "string",
         "MLModelId": "string",
         "Name": "string",
         "OutputUri": "string",
         "StartedAt": number,
         "Status": "string",
         "TotalRecordCount": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeBatchPredictions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeBatchPredictions_ResponseSyntax) **   <a name="amazonml-DescribeBatchPredictions-response-NextToken"></a>
The ID of the next page in the paginated results that indicates at least one more page follows.
Type: String

 ** [Results](#API_DescribeBatchPredictions_ResponseSyntax) **   <a name="amazonml-DescribeBatchPredictions-response-Results"></a>
A list of `BatchPrediction` objects that meet the search criteria.
Type: Array of [BatchPrediction](API_BatchPrediction.md) objects

## Errors
<a name="API_DescribeBatchPredictions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred when trying to process a request.
HTTP Status Code: 500

 ** InvalidInputException **
An error on the client occurred. Typically, the cause is an invalid input value.
HTTP Status Code: 400

## Examples
<a name="API_DescribeBatchPredictions_Examples"></a>

### The following is a sample request and response of the DescribeBatchPredictions operation.
<a name="API_DescribeBatchPredictions_Example_1"></a>

This example illustrates one usage of DescribeBatchPredictions.

#### Sample Request
<a name="API_DescribeBatchPredictions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.DescribeBatchPredictions
{
  "FilterVariable": "Name",
  "Prefix": "bp-",
  "SortOrder": "asc",
  "Limit": 1
}
```

#### Sample Response
<a name="API_DescribeBatchPredictions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "Results": [
    {
      "BatchPredictionDataSourceId": "ds-exampleDataSourceId",
      "BatchPredictionId": "bp-exampleBatchPredictionId",
      "CreatedAt": 1422057670.697,
      "CreatedByIamUser": "arn:aws:iam::<awsAccountId>:user/username",
      "InputDataLocationS3": "s3://bucket/locationToInput/example-data.testing.csv",
      "LastUpdatedAt": 1422057811.431,
      "MLModelId": "pr-exampleModelId",
      "Name": "bp-exampleBatchPredictionName",
      "OutputUri": "s3://bucket/locationToLogs/",
      "Status": "COMPLETED",
      "ComputeTime":"185200",
      "FinishedAt":"1422057711.192",
      "StartedAt":"14220557678.324",
      "TotalRecordCount":"21154",
      "InvalidRecordCount":"0"
    }
  ]
}
```

## See Also
<a name="API_DescribeBatchPredictions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/DescribeBatchPredictions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/DescribeBatchPredictions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/DescribeBatchPredictions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/DescribeBatchPredictions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/DescribeBatchPredictions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/DescribeBatchPredictions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/DescribeBatchPredictions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/DescribeBatchPredictions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/DescribeBatchPredictions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/DescribeBatchPredictions)

---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeEvaluations.html
---

# DescribeEvaluations
<a name="API_DescribeEvaluations"></a>

Returns a list of `DescribeEvaluations` that match the search criteria in the request.

## Request Syntax
<a name="API_DescribeEvaluations_RequestSyntax"></a>

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
<a name="API_DescribeEvaluations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EQ](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-EQ"></a>
The equal to operator. The `Evaluation` results will have `FilterVariable` values that exactly match the value specified with `EQ`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [FilterVariable](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-FilterVariable"></a>
Use one of the following variable to filter a list of `Evaluation` objects:
+  `CreatedAt` - Sets the search criteria to the `Evaluation` creation date.
+  `Status` - Sets the search criteria to the `Evaluation` status.
+  `Name` - Sets the search criteria to the contents of `Evaluation` ** ** `Name`.
+  `IAMUser` - Sets the search criteria to the user account that invoked an `Evaluation`.
+  `MLModelId` - Sets the search criteria to the `MLModel` that was evaluated.
+  `DataSourceId` - Sets the search criteria to the `DataSource` used in `Evaluation`.
+  `DataUri` - Sets the search criteria to the data file(s) used in `Evaluation`. The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
Type: String
Valid Values: `CreatedAt | LastUpdatedAt | Status | Name | IAMUser | MLModelId | DataSourceId | DataURI`
Required: No

 ** [GE](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-GE"></a>
The greater than or equal to operator. The `Evaluation` results will have `FilterVariable` values that are greater than or equal to the value specified with `GE`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [GT](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-GT"></a>
The greater than operator. The `Evaluation` results will have `FilterVariable` values that are greater than the value specified with `GT`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [LE](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-LE"></a>
The less than or equal to operator. The `Evaluation` results will have `FilterVariable` values that are less than or equal to the value specified with `LE`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [Limit](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-Limit"></a>
 The maximum number of `Evaluation` to include in the result.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [LT](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-LT"></a>
The less than operator. The `Evaluation` results will have `FilterVariable` values that are less than the value specified with `LT`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [NE](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-NE"></a>
The not equal to operator. The `Evaluation` results will have `FilterVariable` values not equal to the value specified with `NE`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [NextToken](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-NextToken"></a>
The ID of the page in the paginated results.
Type: String
Required: No

 ** [Prefix](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-Prefix"></a>
A string that is found at the beginning of a variable, such as `Name` or `Id`.
For example, an `Evaluation` could have the `Name` `2014-09-09-HolidayGiftMailer`. To search for this `Evaluation`, select `Name` for the `FilterVariable` and any of the following strings for the `Prefix`:
+ 2014-09
+ 2014-09-09
+ 2014-09-09-Holiday
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [SortOrder](#API_DescribeEvaluations_RequestSyntax) **   <a name="amazonml-DescribeEvaluations-request-SortOrder"></a>
A two-value parameter that determines the sequence of the resulting list of `Evaluation`.
+  `asc` - Arranges the list in ascending order (A-Z, 0-9).
+  `dsc` - Arranges the list in descending order (Z-A, 9-0).
Results are sorted by `FilterVariable`.
Type: String
Valid Values: `asc | dsc`
Required: No

## Response Syntax
<a name="API_DescribeEvaluations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Results": [
      {
         "ComputeTime": number,
         "CreatedAt": number,
         "CreatedByIamUser": "string",
         "EvaluationDataSourceId": "string",
         "EvaluationId": "string",
         "FinishedAt": number,
         "InputDataLocationS3": "string",
         "LastUpdatedAt": number,
         "Message": "string",
         "MLModelId": "string",
         "Name": "string",
         "PerformanceMetrics": {
            "Properties": {
               "string" : "string"
            }
         },
         "StartedAt": number,
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEvaluations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeEvaluations_ResponseSyntax) **   <a name="amazonml-DescribeEvaluations-response-NextToken"></a>
The ID of the next page in the paginated results that indicates at least one more page follows.
Type: String

 ** [Results](#API_DescribeEvaluations_ResponseSyntax) **   <a name="amazonml-DescribeEvaluations-response-Results"></a>
A list of `Evaluation` that meet the search criteria.
Type: Array of [Evaluation](API_Evaluation.md) objects

## Errors
<a name="API_DescribeEvaluations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred when trying to process a request.
HTTP Status Code: 500

 ** InvalidInputException **
An error on the client occurred. Typically, the cause is an invalid input value.
HTTP Status Code: 400

## Examples
<a name="API_DescribeEvaluations_Examples"></a>

### The following is a sample request and response of the DescribeEvaluations operation.
<a name="API_DescribeEvaluations_Example_1"></a>

This example illustrates one usage of DescribeEvaluations.

#### Sample Request
<a name="API_DescribeEvaluations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.DescribeEvaluations
{
  "FilterVariable": "Name",
  "Prefix": "ev-",
  "SortOrder": "asc",
  "Limit": 1
}
```

#### Sample Response
<a name="API_DescribeEvaluations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "NextToken": "{\"EvaluationId\":\"ev-exampleId2\"}",
  "Results": [
    {
      "CreatedAt": 1420745248.785,
      "CreatedByIamUser": "arn:aws:iam::<awsAccountId>:user/username",
      "EvaluationDataSourceId": "ds-exampleDataSourceId",
      "EvaluationId": "ev-exampleId1",
      "InputDataLocationS3": "s3://bucket/locationToInput/example-data.testing.csv",
      "LastUpdatedAt": 1420745524.506,
      "MLModelId": "pr-exampleModelId",
      "Name": "ev-1",
      "PerformanceMetrics":
       {
         "Properties": {"BinaryAUC": "0.9228827246570067"}
       },
      "Status": "COMPLETED",
      "ComputeTime":"185200",
      "FinishedAt":"1420745524.506",
      "StartedAt":"1420745249.324"
    }
  ]
}
```

## See Also
<a name="API_DescribeEvaluations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/DescribeEvaluations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/DescribeEvaluations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/DescribeEvaluations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/DescribeEvaluations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/DescribeEvaluations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/DescribeEvaluations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/DescribeEvaluations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/DescribeEvaluations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/DescribeEvaluations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/DescribeEvaluations)

---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeMLModels.html
---

# DescribeMLModels
<a name="API_DescribeMLModels"></a>

Returns a list of `MLModel` that match the search criteria in the request.

## Request Syntax
<a name="API_DescribeMLModels_RequestSyntax"></a>

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
<a name="API_DescribeMLModels_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EQ](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-EQ"></a>
The equal to operator. The `MLModel` results will have `FilterVariable` values that exactly match the value specified with `EQ`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [FilterVariable](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-FilterVariable"></a>
Use one of the following variables to filter a list of `MLModel`:
+  `CreatedAt` - Sets the search criteria to `MLModel` creation date.
+  `Status` - Sets the search criteria to `MLModel` status.
+  `Name` - Sets the search criteria to the contents of `MLModel` ** ** `Name`.
+  `IAMUser` - Sets the search criteria to the user account that invoked the `MLModel` creation.
+  `TrainingDataSourceId` - Sets the search criteria to the `DataSource` used to train one or more `MLModel`.
+  `RealtimeEndpointStatus` - Sets the search criteria to the `MLModel` real-time endpoint status.
+  `MLModelType` - Sets the search criteria to `MLModel` type: binary, regression, or multi-class.
+  `Algorithm` - Sets the search criteria to the algorithm that the `MLModel` uses.
+  `TrainingDataURI` - Sets the search criteria to the data file(s) used in training a `MLModel`. The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
Type: String
Valid Values: `CreatedAt | LastUpdatedAt | Status | Name | IAMUser | TrainingDataSourceId | RealtimeEndpointStatus | MLModelType | Algorithm | TrainingDataURI`
Required: No

 ** [GE](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-GE"></a>
The greater than or equal to operator. The `MLModel` results will have `FilterVariable` values that are greater than or equal to the value specified with `GE`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [GT](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-GT"></a>
The greater than operator. The `MLModel` results will have `FilterVariable` values that are greater than the value specified with `GT`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [LE](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-LE"></a>
The less than or equal to operator. The `MLModel` results will have `FilterVariable` values that are less than or equal to the value specified with `LE`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [Limit](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-Limit"></a>
The number of pages of information to include in the result. The range of acceptable values is `1` through `100`. The default value is `100`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [LT](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-LT"></a>
The less than operator. The `MLModel` results will have `FilterVariable` values that are less than the value specified with `LT`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [NE](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-NE"></a>
The not equal to operator. The `MLModel` results will have `FilterVariable` values not equal to the value specified with `NE`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [NextToken](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-NextToken"></a>
The ID of the page in the paginated results.
Type: String
Required: No

 ** [Prefix](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-Prefix"></a>
A string that is found at the beginning of a variable, such as `Name` or `Id`.
For example, an `MLModel` could have the `Name` `2014-09-09-HolidayGiftMailer`. To search for this `MLModel`, select `Name` for the `FilterVariable` and any of the following strings for the `Prefix`:
+ 2014-09
+ 2014-09-09
+ 2014-09-09-Holiday
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [SortOrder](#API_DescribeMLModels_RequestSyntax) **   <a name="amazonml-DescribeMLModels-request-SortOrder"></a>
A two-value parameter that determines the sequence of the resulting list of `MLModel`.
+  `asc` - Arranges the list in ascending order (A-Z, 0-9).
+  `dsc` - Arranges the list in descending order (Z-A, 9-0).
Results are sorted by `FilterVariable`.
Type: String
Valid Values: `asc | dsc`
Required: No

## Response Syntax
<a name="API_DescribeMLModels_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Results": [
      {
         "Algorithm": "string",
         "ComputeTime": number,
         "CreatedAt": number,
         "CreatedByIamUser": "string",
         "EndpointInfo": {
            "CreatedAt": number,
            "EndpointStatus": "string",
            "EndpointUrl": "string",
            "PeakRequestsPerSecond": number
         },
         "FinishedAt": number,
         "InputDataLocationS3": "string",
         "LastUpdatedAt": number,
         "Message": "string",
         "MLModelId": "string",
         "MLModelType": "string",
         "Name": "string",
         "ScoreThreshold": number,
         "ScoreThresholdLastUpdatedAt": number,
         "SizeInBytes": number,
         "StartedAt": number,
         "Status": "string",
         "TrainingDataSourceId": "string",
         "TrainingParameters": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMLModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeMLModels_ResponseSyntax) **   <a name="amazonml-DescribeMLModels-response-NextToken"></a>
The ID of the next page in the paginated results that indicates at least one more page follows.
Type: String

 ** [Results](#API_DescribeMLModels_ResponseSyntax) **   <a name="amazonml-DescribeMLModels-response-Results"></a>
A list of `MLModel` that meet the search criteria.
Type: Array of [MLModel](API_MLModel.md) objects

## Errors
<a name="API_DescribeMLModels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred when trying to process a request.
HTTP Status Code: 500

 ** InvalidInputException **
An error on the client occurred. Typically, the cause is an invalid input value.
HTTP Status Code: 400

## Examples
<a name="API_DescribeMLModels_Examples"></a>

### The following is a sample request and response of the DescribeMLModels operation:
<a name="API_DescribeMLModels_Example_1"></a>

This example illustrates one usage of DescribeMLModels.

#### Sample Request
<a name="API_DescribeMLModels_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.DescribeMLModels
{
  "FilterVariable": "Name",
  "Prefix": "ml-",
  "SortOrder": "asc",
  "Limit": 1
}
```

#### Sample Response
<a name="API_DescribeMLModels_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "NextToken": "\"PredictorId\":\"Spr-ml-model-testing\"}",
  "Results": [
    {
      "CreatedAt": 1422475435.595,
      "CreatedByIamUser": "arn:aws:iam::<awsAccountId>:user/username",
      "InputDataLocationS3": "s3://bucket/locationToInput/example-data.testing.csv",
      "LastUpdatedAt": 1422475709.691,
      "MLModelId": "ml-model-testing",
      "MLModelType": "MULTICLASS",
      "EndpointInfo": {
        "CreatedAt": 1424378682.266,
        "EndpointStatus": "READY",
        "EndpointUrl": "<realtime endpoint from Amazon Machine Learning for ml-model-testing>",
        "PeakRequestsPerSecond": 200}
      "Name": "ml-model-name",
      "Algorithm": "sgd",
      "SizeInBytes": 352720,
      "Status": "COMPLETED",
      "ComputeTime":"185200",
      "FinishedAt":"1422475709.691",
      "StartedAt":"1422475438.324",
      "TrainingDataSourceId": "exampleDataSourceId",
      "TrainingParameters":
       {
         "algorithm": "sgd",
         "sgd.l1RegularizationAmount": "0.0",
         "sgd.l2RegularizationAmount": "1E-6",
         "sgd.maxMLModelSizeInBytes": "33554432",
         "sgd.maxPasses": "10"
      }
    }
  ]
}
```

## See Also
<a name="API_DescribeMLModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/DescribeMLModels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/DescribeMLModels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/DescribeMLModels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/DescribeMLModels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/DescribeMLModels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/DescribeMLModels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/DescribeMLModels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/DescribeMLModels)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/DescribeMLModels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/DescribeMLModels)

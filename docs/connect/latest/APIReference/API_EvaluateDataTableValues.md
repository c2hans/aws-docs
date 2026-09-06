---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluateDataTableValues.html
---

# EvaluateDataTableValues
<a name="API_EvaluateDataTableValues"></a>

Evaluates values at the time of the request and returns them. It considers the request's timezone or the table's timezone, in that order, when accessing time based tables. When a value is accessed, the accessor's identity and the time of access are saved alongside the value to help identify values that are actively in use. The term "Batch" is not included in the operation name since it does not meet all the criteria for a batch operation as specified in Batch Operations: AWS API Standards.

## Request Syntax
<a name="API_EvaluateDataTableValues_RequestSyntax"></a>

```
POST /data-tables/{{InstanceId}}/{{DataTableId}}/values/evaluate?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "TimeZone": "{{string}}",
   "Values": [
      {
         "AttributeNames": [ "{{string}}" ],
         "PrimaryValues": [
            {
               "AttributeName": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_EvaluateDataTableValues_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_EvaluateDataTableValues_RequestSyntax) **   <a name="connect-EvaluateDataTableValues-request-uri-DataTableId"></a>
The unique identifier for the data table. Must also accept the table ARN with or without a version alias.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_EvaluateDataTableValues_RequestSyntax) **   <a name="connect-EvaluateDataTableValues-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_EvaluateDataTableValues_RequestSyntax) **   <a name="connect-EvaluateDataTableValues-request-uri-MaxResults"></a>
The maximum number of data table values to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_EvaluateDataTableValues_RequestSyntax) **   <a name="connect-EvaluateDataTableValues-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.

## Request Body
<a name="API_EvaluateDataTableValues_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TimeZone](#API_EvaluateDataTableValues_RequestSyntax) **   <a name="connect-EvaluateDataTableValues-request-TimeZone"></a>
Optional IANA timezone identifier to use when resolving time based dynamic values. Defaults to the data table time zone if not provided.
Type: String
Required: No

 ** [Values](#API_EvaluateDataTableValues_RequestSyntax) **   <a name="connect-EvaluateDataTableValues-request-Values"></a>
A list of value evaluation sets specifying which primary values and attributes to evaluate.
Type: Array of [DataTableValueEvaluationSet](API_DataTableValueEvaluationSet.md) objects
Required: Yes

## Response Syntax
<a name="API_EvaluateDataTableValues_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Values": [
      {
         "AttributeName": "string",
         "Error": boolean,
         "EvaluatedValue": "string",
         "Found": boolean,
         "PrimaryValues": [
            {
               "AttributeName": "string",
               "Value": "string"
            }
         ],
         "RecordId": "string",
         "ValueType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_EvaluateDataTableValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_EvaluateDataTableValues_ResponseSyntax) **   <a name="connect-EvaluateDataTableValues-response-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String

 ** [Values](#API_EvaluateDataTableValues_ResponseSyntax) **   <a name="connect-EvaluateDataTableValues-response-Values"></a>
A list of evaluated values with their computed results, error information, and metadata.
Type: Array of [DataTableEvaluatedValue](API_DataTableEvaluatedValue.md) objects

## Errors
<a name="API_EvaluateDataTableValues_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_EvaluateDataTableValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/EvaluateDataTableValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/EvaluateDataTableValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluateDataTableValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/EvaluateDataTableValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluateDataTableValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/EvaluateDataTableValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/EvaluateDataTableValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/EvaluateDataTableValues)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/EvaluateDataTableValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluateDataTableValues)

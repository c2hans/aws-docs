---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_GetVariables.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# GetVariables
<a name="API_GetVariables"></a>

Gets all of the variables or the specific variable. This is a paginated API. Providing null `maxSizePerPage` results in retrieving maximum of 100 records per page. If you provide `maxSizePerPage` the value must be between 50 and 100. To get the next page result, a provide a pagination token from `GetVariablesResult` as part of your request. Null pagination token fetches the records from the beginning.

## Request Syntax
<a name="API_GetVariables_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "name": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetVariables_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_GetVariables_RequestSyntax) **   <a name="FraudDetector-GetVariables-request-maxResults"></a>
The max size per page determined for the get variable request.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 100.
Required: No

 ** [name](#API_GetVariables_RequestSyntax) **   <a name="FraudDetector-GetVariables-request-name"></a>
The name of the variable.
Type: String
Required: No

 ** [nextToken](#API_GetVariables_RequestSyntax) **   <a name="FraudDetector-GetVariables-request-nextToken"></a>
The next page token of the get variable request.
Type: String
Required: No

## Response Syntax
<a name="API_GetVariables_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "variables": [
      {
         "arn": "string",
         "createdTime": "string",
         "dataSource": "string",
         "dataType": "string",
         "defaultValue": "string",
         "description": "string",
         "lastUpdatedTime": "string",
         "name": "string",
         "variableType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetVariables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetVariables_ResponseSyntax) **   <a name="FraudDetector-GetVariables-response-nextToken"></a>
The next page token to be used in subsequent requests.
Type: String

 ** [variables](#API_GetVariables_ResponseSyntax) **   <a name="FraudDetector-GetVariables-response-variables"></a>
The names of the variables returned.
Type: Array of [Variable](API_Variable.md) objects

## Errors
<a name="API_GetVariables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception indicating the specified resource was not found.
HTTP Status Code: 400

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_GetVariables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/GetVariables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/GetVariables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/GetVariables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/GetVariables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/GetVariables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/GetVariables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/GetVariables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/GetVariables)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/GetVariables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/GetVariables)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

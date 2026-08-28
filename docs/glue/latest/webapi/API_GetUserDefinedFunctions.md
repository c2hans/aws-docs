---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetUserDefinedFunctions.html
---

# GetUserDefinedFunctions
<a name="API_GetUserDefinedFunctions"></a>

Retrieves multiple function definitions from the Data Catalog.

## Request Syntax
<a name="API_GetUserDefinedFunctions_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "FunctionType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Pattern": "{{string}}"
}
```

## Request Parameters
<a name="API_GetUserDefinedFunctions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetUserDefinedFunctions_RequestSyntax) **   <a name="Glue-GetUserDefinedFunctions-request-CatalogId"></a>
The ID of the Data Catalog where the functions to be retrieved are located. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_GetUserDefinedFunctions_RequestSyntax) **   <a name="Glue-GetUserDefinedFunctions-request-DatabaseName"></a>
The name of the catalog database where the functions are located. If none is provided, functions from all the databases across the catalog will be returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [FunctionType](#API_GetUserDefinedFunctions_RequestSyntax) **   <a name="Glue-GetUserDefinedFunctions-request-FunctionType"></a>
An optional function-type pattern string that filters the function definitions returned from Amazon Redshift Federated Permissions Catalog.
Specify a value of `REGULAR_FUNCTION` or `STORED_PROCEDURE`. The `STORED_PROCEDURE` function type is only compatible with Amazon Redshift Federated Permissions Catalog.
Type: String
Valid Values: `REGULAR_FUNCTION | AGGREGATE_FUNCTION | STORED_PROCEDURE`
Required: No

 ** [MaxResults](#API_GetUserDefinedFunctions_RequestSyntax) **   <a name="Glue-GetUserDefinedFunctions-request-MaxResults"></a>
The maximum number of functions to return in one response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetUserDefinedFunctions_RequestSyntax) **   <a name="Glue-GetUserDefinedFunctions-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [Pattern](#API_GetUserDefinedFunctions_RequestSyntax) **   <a name="Glue-GetUserDefinedFunctions-request-Pattern"></a>
An optional function-name pattern string that filters the function definitions returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetUserDefinedFunctions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "UserDefinedFunctions": [
      {
         "CatalogId": "string",
         "ClassName": "string",
         "CreateTime": number,
         "DatabaseName": "string",
         "FunctionName": "string",
         "FunctionType": "string",
         "OwnerName": "string",
         "OwnerType": "string",
         "ResourceUris": [
            {
               "ResourceType": "string",
               "Uri": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetUserDefinedFunctions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetUserDefinedFunctions_ResponseSyntax) **   <a name="Glue-GetUserDefinedFunctions-response-NextToken"></a>
A continuation token, if the list of functions returned does not include the last requested function.
Type: String

 ** [UserDefinedFunctions](#API_GetUserDefinedFunctions_ResponseSyntax) **   <a name="Glue-GetUserDefinedFunctions-response-UserDefinedFunctions"></a>
A list of requested function definitions.
Type: Array of [UserDefinedFunction](API_UserDefinedFunction.md) objects

## Errors
<a name="API_GetUserDefinedFunctions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetUserDefinedFunctions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetUserDefinedFunctions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetUserDefinedFunctions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetUserDefinedFunctions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetUserDefinedFunctions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetUserDefinedFunctions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetUserDefinedFunctions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetUserDefinedFunctions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetUserDefinedFunctions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetUserDefinedFunctions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetUserDefinedFunctions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

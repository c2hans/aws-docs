---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_GetPreparedStatement.html
---

# GetPreparedStatement
<a name="API_GetPreparedStatement"></a>

Retrieves the prepared statement with the specified name from the specified workgroup.

## Request Syntax
<a name="API_GetPreparedStatement_RequestSyntax"></a>

```
{
   "StatementName": "{{string}}",
   "WorkGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPreparedStatement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [StatementName](#API_GetPreparedStatement_RequestSyntax) **   <a name="athena-GetPreparedStatement-request-StatementName"></a>
The name of the prepared statement to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_][a-zA-Z0-9_@:]{1,256}`
Required: Yes

 ** [WorkGroup](#API_GetPreparedStatement_RequestSyntax) **   <a name="athena-GetPreparedStatement-request-WorkGroup"></a>
The workgroup to which the statement to be retrieved belongs.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: Yes

## Response Syntax
<a name="API_GetPreparedStatement_ResponseSyntax"></a>

```
{
   "PreparedStatement": {
      "Description": "string",
      "LastModifiedTime": number,
      "QueryStatement": "string",
      "StatementName": "string",
      "WorkGroupName": "string"
   }
}
```

## Response Elements
<a name="API_GetPreparedStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PreparedStatement](#API_GetPreparedStatement_ResponseSyntax) **   <a name="athena-GetPreparedStatement-response-PreparedStatement"></a>
The name of the prepared statement that was retrieved.
Type: [PreparedStatement](API_PreparedStatement.md) object

## Errors
<a name="API_GetPreparedStatement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource, such as a workgroup, was not found.
 ** ResourceName **
The name of the Amazon resource.
HTTP Status Code: 400

## See Also
<a name="API_GetPreparedStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/GetPreparedStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/GetPreparedStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/GetPreparedStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/GetPreparedStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/GetPreparedStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/GetPreparedStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/GetPreparedStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/GetPreparedStatement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetPreparedStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/GetPreparedStatement)

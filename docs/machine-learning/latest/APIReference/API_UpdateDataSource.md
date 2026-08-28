---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateDataSource.html
---

# UpdateDataSource
<a name="API_UpdateDataSource"></a>

Updates the `DataSourceName` of a `DataSource`.

You can use the `GetDataSource` operation to view the contents of the updated data element.

## Request Syntax
<a name="API_UpdateDataSource_RequestSyntax"></a>

```
{
   "DataSourceId": "{{string}}",
   "DataSourceName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDataSource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataSourceId](#API_UpdateDataSource_RequestSyntax) **   <a name="amazonml-UpdateDataSource-request-DataSourceId"></a>
The ID assigned to the `DataSource` during creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [DataSourceName](#API_UpdateDataSource_RequestSyntax) **   <a name="amazonml-UpdateDataSource-request-DataSourceName"></a>
A new user-supplied name or description of the `DataSource` that will replace the current description.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: Yes

## Response Syntax
<a name="API_UpdateDataSource_ResponseSyntax"></a>

```
{
   "DataSourceId": "string"
}
```

## Response Elements
<a name="API_UpdateDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataSourceId](#API_UpdateDataSource_ResponseSyntax) **   <a name="amazonml-UpdateDataSource-response-DataSourceId"></a>
The ID assigned to the `DataSource` during creation. This value should be identical to the value of the `DataSourceID` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_UpdateDataSource_Errors"></a>

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
<a name="API_UpdateDataSource_Examples"></a>

### The following is a sample request and response of the UpdateDataSource operation.
<a name="API_UpdateDataSource_Example_1"></a>

This example illustrates one usage of UpdateDataSource.

#### Sample Request
<a name="API_UpdateDataSource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.UpdateDataSource
{
  "DataSourceId": "ds-exampleDataSourceId",
  "DataSourceName": "ds-exampleDataSourceName"
}
```

#### Sample Response
<a name="API_UpdateDataSource_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{"DataSourceId": "ds-exampleDataSourceId"}
```

## See Also
<a name="API_UpdateDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/UpdateDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/UpdateDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/UpdateDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/UpdateDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/UpdateDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/UpdateDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/UpdateDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/UpdateDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/UpdateDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/UpdateDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

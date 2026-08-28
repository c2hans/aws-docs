---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeMetricsExport.html
---

# DescribeMetricsExport
<a name="API_DescribeMetricsExport"></a>

Describes the metrics of the application configuration being exported.

## Request Syntax
<a name="API_DescribeMetricsExport_RequestSyntax"></a>

```
POST /describe-metrics-export HTTP/1.1
Content-type: application/json

{
   "metricsExportId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeMetricsExport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeMetricsExport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [metricsExportId](#API_DescribeMetricsExport_RequestSyntax) **   <a name="resiliencehub-DescribeMetricsExport-request-metricsExportId"></a>
Identifier of the metrics export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_DescribeMetricsExport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errorMessage": "string",
   "exportLocation": {
      "bucket": "string",
      "prefix": "string"
   },
   "metricsExportId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DescribeMetricsExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorMessage](#API_DescribeMetricsExport_ResponseSyntax) **   <a name="resiliencehub-DescribeMetricsExport-response-errorMessage"></a>
Explains the error that occurred while exporting the metrics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [exportLocation](#API_DescribeMetricsExport_ResponseSyntax) **   <a name="resiliencehub-DescribeMetricsExport-response-exportLocation"></a>
Specifies the name of the Amazon S3 bucket where the exported metrics is stored.
Type: [S3Location](API_S3Location.md) object

 ** [metricsExportId](#API_DescribeMetricsExport_ResponseSyntax) **   <a name="resiliencehub-DescribeMetricsExport-response-metricsExportId"></a>
Identifier for the metrics export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [status](#API_DescribeMetricsExport_ResponseSyntax) **   <a name="resiliencehub-DescribeMetricsExport-response-status"></a>
Indicates the status of the metrics export task.
Type: String
Valid Values: `Pending | InProgress | Failed | Success`

## Errors
<a name="API_DescribeMetricsExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Resilience Hub service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This exception occurs when the specified resource could not be found.
 ** resourceId **
The identifier of the resource that the exception applies to.
 ** resourceType **
The type of the resource that the exception applies to.
HTTP Status Code: 404

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeMetricsExport_Examples"></a>

### Sample Request
<a name="API_DescribeMetricsExport_Example_1"></a>

The following is an example request payload.

#### Sample Request
<a name="API_DescribeMetricsExport_Example_1_Request"></a>

```
{
  "metricsExportId": "fe0e1e00-03eb-11ee-8796-02038f8a9691"
}
```

### Sample Response
<a name="API_DescribeMetricsExport_Example_2"></a>

The following is an example response payload.

#### Sample Response
<a name="API_DescribeMetricsExport_Example_2_Response"></a>

```
{
  "metricsExportId": "fe0e1e00-03eb-11ee-8796-02038f8a9691",
  "status": "Success",
  "exportLocation": {
    "bucket": "my-bucket-name",
    "prefix": "resiliencehub-metrics/2024-11-14/fe0e1e00-03eb-11ee-8796-02038f8a9691"
  }
}
```

## See Also
<a name="API_DescribeMetricsExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/DescribeMetricsExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/DescribeMetricsExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/DescribeMetricsExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/DescribeMetricsExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/DescribeMetricsExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/DescribeMetricsExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/DescribeMetricsExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/DescribeMetricsExport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/DescribeMetricsExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/DescribeMetricsExport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

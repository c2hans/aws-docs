---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_AssociateSourceToS3TableIntegration.html
---

# AssociateSourceToS3TableIntegration
<a name="API_AssociateSourceToS3TableIntegration"></a>

Associates a data source with an S3 Table Integration for query access in the 'logs' namespace. This enables querying log data using analytics engines that support Iceberg such as Amazon Athena, Amazon Redshift, and Apache Spark.

## Request Syntax
<a name="API_AssociateSourceToS3TableIntegration_RequestSyntax"></a>

```
{
   "dataSource": {
      "name": "{{string}}",
      "type": "{{string}}"
   },
   "integrationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateSourceToS3TableIntegration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dataSource](#API_AssociateSourceToS3TableIntegration_RequestSyntax) **   <a name="CWL-AssociateSourceToS3TableIntegration-request-dataSource"></a>
The data source to associate with the S3 Table Integration. Contains the name and type of the data source.
Type: [DataSource](API_DataSource.md) object
Required: Yes

 ** [integrationArn](#API_AssociateSourceToS3TableIntegration_RequestSyntax) **   <a name="CWL-AssociateSourceToS3TableIntegration-request-integrationArn"></a>
The Amazon Resource Name (ARN) of the S3 Table Integration to associate the data source with.
Type: String
Required: Yes

## Response Syntax
<a name="API_AssociateSourceToS3TableIntegration_ResponseSyntax"></a>

```
{
   "identifier": "string"
}
```

## Response Elements
<a name="API_AssociateSourceToS3TableIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [identifier](#API_AssociateSourceToS3TableIntegration_ResponseSyntax) **   <a name="CWL-AssociateSourceToS3TableIntegration-response-identifier"></a>
The unique identifier for the association between the data source and S3 Table Integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_AssociateSourceToS3TableIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_AssociateSourceToS3TableIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/AssociateSourceToS3TableIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/AssociateSourceToS3TableIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/AssociateSourceToS3TableIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/AssociateSourceToS3TableIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/AssociateSourceToS3TableIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/AssociateSourceToS3TableIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/AssociateSourceToS3TableIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/AssociateSourceToS3TableIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/AssociateSourceToS3TableIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/AssociateSourceToS3TableIntegration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

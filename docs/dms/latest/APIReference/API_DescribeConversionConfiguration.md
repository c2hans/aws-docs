---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html
---

# DescribeConversionConfiguration
<a name="API_DescribeConversionConfiguration"></a>

Returns configuration parameters for a schema conversion project.

 **Required permissions:** `dms:DescribeConversionConfiguration`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_DescribeConversionConfiguration_RequestSyntax"></a>

```
{
   "MigrationProjectIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConversionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MigrationProjectIdentifier](#API_DescribeConversionConfiguration_RequestSyntax) **   <a name="DMS-DescribeConversionConfiguration-request-MigrationProjectIdentifier"></a>
The name or Amazon Resource Name (ARN) for the schema conversion project to describe.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_DescribeConversionConfiguration_ResponseSyntax"></a>

```
{
   "ConversionConfiguration": "string",
   "MigrationProjectIdentifier": "string"
}
```

## Response Elements
<a name="API_DescribeConversionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConversionConfiguration](#API_DescribeConversionConfiguration_ResponseSyntax) **   <a name="DMS-DescribeConversionConfiguration-response-ConversionConfiguration"></a>
A JSON string that contains the schema conversion settings for the migration project. For the format and available settings, see [Specifying schema conversion settings for migration projects](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-settings.html).
Type: String

 ** [MigrationProjectIdentifier](#API_DescribeConversionConfiguration_ResponseSyntax) **   <a name="DMS-DescribeConversionConfiguration-response-MigrationProjectIdentifier"></a>
The name or Amazon Resource Name (ARN) for the schema conversion project.
Type: String

## Errors
<a name="API_DescribeConversionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeConversionConfiguration_Examples"></a>

### Retrieving conversion configuration for a migration project
<a name="API_DescribeConversionConfiguration_Example_1"></a>

The following example retrieves the conversion configuration for a migration project.

#### Sample Request
<a name="API_DescribeConversionConfiguration_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.DescribeConversionConfiguration
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
}
```

#### Sample Response
<a name="API_DescribeConversionConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "ConversionConfiguration": "{\"Common project settings\":{\"ShowSeverityLevelInSql\":\"CRITICAL\",\"EnableGenAiConversion\":false},\"MSSQL_TO_AURORA_POSTGRESQL\":{\"ConvertProceduresToFunction\":true,\"UniqueIndexGeneration\":true,\"CaseSensitivityNames\":false},\"Conversion version\":{\"MSSQL_TO_AURORA_POSTGRESQL_target_engine_version\":\"15\"}}"
}
```

## See Also
<a name="API_DescribeConversionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeConversionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeConversionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeConversionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeConversionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeConversionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeConversionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeConversionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeConversionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeConversionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeConversionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

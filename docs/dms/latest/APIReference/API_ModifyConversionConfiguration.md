---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyConversionConfiguration.html
---

# ModifyConversionConfiguration
<a name="API_ModifyConversionConfiguration"></a>

Modifies the specified schema conversion configuration using the provided parameters.

 **Required permissions:** `dms:UpdateConversionConfiguration`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_ModifyConversionConfiguration_RequestSyntax"></a>

```
{
   "ConversionConfiguration": "{{string}}",
   "MigrationProjectIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_ModifyConversionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConversionConfiguration](#API_ModifyConversionConfiguration_RequestSyntax) **   <a name="DMS-ModifyConversionConfiguration-request-ConversionConfiguration"></a>
A JSON string that contains the schema conversion settings to update. For the format and available settings, see [Specifying schema conversion settings for migration projects](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-settings.html).
Usage:
+ Include only the sections and keys to change. The operation merges supplied values with the existing configuration.
Type: String
Required: Yes

 ** [MigrationProjectIdentifier](#API_ModifyConversionConfiguration_RequestSyntax) **   <a name="DMS-ModifyConversionConfiguration-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_ModifyConversionConfiguration_ResponseSyntax"></a>

```
{
   "MigrationProjectIdentifier": "string"
}
```

## Response Elements
<a name="API_ModifyConversionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MigrationProjectIdentifier](#API_ModifyConversionConfiguration_ResponseSyntax) **   <a name="DMS-ModifyConversionConfiguration-response-MigrationProjectIdentifier"></a>
The name or Amazon Resource Name (ARN) of the modified configuration.
Type: String

## Errors
<a name="API_ModifyConversionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ModifyConversionConfiguration_Examples"></a>

### Modifying conversion configuration for a migration project
<a name="API_ModifyConversionConfiguration_Example_1"></a>

The following example enables generative AI assisted conversion and updates a conversion pair setting for a migration project.

#### Sample Request
<a name="API_ModifyConversionConfiguration_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.ModifyConversionConfiguration
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "ConversionConfiguration": "{\"Common project settings\":{\"EnableGenAiConversion\":true},\"MSSQL_TO_AURORA_POSTGRESQL\":{\"ConvertProceduresToFunction\":false}}"
}
```

#### Sample Response
<a name="API_ModifyConversionConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
}
```

## See Also
<a name="API_ModifyConversionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ModifyConversionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ModifyConversionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ModifyConversionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ModifyConversionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ModifyConversionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ModifyConversionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ModifyConversionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ModifyConversionConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ModifyConversionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ModifyConversionConfiguration)

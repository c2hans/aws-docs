---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateDataProvider.html
---

# CreateDataProvider
<a name="API_CreateDataProvider"></a>

Creates a data provider using the provided settings. A data provider stores a data store type and location information about your database.

 **Required permissions:** `dms:CreateDataProvider`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_CreateDataProvider_RequestSyntax"></a>

```
{
   "DataProviderName": "{{string}}",
   "Description": "{{string}}",
   "Engine": "{{string}}",
   "Settings": { ... },
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Virtual": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateDataProvider_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataProviderName](#API_CreateDataProvider_RequestSyntax) **   <a name="DMS-CreateDataProvider-request-DataProviderName"></a>
A user-friendly name for the data provider.
Type: String
Required: No

 ** [Description](#API_CreateDataProvider_RequestSyntax) **   <a name="DMS-CreateDataProvider-request-Description"></a>
A user-friendly description of the data provider.
Type: String
Required: No

 ** [Engine](#API_CreateDataProvider_RequestSyntax) **   <a name="DMS-CreateDataProvider-request-Engine"></a>
The type of database engine for the data provider.
Valid values: `aurora`, `aurora-postgresql`, `db2`, `db2-zos`, `docdb`, `mariadb`, `mongodb`, `mysql`, `oracle`, `postgres`, `redshift`, `sqlserver`, and `sybase`. A value of `aurora` represents Amazon Aurora MySQL-Compatible Edition.
Type: String
Required: Yes

 ** [Settings](#API_CreateDataProvider_RequestSyntax) **   <a name="DMS-CreateDataProvider-request-Settings"></a>
The settings in JSON format for a data provider.
Type: [DataProviderSettings](API_DataProviderSettings.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Tags](#API_CreateDataProvider_RequestSyntax) **   <a name="DMS-CreateDataProvider-request-Tags"></a>
One or more tags to be assigned to the data provider.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [Virtual](#API_CreateDataProvider_RequestSyntax) **   <a name="DMS-CreateDataProvider-request-Virtual"></a>
Indicates whether the data provider is virtual.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateDataProvider_ResponseSyntax"></a>

```
{
   "DataProvider": {
      "DataProviderArn": "string",
      "DataProviderCreationTime": "string",
      "DataProviderName": "string",
      "Description": "string",
      "Engine": "string",
      "Settings": { ... },
      "Virtual": boolean
   }
}
```

## Response Elements
<a name="API_CreateDataProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataProvider](#API_CreateDataProvider_ResponseSyntax) **   <a name="DMS-CreateDataProvider-response-DataProvider"></a>
The data provider that was created.
Type: [DataProvider](API_DataProvider.md) object

## Errors
<a name="API_CreateDataProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** FailedDependencyFault **
A dependency threw an exception.
HTTP Status Code: 400

 ** ResourceAlreadyExistsFault **
The resource you are attempting to create already exists.
 ** message **

 ** resourceArn **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_CreateDataProvider_Examples"></a>

### Create a Microsoft SQL Server data provider
<a name="API_CreateDataProvider_Example_1"></a>

The following example creates a Microsoft SQL Server data provider.

#### Sample Request
<a name="API_CreateDataProvider_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.CreateDataProvider
{
    "DataProviderName": "example-data-provider",
    "Engine": "sqlserver",
    "Description": "Example data provider for documentation",
    "Settings": {
        "MicrosoftSqlServerSettings": {
            "ServerName": "example-source-server.us-east-1.rds.amazonaws.com",
            "Port": 1433,
            "DatabaseName": "ExampleDatabase",
            "SslMode": "verify-full",
            "CertificateArn": "arn:aws:dms:us-east-1:111122223333:cert:EXAMPLEABCDEFGHIJKLMNOPQRS"
        }
    }
}
```

#### Sample Response
<a name="API_CreateDataProvider_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "DataProvider": {
        "DataProviderName": "example-data-provider",
        "DataProviderArn": "arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "DataProviderCreationTime": "2026-01-09T12:30:00.000000Z",
        "Description": "Example data provider for documentation",
        "Engine": "sqlserver",
        "Settings": {
            "MicrosoftSqlServerSettings": {
                "ServerName": "example-source-server.us-east-1.rds.amazonaws.com",
                "Port": 1433,
                "DatabaseName": "ExampleDatabase",
                "SslMode": "verify-full",
                "CertificateArn": "arn:aws:dms:us-east-1:111122223333:cert:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        }
    }
}
```

### Create a virtual data provider
<a name="API_CreateDataProvider_Example_2"></a>

The following example creates a virtual data provider, which doesn't require a connection to the database.

#### Sample Request
<a name="API_CreateDataProvider_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.CreateDataProvider
{
    "DataProviderName": "example-virtual-data-provider",
    "Engine": "aurora-postgresql",
    "Description": "Example data provider for documentation",
    "Virtual": true,
    "Settings": {
        "PostgreSqlSettings": {
            "ServerName": "virtual",
            "Port": 5432,
            "DatabaseName": "virtual",
            "SslMode": "none"
        }
    }
}
```

#### Sample Response
<a name="API_CreateDataProvider_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "DataProvider": {
        "DataProviderName": "example-virtual-data-provider",
        "DataProviderArn": "arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "DataProviderCreationTime": "2026-01-09T12:30:00.000000Z",
        "Description": "Example data provider for documentation",
        "Engine": "aurora-postgresql",
        "Virtual": true,
        "Settings": {
            "PostgreSqlSettings": {
                "ServerName": "virtual",
                "Port": 5432,
                "DatabaseName": "virtual",
                "SslMode": "none"
            }
        }
    }
}
```

## See Also
<a name="API_CreateDataProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/CreateDataProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/CreateDataProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CreateDataProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/CreateDataProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CreateDataProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/CreateDataProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/CreateDataProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/CreateDataProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/CreateDataProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CreateDataProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

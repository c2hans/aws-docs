---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyDataProvider.html
---

# ModifyDataProvider
<a name="API_ModifyDataProvider"></a>

Modifies the specified data provider using the provided settings.

 **Required permissions:** `dms:UpdateDataProvider`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

**Note**
You must remove the data provider from all migration projects before you can modify it.

## Request Syntax
<a name="API_ModifyDataProvider_RequestSyntax"></a>

```
{
   "DataProviderIdentifier": "{{string}}",
   "DataProviderName": "{{string}}",
   "Description": "{{string}}",
   "Engine": "{{string}}",
   "ExactSettings": {{boolean}},
   "Settings": { ... },
   "Virtual": {{boolean}}
}
```

## Request Parameters
<a name="API_ModifyDataProvider_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataProviderIdentifier](#API_ModifyDataProvider_RequestSyntax) **   <a name="DMS-ModifyDataProvider-request-DataProviderIdentifier"></a>
The identifier of the data provider. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
Type: String
Required: Yes

 ** [DataProviderName](#API_ModifyDataProvider_RequestSyntax) **   <a name="DMS-ModifyDataProvider-request-DataProviderName"></a>
The name of the data provider.
Type: String
Required: No

 ** [Description](#API_ModifyDataProvider_RequestSyntax) **   <a name="DMS-ModifyDataProvider-request-Description"></a>
A user-friendly description of the data provider.
Type: String
Required: No

 ** [Engine](#API_ModifyDataProvider_RequestSyntax) **   <a name="DMS-ModifyDataProvider-request-Engine"></a>
The type of database engine for the data provider.
Valid values: `aurora`, `aurora-postgresql`, `db2`, `db2-zos`, `docdb`, `mariadb`, `mongodb`, `mysql`, `oracle`, `postgres`, `redshift`, `sqlserver`, and `sybase`. A value of `aurora` represents Amazon Aurora MySQL-Compatible Edition.
Type: String
Required: No

 ** [ExactSettings](#API_ModifyDataProvider_RequestSyntax) **   <a name="DMS-ModifyDataProvider-request-ExactSettings"></a>
If this attribute is Y, the current call to `ModifyDataProvider` replaces all existing data provider settings with the exact settings that you specify in this call. If this attribute is N, the current call to `ModifyDataProvider` does two things:
+ It replaces any data provider settings that already exist with new values, for settings with the same names.
+ It creates new data provider settings that you specify in the call, for settings with different names.
Type: Boolean
Required: No

 ** [Settings](#API_ModifyDataProvider_RequestSyntax) **   <a name="DMS-ModifyDataProvider-request-Settings"></a>
The settings in JSON format for a data provider.
Type: [DataProviderSettings](API_DataProviderSettings.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Virtual](#API_ModifyDataProvider_RequestSyntax) **   <a name="DMS-ModifyDataProvider-request-Virtual"></a>
Indicates whether the data provider is virtual.
Type: Boolean
Required: No

## Response Syntax
<a name="API_ModifyDataProvider_ResponseSyntax"></a>

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
<a name="API_ModifyDataProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataProvider](#API_ModifyDataProvider_ResponseSyntax) **   <a name="DMS-ModifyDataProvider-response-DataProvider"></a>
The data provider that was modified.
Type: [DataProvider](API_DataProvider.md) object

## Errors
<a name="API_ModifyDataProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** FailedDependencyFault **
A dependency threw an exception.
HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ModifyDataProvider_Examples"></a>

### Modify a data provider
<a name="API_ModifyDataProvider_Example_1"></a>

The following example updates the description and server name of a data provider.

#### Sample Request
<a name="API_ModifyDataProvider_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.ModifyDataProvider
{
    "DataProviderIdentifier": "arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "Description": "Updated data provider description",
    "Engine": "sqlserver",
    "Settings": {
        "MicrosoftSqlServerSettings": {
            "ServerName": "new-source-server.us-east-1.rds.amazonaws.com"
        }
    }
}
```

#### Sample Response
<a name="API_ModifyDataProvider_Example_1_Response"></a>

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
        "Description": "Updated data provider description",
        "Engine": "sqlserver",
        "Settings": {
            "MicrosoftSqlServerSettings": {
                "ServerName": "new-source-server.us-east-1.rds.amazonaws.com",
                "Port": 1433,
                "DatabaseName": "ExampleDatabase",
                "SslMode": "verify-full",
                "CertificateArn": "arn:aws:dms:us-east-1:111122223333:cert:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        }
    }
}
```

## See Also
<a name="API_ModifyDataProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ModifyDataProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ModifyDataProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ModifyDataProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ModifyDataProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ModifyDataProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ModifyDataProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ModifyDataProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ModifyDataProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ModifyDataProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ModifyDataProvider)

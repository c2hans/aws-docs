---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteDataProvider.html
---

# DeleteDataProvider
<a name="API_DeleteDataProvider"></a>

Deletes the specified data provider.

 **Required permissions:** `dms:DeleteDataProvider`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

**Note**
All migration projects associated with the data provider must be deleted or modified before you can delete the data provider.

## Request Syntax
<a name="API_DeleteDataProvider_RequestSyntax"></a>

```
{
   "DataProviderIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDataProvider_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataProviderIdentifier](#API_DeleteDataProvider_RequestSyntax) **   <a name="DMS-DeleteDataProvider-request-DataProviderIdentifier"></a>
The identifier of the data provider to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteDataProvider_ResponseSyntax"></a>

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
<a name="API_DeleteDataProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataProvider](#API_DeleteDataProvider_ResponseSyntax) **   <a name="DMS-DeleteDataProvider-response-DataProvider"></a>
The data provider that was deleted.
Type: [DataProvider](API_DataProvider.md) object

## Errors
<a name="API_DeleteDataProvider_Errors"></a>

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
<a name="API_DeleteDataProvider_Examples"></a>

### Delete a data provider
<a name="API_DeleteDataProvider_Example_1"></a>

The following example deletes a data provider identified by its ARN.

#### Sample Request
<a name="API_DeleteDataProvider_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.DeleteDataProvider
{
    "DataProviderIdentifier": "arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
}
```

#### Sample Response
<a name="API_DeleteDataProvider_Example_1_Response"></a>

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

## See Also
<a name="API_DeleteDataProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DeleteDataProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DeleteDataProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DeleteDataProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DeleteDataProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DeleteDataProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DeleteDataProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DeleteDataProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DeleteDataProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DeleteDataProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DeleteDataProvider)

---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeDataProviders.html
---

# DescribeDataProviders
<a name="API_DescribeDataProviders"></a>

Returns a paginated list of data providers for your account in the current region.

 **Required permissions:** `dms:ListDataProviders`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_DescribeDataProviders_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeDataProviders_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeDataProviders_RequestSyntax) **   <a name="DMS-DescribeDataProviders-request-Filters"></a>
The filters to apply to the data providers.
The following filter names are supported:
+  `data-provider-identifier` – The data provider name or ARN.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeDataProviders_RequestSyntax) **   <a name="DMS-DescribeDataProviders-request-Marker"></a>
Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
If `Marker` is returned by a previous response, there are more results available. The value of `Marker` is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeDataProviders_RequestSyntax) **   <a name="DMS-DescribeDataProviders-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, AWS DMS includes a pagination token in the response so that you can retrieve the remaining results.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeDataProviders_ResponseSyntax"></a>

```
{
   "DataProviders": [
      {
         "DataProviderArn": "string",
         "DataProviderCreationTime": "string",
         "DataProviderName": "string",
         "Description": "string",
         "Engine": "string",
         "Settings": { ... },
         "Virtual": boolean
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeDataProviders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataProviders](#API_DescribeDataProviders_ResponseSyntax) **   <a name="DMS-DescribeDataProviders-response-DataProviders"></a>
A description of data providers.
Type: Array of [DataProvider](API_DataProvider.md) objects

 ** [Marker](#API_DescribeDataProviders_ResponseSyntax) **   <a name="DMS-DescribeDataProviders-response-Marker"></a>
Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
If `Marker` is returned by a previous response, there are more results available. The value of `Marker` is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.
Type: String

## Errors
<a name="API_DescribeDataProviders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** FailedDependencyFault **
A dependency threw an exception.
HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeDataProviders_Examples"></a>

### Describe data providers with a filter
<a name="API_DescribeDataProviders_Example_1"></a>

The following example retrieves the details of a data provider identified by its ARN.

#### Sample Request
<a name="API_DescribeDataProviders_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.DescribeDataProviders
{
    "Filters": [
        {
            "Name": "data-provider-identifier",
            "Values": [
                "arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_DescribeDataProviders_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "DataProviders": [
        {
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
    ]
}
```

## See Also
<a name="API_DescribeDataProviders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeDataProviders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeDataProviders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeDataProviders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeDataProviders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeDataProviders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeDataProviders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeDataProviders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeDataProviders)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeDataProviders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeDataProviders)

---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEndpointTypes.html
---

# DescribeEndpointTypes
<a name="API_DescribeEndpointTypes"></a>

Returns information about the type of endpoints available.

## Request Syntax
<a name="API_DescribeEndpointTypes_RequestSyntax"></a>

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
<a name="API_DescribeEndpointTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeEndpointTypes_RequestSyntax) **   <a name="DMS-DescribeEndpointTypes-request-Filters"></a>
Filters applied to the endpoint types.
Valid filter names: engine-name \| endpoint-type
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeEndpointTypes_RequestSyntax) **   <a name="DMS-DescribeEndpointTypes-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeEndpointTypes_RequestSyntax) **   <a name="DMS-DescribeEndpointTypes-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeEndpointTypes_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "SupportedEndpointTypes": [
      {
         "EndpointType": "string",
         "EngineDisplayName": "string",
         "EngineName": "string",
         "ReplicationInstanceEngineMinimumVersion": "string",
         "SupportsCDC": boolean
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEndpointTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeEndpointTypes_ResponseSyntax) **   <a name="DMS-DescribeEndpointTypes-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [SupportedEndpointTypes](#API_DescribeEndpointTypes_ResponseSyntax) **   <a name="DMS-DescribeEndpointTypes-response-SupportedEndpointTypes"></a>
The types of endpoints that are supported.
Type: Array of [SupportedEndpointType](API_SupportedEndpointType.md) objects

## Errors
<a name="API_DescribeEndpointTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeEndpointTypes_Examples"></a>

### Example
<a name="API_DescribeEndpointTypes_Example_1"></a>

This example illustrates one usage of DescribeEndpointTypes.

#### Sample Request
<a name="API_DescribeEndpointTypes_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256
Credential=<Credential>,
SignedHeaders=contenttype;date;host;user-
agent;x-amz-date;x-amz-target;x-amzn-
requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.DescribeEndpointTypes
{
   "Filters":[
      {
         "Name":"endpoint-type",
         "Values":[
            "target"
         ]
      }
   ],
   "MaxRecords":0,
   "Marker":""
}
```

#### Sample Response
<a name="API_DescribeEndpointTypes_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "SupportedEndpointTypes": [
        {
            "EngineName": "aurora",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "Amazon Aurora MySQL"
        },
        {
            "EngineName": "aurora",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "Amazon Aurora MySQL"
        },
        {
            "EngineName": "aurora-serverless",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "Amazon Aurora MySQL Serverless"
        },
        {
            "EngineName": "aurora-postgresql",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "Amazon Aurora PostgreSQL"
        },
        {
            "EngineName": "aurora-postgresql",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "Amazon Aurora PostgreSQL"
        },
        {
            "EngineName": "aurora-postgresql-serverless",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "Amazon Aurora PostgreSQL Serverless"
        },
        {
            "EngineName": "docdb",
            "SupportsCDC": true,
            "EndpointType": "source",
            "ReplicationInstanceEngineMinimumVersion": "3.1.1",
            "EngineDisplayName": "Amazon DocumentDB (with MongoDB compatibility)"
        },
        {
            "EngineName": "docdb",
            "SupportsCDC": true,
            "EndpointType": "target",
            "ReplicationInstanceEngineMinimumVersion": "3.1.1",
            "EngineDisplayName": "Amazon DocumentDB (with MongoDB compatibility)"
        },
        {
            "EngineName": "dynamodb",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "Amazon DynamoDB"
        },
        {
            "EngineName": "kinesis",
            "SupportsCDC": true,
            "EndpointType": "target",
            "ReplicationInstanceEngineMinimumVersion": "3.1.3",
            "EngineDisplayName": "Amazon Kinesis"
        },
        {
            "EngineName": "neptune",
            "SupportsCDC": false,
            "EndpointType": "target",
            "ReplicationInstanceEngineMinimumVersion": "3.3.2",
            "EngineDisplayName": "Amazon Neptune"
        },
        {
            "EngineName": "opensearch",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "Amazon OpenSearch Service (successor to Amazon Elasticsearch Service)"
        },
        {
            "EngineName": "redshift",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "Amazon Redshift"
        },
        {
            "EngineName": "s3",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "Amazon S3"
        },
        {
            "EngineName": "s3",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "Amazon S3"
        },
        {
            "EngineName": "dms-transfer",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "AWS DMS Transfer"
        },
        {
            "EngineName": "elasticsearch",
            "SupportsCDC": true,
            "EndpointType": "target",
            "ReplicationInstanceEngineMinimumVersion": "3.1.1",
            "EngineDisplayName": "Elasticsearch Service"
        },
        {
            "EngineName": "db2",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "IBM Db2 LUW"
        },
        {
            "EngineName": "kafka",
            "SupportsCDC": true,
            "EndpointType": "target",
            "ReplicationInstanceEngineMinimumVersion": "3.3.1",
            "EngineDisplayName": "Kafka"
        },
        {
            "EngineName": "mariadb",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "MariaDB"
        },
        {
            "EngineName": "mariadb",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "MariaDB"
        },
        {
            "EngineName": "azuredb",
            "SupportsCDC": false,
            "EndpointType": "source",
            "EngineDisplayName": "Microsoft Azure SQL Database"
        },
        {
            "EngineName": "sqlserver",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "Microsoft SQL Server"
        },
        {
            "EngineName": "sqlserver",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "Microsoft SQL Server"
        },
        {
            "EngineName": "mongodb",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "MongoDB"
        },
        {
            "EngineName": "mysql",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "MySQL"
        },
        {
            "EngineName": "mysql",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "MySQL"
        },
        {
            "EngineName": "oracle",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "Oracle"
        },
        {
            "EngineName": "oracle",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "Oracle"
        },
        {
            "EngineName": "postgres",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "PostgreSQL"
        },
        {
            "EngineName": "postgres",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "PostgreSQL"
        },
        {
            "EngineName": "redis",
            "SupportsCDC": true,
            "EndpointType": "target",
            "ReplicationInstanceEngineMinimumVersion": "3.4.4",
            "EngineDisplayName": "Redis"
        },
        {
            "EngineName": "sybase",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "SAP Sybase ASE"
        },
        {
            "EngineName": "sybase",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "SAP Sybase ASE"
        }
    ]
}
```

## See Also
<a name="API_DescribeEndpointTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeEndpointTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeEndpointTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeEndpointTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeEndpointTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeEndpointTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeEndpointTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeEndpointTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeEndpointTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeEndpointTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeEndpointTypes)

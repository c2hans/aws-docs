---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEndpointSettings.html
---

# DescribeEndpointSettings
<a name="API_DescribeEndpointSettings"></a>

Returns information about the possible endpoint settings available when you create an endpoint for a specific database engine.

## Request Syntax
<a name="API_DescribeEndpointSettings_RequestSyntax"></a>

```
{
   "EngineName": "{{string}}",
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeEndpointSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EngineName](#API_DescribeEndpointSettings_RequestSyntax) **   <a name="DMS-DescribeEndpointSettings-request-EngineName"></a>
The database engine used for your source or target endpoint.
Type: String
Required: Yes

 ** [Marker](#API_DescribeEndpointSettings_RequestSyntax) **   <a name="DMS-DescribeEndpointSettings-request-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeEndpointSettings_RequestSyntax) **   <a name="DMS-DescribeEndpointSettings-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeEndpointSettings_ResponseSyntax"></a>

```
{
   "EndpointSettings": [
      {
         "Applicability": "string",
         "DefaultValue": "string",
         "EnumValues": [ "string" ],
         "IntValueMax": number,
         "IntValueMin": number,
         "Name": "string",
         "Sensitive": boolean,
         "Type": "string",
         "Units": "string"
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeEndpointSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointSettings](#API_DescribeEndpointSettings_ResponseSyntax) **   <a name="DMS-DescribeEndpointSettings-response-EndpointSettings"></a>
Descriptions of the endpoint settings available for your source or target database engine.
Type: Array of [EndpointSetting](API_EndpointSetting.md) objects

 ** [Marker](#API_DescribeEndpointSettings_ResponseSyntax) **   <a name="DMS-DescribeEndpointSettings-response-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

## Errors
<a name="API_DescribeEndpointSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeEndpointSettings_Examples"></a>

### Example
<a name="API_DescribeEndpointSettings_Example_1"></a>

This example illustrates one usage of DescribeEndpointSettings.

#### Sample Request
<a name="API_DescribeEndpointSettings_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DescribeEndpointSettings
{
   "Filters":[
      {
         "Name":"engine-name",
         "Values":[
            "sqlserver"
         ]
      }
   ],
   "MaxRecords":0,
   "Marker":""
}
```

#### Sample Response
<a name="API_DescribeEndpointSettings_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "EndpointSettings": [
        {
            "Name": "BcpPacketSize",
            "Type": "integer",
            "Sensitive": false,
            "Applicability": "TARGET_ONLY",
            "IntValueMin": 1,
            "IntValueMax": 100000
        },
        {
            "Name": "ControlTablesFileGroup",
            "Type": "string",
            "Sensitive": false
        },
        {
            "Name": "DatabaseName",
            "Type": "string",
            "Sensitive": false
        },
        {
            "Name": "Password",
            "Type": "string",
            "Sensitive": true
        },
        {
            "Name": "Port",
            "Type": "integer",
            "Sensitive": false
        },
        {
            "Name": "QuerySingleAlwaysOnNode",
            "Type": "boolean",
            "Sensitive": false
        },
        {
            "Name": "ReadBackupOnly",
            "Type": "boolean",
            "Sensitive": false,
            "Applicability": "SOURCE_ONLY"
        },
        {
            "Name": "SafeguardPolicy",
            "Type": "enum",
            "EnumValues": [
                "rely-on-sql-server-replication-agent",
                "exclusive-automatic-truncation",
                "shared-automatic-truncation"
            ],
            "Sensitive": false,
            "Applicability": "SOURCE_ONLY"
        },
        {
            "Name": "SecretsManagerAccessRoleArn",
            "Type": "string",
            "Sensitive": false
        },
        {
            "Name": "SecretsManagerSecretId",
            "Type": "string",
            "Sensitive": false
        },
        {
            "Name": "ServerName",
            "Type": "string",
            "Sensitive": false
        },
        {
            "Name": "UseBcpFullLoad",
            "Type": "boolean",
            "Sensitive": false,
            "Applicability": "TARGET_ONLY"
        },
        {
            "Name": "UseThirdPartyBackupDevice",
            "Type": "boolean",
            "Sensitive": false
        },
        {
            "Name": "Username",
            "Type": "string",
            "Sensitive": false
        }
    ]
}
```

## See Also
<a name="API_DescribeEndpointSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeEndpointSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeEndpointSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeEndpointSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeEndpointSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeEndpointSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeEndpointSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeEndpointSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeEndpointSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeEndpointSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeEndpointSettings)

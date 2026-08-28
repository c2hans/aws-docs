---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConnections.html
---

# DescribeConnections
<a name="API_DescribeConnections"></a>

Describes the status of the connections that have been made between the replication instance and an endpoint. Connections are created when you test an endpoint.

## Request Syntax
<a name="API_DescribeConnections_RequestSyntax"></a>

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
<a name="API_DescribeConnections_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeConnections_RequestSyntax) **   <a name="DMS-DescribeConnections-request-Filters"></a>
The filters applied to the connection.
Valid filter names: endpoint-arn \| replication-instance-arn
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeConnections_RequestSyntax) **   <a name="DMS-DescribeConnections-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeConnections_RequestSyntax) **   <a name="DMS-DescribeConnections-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeConnections_ResponseSyntax"></a>

```
{
   "Connections": [
      {
         "EndpointArn": "string",
         "EndpointIdentifier": "string",
         "LastFailureMessage": "string",
         "ReplicationInstanceArn": "string",
         "ReplicationInstanceIdentifier": "string",
         "Status": "string"
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connections](#API_DescribeConnections_ResponseSyntax) **   <a name="DMS-DescribeConnections-response-Connections"></a>
A description of the connections.
Type: Array of [Connection](API_Connection.md) objects

 ** [Marker](#API_DescribeConnections_ResponseSyntax) **   <a name="DMS-DescribeConnections-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

## Errors
<a name="API_DescribeConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeConnections_Examples"></a>

### Example
<a name="API_DescribeConnections_Example_1"></a>

This example illustrates one usage of DescribeConnections.

#### Sample Request
<a name="API_DescribeConnections_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DescribeConnections
{
   "Filters":[
      {
         "Name":"endpoint-arn",
         "Values":[
            "arn:aws:dms:us-east-
1:123456789012:endpoint:RZZK4EZW5UANC7Y3P4E776WHBE"
         ]
      }
   ],
   "MaxRecords":0,
   "Marker":""
}
```

#### Sample Response
<a name="API_DescribeConnections_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "Connections":[
      {
         "Status":"successful",
         "ReplicationInstanceIdentifier":"akshay1",
         "EndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:RZZK4EZW5UANC7Y3P4E776WHBE",
         "EndpointIdentifier":"akssrc1",
         "ReplicationInstanceArn":"arn:aws:dms:us-east-
1:123456789012:rep:6USOU366XFJUWATDJGBCJS3VIQ"
      }
   ]
}
```

## See Also
<a name="API_DescribeConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeConnections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeConnections)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

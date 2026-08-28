---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteConnection.html
---

# DeleteConnection
<a name="API_DeleteConnection"></a>

Deletes the connection between a replication instance and an endpoint.

## Request Syntax
<a name="API_DeleteConnection_RequestSyntax"></a>

```
{
   "EndpointArn": "{{string}}",
   "ReplicationInstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointArn](#API_DeleteConnection_RequestSyntax) **   <a name="DMS-DeleteConnection-request-EndpointArn"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
Type: String
Required: Yes

 ** [ReplicationInstanceArn](#API_DeleteConnection_RequestSyntax) **   <a name="DMS-DeleteConnection-request-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of the replication instance.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteConnection_ResponseSyntax"></a>

```
{
   "Connection": {
      "EndpointArn": "string",
      "EndpointIdentifier": "string",
      "LastFailureMessage": "string",
      "ReplicationInstanceArn": "string",
      "ReplicationInstanceIdentifier": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_DeleteConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connection](#API_DeleteConnection_ResponseSyntax) **   <a name="DMS-DeleteConnection-response-Connection"></a>
The connection that is being deleted.
Type: [Connection](API_Connection.md) object

## Errors
<a name="API_DeleteConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

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
<a name="API_DeleteConnection_Examples"></a>

### Example
<a name="API_DeleteConnection_Example_1"></a>

This example illustrates one usage of DeleteConnection.

#### Sample Request
<a name="API_DeleteConnection_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DeleteConnection
{
   "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:6USOU366XFJUWATDJGBCJS3VIQ",
   "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:WKBULDZKUDQZIHPOUUSEH34EMU"
}
```

#### Sample Response
<a name="API_DeleteConnection_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "Connection":{
      "Status":"deleting",
      "ReplicationInstanceIdentifier":"akshay1",
      "EndpointArn":"arn:aws:dms:us-east-1:123456789012:endpoint:WKBULDZKUDQZIHPOUUSEH34EMU",
      "EndpointIdentifier":"akshay",
      "ReplicationInstanceArn":"arn:aws:dms:us-east-1:123456789012:rep:6USOU366XFJUWATDJGBCJS3VIQ"
   }
}
```

## See Also
<a name="API_DeleteConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DeleteConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DeleteConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DeleteConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DeleteConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DeleteConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DeleteConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DeleteConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DeleteConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DeleteConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DeleteConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

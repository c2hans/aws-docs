---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetConnection.html
---

# GetConnection
<a name="API_GetConnection"></a>

**Note**
 AWS uses this action to install Outpost servers.

 Gets information about the specified connection.

 Use CloudTrail to monitor this action or AWS managed policy for AWS Outposts to secure it. For more information, see [AWS managed policies for AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/security-iam-awsmanpol.html) and [ Logging AWS Outposts API calls with AWS CloudTrail](https://docs.aws.amazon.com/outposts/latest/userguide/logging-using-cloudtrail.html) in the * AWS Outposts User Guide*.

## Request Syntax
<a name="API_GetConnection_RequestSyntax"></a>

```
GET /connections/{{ConnectionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionId](#API_GetConnection_RequestSyntax) **   <a name="outposts-GetConnection-request-uri-ConnectionId"></a>
 The ID of the connection.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[a-zA-Z0-9+/=]{1,1024}$`
Required: Yes

## Request Body
<a name="API_GetConnection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectionDetails": {
      "AllowedIps": [ "string" ],
      "ClientPublicKey": "string",
      "ClientTunnelAddress": "string",
      "ServerEndpoint": "string",
      "ServerPublicKey": "string",
      "ServerTunnelAddress": "string"
   },
   "ConnectionId": "string"
}
```

## Response Elements
<a name="API_GetConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionDetails](#API_GetConnection_ResponseSyntax) **   <a name="outposts-GetConnection-response-ConnectionDetails"></a>
 Information about the connection.
Type: [ConnectionDetails](API_ConnectionDetails.md) object

 ** [ConnectionId](#API_GetConnection_ResponseSyntax) **   <a name="outposts-GetConnection-response-ConnectionId"></a>
 The ID of the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[a-zA-Z0-9+/=]{1,1024}$`

## Errors
<a name="API_GetConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/GetConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/GetConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/GetConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/GetConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/GetConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/GetConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/GetConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/GetConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/GetConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/GetConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

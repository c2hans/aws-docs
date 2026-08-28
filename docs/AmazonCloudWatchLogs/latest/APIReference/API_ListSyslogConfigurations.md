---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListSyslogConfigurations.html
---

# ListSyslogConfigurations
<a name="API_ListSyslogConfigurations"></a>

Returns a list of syslog configurations. You can optionally filter the results by log group or VPC endpoint.

## Request Syntax
<a name="API_ListSyslogConfigurations_RequestSyntax"></a>

```
{
   "logGroupIdentifier": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "vpcEndpointId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSyslogConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [logGroupIdentifier](#API_ListSyslogConfigurations_RequestSyntax) **   <a name="CWL-ListSyslogConfigurations-request-logGroupIdentifier"></a>
The name or ARN of the log group to filter syslog configurations for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** [maxResults](#API_ListSyslogConfigurations_RequestSyntax) **   <a name="CWL-ListSyslogConfigurations-request-maxResults"></a>
The maximum number of syslog configurations to return in the response.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListSyslogConfigurations_RequestSyntax) **   <a name="CWL-ListSyslogConfigurations-request-nextToken"></a>
The token for the next set of items to return. You received this token from a previous call.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [vpcEndpointId](#API_ListSyslogConfigurations_RequestSyntax) **   <a name="CWL-ListSyslogConfigurations-request-vpcEndpointId"></a>
The ID of the VPC endpoint to filter syslog configurations for.
Type: String
Pattern: `^vpce-[0-9a-f]{1,64}$`
Required: No

## Response Syntax
<a name="API_ListSyslogConfigurations_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "syslogConfigurations": [
      {
         "createdAt": number,
         "logGroupArn": "string",
         "sourceType": "string",
         "vpcEndpointId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSyslogConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSyslogConfigurations_ResponseSyntax) **   <a name="CWL-ListSyslogConfigurations-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

 ** [syslogConfigurations](#API_ListSyslogConfigurations_ResponseSyntax) **   <a name="CWL-ListSyslogConfigurations-response-syslogConfigurations"></a>
The list of syslog configurations.
Type: Array of [SyslogConfiguration](API_SyslogConfiguration.md) objects

## Errors
<a name="API_ListSyslogConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation is not valid on the specified resource.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

## Examples
<a name="API_ListSyslogConfigurations_Examples"></a>

### To list syslog configurations
<a name="API_ListSyslogConfigurations_Example_1"></a>

The following example lists the syslog configurations for the specified log group.

#### Sample Request
<a name="API_ListSyslogConfigurations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.ListSyslogConfigurations
{
  "logGroupIdentifier": "arn:aws:logs:us-east-1:123456789012:log-group:my-syslog-group"
}
```

#### Sample Response
<a name="API_ListSyslogConfigurations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "syslogConfigurations": [
    {
      "logGroupArn": "arn:aws:logs:us-east-1:123456789012:log-group:my-syslog-group",
      "sourceType": "VPCE",
      "vpcEndpointId": "vpce-0123456789abcdef0",
      "createdAt": 1718000000000
    }
  ]
}
```

## See Also
<a name="API_ListSyslogConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/ListSyslogConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/ListSyslogConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ListSyslogConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/ListSyslogConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ListSyslogConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/ListSyslogConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/ListSyslogConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/ListSyslogConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/ListSyslogConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ListSyslogConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

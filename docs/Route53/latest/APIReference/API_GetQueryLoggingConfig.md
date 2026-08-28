---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetQueryLoggingConfig.html
---

# GetQueryLoggingConfig
<a name="API_GetQueryLoggingConfig"></a>

Gets information about a specified configuration for DNS query logging.

For more information about DNS query logs, see [CreateQueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html) and [Logging DNS Queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html).

## Request Syntax
<a name="API_GetQueryLoggingConfig_RequestSyntax"></a>

```
GET /2013-04-01/queryloggingconfig/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetQueryLoggingConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetQueryLoggingConfig_RequestSyntax) **   <a name="Route53-GetQueryLoggingConfig-request-uri-Id"></a>
The ID of the configuration for DNS query logging that you want to get information about.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_GetQueryLoggingConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQueryLoggingConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetQueryLoggingConfigResponse>
   <QueryLoggingConfig>
      <CloudWatchLogsLogGroupArn>string</CloudWatchLogsLogGroupArn>
      <HostedZoneId>string</HostedZoneId>
      <Id>string</Id>
   </QueryLoggingConfig>
</GetQueryLoggingConfigResponse>
```

## Response Elements
<a name="API_GetQueryLoggingConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetQueryLoggingConfigResponse](#API_GetQueryLoggingConfig_ResponseSyntax) **   <a name="Route53-GetQueryLoggingConfig-response-GetQueryLoggingConfigResponse"></a>
Root level tag for the GetQueryLoggingConfigResponse parameters.
Required: Yes

 ** [QueryLoggingConfig](#API_GetQueryLoggingConfig_ResponseSyntax) **   <a name="Route53-GetQueryLoggingConfig-response-QueryLoggingConfig"></a>
A complex type that contains information about the query logging configuration that you specified in a [GetQueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetQueryLoggingConfig.html) request.
Type: [QueryLoggingConfig](API_QueryLoggingConfig.md) object

## Errors
<a name="API_GetQueryLoggingConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchQueryLoggingConfig **
There is no DNS query logging configuration with the specified ID.
HTTP Status Code: 404

## Examples
<a name="API_GetQueryLoggingConfig_Examples"></a>

### Example Request
<a name="API_GetQueryLoggingConfig_Example_1"></a>

The following request gets information about the configuration with the ID `87654321-dcba-1234-abcd-1a2b3c4d5e6f`.

```
GET /2013-04-01/queryloggingconfig HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<GetQueryLoggingConfigRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Id>87654321-dcba-1234-abcd-1a2b3c4d5e6f</Id>
</GetQueryLoggingConfigRequest>
```

### Example Response
<a name="API_GetQueryLoggingConfig_Example_2"></a>

This example illustrates one usage of GetQueryLoggingConfig.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetQueryLoggingConfigResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <QueryLoggingConfig>
      <Id>87654321-dcba-1234-abcd-1a2b3c4d5e6f</Id>
      <HostedZoneId>Z1D633PJN98FT9</HostedZoneId>
      <CloudWatchLogsLogGroupArn>arn:aws:logs:us-east-1:111111111111:log-group:example.com:*</CloudWatchLogsLogGroupArn>
   </QueryLoggingConfig>
</GetQueryLoggingConfigResponse>
```

## See Also
<a name="API_GetQueryLoggingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetQueryLoggingConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetQueryLoggingConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetQueryLoggingConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetQueryLoggingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetQueryLoggingConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetQueryLoggingConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetQueryLoggingConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetQueryLoggingConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetQueryLoggingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetQueryLoggingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

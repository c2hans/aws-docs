---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponentConfiguration.html
---

# DescribeComponentConfiguration
<a name="API_DescribeComponentConfiguration"></a>

Describes the monitoring configuration of the component.

## Request Syntax
<a name="API_DescribeComponentConfiguration_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "ComponentName": "{{string}}",
   "ResourceGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeComponentConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_DescribeComponentConfiguration_RequestSyntax) **   <a name="appinsights-DescribeComponentConfiguration-request-AccountId"></a>
The AWS account ID for the resource group owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [ComponentName](#API_DescribeComponentConfiguration_RequestSyntax) **   <a name="appinsights-DescribeComponentConfiguration-request-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `(?:^[\d\w\-_\.+]*$)|(?:^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$)`
Required: Yes

 ** [ResourceGroupName](#API_DescribeComponentConfiguration_RequestSyntax) **   <a name="appinsights-DescribeComponentConfiguration-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

## Response Syntax
<a name="API_DescribeComponentConfiguration_ResponseSyntax"></a>

```
{
   "ComponentConfiguration": "string",
   "Monitor": boolean,
   "Tier": "string"
}
```

## Response Elements
<a name="API_DescribeComponentConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComponentConfiguration](#API_DescribeComponentConfiguration_ResponseSyntax) **   <a name="appinsights-DescribeComponentConfiguration-response-ComponentConfiguration"></a>
The configuration settings of the component. The value is the escaped JSON of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `[\S\s]+`

 ** [Monitor](#API_DescribeComponentConfiguration_ResponseSyntax) **   <a name="appinsights-DescribeComponentConfiguration-response-Monitor"></a>
Indicates whether the application component is monitored.
Type: Boolean

 ** [Tier](#API_DescribeComponentConfiguration_ResponseSyntax) **   <a name="appinsights-DescribeComponentConfiguration-response-Tier"></a>
The tier of the application component. Supported tiers include `DOT_NET_CORE`, `DOT_NET_WORKER`, `DOT_NET_WEB`, `SQL_SERVER`, and `DEFAULT`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Valid Values: `CUSTOM | DEFAULT | DOT_NET_CORE | DOT_NET_WORKER | DOT_NET_WEB_TIER | DOT_NET_WEB | SQL_SERVER | SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP | MYSQL | POSTGRESQL | JAVA_JMX | ORACLE | SAP_HANA_MULTI_NODE | SAP_HANA_SINGLE_NODE | SAP_HANA_HIGH_AVAILABILITY | SAP_ASE_SINGLE_NODE | SAP_ASE_HIGH_AVAILABILITY | SQL_SERVER_FAILOVER_CLUSTER_INSTANCE | SHAREPOINT | ACTIVE_DIRECTORY | SAP_NETWEAVER_STANDARD | SAP_NETWEAVER_DISTRIBUTED | SAP_NETWEAVER_HIGH_AVAILABILITY`

## Errors
<a name="API_DescribeComponentConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeComponentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/DescribeComponentConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/DescribeComponentConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/DescribeComponentConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/DescribeComponentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/DescribeComponentConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/DescribeComponentConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/DescribeComponentConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/DescribeComponentConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/DescribeComponentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/DescribeComponentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

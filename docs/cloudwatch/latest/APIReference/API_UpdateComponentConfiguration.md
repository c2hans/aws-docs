---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.html
---

# UpdateComponentConfiguration
<a name="API_UpdateComponentConfiguration"></a>

Updates the monitoring configurations for the component. The configuration input parameter is an escaped JSON of the configuration and should match the schema of what is returned by `DescribeComponentConfigurationRecommendation`.

## Request Syntax
<a name="API_UpdateComponentConfiguration_RequestSyntax"></a>

```
{
   "AutoConfigEnabled": {{boolean}},
   "ComponentConfiguration": "{{string}}",
   "ComponentName": "{{string}}",
   "Monitor": {{boolean}},
   "ResourceGroupName": "{{string}}",
   "Tier": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateComponentConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoConfigEnabled](#API_UpdateComponentConfiguration_RequestSyntax) **   <a name="appinsights-UpdateComponentConfiguration-request-AutoConfigEnabled"></a>
 Automatically configures the component by applying the recommended configurations.
Type: Boolean
Required: No

 ** [ComponentConfiguration](#API_UpdateComponentConfiguration_RequestSyntax) **   <a name="appinsights-UpdateComponentConfiguration-request-ComponentConfiguration"></a>
The configuration settings of the component. The value is the escaped JSON of the configuration. For more information about the JSON format, see [Working with JSON](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/working-with-json.html). You can send a request to `DescribeComponentConfigurationRecommendation` to see the recommended configuration for a component. For the complete format of the component configuration file, see [Component Configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `[\S\s]+`
Required: No

 ** [ComponentName](#API_UpdateComponentConfiguration_RequestSyntax) **   <a name="appinsights-UpdateComponentConfiguration-request-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `(?:^[\d\w\-_\.+]*$)|(?:^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$)`
Required: Yes

 ** [Monitor](#API_UpdateComponentConfiguration_RequestSyntax) **   <a name="appinsights-UpdateComponentConfiguration-request-Monitor"></a>
Indicates whether the application component is monitored.
Type: Boolean
Required: No

 ** [ResourceGroupName](#API_UpdateComponentConfiguration_RequestSyntax) **   <a name="appinsights-UpdateComponentConfiguration-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [Tier](#API_UpdateComponentConfiguration_RequestSyntax) **   <a name="appinsights-UpdateComponentConfiguration-request-Tier"></a>
The tier of the application component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Valid Values: `CUSTOM | DEFAULT | DOT_NET_CORE | DOT_NET_WORKER | DOT_NET_WEB_TIER | DOT_NET_WEB | SQL_SERVER | SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP | MYSQL | POSTGRESQL | JAVA_JMX | ORACLE | SAP_HANA_MULTI_NODE | SAP_HANA_SINGLE_NODE | SAP_HANA_HIGH_AVAILABILITY | SAP_ASE_SINGLE_NODE | SAP_ASE_HIGH_AVAILABILITY | SQL_SERVER_FAILOVER_CLUSTER_INSTANCE | SHAREPOINT | ACTIVE_DIRECTORY | SAP_NETWEAVER_STANDARD | SAP_NETWEAVER_DISTRIBUTED | SAP_NETWEAVER_HIGH_AVAILABILITY`
Required: No

## Response Elements
<a name="API_UpdateComponentConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateComponentConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is already created or in use.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateComponentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/UpdateComponentConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/UpdateComponentConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/UpdateComponentConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/UpdateComponentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/UpdateComponentConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/UpdateComponentConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/UpdateComponentConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/UpdateComponentConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/UpdateComponentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/UpdateComponentConfiguration)

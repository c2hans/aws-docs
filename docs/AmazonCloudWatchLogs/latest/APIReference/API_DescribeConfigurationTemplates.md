---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html
---

# DescribeConfigurationTemplates
<a name="API_DescribeConfigurationTemplates"></a>

Use this operation to return the valid and default values that are used when creating delivery sources, delivery destinations, and deliveries. For more information about deliveries, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).

## Request Syntax
<a name="API_DescribeConfigurationTemplates_RequestSyntax"></a>

```
{
   "deliveryDestinationTypes": [ "{{string}}" ],
   "limit": {{number}},
   "logTypes": [ "{{string}}" ],
   "nextToken": "{{string}}",
   "resourceTypes": [ "{{string}}" ],
   "service": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConfigurationTemplates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deliveryDestinationTypes](#API_DescribeConfigurationTemplates_RequestSyntax) **   <a name="CWL-DescribeConfigurationTemplates-request-deliveryDestinationTypes"></a>
Use this parameter to filter the response to include only the configuration templates that apply to the delivery destination types that you specify here.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `S3 | CWL | FH | XRAY`
Required: No

 ** [limit](#API_DescribeConfigurationTemplates_RequestSyntax) **   <a name="CWL-DescribeConfigurationTemplates-request-limit"></a>
Use this parameter to limit the number of configuration templates that are returned in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [logTypes](#API_DescribeConfigurationTemplates_RequestSyntax) **   <a name="CWL-DescribeConfigurationTemplates-request-logTypes"></a>
Use this parameter to filter the response to include only the configuration templates that apply to the log types that you specify here.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w]*`
Required: No

 ** [nextToken](#API_DescribeConfigurationTemplates_RequestSyntax) **   <a name="CWL-DescribeConfigurationTemplates-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [resourceTypes](#API_DescribeConfigurationTemplates_RequestSyntax) **   <a name="CWL-DescribeConfigurationTemplates-request-resourceTypes"></a>
Use this parameter to filter the response to include only the configuration templates that apply to the resource types that you specify here.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-_]*`
Required: No

 ** [service](#API_DescribeConfigurationTemplates_RequestSyntax) **   <a name="CWL-DescribeConfigurationTemplates-request-service"></a>
Use this parameter to filter the response to include only the configuration templates that apply to the AWS service that you specify here.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w_-]*`
Required: No

## Response Syntax
<a name="API_DescribeConfigurationTemplates_ResponseSyntax"></a>

```
{
   "configurationTemplates": [
      {
         "allowedActionForAllowVendedLogsDeliveryForResource": "string",
         "allowedFieldDelimiters": [ "string" ],
         "allowedFields": [
            {
               "mandatory": boolean,
               "name": "string"
            }
         ],
         "allowedOutputFormats": [ "string" ],
         "allowedSuffixPathFields": [ "string" ],
         "defaultDeliveryConfigValues": {
            "fieldDelimiter": "string",
            "recordFields": [ "string" ],
            "s3DeliveryConfiguration": {
               "enableHiveCompatiblePath": boolean,
               "suffixPath": "string"
            }
         },
         "deliveryDestinationType": "string",
         "deliverySourceConfiguration": [
            {
               "defaultValue": "string",
               "keyName": "string",
               "maxValue": number,
               "minValue": number,
               "supportedValues": [ "string" ],
               "valueType": "string"
            }
         ],
         "logType": "string",
         "resourceType": "string",
         "s3TablesIntegration": {
            "datasourceName": "string",
            "datasourceType": "string"
         },
         "service": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConfigurationTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurationTemplates](#API_DescribeConfigurationTemplates_ResponseSyntax) **   <a name="CWL-DescribeConfigurationTemplates-response-configurationTemplates"></a>
An array of objects, where each object describes one configuration template that matches the filters that you specified in the request.
Type: Array of [ConfigurationTemplate](API_ConfigurationTemplate.md) objects

 ** [nextToken](#API_DescribeConfigurationTemplates_ResponseSyntax) **   <a name="CWL-DescribeConfigurationTemplates-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeConfigurationTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConfigurationTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeConfigurationTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeConfigurationTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeConfigurationTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeConfigurationTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeConfigurationTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeConfigurationTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeConfigurationTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeConfigurationTemplates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeConfigurationTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeConfigurationTemplates)

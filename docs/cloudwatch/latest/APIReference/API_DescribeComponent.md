---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponent.html
---

# DescribeComponent
<a name="API_DescribeComponent"></a>

Describes a component and lists the resources that are grouped together in a component.

## Request Syntax
<a name="API_DescribeComponent_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "ComponentName": "{{string}}",
   "ResourceGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_DescribeComponent_RequestSyntax) **   <a name="appinsights-DescribeComponent-request-AccountId"></a>
The AWS account ID for the resource group owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [ComponentName](#API_DescribeComponent_RequestSyntax) **   <a name="appinsights-DescribeComponent-request-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `(?:^[\d\w\-_\.+]*$)|(?:^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$)`
Required: Yes

 ** [ResourceGroupName](#API_DescribeComponent_RequestSyntax) **   <a name="appinsights-DescribeComponent-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

## Response Syntax
<a name="API_DescribeComponent_ResponseSyntax"></a>

```
{
   "ApplicationComponent": {
      "ComponentName": "string",
      "ComponentRemarks": "string",
      "DetectedWorkload": {
         "string" : {
            "string" : "string"
         }
      },
      "Monitor": boolean,
      "OsType": "string",
      "ResourceType": "string",
      "Tier": "string"
   },
   "ResourceList": [ "string" ]
}
```

## Response Elements
<a name="API_DescribeComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationComponent](#API_DescribeComponent_ResponseSyntax) **   <a name="appinsights-DescribeComponent-response-ApplicationComponent"></a>
Describes a standalone resource or similarly grouped resources that the application is made up of.
Type: [ApplicationComponent](API_ApplicationComponent.md) object

 ** [ResourceList](#API_DescribeComponent_ResponseSyntax) **   <a name="appinsights-DescribeComponent-response-ResourceList"></a>
The list of resource ARNs that belong to the component.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`

## Errors
<a name="API_DescribeComponent_Errors"></a>

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
<a name="API_DescribeComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/DescribeComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/DescribeComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/DescribeComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/DescribeComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/DescribeComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/DescribeComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/DescribeComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/DescribeComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/DescribeComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/DescribeComponent)

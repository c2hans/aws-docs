---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_AddWorkload.html
---

# AddWorkload
<a name="API_AddWorkload"></a>

Adds a workload to a component. Each component can have at most five workloads.

## Request Syntax
<a name="API_AddWorkload_RequestSyntax"></a>

```
{
   "ComponentName": "{{string}}",
   "ResourceGroupName": "{{string}}",
   "WorkloadConfiguration": {
      "Configuration": "{{string}}",
      "Tier": "{{string}}",
      "WorkloadName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_AddWorkload_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComponentName](#API_AddWorkload_RequestSyntax) **   <a name="appinsights-AddWorkload-request-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `(?:^[\d\w\-_\.+]*$)|(?:^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$)`
Required: Yes

 ** [ResourceGroupName](#API_AddWorkload_RequestSyntax) **   <a name="appinsights-AddWorkload-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [WorkloadConfiguration](#API_AddWorkload_RequestSyntax) **   <a name="appinsights-AddWorkload-request-WorkloadConfiguration"></a>
The configuration settings of the workload. The value is the escaped JSON of the configuration.
Type: [WorkloadConfiguration](API_WorkloadConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_AddWorkload_ResponseSyntax"></a>

```
{
   "WorkloadConfiguration": {
      "Configuration": "string",
      "Tier": "string",
      "WorkloadName": "string"
   },
   "WorkloadId": "string"
}
```

## Response Elements
<a name="API_AddWorkload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkloadConfiguration](#API_AddWorkload_ResponseSyntax) **   <a name="appinsights-AddWorkload-response-WorkloadConfiguration"></a>
The configuration settings of the workload. The value is the escaped JSON of the configuration.
Type: [WorkloadConfiguration](API_WorkloadConfiguration.md) object

 ** [WorkloadId](#API_AddWorkload_ResponseSyntax) **   <a name="appinsights-AddWorkload-response-WorkloadId"></a>
The ID of the workload.
Type: String
Length Constraints: Fixed length of 38.
Pattern: `w-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`

## Errors
<a name="API_AddWorkload_Errors"></a>

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
<a name="API_AddWorkload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/AddWorkload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/AddWorkload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/AddWorkload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/AddWorkload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/AddWorkload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/AddWorkload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/AddWorkload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/AddWorkload)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/AddWorkload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/AddWorkload)

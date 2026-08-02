---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_RemoveWorkload.html
---

# RemoveWorkload
<a name="API_RemoveWorkload"></a>

Remove workload from a component.

## Request Syntax
<a name="API_RemoveWorkload_RequestSyntax"></a>

```
{
   "ComponentName": "{{string}}",
   "ResourceGroupName": "{{string}}",
   "WorkloadId": "{{string}}"
}
```

## Request Parameters
<a name="API_RemoveWorkload_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComponentName](#API_RemoveWorkload_RequestSyntax) **   <a name="appinsights-RemoveWorkload-request-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `(?:^[\d\w\-_\.+]*$)|(?:^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$)`
Required: Yes

 ** [ResourceGroupName](#API_RemoveWorkload_RequestSyntax) **   <a name="appinsights-RemoveWorkload-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [WorkloadId](#API_RemoveWorkload_RequestSyntax) **   <a name="appinsights-RemoveWorkload-request-WorkloadId"></a>
The ID of the workload.
Type: String
Length Constraints: Fixed length of 38.
Pattern: `w-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
Required: Yes

## Response Elements
<a name="API_RemoveWorkload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveWorkload_Errors"></a>

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
<a name="API_RemoveWorkload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/RemoveWorkload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/RemoveWorkload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/RemoveWorkload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/RemoveWorkload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/RemoveWorkload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/RemoveWorkload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/RemoveWorkload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/RemoveWorkload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/RemoveWorkload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/RemoveWorkload)

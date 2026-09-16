---
source_url: https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_DeleteHomeRegionControl.html
---

# DeleteHomeRegionControl
<a name="API_DeleteHomeRegionControl"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

This operation deletes the home region configuration for the calling account. The operation does not delete discovery or migration tracking data in the home region.

## Request Syntax
<a name="API_DeleteHomeRegionControl_RequestSyntax"></a>

```
{
   "ControlId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteHomeRegionControl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ControlId](#API_DeleteHomeRegionControl_RequestSyntax) **   <a name="migrationhubhomeregion-DeleteHomeRegionControl-request-ControlId"></a>
A unique identifier that's generated for each home region control. It's always a string that begins with "hrc-" followed by 12 lowercase letters and numbers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^hrc-[a-z0-9]{12}$`
Required: Yes

## Response Elements
<a name="API_DeleteHomeRegionControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteHomeRegionControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerError **
Exception raised when an internal, configuration, or dependency error is encountered.
HTTP Status Code: 500

 ** InvalidInputException **
Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type.
HTTP Status Code: 400

 ** ServiceUnavailableException **
Exception raised when a request fails due to temporary unavailability of the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 400

## See Also
<a name="API_DeleteHomeRegionControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhub-config-2019-06-30/DeleteHomeRegionControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhub-config-2019-06-30/DeleteHomeRegionControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhub-config-2019-06-30/DeleteHomeRegionControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhub-config-2019-06-30/DeleteHomeRegionControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhub-config-2019-06-30/DeleteHomeRegionControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhub-config-2019-06-30/DeleteHomeRegionControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhub-config-2019-06-30/DeleteHomeRegionControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhub-config-2019-06-30/DeleteHomeRegionControl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhub-config-2019-06-30/DeleteHomeRegionControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhub-config-2019-06-30/DeleteHomeRegionControl)

---
source_url: https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_CreateHomeRegionControl.html
---

# CreateHomeRegionControl
<a name="API_CreateHomeRegionControl"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

This API sets up the home region for the calling account only.

## Request Syntax
<a name="API_CreateHomeRegionControl_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "HomeRegion": "{{string}}",
   "Target": {
      "Id": "{{string}}",
      "Type": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateHomeRegionControl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DryRun](#API_CreateHomeRegionControl_RequestSyntax) **   <a name="migrationhubhomeregion-CreateHomeRegionControl-request-DryRun"></a>
Optional Boolean flag to indicate whether any effect should take place. It tests whether the caller has permission to make the call.
Type: Boolean
Required: No

 ** [HomeRegion](#API_CreateHomeRegionControl_RequestSyntax) **   <a name="migrationhubhomeregion-CreateHomeRegionControl-request-HomeRegion"></a>
The name of the home region of the calling account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^([a-z]+)-([a-z]+)-([0-9]+)$`
Required: Yes

 ** [Target](#API_CreateHomeRegionControl_RequestSyntax) **   <a name="migrationhubhomeregion-CreateHomeRegionControl-request-Target"></a>
The account for which this command sets up a home region control. The `Target` is always of type `ACCOUNT`.
Type: [Target](API_Target.md) object
Required: Yes

## Response Syntax
<a name="API_CreateHomeRegionControl_ResponseSyntax"></a>

```
{
   "HomeRegionControl": {
      "ControlId": "string",
      "HomeRegion": "string",
      "RequestedTime": number,
      "Target": {
         "Id": "string",
         "Type": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateHomeRegionControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HomeRegionControl](#API_CreateHomeRegionControl_ResponseSyntax) **   <a name="migrationhubhomeregion-CreateHomeRegionControl-response-HomeRegionControl"></a>
This object is the `HomeRegionControl` object that's returned by a successful call to `CreateHomeRegionControl`.
Type: [HomeRegionControl](API_HomeRegionControl.md) object

## Errors
<a name="API_CreateHomeRegionControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** DryRunOperation **
Exception raised to indicate that authorization of an action was successful, when the `DryRun` flag is set to true.
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
<a name="API_CreateHomeRegionControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhub-config-2019-06-30/CreateHomeRegionControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhub-config-2019-06-30/CreateHomeRegionControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhub-config-2019-06-30/CreateHomeRegionControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhub-config-2019-06-30/CreateHomeRegionControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhub-config-2019-06-30/CreateHomeRegionControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhub-config-2019-06-30/CreateHomeRegionControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhub-config-2019-06-30/CreateHomeRegionControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhub-config-2019-06-30/CreateHomeRegionControl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhub-config-2019-06-30/CreateHomeRegionControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhub-config-2019-06-30/CreateHomeRegionControl)

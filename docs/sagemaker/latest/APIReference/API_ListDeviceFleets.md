---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListDeviceFleets.html
---

# ListDeviceFleets
<a name="API_ListDeviceFleets"></a>

Returns a list of devices in the fleet.

## Request Syntax
<a name="API_ListDeviceFleets_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDeviceFleets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDeviceFleets_RequestSyntax) **   <a name="sagemaker-ListDeviceFleets-request-MaxResults"></a>
The maximum number of results to select.
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [NameContains](#API_ListDeviceFleets_RequestSyntax) **   <a name="sagemaker-ListDeviceFleets-request-NameContains"></a>
Filter for fleets containing this name in their fleet device name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListDeviceFleets_RequestSyntax) **   <a name="sagemaker-ListDeviceFleets-request-NextToken"></a>
The response from the last list when returning a list large enough to need tokening.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListDeviceFleets_RequestSyntax) **   <a name="sagemaker-ListDeviceFleets-request-SortBy"></a>
The column to sort by.
Type: String
Valid Values: `NAME | CREATION_TIME | LAST_MODIFIED_TIME`
Required: No

 ** [SortOrder](#API_ListDeviceFleets_RequestSyntax) **   <a name="sagemaker-ListDeviceFleets-request-SortOrder"></a>
What direction to sort in.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListDeviceFleets_ResponseSyntax"></a>

```
{
   "DeviceFleetSummaries": [
      {
         "DeviceFleetArn": "string",
         "DeviceFleetName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDeviceFleets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeviceFleetSummaries](#API_ListDeviceFleets_ResponseSyntax) **   <a name="sagemaker-ListDeviceFleets-response-DeviceFleetSummaries"></a>
Summary of the device fleet.
Type: Array of [DeviceFleetSummary](API_DeviceFleetSummary.md) objects

 ** [NextToken](#API_ListDeviceFleets_ResponseSyntax) **   <a name="sagemaker-ListDeviceFleets-response-NextToken"></a>
The response from the last list when returning a list large enough to need tokening.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListDeviceFleets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListDeviceFleets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListDeviceFleets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListDeviceFleets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListDeviceFleets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListDeviceFleets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListDeviceFleets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListDeviceFleets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListDeviceFleets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListDeviceFleets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListDeviceFleets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListDeviceFleets)

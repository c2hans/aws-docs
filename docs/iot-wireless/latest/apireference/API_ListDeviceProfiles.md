---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDeviceProfiles.html
---

# ListDeviceProfiles
<a name="API_ListDeviceProfiles"></a>

Lists the device profiles registered to your AWS account.

## Request Syntax
<a name="API_ListDeviceProfiles_RequestSyntax"></a>

```
GET /device-profiles?deviceProfileType={{DeviceProfileType}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDeviceProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeviceProfileType](#API_ListDeviceProfiles_RequestSyntax) **   <a name="iotwireless-ListDeviceProfiles-request-uri-DeviceProfileType"></a>
A filter to list only device profiles that use this type, which can be `LoRaWAN` or `Sidewalk`.
Valid Values: `Sidewalk | LoRaWAN`

 ** [MaxResults](#API_ListDeviceProfiles_RequestSyntax) **   <a name="iotwireless-ListDeviceProfiles-request-uri-MaxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 0. Maximum value of 250.

 ** [NextToken](#API_ListDeviceProfiles_RequestSyntax) **   <a name="iotwireless-ListDeviceProfiles-request-uri-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.
Length Constraints: Maximum length of 4096.

## Request Body
<a name="API_ListDeviceProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDeviceProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DeviceProfileList": [
      {
         "Arn": "string",
         "Id": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDeviceProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeviceProfileList](#API_ListDeviceProfiles_ResponseSyntax) **   <a name="iotwireless-ListDeviceProfiles-response-DeviceProfileList"></a>
The list of device profiles.
Type: Array of [DeviceProfile](API_DeviceProfile.md) objects

 ** [NextToken](#API_ListDeviceProfiles_ResponseSyntax) **   <a name="iotwireless-ListDeviceProfiles-response-NextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String
Length Constraints: Maximum length of 4096.

## Errors
<a name="API_ListDeviceProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListDeviceProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/ListDeviceProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/ListDeviceProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ListDeviceProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/ListDeviceProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ListDeviceProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/ListDeviceProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/ListDeviceProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/ListDeviceProfiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/ListDeviceProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ListDeviceProfiles)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

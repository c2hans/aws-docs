---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetDevices.html
---

# GetDevices
<a name="API_GetDevices"></a>

Gets information about one or more of your devices in a global network.

## Request Syntax
<a name="API_GetDevices_RequestSyntax"></a>

```
GET /global-networks/{{globalNetworkId}}/devices?deviceIds={{DeviceIds}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&siteId={{SiteId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDevices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeviceIds](#API_GetDevices_RequestSyntax) **   <a name="networkmanager-GetDevices-request-uri-DeviceIds"></a>
One or more device IDs. The maximum is 10.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`

 ** [globalNetworkId](#API_GetDevices_RequestSyntax) **   <a name="networkmanager-GetDevices-request-uri-GlobalNetworkId"></a>
The ID of the global network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

 ** [MaxResults](#API_GetDevices_RequestSyntax) **   <a name="networkmanager-GetDevices-request-uri-MaxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 500.

 ** [NextToken](#API_GetDevices_RequestSyntax) **   <a name="networkmanager-GetDevices-request-uri-NextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

 ** [SiteId](#API_GetDevices_RequestSyntax) **   <a name="networkmanager-GetDevices-request-uri-SiteId"></a>
The ID of the site.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`

## Request Body
<a name="API_GetDevices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDevices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Devices": [
      {
         "AWSLocation": {
            "SubnetArn": "string",
            "Zone": "string"
         },
         "CreatedAt": number,
         "Description": "string",
         "DeviceArn": "string",
         "DeviceId": "string",
         "GlobalNetworkId": "string",
         "Location": {
            "Address": "string",
            "Latitude": "string",
            "Longitude": "string"
         },
         "Model": "string",
         "SerialNumber": "string",
         "SiteId": "string",
         "State": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "Type": "string",
         "Vendor": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Devices](#API_GetDevices_ResponseSyntax) **   <a name="networkmanager-GetDevices-response-Devices"></a>
The devices.
Type: Array of [Device](API_Device.md) objects

 ** [NextToken](#API_GetDevices_ResponseSyntax) **   <a name="networkmanager-GetDevices-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Errors
<a name="API_GetDevices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** Context **
The specified resource could not be found.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason for the error.
HTTP Status Code: 400

## See Also
<a name="API_GetDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/GetDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetDevices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetDevices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ListDevices.html
---

# ListDevices
<a name="API_ListDevices"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns a list of devices.

## Request Syntax
<a name="API_ListDevices_RequestSyntax"></a>

```
GET /devices?DeviceAggregatedStatusFilter={{DeviceAggregatedStatusFilter}}&MaxResults={{MaxResults}}&NameFilter={{NameFilter}}&NextToken={{NextToken}}&SortBy={{SortBy}}&SortOrder={{SortOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDevices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeviceAggregatedStatusFilter](#API_ListDevices_RequestSyntax) **   <a name="panorama-ListDevices-request-uri-DeviceAggregatedStatusFilter"></a>
Filter based on a device's status.
Valid Values: `ERROR | AWAITING_PROVISIONING | PENDING | FAILED | DELETING | ONLINE | OFFLINE | LEASE_EXPIRED | UPDATE_NEEDED | REBOOTING`

 ** [MaxResults](#API_ListDevices_RequestSyntax) **   <a name="panorama-ListDevices-request-uri-MaxResults"></a>
The maximum number of devices to return in one page of results.
Valid Range: Minimum value of 0. Maximum value of 25.

 ** [NameFilter](#API_ListDevices_RequestSyntax) **   <a name="panorama-ListDevices-request-uri-NameFilter"></a>
Filter based on device's name. Prefixes supported.

 ** [NextToken](#API_ListDevices_RequestSyntax) **   <a name="panorama-ListDevices-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

 ** [SortBy](#API_ListDevices_RequestSyntax) **   <a name="panorama-ListDevices-request-uri-SortBy"></a>
The target column to be sorted on. Default column sort is CREATED\_TIME.
Valid Values: `DEVICE_ID | CREATED_TIME | NAME | DEVICE_AGGREGATED_STATUS`

 ** [SortOrder](#API_ListDevices_RequestSyntax) **   <a name="panorama-ListDevices-request-uri-SortOrder"></a>
The sorting order for the returned list. SortOrder is DESCENDING by default based on CREATED\_TIME. Otherwise, SortOrder is ASCENDING.
Valid Values: `ASCENDING | DESCENDING`

## Request Body
<a name="API_ListDevices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDevices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Devices": [
      {
         "Brand": "string",
         "CreatedTime": number,
         "CurrentSoftware": "string",
         "Description": "string",
         "DeviceAggregatedStatus": "string",
         "DeviceId": "string",
         "LastUpdatedTime": number,
         "LatestDeviceJob": {
            "ImageVersion": "string",
            "JobType": "string",
            "Status": "string"
         },
         "LeaseExpirationTime": number,
         "Name": "string",
         "ProvisioningStatus": "string",
         "Tags": {
            "string" : "string"
         },
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Devices](#API_ListDevices_ResponseSyntax) **   <a name="panorama-ListDevices-response-Devices"></a>
A list of devices.
Type: Array of [Device](API_Device.md) objects

 ** [NextToken](#API_ListDevices_ResponseSyntax) **   <a name="panorama-ListDevices-response-NextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

## Errors
<a name="API_ListDevices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** ConflictException **
The target resource is in use.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/ListDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/ListDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ListDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/ListDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ListDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/ListDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/ListDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/ListDevices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/ListDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ListDevices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

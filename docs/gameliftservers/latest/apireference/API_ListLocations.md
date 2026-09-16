---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListLocations.html
---

# ListLocations
<a name="API_ListLocations"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Lists all custom and AWS locations where Amazon GameLift Servers can host game servers. This operation also returns UDP ping beacon information for locations, which you can use to measure network latency between player devices and potential hosting locations.

The set of locations returned by this API depends on the AWS Region you specify when calling this API (or your default Region if you don't specify one).

When you call from:
+  **A home Region of a fleet that supports multi-locations:** API returns information for *all* hosting locations
+  **A home Region of a fleet that supports a single location:** API returns information for that location

Note that if you call this API using a location that doesn't have a service endpoint, such as one that can only be a remote location in a multi-location fleet, the API returns an error.

Consult the table of supported locations in [Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) to identify home Regions that support single and multi-location fleets.

Avoid calling `ListLocations` before each latency measurement, as it's not designed for high-volume requests. The beacon endpoint information returned by this API are static and won't change as long as Amazon GameLift Servers supports game hosting in that location.

 **Learn more**

 [Service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html)

 [UDP ping beacons](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-udp-ping-beacons.html)

## Request Syntax
<a name="API_ListLocations_RequestSyntax"></a>

```
{
   "Filters": [ "{{string}}" ],
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLocations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Filters](#API_ListLocations_RequestSyntax) **   <a name="gameliftservers-ListLocations-request-Filters"></a>
Filters the list for `AWS` or `CUSTOM` locations. Use this parameter to narrow down results to only AWS-managed locations (Amazon EC2 or container) or only your custom locations (such as an Amazon GameLift Servers Anywhere fleet).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `AWS | CUSTOM`
Required: No

 ** [Limit](#API_ListLocations_RequestSyntax) **   <a name="gameliftservers-ListLocations-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_ListLocations_RequestSyntax) **   <a name="gameliftservers-ListLocations-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListLocations_ResponseSyntax"></a>

```
{
   "Locations": [
      {
         "LocationArn": "string",
         "LocationName": "string",
         "PingBeacon": {
            "UDPEndpoint": {
               "Domain": "string",
               "Port": number
            }
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Locations](#API_ListLocations_ResponseSyntax) **   <a name="gameliftservers-ListLocations-response-Locations"></a>
A collection of locations, including both AWS and custom locations. Each location includes a name and ping beacon information that can be used to measure network latency between player devices and the location.
Type: Array of [LocationModel](API_LocationModel.md) objects

 ** [NextToken](#API_ListLocations_ResponseSyntax) **   <a name="gameliftservers-ListLocations-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListLocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_ListLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListLocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListLocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListLocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListLocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListLocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListLocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListLocations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListLocations)

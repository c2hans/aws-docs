---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLags.html
---

# DescribeLags
<a name="API_DescribeLags"></a>

Describes all your link aggregation groups (LAG) or the specified LAG.

## Request Syntax
<a name="API_DescribeLags_RequestSyntax"></a>

```
{
   "lagId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [lagId](#API_DescribeLags_RequestSyntax) **   <a name="DX-DescribeLags-request-lagId"></a>
The ID of the LAG.
Type: String
Required: No

 ** [maxResults](#API_DescribeLags_RequestSyntax) **   <a name="DX-DescribeLags-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeLags_RequestSyntax) **   <a name="DX-DescribeLags-request-nextToken"></a>
The token for the next page of results.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeLags_ResponseSyntax"></a>

```
{
   "lags": [
      {
         "allowsHostedConnections": boolean,
         "awsDevice": "string",
         "awsDeviceV2": "string",
         "awsLogicalDeviceId": "string",
         "connections": [
            {
               "awsDevice": "string",
               "awsDeviceV2": "string",
               "awsLogicalDeviceId": "string",
               "bandwidth": "string",
               "connectionId": "string",
               "connectionName": "string",
               "connectionState": "string",
               "encryptionMode": "string",
               "hasLogicalRedundancy": "string",
               "jumboFrameCapable": boolean,
               "lagId": "string",
               "loaIssueTime": number,
               "location": "string",
               "macSecCapable": boolean,
               "macSecKeys": [
                  {
                     "ckn": "string",
                     "secretARN": "string",
                     "startOn": "string",
                     "state": "string"
                  }
               ],
               "ownerAccount": "string",
               "partnerInterconnectMacSecCapable": boolean,
               "partnerName": "string",
               "portEncryptionStatus": "string",
               "prefixPoolSizeIpv4": number,
               "prefixPoolSizeIpv6": number,
               "prefixPoolUnallocatedCountIpv4": number,
               "prefixPoolUnallocatedCountIpv6": number,
               "providerName": "string",
               "rateLimiterStatus": {
                  "inUse": number,
                  "maxAllowed": number,
                  "remaining": number,
                  "totalBandwidth": "string"
               },
               "region": "string",
               "tags": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ],
               "vlan": number
            }
         ],
         "connectionsBandwidth": "string",
         "encryptionMode": "string",
         "hasLogicalRedundancy": "string",
         "jumboFrameCapable": boolean,
         "lagId": "string",
         "lagName": "string",
         "lagState": "string",
         "location": "string",
         "macSecCapable": boolean,
         "macSecKeys": [
            {
               "ckn": "string",
               "secretARN": "string",
               "startOn": "string",
               "state": "string"
            }
         ],
         "minimumLinks": number,
         "numberOfConnections": number,
         "ownerAccount": "string",
         "prefixPoolSizeIpv4": number,
         "prefixPoolSizeIpv6": number,
         "prefixPoolUnallocatedCountIpv4": number,
         "prefixPoolUnallocatedCountIpv6": number,
         "providerName": "string",
         "rateLimiterStatus": {
            "inUse": number,
            "maxAllowed": number,
            "remaining": number,
            "totalBandwidth": "string"
         },
         "region": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeLags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lags](#API_DescribeLags_ResponseSyntax) **   <a name="DX-DescribeLags-response-lags"></a>
The LAGs.
Type: Array of [Lag](API_Lag.md) objects

 ** [nextToken](#API_DescribeLags_ResponseSyntax) **   <a name="DX-DescribeLags-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_DescribeLags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeLags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeLags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeLags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeLags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeLags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeLags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeLags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeLags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeLags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeLags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeLags)

---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateConnectionsBillingMode.html
---

# UpdateConnectionsBillingMode
<a name="API_UpdateConnectionsBillingMode"></a>

Updates the billing mode for the specified Direct Connect connections. You can update the billing mode for up to 200 connections in a single request.

## Request Syntax
<a name="API_UpdateConnectionsBillingMode_RequestSyntax"></a>

```
{
   "billingMode": "{{string}}",
   "connectionIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateConnectionsBillingMode_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [billingMode](#API_UpdateConnectionsBillingMode_RequestSyntax) **   <a name="DX-UpdateConnectionsBillingMode-request-billingMode"></a>
The billing mode to apply to the specified connections. The valid values are `PayAsYouGo`, `FlatRateTier1`, `FlatRateTier2`, `FlatRateTier3`, `FlatRateTier4`, and `FlatRateTier5`.
Type: String
Valid Values: `PayAsYouGo | FlatRateTier1 | FlatRateTier2 | FlatRateTier3 | FlatRateTier4 | FlatRateTier5`
Required: Yes

 ** [connectionIds](#API_UpdateConnectionsBillingMode_RequestSyntax) **   <a name="DX-UpdateConnectionsBillingMode-request-connectionIds"></a>
The IDs of the connections to update. You can specify from 1 to 200 connections.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: Yes

## Response Syntax
<a name="API_UpdateConnectionsBillingMode_ResponseSyntax"></a>

```
{
   "billingMode": "string",
   "connections": [
      {
         "awsDevice": "string",
         "awsDeviceV2": "string",
         "awsLogicalDeviceId": "string",
         "bandwidth": "string",
         "billingMode": "string",
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
   ]
}
```

## Response Elements
<a name="API_UpdateConnectionsBillingMode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [billingMode](#API_UpdateConnectionsBillingMode_ResponseSyntax) **   <a name="DX-UpdateConnectionsBillingMode-response-billingMode"></a>
The billing mode applied to the connections.
Type: String
Valid Values: `PayAsYouGo | FlatRateTier1 | FlatRateTier2 | FlatRateTier3 | FlatRateTier4 | FlatRateTier5 | PortPairFlatRateTier1 | PortPairFlatRateTier2 | PortPairFlatRateTier3 | PortPairFlatRateTier4 | PortPairFlatRateTier5`

 ** [connections](#API_UpdateConnectionsBillingMode_ResponseSyntax) **   <a name="DX-UpdateConnectionsBillingMode-response-connections"></a>
The connections with the updated billing mode.
Type: Array of [Connection](API_Connection.md) objects

## Errors
<a name="API_UpdateConnectionsBillingMode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConnectionsBillingMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/UpdateConnectionsBillingMode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/UpdateConnectionsBillingMode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/UpdateConnectionsBillingMode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/UpdateConnectionsBillingMode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/UpdateConnectionsBillingMode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/UpdateConnectionsBillingMode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/UpdateConnectionsBillingMode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/UpdateConnectionsBillingMode)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/UpdateConnectionsBillingMode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/UpdateConnectionsBillingMode)

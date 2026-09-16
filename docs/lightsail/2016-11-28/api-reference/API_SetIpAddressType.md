---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetIpAddressType.html
---

# SetIpAddressType
<a name="API_SetIpAddressType"></a>

Sets the IP address type for an Amazon Lightsail resource.

Use this action to enable dual-stack for a resource, which enables IPv4 and IPv6 for the specified resource. Alternately, you can use this action to disable dual-stack, and enable IPv4 only.

## Request Syntax
<a name="API_SetIpAddressType_RequestSyntax"></a>

```
{
   "acceptBundleUpdate": {{boolean}},
   "ipAddressType": "{{string}}",
   "resourceName": "{{string}}",
   "resourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_SetIpAddressType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [acceptBundleUpdate](#API_SetIpAddressType_RequestSyntax) **   <a name="Lightsail-SetIpAddressType-request-acceptBundleUpdate"></a>
Required parameter to accept the instance bundle update when changing to, and from, IPv6-only.
An instance bundle will change when switching from `dual-stack` or `ipv4`, to `ipv6`. It also changes when switching from `ipv6`, to `dual-stack` or `ipv4`.
You must include this parameter in the command to update the bundle. For example, if you switch from `dual-stack` to `ipv6`, the bundle will be updated, and billing for the IPv6-only instance bundle begins immediately.
Type: Boolean
Required: No

 ** [ipAddressType](#API_SetIpAddressType_RequestSyntax) **   <a name="Lightsail-SetIpAddressType-request-ipAddressType"></a>
The IP address type to set for the specified resource.
The possible values are `ipv4` for IPv4 only, `ipv6` for IPv6 only, and `dualstack` for IPv4 and IPv6.
Type: String
Valid Values: `dualstack | ipv4 | ipv6`
Required: Yes

 ** [resourceName](#API_SetIpAddressType_RequestSyntax) **   <a name="Lightsail-SetIpAddressType-request-resourceName"></a>
The name of the resource for which to set the IP address type.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [resourceType](#API_SetIpAddressType_RequestSyntax) **   <a name="Lightsail-SetIpAddressType-request-resourceType"></a>
The resource type.
The resource values are `Distribution`, `Instance`, and `LoadBalancer`.
Distribution-related APIs are available only in the N. Virginia (`us-east-1`) AWS Region. Set your AWS Region configuration to `us-east-1` to create, view, or edit distributions.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: Yes

## Response Syntax
<a name="API_SetIpAddressType_ResponseSyntax"></a>

```
{
   "operations": [
      {
         "createdAt": number,
         "errorCode": "string",
         "errorDetails": "string",
         "id": "string",
         "isTerminal": boolean,
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "operationDetails": "string",
         "operationType": "string",
         "resourceName": "string",
         "resourceType": "string",
         "status": "string",
         "statusChangedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_SetIpAddressType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_SetIpAddressType_ResponseSyntax) **   <a name="Lightsail-SetIpAddressType-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_SetIpAddressType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** AccountSetupInProgressException **
Lightsail throws this exception when an account is still in the setup in progress state.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_SetIpAddressType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/SetIpAddressType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/SetIpAddressType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/SetIpAddressType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/SetIpAddressType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/SetIpAddressType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/SetIpAddressType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/SetIpAddressType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/SetIpAddressType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/SetIpAddressType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/SetIpAddressType)

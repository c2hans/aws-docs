---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html
---

# RegisterCompute
<a name="API_RegisterCompute"></a>

 **This API works with the following fleet types:** Anywhere, Container

Registers a compute resource in an Amazon GameLift Servers Anywhere fleet.

For an Anywhere fleet or a container fleet that's running the Amazon GameLift Servers Agent, the Agent handles all compute registry tasks for you. For an Anywhere fleet that doesn't use the Agent, call this operation to register fleet computes.

To register a compute, give the compute a name (must be unique within the fleet) and specify the compute resource's DNS name or IP address. Provide a fleet ID and a fleet location to associate with the compute being registered. You can optionally include the path to a TLS certificate on the compute resource.

If successful, this operation returns compute details, including an Amazon GameLift Servers SDK endpoint or Agent endpoint. Game server processes running on the compute can use this endpoint to communicate with the Amazon GameLift Servers service. Each server process includes the SDK endpoint in its call to the Amazon GameLift Servers server SDK action `InitSDK()`.

To view compute details, call [DescribeCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeCompute.html) with the compute name.

 **Learn more**
+  [Create an Anywhere fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-anywhere.html)
+  [Test your integration](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-testing.html)
+  [Server SDK reference guides](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk.html) (for version 5.x)

## Request Syntax
<a name="API_RegisterCompute_RequestSyntax"></a>

```
{
   "CertificatePath": "{{string}}",
   "ComputeName": "{{string}}",
   "DnsName": "{{string}}",
   "FleetId": "{{string}}",
   "IpAddress": "{{string}}",
   "Location": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterCompute_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ComputeName](#API_RegisterCompute_RequestSyntax) **   <a name="gameliftservers-RegisterCompute-request-ComputeName"></a>
A descriptive label for the compute resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
Required: Yes

 ** [FleetId](#API_RegisterCompute_RequestSyntax) **   <a name="gameliftservers-RegisterCompute-request-FleetId"></a>
A unique identifier for the fleet to register the compute to. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [CertificatePath](#API_RegisterCompute_RequestSyntax) **   <a name="gameliftservers-RegisterCompute-request-CertificatePath"></a>
The path to a TLS certificate on your compute resource. Amazon GameLift Servers doesn't validate the path and certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [DnsName](#API_RegisterCompute_RequestSyntax) **   <a name="gameliftservers-RegisterCompute-request-DnsName"></a>
The DNS name of the compute resource. Amazon GameLift Servers requires either a DNS name or IP address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[0-9a-zA-Z_\-\.]+`
Required: No

 ** [IpAddress](#API_RegisterCompute_RequestSyntax) **   <a name="gameliftservers-RegisterCompute-request-IpAddress"></a>
The IP address of the compute resource. Amazon GameLift Servers requires either a DNS name or IP address. When registering an Anywhere fleet, an IP address is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9A-Fa-f\:\.]+`
Required: No

 ** [Location](#API_RegisterCompute_RequestSyntax) **   <a name="gameliftservers-RegisterCompute-request-Location"></a>
The name of a custom location to associate with the compute resource being registered. This parameter is required when registering a compute for an Anywhere fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

## Response Syntax
<a name="API_RegisterCompute_ResponseSyntax"></a>

```
{
   "Compute": {
      "ComputeArn": "string",
      "ComputeName": "string",
      "ComputeStatus": "string",
      "ContainerAttributes": [
         {
            "ContainerName": "string",
            "ContainerRuntimeId": "string"
         }
      ],
      "CreationTime": number,
      "DnsName": "string",
      "FleetArn": "string",
      "FleetId": "string",
      "GameLiftAgentEndpoint": "string",
      "GameLiftServiceSdkEndpoint": "string",
      "GameServerContainerGroupDefinitionArn": "string",
      "InstanceId": "string",
      "IpAddress": "string",
      "Location": "string",
      "OperatingSystem": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_RegisterCompute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Compute](#API_RegisterCompute_ResponseSyntax) **   <a name="gameliftservers-RegisterCompute-response-Compute"></a>
The details of the compute resource you registered.
Type: [Compute](API_Compute.md) object

## Errors
<a name="API_RegisterCompute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
HTTP Status Code: 400

 ** NotReadyException **
 The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with [exponential backoffs and jitter](http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/).
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_RegisterCompute_Examples"></a>

### Register your laptop as a testing compute resource
<a name="API_RegisterCompute_Example_1"></a>

The following example registers a development laptop with the IP address of `10.1.2.3.4` to an Anywhere fleet with the fleet ID `fleet-1234`.

#### Sample Request
<a name="API_RegisterCompute_Example_1_Request"></a>

```
{
    "FleetId": "fleet-1234",
    "ComputeName": "DevLaptop",
    "IpAddress": "10.1.2.3",
    "Location": "custom-location1"
}
```

#### Sample Response
<a name="API_RegisterCompute_Example_1_Response"></a>

```
{
    FleetId = fleet-1234,
    ComputeName = DevLaptop,
    Status = ACTIVE,
    IpAddress = 10.1.2.3,
    GameLiftServiceSdkEndpoint = wss://12345678.execute-api.amazonaws.com/
}
```

## See Also
<a name="API_RegisterCompute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/RegisterCompute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/RegisterCompute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/RegisterCompute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/RegisterCompute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/RegisterCompute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/RegisterCompute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/RegisterCompute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/RegisterCompute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/RegisterCompute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/RegisterCompute)

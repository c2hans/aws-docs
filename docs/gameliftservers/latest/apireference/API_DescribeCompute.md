---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeCompute.html
---

# DescribeCompute
<a name="API_DescribeCompute"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves properties for a specific compute resource in an Amazon GameLift Servers fleet. You can list all computes in a fleet by calling [ListCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html).

 **Request options**

Provide the fleet ID and compute name. The compute name varies depending on the type of fleet.
+ For a compute in a managed EC2 fleet, provide an instance ID. Each instance in the fleet is a compute.
+ For a compute in a managed container fleet, provide a compute name. In a container fleet, each game server container group on a fleet instance is assigned a compute name.
+ For a compute in an Anywhere fleet, provide a registered compute name. Anywhere fleet computes are created when you register a hosting resource with the fleet.

 **Results**

If successful, this operation returns details for the requested compute resource. Depending on the fleet's compute type, the result includes the following information:
+ For a managed EC2 fleet, this operation returns information about the EC2 instance.
+ For a managed container fleet, this operation returns information about the container group and the instance it's running on.
+ For an Anywhere fleet, this operation returns information about the registered compute.

## Request Syntax
<a name="API_DescribeCompute_RequestSyntax"></a>

```
{
   "ComputeName": "{{string}}",
   "FleetId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCompute_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ComputeName](#API_DescribeCompute_RequestSyntax) **   <a name="gameliftservers-DescribeCompute-request-ComputeName"></a>
The unique identifier of the compute resource to retrieve properties for. For a managed container fleet or Anywhere fleet, use a compute name. For an EC2 fleet, use an instance ID. To retrieve a fleet's compute identifiers, call [ListCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html).
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?$|^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
Required: Yes

 ** [FleetId](#API_DescribeCompute_RequestSyntax) **   <a name="gameliftservers-DescribeCompute-request-FleetId"></a>
A unique identifier for the fleet that the compute belongs to. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

## Response Syntax
<a name="API_DescribeCompute_ResponseSyntax"></a>

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
<a name="API_DescribeCompute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Compute](#API_DescribeCompute_ResponseSyntax) **   <a name="gameliftservers-DescribeCompute-response-Compute"></a>
The set of properties for the requested compute resource.
Type: [Compute](API_Compute.md) object

## Errors
<a name="API_DescribeCompute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCompute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeCompute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeCompute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeCompute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeCompute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeCompute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeCompute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeCompute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeCompute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeCompute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeCompute)

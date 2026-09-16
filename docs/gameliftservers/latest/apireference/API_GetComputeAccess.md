---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetComputeAccess.html
---

# GetComputeAccess
<a name="API_GetComputeAccess"></a>

 **This API works with the following fleet types:** EC2, Container

Requests authorization to remotely connect to a hosting resource in a Amazon GameLift Servers managed fleet. This operation is not used with Amazon GameLift Servers Anywhere fleets.

 **Request options**

Provide the fleet ID and compute name. The compute name varies depending on the type of fleet.
+ For a compute in a managed EC2 fleet, provide an instance ID. Each instance in the fleet is a compute.
+ For a compute in a managed container fleet, provide a compute name. In a container fleet, each game server container group on a fleet instance is assigned a compute name.

 **Results**

If successful, this operation returns a set of temporary AWS credentials, including a two-part access key and a session token.
+ With a managed EC2 fleet (where compute type is `EC2`), use these credentials with Amazon EC2 Systems Manager (SSM) to start a session with the compute. For more details, see [ Starting a session (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html#sessions-start-cli) in the *Amazon EC2 Systems Manager User Guide*.
+ With a managed container fleet, use these credentials and the target value with SSM to connect to the fleet instance with the container group. When connected to the instance, use Docker commands to interact with the container using the container name and runtime ID.

## Request Syntax
<a name="API_GetComputeAccess_RequestSyntax"></a>

```
{
   "ComputeName": "{{string}}",
   "FleetId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetComputeAccess_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ComputeName](#API_GetComputeAccess_RequestSyntax) **   <a name="gameliftservers-GetComputeAccess-request-ComputeName"></a>
A unique identifier for the compute resource that you want to connect to. For an EC2 fleet, use an instance ID. For a managed container fleet, use a compute name. You can retrieve a fleet's compute names by calling [ListCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html).
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?$|^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
Required: Yes

 ** [FleetId](#API_GetComputeAccess_RequestSyntax) **   <a name="gameliftservers-GetComputeAccess-request-FleetId"></a>
A unique identifier for the fleet that holds the compute resource that you want to connect to. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

## Response Syntax
<a name="API_GetComputeAccess_ResponseSyntax"></a>

```
{
   "ComputeArn": "string",
   "ComputeName": "string",
   "ContainerIdentifiers": [
      {
         "ContainerName": "string",
         "ContainerRuntimeId": "string"
      }
   ],
   "Credentials": {
      "AccessKeyId": "string",
      "SecretAccessKey": "string",
      "SessionToken": "string"
   },
   "FleetArn": "string",
   "FleetId": "string",
   "Target": "string"
}
```

## Response Elements
<a name="API_GetComputeAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComputeArn](#API_GetComputeAccess_ResponseSyntax) **   <a name="gameliftservers-GetComputeAccess-response-ComputeArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to an Amazon GameLift Servers compute resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::compute/compute-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`

 ** [ComputeName](#API_GetComputeAccess_ResponseSyntax) **   <a name="gameliftservers-GetComputeAccess-response-ComputeName"></a>
The identifier of the compute resource to be accessed. This value might be either a compute name or an instance ID.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?$|^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`

 ** [ContainerIdentifiers](#API_GetComputeAccess_ResponseSyntax) **   <a name="gameliftservers-GetComputeAccess-response-ContainerIdentifiers"></a>
For a managed container fleet, a list of containers on the compute. Use the container runtime ID with Docker commands to connect to a specific container.
Type: Array of [ContainerIdentifier](API_ContainerIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [Credentials](#API_GetComputeAccess_ResponseSyntax) **   <a name="gameliftservers-GetComputeAccess-response-Credentials"></a>
A set of temporary AWS credentials for use when connecting to the compute resource with Amazon EC2 Systems Manager (SSM).
Type: [AwsCredentials](API_AwsCredentials.md) object

 ** [FleetArn](#API_GetComputeAccess_ResponseSyntax) **   <a name="gameliftservers-GetComputeAccess-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_GetComputeAccess_ResponseSyntax) **   <a name="gameliftservers-GetComputeAccess-response-FleetId"></a>
The ID of the fleet that holds the compute resource to be accessed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [Target](#API_GetComputeAccess_ResponseSyntax) **   <a name="gameliftservers-GetComputeAccess-response-Target"></a>
The instance ID where the compute resource is running.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.

## Errors
<a name="API_GetComputeAccess_Errors"></a>

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
<a name="API_GetComputeAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/GetComputeAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/GetComputeAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GetComputeAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/GetComputeAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GetComputeAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/GetComputeAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/GetComputeAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/GetComputeAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/GetComputeAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GetComputeAccess)

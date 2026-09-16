---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDevEndpoints.html
---

# GetDevEndpoints
<a name="API_GetDevEndpoints"></a>

Retrieves all the development endpoints in this AWS account.

**Note**
When you create a development endpoint in a virtual private cloud (VPC), AWS Glue returns only a private IP address and the public IP address field is not populated. When you create a non-VPC development endpoint, AWS Glue returns only a public IP address.

## Request Syntax
<a name="API_GetDevEndpoints_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDevEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetDevEndpoints_RequestSyntax) **   <a name="Glue-GetDevEndpoints-request-MaxResults"></a>
The maximum size of information to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_GetDevEndpoints_RequestSyntax) **   <a name="Glue-GetDevEndpoints-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_GetDevEndpoints_ResponseSyntax"></a>

```
{
   "DevEndpoints": [
      {
         "Arguments": {
            "string" : "string"
         },
         "AvailabilityZone": "string",
         "CreatedTimestamp": number,
         "EndpointName": "string",
         "ExtraJarsS3Path": "string",
         "ExtraPythonLibsS3Path": "string",
         "FailureReason": "string",
         "GlueVersion": "string",
         "LastModifiedTimestamp": number,
         "LastUpdateStatus": "string",
         "NumberOfNodes": number,
         "NumberOfWorkers": number,
         "PrivateAddress": "string",
         "PublicAddress": "string",
         "PublicKey": "string",
         "PublicKeys": [ "string" ],
         "RoleArn": "string",
         "SecurityConfiguration": "string",
         "SecurityGroupIds": [ "string" ],
         "Status": "string",
         "SubnetId": "string",
         "VpcId": "string",
         "WorkerType": "string",
         "YarnEndpointAddress": "string",
         "ZeppelinRemoteSparkInterpreterPort": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetDevEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DevEndpoints](#API_GetDevEndpoints_ResponseSyntax) **   <a name="Glue-GetDevEndpoints-response-DevEndpoints"></a>
A list of `DevEndpoint` definitions.
Type: Array of [DevEndpoint](API_DevEndpoint.md) objects

 ** [NextToken](#API_GetDevEndpoints_ResponseSyntax) **   <a name="Glue-GetDevEndpoints-response-NextToken"></a>
A continuation token, if not all `DevEndpoint` definitions have yet been returned.
Type: String

## Errors
<a name="API_GetDevEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetDevEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDevEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDevEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDevEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDevEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDevEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDevEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDevEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDevEndpoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDevEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDevEndpoints)

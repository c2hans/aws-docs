---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetDevEndpoints.html
---

# BatchGetDevEndpoints
<a name="API_BatchGetDevEndpoints"></a>

Returns a list of resource metadata for a given list of development endpoint names. After calling the `ListDevEndpoints` operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.

## Request Syntax
<a name="API_BatchGetDevEndpoints_RequestSyntax"></a>

```
{
   "DevEndpointNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetDevEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DevEndpointNames](#API_BatchGetDevEndpoints_RequestSyntax) **   <a name="Glue-BatchGetDevEndpoints-request-DevEndpointNames"></a>
The list of `DevEndpoint` names, which might be the names returned from the `ListDevEndpoint` operation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_BatchGetDevEndpoints_ResponseSyntax"></a>

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
   "DevEndpointsNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetDevEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DevEndpoints](#API_BatchGetDevEndpoints_ResponseSyntax) **   <a name="Glue-BatchGetDevEndpoints-response-DevEndpoints"></a>
A list of `DevEndpoint` definitions.
Type: Array of [DevEndpoint](API_DevEndpoint.md) objects

 ** [DevEndpointsNotFound](#API_BatchGetDevEndpoints_ResponseSyntax) **   <a name="Glue-BatchGetDevEndpoints-response-DevEndpointsNotFound"></a>
A list of `DevEndpoints` not found.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.

## Errors
<a name="API_BatchGetDevEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
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
<a name="API_BatchGetDevEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetDevEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetDevEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetDevEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetDevEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetDevEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetDevEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetDevEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetDevEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetDevEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetDevEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

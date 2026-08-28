---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateDevEndpoint.html
---

# CreateDevEndpoint
<a name="API_CreateDevEndpoint"></a>

Creates a new development endpoint.

## Request Syntax
<a name="API_CreateDevEndpoint_RequestSyntax"></a>

```
{
   "Arguments": {
      "{{string}}" : "{{string}}"
   },
   "EndpointName": "{{string}}",
   "ExtraJarsS3Path": "{{string}}",
   "ExtraPythonLibsS3Path": "{{string}}",
   "GlueVersion": "{{string}}",
   "NumberOfNodes": {{number}},
   "NumberOfWorkers": {{number}},
   "PublicKey": "{{string}}",
   "PublicKeys": [ "{{string}}" ],
   "RoleArn": "{{string}}",
   "SecurityConfiguration": "{{string}}",
   "SecurityGroupIds": [ "{{string}}" ],
   "SubnetId": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "WorkerType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateDevEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Arguments](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-Arguments"></a>
A map of arguments used to configure the `DevEndpoint`.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [EndpointName](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-EndpointName"></a>
The name to be assigned to the new `DevEndpoint`.
Type: String
Required: Yes

 ** [ExtraJarsS3Path](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-ExtraJarsS3Path"></a>
The path to one or more Java `.jar` files in an S3 bucket that should be loaded in your `DevEndpoint`.
Type: String
Required: No

 ** [ExtraPythonLibsS3Path](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-ExtraPythonLibsS3Path"></a>
The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your `DevEndpoint`. Multiple values must be complete paths separated by a comma.
You can only use pure Python libraries with a `DevEndpoint`. Libraries that rely on C extensions, such as the [pandas](http://pandas.pydata.org/) Python data analysis library, are not yet supported.
Type: String
Required: No

 ** [GlueVersion](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-GlueVersion"></a>
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.
Development endpoints that are created without specifying a Glue version default to Glue 0.9.
You can specify a version of Python support for development endpoints by using the `Arguments` parameter in the `CreateDevEndpoint` or `UpdateDevEndpoint` APIs. If no arguments are provided, the version defaults to Python 2.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** [NumberOfNodes](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-NumberOfNodes"></a>
The number of AWS Glue Data Processing Units (DPUs) to allocate to this `DevEndpoint`.
Type: Integer
Required: No

 ** [NumberOfWorkers](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-NumberOfWorkers"></a>
The number of workers of a defined `workerType` that are allocated to the development endpoint.
The maximum number of workers you can define are 299 for `G.1X`, and 149 for `G.2X`.
Type: Integer
Required: No

 ** [PublicKey](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-PublicKey"></a>
The public key to be used by this `DevEndpoint` for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.
Type: String
Required: No

 ** [PublicKeys](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-PublicKeys"></a>
A list of public keys to be used by the development endpoints for authentication. The use of this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.
If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the `UpdateDevEndpoint` API with the public key content in the `deletePublicKeys` attribute, and the list of new keys in the `addPublicKeys` attribute.
Type: Array of strings
Array Members: Maximum number of 5 items.
Required: No

 ** [RoleArn](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-RoleArn"></a>
The IAM role for the `DevEndpoint`.
Type: String
Pattern: `arn:aws:iam::\d{12}:role/.*`
Required: Yes

 ** [SecurityConfiguration](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-SecurityConfiguration"></a>
The name of the `SecurityConfiguration` structure to be used with this `DevEndpoint`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [SecurityGroupIds](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-SecurityGroupIds"></a>
Security group IDs for the security groups to be used by the new `DevEndpoint`.
Type: Array of strings
Required: No

 ** [SubnetId](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-SubnetId"></a>
The subnet ID for the new `DevEndpoint` to use.
Type: String
Required: No

 ** [Tags](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-Tags"></a>
The tags to use with this DevEndpoint. You may use tags to limit access to the DevEndpoint. For more information about tags in AWS Glue, see [AWS Tags in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html) in the developer guide.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [WorkerType](#API_CreateDevEndpoint_RequestSyntax) **   <a name="Glue-CreateDevEndpoint-request-WorkerType"></a>
The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X.
+ For the `Standard` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
+ For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
+ For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
Known issue: when a development endpoint is created with the `G.2X` `WorkerType` configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk.
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`
Required: No

## Response Syntax
<a name="API_CreateDevEndpoint_ResponseSyntax"></a>

```
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
   "NumberOfNodes": number,
   "NumberOfWorkers": number,
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
```

## Response Elements
<a name="API_CreateDevEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arguments](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-Arguments"></a>
The map of arguments used to configure this `DevEndpoint`.
Valid arguments are:
+  `"--enable-glue-datacatalog": ""`
You can specify a version of Python support for development endpoints by using the `Arguments` parameter in the `CreateDevEndpoint` or `UpdateDevEndpoint` APIs. If no arguments are provided, the version defaults to Python 2.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.

 ** [AvailabilityZone](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-AvailabilityZone"></a>
The AWS Availability Zone where this `DevEndpoint` is located.
Type: String

 ** [CreatedTimestamp](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-CreatedTimestamp"></a>
The point in time at which this `DevEndpoint` was created.
Type: Timestamp

 ** [EndpointName](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-EndpointName"></a>
The name assigned to the new `DevEndpoint`.
Type: String

 ** [ExtraJarsS3Path](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-ExtraJarsS3Path"></a>
Path to one or more Java `.jar` files in an S3 bucket that will be loaded in your `DevEndpoint`.
Type: String

 ** [ExtraPythonLibsS3Path](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-ExtraPythonLibsS3Path"></a>
The paths to one or more Python libraries in an S3 bucket that will be loaded in your `DevEndpoint`.
Type: String

 ** [FailureReason](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-FailureReason"></a>
The reason for a current failure in this `DevEndpoint`.
Type: String

 ** [GlueVersion](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-GlueVersion"></a>
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`

 ** [NumberOfNodes](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-NumberOfNodes"></a>
The number of AWS Glue Data Processing Units (DPUs) allocated to this DevEndpoint.
Type: Integer

 ** [NumberOfWorkers](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-NumberOfWorkers"></a>
The number of workers of a defined `workerType` that are allocated to the development endpoint.
Type: Integer

 ** [RoleArn](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the role assigned to the new `DevEndpoint`.
Type: String
Pattern: `arn:aws:iam::\d{12}:role/.*`

 ** [SecurityConfiguration](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-SecurityConfiguration"></a>
The name of the `SecurityConfiguration` structure being used with this `DevEndpoint`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [SecurityGroupIds](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-SecurityGroupIds"></a>
The security groups assigned to the new `DevEndpoint`.
Type: Array of strings

 ** [Status](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-Status"></a>
The current status of the new `DevEndpoint`.
Type: String

 ** [SubnetId](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-SubnetId"></a>
The subnet ID assigned to the new `DevEndpoint`.
Type: String

 ** [VpcId](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-VpcId"></a>
The ID of the virtual private cloud (VPC) used by this `DevEndpoint`.
Type: String

 ** [WorkerType](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-WorkerType"></a>
The type of predefined worker that is allocated to the development endpoint. May be a value of Standard, G.1X, or G.2X.
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`

 ** [YarnEndpointAddress](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-YarnEndpointAddress"></a>
The address of the YARN endpoint used by this `DevEndpoint`.
Type: String

 ** [ZeppelinRemoteSparkInterpreterPort](#API_CreateDevEndpoint_ResponseSyntax) **   <a name="Glue-CreateDevEndpoint-response-ZeppelinRemoteSparkInterpreterPort"></a>
The Apache Zeppelin port for the remote Apache Spark interpreter.
Type: Integer

## Errors
<a name="API_CreateDevEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
The same unique identifier was associated with two different records.
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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateDevEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateDevEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateDevEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateDevEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateDevEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateDevEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateDevEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateDevEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateDevEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateDevEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateDevEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

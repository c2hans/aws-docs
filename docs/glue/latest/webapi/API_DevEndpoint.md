---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DevEndpoint.html
---

# DevEndpoint
<a name="API_DevEndpoint"></a>

A development endpoint where a developer can remotely debug extract, transform, and load (ETL) scripts.

## Contents
<a name="API_DevEndpoint_Contents"></a>

 ** Arguments **   <a name="Glue-Type-DevEndpoint-Arguments"></a>
A map of arguments used to configure the `DevEndpoint`.
Valid arguments are:
+  `"--enable-glue-datacatalog": ""`
You can specify a version of Python support for development endpoints by using the `Arguments` parameter in the `CreateDevEndpoint` or `UpdateDevEndpoint` APIs. If no arguments are provided, the version defaults to Python 2.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** AvailabilityZone **   <a name="Glue-Type-DevEndpoint-AvailabilityZone"></a>
The AWS Availability Zone where this `DevEndpoint` is located.
Type: String
Required: No

 ** CreatedTimestamp **   <a name="Glue-Type-DevEndpoint-CreatedTimestamp"></a>
The point in time at which this DevEndpoint was created.
Type: Timestamp
Required: No

 ** EndpointName **   <a name="Glue-Type-DevEndpoint-EndpointName"></a>
The name of the `DevEndpoint`.
Type: String
Required: No

 ** ExtraJarsS3Path **   <a name="Glue-Type-DevEndpoint-ExtraJarsS3Path"></a>
The path to one or more Java `.jar` files in an S3 bucket that should be loaded in your `DevEndpoint`.
You can only use pure Java/Scala libraries with a `DevEndpoint`.
Type: String
Required: No

 ** ExtraPythonLibsS3Path **   <a name="Glue-Type-DevEndpoint-ExtraPythonLibsS3Path"></a>
The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your `DevEndpoint`. Multiple values must be complete paths separated by a comma.
You can only use pure Python libraries with a `DevEndpoint`. Libraries that rely on C extensions, such as the [pandas](http://pandas.pydata.org/) Python data analysis library, are not currently supported.
Type: String
Required: No

 ** FailureReason **   <a name="Glue-Type-DevEndpoint-FailureReason"></a>
The reason for a current failure in this `DevEndpoint`.
Type: String
Required: No

 ** GlueVersion **   <a name="Glue-Type-DevEndpoint-GlueVersion"></a>
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.
Development endpoints that are created without specifying a Glue version default to Glue 0.9.
You can specify a version of Python support for development endpoints by using the `Arguments` parameter in the `CreateDevEndpoint` or `UpdateDevEndpoint` APIs. If no arguments are provided, the version defaults to Python 2.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** LastModifiedTimestamp **   <a name="Glue-Type-DevEndpoint-LastModifiedTimestamp"></a>
The point in time at which this `DevEndpoint` was last modified.
Type: Timestamp
Required: No

 ** LastUpdateStatus **   <a name="Glue-Type-DevEndpoint-LastUpdateStatus"></a>
The status of the last update.
Type: String
Required: No

 ** NumberOfNodes **   <a name="Glue-Type-DevEndpoint-NumberOfNodes"></a>
The number of AWS Glue Data Processing Units (DPUs) allocated to this `DevEndpoint`.
Type: Integer
Required: No

 ** NumberOfWorkers **   <a name="Glue-Type-DevEndpoint-NumberOfWorkers"></a>
The number of workers of a defined `workerType` that are allocated to the development endpoint.
The maximum number of workers you can define are 299 for `G.1X`, and 149 for `G.2X`.
Type: Integer
Required: No

 ** PrivateAddress **   <a name="Glue-Type-DevEndpoint-PrivateAddress"></a>
A private IP address to access the `DevEndpoint` within a VPC if the `DevEndpoint` is created within one. The `PrivateAddress` field is present only when you create the `DevEndpoint` within your VPC.
Type: String
Required: No

 ** PublicAddress **   <a name="Glue-Type-DevEndpoint-PublicAddress"></a>
The public IP address used by this `DevEndpoint`. The `PublicAddress` field is present only when you create a non-virtual private cloud (VPC) `DevEndpoint`.
Type: String
Required: No

 ** PublicKey **   <a name="Glue-Type-DevEndpoint-PublicKey"></a>
The public key to be used by this `DevEndpoint` for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.
Type: String
Required: No

 ** PublicKeys **   <a name="Glue-Type-DevEndpoint-PublicKeys"></a>
A list of public keys to be used by the `DevEndpoints` for authentication. Using this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.
If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the `UpdateDevEndpoint` API operation with the public key content in the `deletePublicKeys` attribute, and the list of new keys in the `addPublicKeys` attribute.
Type: Array of strings
Array Members: Maximum number of 5 items.
Required: No

 ** RoleArn **   <a name="Glue-Type-DevEndpoint-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used in this `DevEndpoint`.
Type: String
Pattern: `arn:aws:iam::\d{12}:role/.*`
Required: No

 ** SecurityConfiguration **   <a name="Glue-Type-DevEndpoint-SecurityConfiguration"></a>
The name of the `SecurityConfiguration` structure to be used with this `DevEndpoint`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** SecurityGroupIds **   <a name="Glue-Type-DevEndpoint-SecurityGroupIds"></a>
A list of security group identifiers used in this `DevEndpoint`.
Type: Array of strings
Required: No

 ** Status **   <a name="Glue-Type-DevEndpoint-Status"></a>
The current status of this `DevEndpoint`.
Type: String
Required: No

 ** SubnetId **   <a name="Glue-Type-DevEndpoint-SubnetId"></a>
The subnet ID for this `DevEndpoint`.
Type: String
Required: No

 ** VpcId **   <a name="Glue-Type-DevEndpoint-VpcId"></a>
The ID of the virtual private cloud (VPC) used by this `DevEndpoint`.
Type: String
Required: No

 ** WorkerType **   <a name="Glue-Type-DevEndpoint-WorkerType"></a>
The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X.
+ For the `Standard` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
+ For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
+ For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
Known issue: when a development endpoint is created with the `G.2X` `WorkerType` configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk.
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`
Required: No

 ** YarnEndpointAddress **   <a name="Glue-Type-DevEndpoint-YarnEndpointAddress"></a>
The YARN endpoint address used by this `DevEndpoint`.
Type: String
Required: No

 ** ZeppelinRemoteSparkInterpreterPort **   <a name="Glue-Type-DevEndpoint-ZeppelinRemoteSparkInterpreterPort"></a>
The Apache Zeppelin port for the remote Apache Spark interpreter.
Type: Integer
Required: No

## See Also
<a name="API_DevEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DevEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DevEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DevEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateInstanceProfile.html
---

# CreateInstanceProfile
<a name="API_CreateInstanceProfile"></a>

Creates the instance profile using the specified parameters.

 **Required permissions:** `dms:CreateInstanceProfile`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_CreateInstanceProfile_RequestSyntax"></a>

```
{
   "AvailabilityZone": "{{string}}",
   "Description": "{{string}}",
   "InstanceProfileName": "{{string}}",
   "KmsKeyArn": "{{string}}",
   "NetworkType": "{{string}}",
   "PubliclyAccessible": {{boolean}},
   "SubnetGroupIdentifier": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcSecurityGroups": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreateInstanceProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZone](#API_CreateInstanceProfile_RequestSyntax) **   <a name="DMS-CreateInstanceProfile-request-AvailabilityZone"></a>
The Availability Zone where the instance profile will be created. The default value is a random, system-chosen Availability Zone in the AWS Region where your data provider is created, for examplem `us-east-1d`.
Type: String
Required: No

 ** [Description](#API_CreateInstanceProfile_RequestSyntax) **   <a name="DMS-CreateInstanceProfile-request-Description"></a>
A user-friendly description of the instance profile.
Type: String
Required: No

 ** [InstanceProfileName](#API_CreateInstanceProfile_RequestSyntax) **   <a name="DMS-CreateInstanceProfile-request-InstanceProfileName"></a>
A user-friendly name for the instance profile.
Type: String
Required: No

 ** [KmsKeyArn](#API_CreateInstanceProfile_RequestSyntax) **   <a name="DMS-CreateInstanceProfile-request-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key that is used to encrypt the connection parameters for the instance profile.
If you don't specify a value for the `KmsKeyArn` parameter, then AWS DMS uses an AWS owned encryption key to encrypt your resources.
Type: String
Required: No

 ** [NetworkType](#API_CreateInstanceProfile_RequestSyntax) **   <a name="DMS-CreateInstanceProfile-request-NetworkType"></a>
Specifies the network type for the instance profile. A value of `IPV4` represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of `IPV6` represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of `DUAL` represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.
Type: String
Required: No

 ** [PubliclyAccessible](#API_CreateInstanceProfile_RequestSyntax) **   <a name="DMS-CreateInstanceProfile-request-PubliclyAccessible"></a>
Specifies the accessibility options for the instance profile. A value of `true` represents an instance profile with a public IP address. A value of `false` represents an instance profile with a private IP address. The default value is `true`.
Type: Boolean
Required: No

 ** [SubnetGroupIdentifier](#API_CreateInstanceProfile_RequestSyntax) **   <a name="DMS-CreateInstanceProfile-request-SubnetGroupIdentifier"></a>
A subnet group to associate with the instance profile.
Type: String
Required: No

 ** [Tags](#API_CreateInstanceProfile_RequestSyntax) **   <a name="DMS-CreateInstanceProfile-request-Tags"></a>
One or more tags to be assigned to the instance profile.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [VpcSecurityGroups](#API_CreateInstanceProfile_RequestSyntax) **   <a name="DMS-CreateInstanceProfile-request-VpcSecurityGroups"></a>
Specifies the VPC security group names to be used with the instance profile. The VPC security group must work with the VPC containing the instance profile.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_CreateInstanceProfile_ResponseSyntax"></a>

```
{
   "InstanceProfile": {
      "AvailabilityZone": "string",
      "Description": "string",
      "InstanceProfileArn": "string",
      "InstanceProfileCreationTime": "string",
      "InstanceProfileName": "string",
      "KmsKeyArn": "string",
      "NetworkType": "string",
      "PubliclyAccessible": boolean,
      "SubnetGroupIdentifier": "string",
      "VpcSecurityGroups": [ "string" ]
   }
}
```

## Response Elements
<a name="API_CreateInstanceProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceProfile](#API_CreateInstanceProfile_ResponseSyntax) **   <a name="DMS-CreateInstanceProfile-response-InstanceProfile"></a>
The instance profile that was created.
Type: [InstanceProfile](API_InstanceProfile.md) object

## Errors
<a name="API_CreateInstanceProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** FailedDependencyFault **
A dependency threw an exception.
HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **
 AWS DMS cannot access the KMS key.
 ** message **

HTTP Status Code: 400

 ** ResourceAlreadyExistsFault **
The resource you are attempting to create already exists.
 ** message **

 ** resourceArn **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

 ** S3AccessDeniedFault **
Insufficient privileges are preventing access to an Amazon S3 object.
HTTP Status Code: 400

 ** S3ResourceNotFoundFault **
A specified Amazon S3 bucket, bucket folder, or other object can't be found.
HTTP Status Code: 400

## Examples
<a name="API_CreateInstanceProfile_Examples"></a>

### Create an instance profile
<a name="API_CreateInstanceProfile_Example_1"></a>

The following example creates an instance profile.

#### Sample Request
<a name="API_CreateInstanceProfile_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.CreateInstanceProfile
{
    "InstanceProfileName": "example-instance-profile",
    "Description": "Example instance profile for documentation",
    "SubnetGroupIdentifier": "example-replication-subnet-group",
    "VpcSecurityGroups": ["sg-0123456789abcdef0"],
    "KmsKeyArn": "arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "NetworkType": "IPV4",
    "PubliclyAccessible": false
}
```

#### Sample Response
<a name="API_CreateInstanceProfile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "InstanceProfile": {
        "InstanceProfileArn": "arn:aws:dms:us-east-1:111122223333:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "KmsKeyArn": "arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "PubliclyAccessible": false,
        "NetworkType": "IPV4",
        "InstanceProfileName": "example-instance-profile",
        "Description": "Example instance profile for documentation",
        "InstanceProfileCreationTime": "2026-01-09T12:30:00.000000Z",
        "SubnetGroupIdentifier": "example-replication-subnet-group",
        "VpcSecurityGroups": [
            "sg-0123456789abcdef0"
        ]
    }
}
```

## See Also
<a name="API_CreateInstanceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/CreateInstanceProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/CreateInstanceProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CreateInstanceProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/CreateInstanceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CreateInstanceProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/CreateInstanceProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/CreateInstanceProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/CreateInstanceProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/CreateInstanceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CreateInstanceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

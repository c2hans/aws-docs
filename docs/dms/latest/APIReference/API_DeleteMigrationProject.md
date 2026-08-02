---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteMigrationProject.html
---

# DeleteMigrationProject
<a name="API_DeleteMigrationProject"></a>

Deletes the specified migration project.

 **Required permissions:** `dms:DeleteMigrationProject`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

**Note**
The migration project must be closed before you can delete it.

## Request Syntax
<a name="API_DeleteMigrationProject_RequestSyntax"></a>

```
{
   "MigrationProjectIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteMigrationProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MigrationProjectIdentifier](#API_DeleteMigrationProject_RequestSyntax) **   <a name="DMS-DeleteMigrationProject-request-MigrationProjectIdentifier"></a>
The name or Amazon Resource Name (ARN) of the migration project to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteMigrationProject_ResponseSyntax"></a>

```
{
   "MigrationProject": {
      "Description": "string",
      "InstanceProfileArn": "string",
      "InstanceProfileName": "string",
      "MigrationProjectArn": "string",
      "MigrationProjectCreationTime": "string",
      "MigrationProjectName": "string",
      "SchemaConversionApplicationAttributes": {
         "S3BucketPath": "string",
         "S3BucketRoleArn": "string"
      },
      "SourceDataProviderDescriptors": [
         {
            "DataProviderArn": "string",
            "DataProviderName": "string",
            "SecretsManagerAccessRoleArn": "string",
            "SecretsManagerSecretId": "string"
         }
      ],
      "TargetDataProviderDescriptors": [
         {
            "DataProviderArn": "string",
            "DataProviderName": "string",
            "SecretsManagerAccessRoleArn": "string",
            "SecretsManagerSecretId": "string"
         }
      ],
      "TransformationRules": "string"
   }
}
```

## Response Elements
<a name="API_DeleteMigrationProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MigrationProject](#API_DeleteMigrationProject_ResponseSyntax) **   <a name="DMS-DeleteMigrationProject-response-MigrationProject"></a>
The migration project that was deleted.
Type: [MigrationProject](API_MigrationProject.md) object

## Errors
<a name="API_DeleteMigrationProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

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

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DeleteMigrationProject_Examples"></a>

### Delete a migration project
<a name="API_DeleteMigrationProject_Example_1"></a>

The following example deletes a migration project identified by its ARN.

#### Sample Request
<a name="API_DeleteMigrationProject_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.DeleteMigrationProject
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
}
```

#### Sample Response
<a name="API_DeleteMigrationProject_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "MigrationProject": {
        "MigrationProjectName": "example-migration-project",
        "MigrationProjectArn": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "MigrationProjectCreationTime": "2026-01-09T12:30:00.000000Z",
        "SourceDataProviderDescriptors": [
            {
                "SecretsManagerSecretId": "arn:aws:secretsmanager:us-east-1:111122223333:secret:example-source-secret-A1B2C3",
                "SecretsManagerAccessRoleArn": "arn:aws:iam::111122223333:role/example-secrets-manager-role",
                "DataProviderName": "example-data-provider",
                "DataProviderArn": "arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        ],
        "TargetDataProviderDescriptors": [
            {
                "SecretsManagerSecretId": "arn:aws:secretsmanager:us-east-1:111122223333:secret:example-target-secret-A1B2C3",
                "SecretsManagerAccessRoleArn": "arn:aws:iam::111122223333:role/example-secrets-manager-role",
                "DataProviderName": "example-data-provider",
                "DataProviderArn": "arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        ],
        "InstanceProfileArn": "arn:aws:dms:us-east-1:111122223333:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "InstanceProfileName": "example-instance-profile",
        "TransformationRules": "{\"rules\":[{\"rule-type\":\"transformation\",\"rule-id\":\"1\",\"rule-name\":\"1\",\"rule-target\":\"schema\",\"rule-action\":\"rename\",\"object-locator\":{\"schema-name\":\"ExampleSchema\"},\"value\":\"TargetSchema\"}]}",
        "Description": "Example migration project for documentation",
        "SchemaConversionApplicationAttributes": {
            "S3BucketPath": "s3://amzn-s3-demo-bucket",
            "S3BucketRoleArn": "arn:aws:iam::111122223333:role/example-s3-access-role"
        }
    }
}
```

## See Also
<a name="API_DeleteMigrationProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DeleteMigrationProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DeleteMigrationProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DeleteMigrationProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DeleteMigrationProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DeleteMigrationProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DeleteMigrationProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DeleteMigrationProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DeleteMigrationProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DeleteMigrationProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DeleteMigrationProject)

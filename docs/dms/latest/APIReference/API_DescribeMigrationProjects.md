---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMigrationProjects.html
---

# DescribeMigrationProjects
<a name="API_DescribeMigrationProjects"></a>

Returns a paginated list of migration projects for your account in the current region.

 **Required permissions:** `dms:ListMigrationProjects`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_DescribeMigrationProjects_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeMigrationProjects_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeMigrationProjects_RequestSyntax) **   <a name="DMS-DescribeMigrationProjects-request-Filters"></a>
The filters to apply to the migration projects.
The following filter names are supported:
+  `migration-project-identifier` – The migration project name or ARN.
+  `instance-profile-identifier` – The instance profile name or ARN.
+  `data-provider-identifier` – The source or target data provider name or ARN.
+  `source-data-provider-identifier` – The source data provider name or ARN.
+  `target-data-provider-identifier` – The target data provider name or ARN.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeMigrationProjects_RequestSyntax) **   <a name="DMS-DescribeMigrationProjects-request-Marker"></a>
Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
If `Marker` is returned by a previous response, there are more results available. The value of `Marker` is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeMigrationProjects_RequestSyntax) **   <a name="DMS-DescribeMigrationProjects-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, AWS DMS includes a pagination token in the response so that you can retrieve the remaining results.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeMigrationProjects_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "MigrationProjects": [
      {
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
   ]
}
```

## Response Elements
<a name="API_DescribeMigrationProjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeMigrationProjects_ResponseSyntax) **   <a name="DMS-DescribeMigrationProjects-response-Marker"></a>
Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
If `Marker` is returned by a previous response, there are more results available. The value of `Marker` is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.
Type: String

 ** [MigrationProjects](#API_DescribeMigrationProjects_ResponseSyntax) **   <a name="DMS-DescribeMigrationProjects-response-MigrationProjects"></a>
A description of migration projects.
Type: Array of [MigrationProject](API_MigrationProject.md) objects

## Errors
<a name="API_DescribeMigrationProjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** FailedDependencyFault **
A dependency threw an exception.
HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeMigrationProjects_Examples"></a>

### Describe migration projects with a filter
<a name="API_DescribeMigrationProjects_Example_1"></a>

The following example retrieves the details of a migration project identified by its ARN.

#### Sample Request
<a name="API_DescribeMigrationProjects_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.DescribeMigrationProjects
{
    "Filters": [
        {
            "Name": "migration-project-identifier",
            "Values": [
                "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_DescribeMigrationProjects_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "MigrationProjects": [
        {
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
    ]
}
```

## See Also
<a name="API_DescribeMigrationProjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeMigrationProjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeMigrationProjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeMigrationProjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeMigrationProjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeMigrationProjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeMigrationProjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeMigrationProjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeMigrationProjects)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeMigrationProjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeMigrationProjects)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

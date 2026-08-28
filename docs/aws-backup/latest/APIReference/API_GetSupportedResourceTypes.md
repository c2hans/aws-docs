---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetSupportedResourceTypes.html
---

# GetSupportedResourceTypes
<a name="API_GetSupportedResourceTypes"></a>

Returns the AWS resource types supported by AWS Backup.

## Request Syntax
<a name="API_GetSupportedResourceTypes_RequestSyntax"></a>

```
GET /supported-resource-types HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSupportedResourceTypes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetSupportedResourceTypes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSupportedResourceTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ResourceTypes": [ "string" ]
}
```

## Response Elements
<a name="API_GetSupportedResourceTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceTypes](#API_GetSupportedResourceTypes_ResponseSyntax) **   <a name="Backup-GetSupportedResourceTypes-response-ResourceTypes"></a>
Contains a string with the supported AWS resource types:
+  `Aurora` for Amazon Aurora
+  `CloudFormation` for AWS CloudFormation
+  `DocumentDB` for Amazon DocumentDB (with MongoDB compatibility)
+  `DynamoDB` for Amazon DynamoDB
+  `EBS` for Amazon Elastic Block Store
+  `EC2` for Amazon Elastic Compute Cloud
+  `EFS` for Amazon Elastic File System
+  `EKS` for Amazon Elastic Kubernetes Service
+  `FSx` for Amazon FSx
+  `Neptune` for Amazon Neptune
+  `RDS` for Amazon Relational Database Service
+  `Redshift` for Amazon Redshift
+  `S3` for Amazon Simple Storage Service (Amazon S3)
+  `SAP HANA on Amazon EC2` for SAP HANA databases on Amazon Elastic Compute Cloud instances
+  `Storage Gateway` for AWS Storage Gateway
+  `Timestream` for Amazon Timestream
+  `VirtualMachine` for VMware virtual machines
Type: Array of strings
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

## Errors
<a name="API_GetSupportedResourceTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_GetSupportedResourceTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/GetSupportedResourceTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/GetSupportedResourceTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/GetSupportedResourceTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/GetSupportedResourceTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/GetSupportedResourceTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/GetSupportedResourceTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/GetSupportedResourceTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/GetSupportedResourceTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/GetSupportedResourceTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/GetSupportedResourceTypes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

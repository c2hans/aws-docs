---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateFleetAdvisorCollector.html
---

# CreateFleetAdvisorCollector
<a name="API_CreateFleetAdvisorCollector"></a>

**Important**
 End of support notice: On May 20, 2026, AWS will end support for AWS DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor; console or AWS DMS Fleet Advisor; resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

Creates a Fleet Advisor collector using the specified parameters.

## Request Syntax
<a name="API_CreateFleetAdvisorCollector_RequestSyntax"></a>

```
{
   "CollectorName": "{{string}}",
   "Description": "{{string}}",
   "S3BucketName": "{{string}}",
   "ServiceAccessRoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateFleetAdvisorCollector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CollectorName](#API_CreateFleetAdvisorCollector_RequestSyntax) **   <a name="DMS-CreateFleetAdvisorCollector-request-CollectorName"></a>
The name of your Fleet Advisor collector (for example, `sample-collector`).
Type: String
Required: Yes

 ** [Description](#API_CreateFleetAdvisorCollector_RequestSyntax) **   <a name="DMS-CreateFleetAdvisorCollector-request-Description"></a>
A summary description of your Fleet Advisor collector.
Type: String
Required: No

 ** [S3BucketName](#API_CreateFleetAdvisorCollector_RequestSyntax) **   <a name="DMS-CreateFleetAdvisorCollector-request-S3BucketName"></a>
The Amazon S3 bucket that the Fleet Advisor collector uses to store inventory metadata.
Type: String
Required: Yes

 ** [ServiceAccessRoleArn](#API_CreateFleetAdvisorCollector_RequestSyntax) **   <a name="DMS-CreateFleetAdvisorCollector-request-ServiceAccessRoleArn"></a>
The IAM role that grants permissions to access the specified Amazon S3 bucket.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateFleetAdvisorCollector_ResponseSyntax"></a>

```
{
   "CollectorName": "string",
   "CollectorReferencedId": "string",
   "Description": "string",
   "S3BucketName": "string",
   "ServiceAccessRoleArn": "string"
}
```

## Response Elements
<a name="API_CreateFleetAdvisorCollector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CollectorName](#API_CreateFleetAdvisorCollector_ResponseSyntax) **   <a name="DMS-CreateFleetAdvisorCollector-response-CollectorName"></a>
The name of the new Fleet Advisor collector.
Type: String

 ** [CollectorReferencedId](#API_CreateFleetAdvisorCollector_ResponseSyntax) **   <a name="DMS-CreateFleetAdvisorCollector-response-CollectorReferencedId"></a>
The unique ID of the new Fleet Advisor collector, for example: `22fda70c-40d5-4acf-b233-a495bd8eb7f5`
Type: String

 ** [Description](#API_CreateFleetAdvisorCollector_ResponseSyntax) **   <a name="DMS-CreateFleetAdvisorCollector-response-Description"></a>
A summary description of the Fleet Advisor collector.
Type: String

 ** [S3BucketName](#API_CreateFleetAdvisorCollector_ResponseSyntax) **   <a name="DMS-CreateFleetAdvisorCollector-response-S3BucketName"></a>
The Amazon S3 bucket that the collector uses to store inventory metadata.
Type: String

 ** [ServiceAccessRoleArn](#API_CreateFleetAdvisorCollector_ResponseSyntax) **   <a name="DMS-CreateFleetAdvisorCollector-response-ServiceAccessRoleArn"></a>
The IAM role that grants permissions to access the specified Amazon S3 bucket.
Type: String

## Errors
<a name="API_CreateFleetAdvisorCollector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
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

## See Also
<a name="API_CreateFleetAdvisorCollector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/CreateFleetAdvisorCollector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/CreateFleetAdvisorCollector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CreateFleetAdvisorCollector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/CreateFleetAdvisorCollector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CreateFleetAdvisorCollector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/CreateFleetAdvisorCollector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/CreateFleetAdvisorCollector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/CreateFleetAdvisorCollector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/CreateFleetAdvisorCollector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CreateFleetAdvisorCollector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

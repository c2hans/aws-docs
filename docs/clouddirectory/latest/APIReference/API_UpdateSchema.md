---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_UpdateSchema.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# UpdateSchema
<a name="API_UpdateSchema"></a>

Updates the schema name with a new name. Only development schema names can be updated.

## Request Syntax
<a name="API_UpdateSchema_RequestSyntax"></a>

```
PUT /amazonclouddirectory/2017-01-11/schema/update HTTP/1.1
x-amz-data-partition: {{SchemaArn}}
Content-type: application/json

{
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSchema_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SchemaArn](#API_UpdateSchema_RequestSyntax) **   <a name="amazoncds-UpdateSchema-request-SchemaArn"></a>
The Amazon Resource Name (ARN) of the development schema. For more information, see [Arn Examples](arns.md).
Required: Yes

## Request Body
<a name="API_UpdateSchema_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateSchema_RequestSyntax) **   <a name="amazoncds-UpdateSchema-request-Name"></a>
The name of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

## Response Syntax
<a name="API_UpdateSchema_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SchemaArn": "string"
}
```

## Response Elements
<a name="API_UpdateSchema_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SchemaArn](#API_UpdateSchema_ResponseSyntax) **   <a name="amazoncds-UpdateSchema-response-SchemaArn"></a>
The ARN that is associated with the updated schema. For more information, see [Arn Examples](arns.md).
Type: String

## Errors
<a name="API_UpdateSchema_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md) and check your permissions.
HTTP Status Code: 403

 ** InternalServiceException **
Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/) site to see if there are any operational issues with the service.
HTTP Status Code: 500

 ** InvalidArnException **
Indicates that the provided ARN value is not valid.
HTTP Status Code: 400

 ** LimitExceededException **
Indicates that limits are exceeded. See [Limits](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/limits.html) for more information.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource could not be found.
HTTP Status Code: 404

 ** RetryableConflictException **
Occurs when a conflict with a previous successful write is detected. For example, if a write operation occurs on an object and then an attempt is made to read the object using “SERIALIZABLE” consistency, this exception may result. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 409

 ** SchemaAlreadyExistsException **
Indicates that a schema could not be created due to a naming conflict. Please select a different name and then try again.
HTTP Status Code: 400

 ** ValidationException **
Indicates that your request is malformed in some manner. See the exception message.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/UpdateSchema)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/clouddirectory-2017-01-11/UpdateSchema)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/UpdateSchema)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/UpdateSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/UpdateSchema)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/UpdateSchema)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/UpdateSchema)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/UpdateSchema)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/UpdateSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/UpdateSchema)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

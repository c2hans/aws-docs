---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateViewVersion.html
---

# CreateViewVersion
<a name="API_CreateViewVersion"></a>

Publishes a new version of the view identifier.

Versions are immutable and monotonically increasing.

It returns the highest version if there is no change in content compared to that version. An error is displayed if the supplied ViewContentSha256 is different from the ViewContentSha256 of the `$LATEST` alias.

## Request Syntax
<a name="API_CreateViewVersion_RequestSyntax"></a>

```
PUT /views/{{InstanceId}}/{{ViewId}}/versions HTTP/1.1
Content-type: application/json

{
   "VersionDescription": "{{string}}",
   "ViewContentSha256": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateViewVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateViewVersion_RequestSyntax) **   <a name="connect-CreateViewVersion-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9\_\-:\/]+$`
Required: Yes

 ** [ViewId](#API_CreateViewVersion_RequestSyntax) **   <a name="connect-CreateViewVersion-request-uri-ViewId"></a>
The identifier of the view. Both `ViewArn` and `ViewId` can be used.
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `^[a-zA-Z0-9\_\-:\/$]+$`
Required: Yes

## Request Body
<a name="API_CreateViewVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [VersionDescription](#API_CreateViewVersion_RequestSyntax) **   <a name="connect-CreateViewVersion-request-VersionDescription"></a>
The description for the version being published.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@,()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@,()']*)$`
Required: No

 ** [ViewContentSha256](#API_CreateViewVersion_RequestSyntax) **   <a name="connect-CreateViewVersion-request-ViewContentSha256"></a>
Indicates the checksum value of the latest published view content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]$`
Required: No

## Response Syntax
<a name="API_CreateViewVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "View": {
      "Arn": "string",
      "Content": {
         "Actions": [ "string" ],
         "InputSchema": "string",
         "Template": "string"
      },
      "CreatedTime": number,
      "Description": "string",
      "Id": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "Status": "string",
      "Tags": {
         "string" : "string"
      },
      "Type": "string",
      "Version": number,
      "VersionDescription": "string",
      "ViewContentSha256": "string"
   }
}
```

## Response Elements
<a name="API_CreateViewVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [View](#API_CreateViewVersion_ResponseSyntax) **   <a name="connect-CreateViewVersion-response-View"></a>
All view data is contained within the View object.
Type: [View](API_View.md) object

## Errors
<a name="API_CreateViewVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceInUseException **
That resource is already in use (for example, you're trying to add a record with the same name as an existing record). If you are trying to delete a resource (for example, DeleteHoursOfOperation or DeletePredefinedAttribute), remove its reference from related resources and then try again.
 ** ResourceId **
The identifier for the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** TooManyRequestsException **
Displayed when rate-related API limits are exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateViewVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateViewVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateViewVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateViewVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateViewVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateViewVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateViewVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateViewVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateViewVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateViewVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateViewVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

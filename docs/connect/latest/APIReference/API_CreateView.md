---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateView.html
---

# CreateView
<a name="API_CreateView"></a>

Creates a new view with the possible status of `SAVED` or `PUBLISHED`.

The views will have a unique name for each connect instance.

It performs basic content validation if the status is `SAVED` or full content validation if the status is set to `PUBLISHED`. An error is returned if validation fails. It associates either the `$SAVED` qualifier or both of the `$SAVED` and `$LATEST` qualifiers with the provided view content based on the status. The view is idempotent if ClientToken is provided.

## Request Syntax
<a name="API_CreateView_RequestSyntax"></a>

```
PUT /views/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Content": {
      "Actions": [ "{{string}}" ],
      "Template": "{{string}}"
   },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Status": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateView_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateView_RequestSyntax) **   <a name="connect-CreateView-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9\_\-:\/]+$`
Required: Yes

## Request Body
<a name="API_CreateView_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateView_RequestSyntax) **   <a name="connect-CreateView-request-ClientToken"></a>
A unique Id for each create view request to avoid duplicate view creation. For example, the view is idempotent ClientToken is provided.
Type: String
Length Constraints: Maximum length of 500.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Required: No

 ** [Content](#API_CreateView_RequestSyntax) **   <a name="connect-CreateView-request-Content"></a>
View content containing all content necessary to render a view except for runtime input data.
The total uncompressed content has a maximum file size of 400kB.
Type: [ViewInputContent](API_ViewInputContent.md) object
Required: Yes

 ** [Description](#API_CreateView_RequestSyntax) **   <a name="connect-CreateView-request-Description"></a>
The description of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@,()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@,()']*)$`
Required: No

 ** [Name](#API_CreateView_RequestSyntax) **   <a name="connect-CreateView-request-Name"></a>
The name of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@()']*)$`
Required: Yes

 ** [Status](#API_CreateView_RequestSyntax) **   <a name="connect-CreateView-request-Status"></a>
Indicates the view status as either `SAVED` or `PUBLISHED`. The `PUBLISHED` status will initiate validation on the content.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: Yes

 ** [Tags](#API_CreateView_RequestSyntax) **   <a name="connect-CreateView-request-Tags"></a>
The tags associated with the view resource (not specific to view version).These tags can be used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateView_ResponseSyntax"></a>

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
<a name="API_CreateView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [View](#API_CreateView_ResponseSyntax) **   <a name="connect-CreateView-response-View"></a>
A view resource object. Contains metadata and content necessary to render the view.
Type: [View](API_View.md) object

## Errors
<a name="API_CreateView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

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
<a name="API_CreateView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateView)

---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetTagSyncTask.html
---

# GetTagSyncTask
<a name="API_GetTagSyncTask"></a>

Returns information about a specified tag-sync task.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:GetTagSyncTask` on the application group

## Request Syntax
<a name="API_GetTagSyncTask_RequestSyntax"></a>

```
POST /get-tag-sync-task HTTP/1.1
Content-type: application/json

{
   "TaskArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetTagSyncTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTagSyncTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TaskArn](#API_GetTagSyncTask_RequestSyntax) **   <a name="ARG-GetTagSyncTask-request-TaskArn"></a>
The Amazon resource name (ARN) of the tag-sync task.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}/tag-sync-task/[a-z0-9]{26}`
Required: Yes

## Response Syntax
<a name="API_GetTagSyncTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "ErrorMessage": "string",
   "GroupArn": "string",
   "GroupName": "string",
   "ResourceQuery": {
      "Query": "string",
      "Type": "string"
   },
   "RoleArn": "string",
   "Status": "string",
   "TagKey": "string",
   "TagValue": "string",
   "TaskArn": "string"
}
```

## Response Elements
<a name="API_GetTagSyncTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_GetTagSyncTask_ResponseSyntax) **   <a name="ARG-GetTagSyncTask-response-CreatedAt"></a>
The timestamp of when the tag-sync task was created.
Type: Timestamp

 ** [ErrorMessage](#API_GetTagSyncTask_ResponseSyntax) **   <a name="ARG-GetTagSyncTask-response-ErrorMessage"></a>
The specific error message in cases where the tag-sync task status is `ERROR`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [GroupArn](#API_GetTagSyncTask_ResponseSyntax) **   <a name="ARG-GetTagSyncTask-response-GroupArn"></a>
The Amazon resource name (ARN) of the application group.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`

 ** [GroupName](#API_GetTagSyncTask_ResponseSyntax) **   <a name="ARG-GetTagSyncTask-response-GroupName"></a>
The name of the application group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}`

 ** [ResourceQuery](#API_GetTagSyncTask_ResponseSyntax) **   <a name="ARG-GetTagSyncTask-response-ResourceQuery"></a>
The query you can use to define a resource group or a search for resources. A `ResourceQuery` specifies both a query `Type` and a `Query` string as JSON string objects. See the examples section for example JSON strings. For more information about creating a resource group with a resource query, see [Build queries and groups in AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html) in the * AWS Resource Groups User Guide*
When you combine all of the elements together into a single string, any double quotes that are embedded inside another double quote pair must be escaped by preceding the embedded double quote with a backslash character (\\). For example, a complete `ResourceQuery` parameter must be formatted like the following CLI parameter example:
 `--resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'`
In the preceding example, all of the double quote characters in the value part of the `Query` element must be escaped because the value itself is surrounded by double quotes. For more information, see [Quoting strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the * AWS Command Line Interface User Guide*.
For the complete list of resource types that you can use in the array value for `ResourceTypeFilters`, see [Resources you can use with AWS Resource Groups and Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the * AWS Resource Groups User Guide*. For example:
 `"ResourceTypeFilters":["AWS::S3::Bucket", "AWS::EC2::Instance"]`
Type: [ResourceQuery](API_ResourceQuery.md) object

 ** [RoleArn](#API_GetTagSyncTask_ResponseSyntax) **   <a name="ARG-GetTagSyncTask-response-RoleArn"></a>
The Amazon resource name (ARN) of the role assumed by Resource Groups to tag and untag resources on your behalf.
For more information about this role, review [Tag-sync required permissions](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html#tag-sync-role).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [Status](#API_GetTagSyncTask_ResponseSyntax) **   <a name="ARG-GetTagSyncTask-response-Status"></a>
The status of the tag-sync task.
Valid values include:
+  `ACTIVE` - The tag-sync task is actively managing resources in the application by adding or removing the `awsApplication` tag from resources when they are tagged or untagged with the specified tag key-value pair.
+  `ERROR` - The tag-sync task is not actively managing resources in the application. Review the `ErrorMessage` for more information about resolving the error.
Type: String
Valid Values: `ACTIVE | ERROR`

 ** [TagKey](#API_GetTagSyncTask_ResponseSyntax) **   <a name="ARG-GetTagSyncTask-response-TagKey"></a>
The tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

 ** [TagValue](#API_GetTagSyncTask_ResponseSyntax) **   <a name="ARG-GetTagSyncTask-response-TagValue"></a>
The tag value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

 ** [TaskArn](#API_GetTagSyncTask_ResponseSyntax) **   <a name="ARG-GetTagSyncTask-response-TaskArn"></a>
The Amazon resource name (ARN) of the tag-sync task.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}/tag-sync-task/[a-z0-9]{26}`

## Errors
<a name="API_GetTagSyncTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The request includes one or more parameters that violate validation rules.
HTTP Status Code: 400

 ** ForbiddenException **
The caller isn't authorized to make the request. Check permissions.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal error occurred while processing the request. Try again later.
HTTP Status Code: 500

 ** MethodNotAllowedException **
The request uses an HTTP method that isn't allowed for the specified resource.
HTTP Status Code: 405

 ** NotFoundException **
One or more of the specified resources don't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
You've exceeded throttling limits by making too many requests in a period of time.
HTTP Status Code: 429

 ** UnauthorizedException **
The request was rejected because it doesn't have valid credentials for the target resource.
HTTP Status Code: 401

## See Also
<a name="API_GetTagSyncTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/GetTagSyncTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/GetTagSyncTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/GetTagSyncTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/GetTagSyncTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/GetTagSyncTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/GetTagSyncTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/GetTagSyncTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/GetTagSyncTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/GetTagSyncTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/GetTagSyncTask)

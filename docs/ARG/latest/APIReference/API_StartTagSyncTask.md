---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_StartTagSyncTask.html
---

# StartTagSyncTask
<a name="API_StartTagSyncTask"></a>

Creates a new tag-sync task to onboard and sync resources tagged with a specific tag key-value pair to an application. To start a tag-sync task, you need a [resource tagging role](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html#tag-sync-role). The resource tagging role grants permissions to tag and untag applications resources and must include a trust policy that allows Resource Groups to assume the role and perform resource tagging tasks on your behalf.

For instructions on creating a tag-sync task, see [Create a tag-sync using the Resource Groups API](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html#create-tag-sync) in the * AWS Service Catalog AppRegistry Administrator Guide*.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:StartTagSyncTask` on the application group
+  `resource-groups:CreateGroup`
+  `iam:PassRole` on the role provided in the request

## Request Syntax
<a name="API_StartTagSyncTask_RequestSyntax"></a>

```
POST /start-tag-sync-task HTTP/1.1
Content-type: application/json

{
   "Group": "{{string}}",
   "ResourceQuery": {
      "Query": "{{string}}",
      "Type": "{{string}}"
   },
   "RoleArn": "{{string}}",
   "TagKey": "{{string}}",
   "TagValue": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartTagSyncTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartTagSyncTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Group](#API_StartTagSyncTask_RequestSyntax) **   <a name="ARG-StartTagSyncTask-request-Group"></a>
The Amazon resource name (ARN) or name of the application group for which you want to create a tag-sync task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}|arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: Yes

 ** [RoleArn](#API_StartTagSyncTask_RequestSyntax) **   <a name="ARG-StartTagSyncTask-request-RoleArn"></a>
The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [ResourceQuery](#API_StartTagSyncTask_RequestSyntax) **   <a name="ARG-StartTagSyncTask-request-ResourceQuery"></a>
The query you can use to create the tag-sync task. With this method, all resources matching the query are added to the specified application group. A `ResourceQuery` specifies both a query `Type` and a `Query` string as JSON string objects. For more information on defining a resource query for a tag-sync task, see the tag-based query type in [ Types of resource group queries](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#getting_started-query_types) in * AWS Resource Groups User Guide*.
When using the `ResourceQuery` parameter, you cannot use the `TagKey` and `TagValue` parameters.
When you combine all of the elements together into a single string, any double quotes that are embedded inside another double quote pair must be escaped by preceding the embedded double quote with a backslash character (\\). For example, a complete `ResourceQuery` parameter must be formatted like the following CLI parameter example:
 `--resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'`
In the preceding example, all of the double quote characters in the value part of the `Query` element must be escaped because the value itself is surrounded by double quotes. For more information, see [Quoting strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the * AWS Command Line Interface User Guide*.
For the complete list of resource types that you can use in the array value for `ResourceTypeFilters`, see [Resources you can use with AWS Resource Groups and Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the * AWS Resource Groups User Guide*. For example:
 `"ResourceTypeFilters":["AWS::S3::Bucket", "AWS::EC2::Instance"]`
Type: [ResourceQuery](API_ResourceQuery.md) object
Required: No

 ** [TagKey](#API_StartTagSyncTask_RequestSyntax) **   <a name="ARG-StartTagSyncTask-request-TagKey"></a>
The tag key. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application.
When using the `TagKey` parameter, you must also specify the `TagValue` parameter. If you specify a tag key-value pair, you can't use the `ResourceQuery` parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [TagValue](#API_StartTagSyncTask_RequestSyntax) **   <a name="ARG-StartTagSyncTask-request-TagValue"></a>
The tag value. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application.
When using the `TagValue` parameter, you must also specify the `TagKey` parameter. If you specify a tag key-value pair, you can't use the `ResourceQuery` parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_StartTagSyncTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "GroupArn": "string",
   "GroupName": "string",
   "ResourceQuery": {
      "Query": "string",
      "Type": "string"
   },
   "RoleArn": "string",
   "TagKey": "string",
   "TagValue": "string",
   "TaskArn": "string"
}
```

## Response Elements
<a name="API_StartTagSyncTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GroupArn](#API_StartTagSyncTask_ResponseSyntax) **   <a name="ARG-StartTagSyncTask-response-GroupArn"></a>
The Amazon resource name (ARN) of the application group for which you want to add or remove resources.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`

 ** [GroupName](#API_StartTagSyncTask_ResponseSyntax) **   <a name="ARG-StartTagSyncTask-response-GroupName"></a>
The name of the application group to onboard and sync resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}`

 ** [ResourceQuery](#API_StartTagSyncTask_ResponseSyntax) **   <a name="ARG-StartTagSyncTask-response-ResourceQuery"></a>
The query you can use to define a resource group or a search for resources. A `ResourceQuery` specifies both a query `Type` and a `Query` string as JSON string objects. See the examples section for example JSON strings. For more information about creating a resource group with a resource query, see [Build queries and groups in AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html) in the * AWS Resource Groups User Guide*
When you combine all of the elements together into a single string, any double quotes that are embedded inside another double quote pair must be escaped by preceding the embedded double quote with a backslash character (\\). For example, a complete `ResourceQuery` parameter must be formatted like the following CLI parameter example:
 `--resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'`
In the preceding example, all of the double quote characters in the value part of the `Query` element must be escaped because the value itself is surrounded by double quotes. For more information, see [Quoting strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the * AWS Command Line Interface User Guide*.
For the complete list of resource types that you can use in the array value for `ResourceTypeFilters`, see [Resources you can use with AWS Resource Groups and Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the * AWS Resource Groups User Guide*. For example:
 `"ResourceTypeFilters":["AWS::S3::Bucket", "AWS::EC2::Instance"]`
Type: [ResourceQuery](API_ResourceQuery.md) object

 ** [RoleArn](#API_StartTagSyncTask_ResponseSyntax) **   <a name="ARG-StartTagSyncTask-response-RoleArn"></a>
The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [TagKey](#API_StartTagSyncTask_ResponseSyntax) **   <a name="ARG-StartTagSyncTask-response-TagKey"></a>
The tag key of the tag-sync task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

 ** [TagValue](#API_StartTagSyncTask_ResponseSyntax) **   <a name="ARG-StartTagSyncTask-response-TagValue"></a>
The tag value of the tag-sync task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

 ** [TaskArn](#API_StartTagSyncTask_ResponseSyntax) **   <a name="ARG-StartTagSyncTask-response-TaskArn"></a>
The Amazon resource name (ARN) of the new tag-sync task.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}/tag-sync-task/[a-z0-9]{26}`

## Errors
<a name="API_StartTagSyncTask_Errors"></a>

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
<a name="API_StartTagSyncTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/StartTagSyncTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/StartTagSyncTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/StartTagSyncTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/StartTagSyncTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/StartTagSyncTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/StartTagSyncTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/StartTagSyncTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/StartTagSyncTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/StartTagSyncTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/StartTagSyncTask)

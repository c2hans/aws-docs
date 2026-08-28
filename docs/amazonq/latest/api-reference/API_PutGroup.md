---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutGroup.html
---

# PutGroup
<a name="API_PutGroup"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Create, or updates, a mapping of users—who have access to a document—to groups.

You can also map sub groups to groups. For example, the group "Company Intellectual Property Teams" includes sub groups "Research" and "Engineering". These sub groups include their own list of users or people who work in these teams. Only users who work in research and engineering, and therefore belong in the intellectual property group, can see top-secret company documents in their Amazon Q Business chat results.

There are two options for creating groups, either passing group members inline or using an S3 file via the S3PathForGroupMembers field. For inline groups, there is a limit of 1000 members per group and for provided S3 files there is a limit of 100 thousand members. When creating a group using an S3 file, you provide both an S3 file and a `RoleArn` for Amazon Q Buisness to access the file.

## Request Syntax
<a name="API_PutGroup_RequestSyntax"></a>

```
PUT /applications/{{applicationId}}/indices/{{indexId}}/groups HTTP/1.1
Content-type: application/json

{
   "dataSourceId": "{{string}}",
   "groupMembers": {
      "memberGroups": [
         {
            "groupName": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "memberUsers": [
         {
            "type": "{{string}}",
            "userId": "{{string}}"
         }
      ],
      "s3PathForGroupMembers": {
         "bucket": "{{string}}",
         "key": "{{string}}"
      }
   },
   "groupName": "{{string}}",
   "roleArn": "{{string}}",
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_PutGroup_RequestSyntax) **   <a name="qbusiness-PutGroup-request-uri-applicationId"></a>
The identifier of the application in which the user and group mapping belongs.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [indexId](#API_PutGroup_RequestSyntax) **   <a name="qbusiness-PutGroup-request-uri-indexId"></a>
The identifier of the index in which you want to map users to their groups.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_PutGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataSourceId](#API_PutGroup_RequestSyntax) **   <a name="qbusiness-PutGroup-request-dataSourceId"></a>
The identifier of the data source for which you want to map users to their groups. This is useful if a group is tied to multiple data sources, but you only want the group to access documents of a certain data source. For example, the groups "Research", "Engineering", and "Sales and Marketing" are all tied to the company's documents stored in the data sources Confluence and Salesforce. However, "Sales and Marketing" team only needs access to customer-related documents stored in Salesforce.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** [groupMembers](#API_PutGroup_RequestSyntax) **   <a name="qbusiness-PutGroup-request-groupMembers"></a>
A list of users or sub groups that belong to a group. This is for generating Amazon Q Business chat results only from document a user has access to.
Type: [GroupMembers](API_GroupMembers.md) object
Required: Yes

 ** [groupName](#API_PutGroup_RequestSyntax) **   <a name="qbusiness-PutGroup-request-groupName"></a>
The list that contains your users or sub groups that belong the same group. For example, the group "Company" includes the user "CEO" and the sub groups "Research", "Engineering", and "Sales and Marketing".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`
Required: Yes

 ** [roleArn](#API_PutGroup_RequestSyntax) **   <a name="qbusiness-PutGroup-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has access to the S3 file that contains your list of users that belong to a group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** [type](#API_PutGroup_RequestSyntax) **   <a name="qbusiness-PutGroup-request-type"></a>
The type of the group.
Type: String
Valid Values: `INDEX | DATASOURCE`
Required: Yes

## Response Syntax
<a name="API_PutGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** ConflictException **
You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.
 ** message **
The message describing a `ConflictException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded the set limits for your Amazon Q Business service.
 ** message **
The message describing a `ServiceQuotaExceededException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## Examples
<a name="API_PutGroup_Examples"></a>

### PutGroup S3 File
<a name="API_PutGroup_Example_1"></a>

The following is an example of an S3 file for declaring a group.

```
{
   "members": [
       {
           "id": "group1",
           "type": "GROUP",
           "dataSourceId": "group-data-source-id"
       },
       {
           "id": "group2",
           "type": "GROUP"
       },
       {
           "id": "user1",
           "type": "USER",
           "dataSourceId": "group-data-source-id"
       },
       {
           "id": "user2",
           "type": "USER",
           "dataSourceId": "group-data-source-id"
       }
   ]
}
```

## See Also
<a name="API_PutGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/PutGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/PutGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/PutGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/PutGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/PutGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/PutGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/PutGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/PutGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/PutGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/PutGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

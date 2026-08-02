---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateGroup.html
---

# CreateGroup
<a name="API_CreateGroup"></a>

Creates a group which you can use to associate canaries with each other, including cross-Region canaries. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group.

Groups are global resources. When you create a group, it is replicated across AWS Regions, and you can view it and add canaries to it from any Region. Although the group ARN format reflects the Region name where it was created, a group is not constrained to any Region. This means that you can put canaries from multiple Regions into the same group, and then use that group to view and manage all of those canaries in a single view.

Groups are supported in all Regions except the Regions that are disabled by default. For more information about these Regions, see [Enabling a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable).

Each group can contain as many as 10 canaries. You can have as many as 20 groups in your account. Any single canary can be a member of up to 10 groups.

## Request Syntax
<a name="API_CreateGroup_RequestSyntax"></a>

```
POST /group HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateGroup_RequestSyntax) **   <a name="synthetics-CreateGroup-request-Name"></a>
The name for the group. It can include any Unicode characters.
The names for all groups in your account, across all Regions, must be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Tags](#API_CreateGroup_RequestSyntax) **   <a name="synthetics-CreateGroup-request-Tags"></a>
A list of key-value pairs to associate with the group. You can associate as many as 50 tags with a group.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Group": {
      "Arn": "string",
      "CreatedTime": number,
      "Id": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Group](#API_CreateGroup_ResponseSyntax) **   <a name="synthetics-CreateGroup-response-Group"></a>
A structure that contains information about the group that was just created.
Type: [Group](API_Group.md) object

## Errors
<a name="API_CreateGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A conflicting operation is already in progress.
HTTP Status Code: 409

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request exceeded a service quota value.
HTTP Status Code: 402

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_CreateGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/CreateGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/CreateGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CreateGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/CreateGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CreateGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/CreateGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/CreateGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/CreateGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/CreateGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CreateGroup)

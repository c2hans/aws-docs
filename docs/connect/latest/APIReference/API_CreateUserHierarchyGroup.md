---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateUserHierarchyGroup.html
---

# CreateUserHierarchyGroup
<a name="API_CreateUserHierarchyGroup"></a>

Creates a new user hierarchy group.

## Request Syntax
<a name="API_CreateUserHierarchyGroup_RequestSyntax"></a>

```
PUT /user-hierarchy-groups/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "ParentGroupId": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateUserHierarchyGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateUserHierarchyGroup_RequestSyntax) **   <a name="connect-CreateUserHierarchyGroup-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateUserHierarchyGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateUserHierarchyGroup_RequestSyntax) **   <a name="connect-CreateUserHierarchyGroup-request-Name"></a>
The name of the user hierarchy group. Must not be more than 100 characters.
Type: String
Required: Yes

 ** [ParentGroupId](#API_CreateUserHierarchyGroup_RequestSyntax) **   <a name="connect-CreateUserHierarchyGroup-request-ParentGroupId"></a>
The identifier for the parent hierarchy group. The user hierarchy is created at level one if the parent group ID is null.
Type: String
Required: No

 ** [Tags](#API_CreateUserHierarchyGroup_RequestSyntax) **   <a name="connect-CreateUserHierarchyGroup-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateUserHierarchyGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HierarchyGroupArn": "string",
   "HierarchyGroupId": "string"
}
```

## Response Elements
<a name="API_CreateUserHierarchyGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HierarchyGroupArn](#API_CreateUserHierarchyGroup_ResponseSyntax) **   <a name="connect-CreateUserHierarchyGroup-response-HierarchyGroupArn"></a>
The Amazon Resource Name (ARN) of the hierarchy group.
Type: String

 ** [HierarchyGroupId](#API_CreateUserHierarchyGroup_ResponseSyntax) **   <a name="connect-CreateUserHierarchyGroup-response-HierarchyGroupId"></a>
The identifier of the hierarchy group.
Type: String

## Errors
<a name="API_CreateUserHierarchyGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateUserHierarchyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateUserHierarchyGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateUserHierarchyGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateUserHierarchyGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateUserHierarchyGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateUserHierarchyGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateUserHierarchyGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateUserHierarchyGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateUserHierarchyGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateUserHierarchyGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateUserHierarchyGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

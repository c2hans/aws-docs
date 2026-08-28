---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_UpdateGroup.html
---

# UpdateGroup
<a name="API_UpdateGroup"></a>

Updates the description for an existing group. You cannot update the name of a resource group.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:UpdateGroup`

## Request Syntax
<a name="API_UpdateGroup_RequestSyntax"></a>

```
POST /update-group HTTP/1.1
Content-type: application/json

{
   "Criticality": {{number}},
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "Group": "{{string}}",
   "GroupName": "{{string}}",
   "Owner": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Criticality](#API_UpdateGroup_RequestSyntax) **   <a name="ARG-UpdateGroup-request-Criticality"></a>
The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [Description](#API_UpdateGroup_RequestSyntax) **   <a name="ARG-UpdateGroup-request-Description"></a>
The new description that you want to update the resource group with. Descriptions can contain letters, numbers, hyphens, underscores, periods, and spaces.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\sa-zA-Z0-9_\.-]*`
Required: No

 ** [DisplayName](#API_UpdateGroup_RequestSyntax) **   <a name="ARG-UpdateGroup-request-DisplayName"></a>
The name of the application group, which you can change at any time.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [Group](#API_UpdateGroup_RequestSyntax) **   <a name="ARG-UpdateGroup-request-Group"></a>
The name or the ARN of the resource group to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}|arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: No

 ** [GroupName](#API_UpdateGroup_RequestSyntax) **   <a name="ARG-UpdateGroup-request-GroupName"></a>
 *This parameter has been deprecated.*
Don't use this parameter. Use `Group` instead.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}`
Required: No

 ** [Owner](#API_UpdateGroup_RequestSyntax) **   <a name="ARG-UpdateGroup-request-Owner"></a>
A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_UpdateGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Group": {
      "ApplicationTag": {
         "string" : "string"
      },
      "Criticality": number,
      "Description": "string",
      "DisplayName": "string",
      "GroupArn": "string",
      "Name": "string",
      "Owner": "string"
   }
}
```

## Response Elements
<a name="API_UpdateGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Group](#API_UpdateGroup_ResponseSyntax) **   <a name="ARG-UpdateGroup-response-Group"></a>
The update description of the resource group.
Type: [Group](API_Group.md) object

## Errors
<a name="API_UpdateGroup_Errors"></a>

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

## Examples
<a name="API_UpdateGroup_Examples"></a>

### Example
<a name="API_UpdateGroup_Example_1"></a>

The following example adds or updates the description attached to the specified resource group.

#### Sample Request
<a name="API_UpdateGroup_Example_1_Request"></a>

```
POST /update-group HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.update-group
X-Amz-Date: 20220120T224252Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 51

{
    "Group": "MyTest",
    "Description": "My Test group"
}
```

#### Sample Response
<a name="API_UpdateGroup_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 20 Jan 2022 22:42:52 GMT
Content-Type: application/json
Content-Length: 155
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "Group":{
        "GroupArn":"arn:aws:resource-groups:us-west-2:123456789012:group/MyTest",
        "Name":"MyTest",
        "Description":"My Test group",
        "OwnerId":"123456789012"
    }
}
```

## See Also
<a name="API_UpdateGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/UpdateGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/UpdateGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/UpdateGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/UpdateGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/UpdateGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/UpdateGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/UpdateGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/UpdateGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/UpdateGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/UpdateGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

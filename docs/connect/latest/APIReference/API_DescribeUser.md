---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html
---

# DescribeUser
<a name="API_DescribeUser"></a>

Describes the specified user. You can [find the instance ID in the Connect Customer console](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) (it’s the final part of the ARN). The console does not display the user IDs. Instead, list the users and note the IDs provided in the output.

## Request Syntax
<a name="API_DescribeUser_RequestSyntax"></a>

```
GET /users/{{InstanceId}}/{{UserId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeUser_RequestSyntax) **   <a name="connect-DescribeUser-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UserId](#API_DescribeUser_RequestSyntax) **   <a name="connect-DescribeUser-request-uri-UserId"></a>
The identifier of the user account.
Required: Yes

## Request Body
<a name="API_DescribeUser_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeUser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "User": {
      "AfterContactWorkConfigs": [
         {
            "AfterContactWorkConfig": {
               "AfterContactWorkTimeLimit": number
            },
            "AgentFirstCallbackAfterContactWorkConfig": {
               "AfterContactWorkTimeLimit": number
            },
            "Channel": "string"
         }
      ],
      "Arn": "string",
      "AutoAcceptConfigs": [
         {
            "AgentFirstCallbackAutoAccept": boolean,
            "AutoAccept": boolean,
            "Channel": "string"
         }
      ],
      "DirectoryUserId": "string",
      "HierarchyGroupId": "string",
      "Id": "string",
      "IdentityInfo": {
         "Email": "string",
         "FirstName": "string",
         "LastName": "string",
         "Mobile": "string",
         "SecondaryEmail": "string"
      },
      "LastModifiedRegion": "string",
      "LastModifiedTime": number,
      "PersistentConnectionConfigs": [
         {
            "Channel": "string",
            "PersistentConnection": boolean
         }
      ],
      "PhoneConfig": {
         "AfterContactWorkTimeLimit": number,
         "AutoAccept": boolean,
         "DeskPhoneNumber": "string",
         "PersistentConnection": boolean,
         "PhoneType": "string"
      },
      "PhoneNumberConfigs": [
         {
            "Channel": "string",
            "PhoneNumber": "string",
            "PhoneType": "string"
         }
      ],
      "RoutingProfileId": "string",
      "SecurityProfileIds": [ "string" ],
      "Tags": {
         "string" : "string"
      },
      "Username": "string",
      "VoiceEnhancementConfigs": [
         {
            "Channel": "string",
            "VoiceEnhancementMode": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [User](#API_DescribeUser_ResponseSyntax) **   <a name="connect-DescribeUser-response-User"></a>
Information about the user account and configuration settings.
Type: [User](API_User.md) object

## Errors
<a name="API_DescribeUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeUser)

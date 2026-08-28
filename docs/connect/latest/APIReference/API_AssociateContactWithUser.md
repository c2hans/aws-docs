---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateContactWithUser.html
---

# AssociateContactWithUser
<a name="API_AssociateContactWithUser"></a>

Associates a queued contact with an agent.

 **Use cases**

Following are common uses cases for this API:
+ Programmatically assign queued contacts to available users.
+ Leverage the IAM context key `connect:PreferredUserArn` to restrict contact association to specific preferred user.

 **Important things to know**
+ Use this API with chat, email, task, and voice contacts. For voice callbacks, this API does not support customer-first mode.
+ This API can be used to offer a contact to an agent even if the agent is currently at maximum concurrency for the channel.
+ Use it to associate contacts with users regardless of their current state, including custom states. Ensure your application logic accounts for user availability before making associations.
+ It honors the IAM context key `connect:PreferredUserArn` to prevent unauthorized contact associations.
+ It respects the IAM context key `connect:PreferredUserArn` to enforce authorization controls and prevent unauthorized contact associations. Verify that your IAM policies are properly configured to support your intended use cases.
+ The service quota *Queues per routing profile per instance* applies to manually assigned queues, too. For more information about this quota, see [Connect Customer quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#connect-quotas) in the *Connect Customer Administrator Guide*.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_AssociateContactWithUser_RequestSyntax"></a>

```
POST /contacts/{{InstanceId}}/{{ContactId}}/associate-user HTTP/1.1
Content-type: application/json

{
   "UserId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateContactWithUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_AssociateContactWithUser_RequestSyntax) **   <a name="connect-AssociateContactWithUser-request-uri-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_AssociateContactWithUser_RequestSyntax) **   <a name="connect-AssociateContactWithUser-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_AssociateContactWithUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [UserId](#API_AssociateContactWithUser_RequestSyntax) **   <a name="connect-AssociateContactWithUser-request-UserId"></a>
The identifier for the user. This can be the ID or the ARN of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_AssociateContactWithUser_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateContactWithUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateContactWithUser_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_AssociateContactWithUser_Examples"></a>

### Example request to associate a queued contact with a user
<a name="API_AssociateContactWithUser_Example_1"></a>

Following is an example of associating a queued contact with a user.

```
POST https://connect.us-west-2.amazonaws.com/contacts/{InstanceId}/{ContactId}/associate-user HTTP/1.1
Content-type: application/json

{
     "UserId": "string"
}
```

### Example response if the association succeeds
<a name="API_AssociateContactWithUser_Example_2"></a>

If the association succeeds an HTTP 200 OK response is returned.

```
HTTP/1.1 200
```

## See Also
<a name="API_AssociateContactWithUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateContactWithUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateContactWithUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateContactWithUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateContactWithUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateContactWithUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateContactWithUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateContactWithUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateContactWithUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateContactWithUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateContactWithUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPermission.html
---

# PutPermission
<a name="API_PutPermission"></a>

Running `PutPermission` permits the specified AWS account or AWS organization to put events to the specified *event bus*. Amazon EventBridge rules in your account are triggered by these events arriving to an event bus in your account.

For another account to send events to your account, that external account must have an EventBridge rule with your account's event bus as a target.

To enable multiple AWS accounts to put events to your event bus, run `PutPermission` once for each of these accounts. Or, if all the accounts are members of the same AWS organization, you can run `PutPermission` once specifying `Principal` as "\*" and specifying the AWS organization ID in `Condition`, to grant permissions to all accounts in that organization.

If you grant permissions using an organization, then accounts in that organization must specify a `RoleArn` with proper permissions when they use `PutTarget` to add your account's event bus as a target. For more information, see [Sending and Receiving Events Between AWS Accounts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html) in the *Amazon EventBridge User Guide*.

The permission policy on the event bus cannot exceed 10 KB in size.

## Request Syntax
<a name="API_PutPermission_RequestSyntax"></a>

```
{
   "Action": "{{string}}",
   "Condition": {
      "Key": "{{string}}",
      "Type": "{{string}}",
      "Value": "{{string}}"
   },
   "EventBusName": "{{string}}",
   "Policy": "{{string}}",
   "Principal": "{{string}}",
   "StatementId": "{{string}}"
}
```

## Request Parameters
<a name="API_PutPermission_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Action](#API_PutPermission_RequestSyntax) **   <a name="eventbridge-PutPermission-request-Action"></a>
The action that you are enabling the other account to perform.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `events:[a-zA-Z]+`
Required: No

 ** [Condition](#API_PutPermission_RequestSyntax) **   <a name="eventbridge-PutPermission-request-Condition"></a>
This parameter enables you to limit the permission to accounts that fulfill a certain condition, such as being a member of a certain AWS organization. For more information about AWS Organizations, see [What Is AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) in the * AWS Organizations User Guide*.
If you specify `Condition` with an AWS organization ID, and specify "\*" as the value for `Principal`, you grant permission to all the accounts in the named organization.
The `Condition` is a JSON string which must contain `Type`, `Key`, and `Value` fields.
Type: [Condition](API_Condition.md) object
Required: No

 ** [EventBusName](#API_PutPermission_RequestSyntax) **   <a name="eventbridge-PutPermission-request-EventBusName"></a>
The name of the event bus associated with the rule. If you omit this, the default event bus is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [Policy](#API_PutPermission_RequestSyntax) **   <a name="eventbridge-PutPermission-request-Policy"></a>
A JSON string that describes the permission policy statement. You can include a `Policy` parameter in the request instead of using the `StatementId`, `Action`, `Principal`, or `Condition` parameters.
Type: String
Required: No

 ** [Principal](#API_PutPermission_RequestSyntax) **   <a name="eventbridge-PutPermission-request-Principal"></a>
The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify "\*" to permit any account to put events to your default event bus.
If you specify "\*" without specifying `Condition`, avoid creating rules that may match undesirable events. To create more secure rules, make sure that the event pattern for each rule contains an `account` field with a specific account ID from which to receive events. Rules with an account field do not match any events sent from other accounts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `(\d{12}|\*)`
Required: No

 ** [StatementId](#API_PutPermission_RequestSyntax) **   <a name="eventbridge-PutPermission-request-StatementId"></a>
An identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this `StatementId` when you run [RemovePermission](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemovePermission.html).
Each `StatementId` must be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

## Response Elements
<a name="API_PutPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutPermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** OperationDisabledException **
The operation you are attempting is not available in this region.
HTTP Status Code: 400

 ** PolicyLengthExceededException **
The event bus policy is too long. For more information, see the limits.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## Examples
<a name="API_PutPermission_Examples"></a>

The following example enables the current account to receive events from account `111122223333`.

### Example
<a name="API_PutPermission_Example_1"></a>

This example illustrates one usage of PutPermission.

#### Sample Request
<a name="API_PutPermission_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutPermission

{
   "Action":"events:PutEvents"
   "Principal":"111122223333"
   "StatementId":"MyStatement"

}
```

### Example
<a name="API_PutPermission_Example_2"></a>

The following example grants permissions to all accounts in the organization with an ID of `o-1234567890`

#### Sample Request
<a name="API_PutPermission_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutPermission

{
   "Action":"events:PutEvents"
   "Principal":"*"
   "Condition": '{"Type" : "StringEquals", "Key": "aws:PrincipalOrgID", "Value": "o-1234567890"}'
   "StatementId":"MyStatement"

}
```

## See Also
<a name="API_PutPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/PutPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/PutPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/PutPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/PutPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/PutPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/PutPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/PutPermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/PutPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/PutPermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

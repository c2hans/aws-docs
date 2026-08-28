---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Assigns one or more tags (key-value pairs) to the specified EventBridge resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In EventBridge, rules and event buses can be tagged.

Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

You can use the `TagResource` action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.

You can associate as many as 50 tags with a resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_TagResource_RequestSyntax) **   <a name="eventbridge-TagResource-request-ResourceARN"></a>
The ARN of the EventBridge resource that you're adding tags to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: Yes

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="eventbridge-TagResource-request-Tags"></a>
The list of key-value pairs to associate with the resource.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ManagedRuleException **
This rule was created by an AWS service on behalf of your account. It is managed by that service. If you see this error in response to `DeleteRule` or `RemoveTargets`, you can use the `Force` parameter in those calls to delete the rule or remove targets from the rule. You cannot modify these managed rules by using `DisableRule`, `EnableRule`, `PutTargets`, `PutRule`, `TagResource`, or `UntagResource`.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## Examples
<a name="API_TagResource_Examples"></a>

### Adds two tags to a EventBridge rule
<a name="API_TagResource_Example_1"></a>

The following is an example of a `TagResource` request.

#### Sample Request
<a name="API_TagResource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.TagResource

{
    "ResourceARN": "arn:aws:events:us-west-1:123456789012:rule/test",
    "Tags": [
        {
            "Key": "Stack",
            "Value": "Prod"
        },
        {
            "Key": "Team",
            "Value": "Green"
        }
    ]
}
```

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/TagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

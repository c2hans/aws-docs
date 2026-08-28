---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RemoveTagsFromOnPremisesInstances.html
---

# RemoveTagsFromOnPremisesInstances
<a name="API_RemoveTagsFromOnPremisesInstances"></a>

Removes one or more tags from one or more on-premises instances.

## Request Syntax
<a name="API_RemoveTagsFromOnPremisesInstances_RequestSyntax"></a>

```
{
   "instanceNames": [ "{{string}}" ],
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_RemoveTagsFromOnPremisesInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [instanceNames](#API_RemoveTagsFromOnPremisesInstances_RequestSyntax) **   <a name="CodeDeploy-RemoveTagsFromOnPremisesInstances-request-instanceNames"></a>
The names of the on-premises instances from which to remove tags.
Type: Array of strings
Required: Yes

 ** [tags](#API_RemoveTagsFromOnPremisesInstances_RequestSyntax) **   <a name="CodeDeploy-RemoveTagsFromOnPremisesInstances-request-tags"></a>
The tag key-value pairs to remove from the on-premises instances.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

## Response Elements
<a name="API_RemoveTagsFromOnPremisesInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveTagsFromOnPremisesInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InstanceLimitExceededException **
The maximum number of allowed on-premises instances in a single call was exceeded.
HTTP Status Code: 400

 ** InstanceNameRequiredException **
An on-premises instance name was not specified.
HTTP Status Code: 400

 ** InstanceNotRegisteredException **
The specified on-premises instance is not registered.
HTTP Status Code: 400

 ** InvalidInstanceNameException **
The on-premises instance name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidTagException **
The tag was specified in an invalid format.
HTTP Status Code: 400

 ** TagLimitExceededException **
The maximum allowed number of tags was exceeded.
HTTP Status Code: 400

 ** TagRequiredException **
A tag was not specified.
HTTP Status Code: 400

## Examples
<a name="API_RemoveTagsFromOnPremisesInstances_Examples"></a>

### Example
<a name="API_RemoveTagsFromOnPremisesInstances_Example_1"></a>

This example illustrates one usage of RemoveTagsFromOnPremisesInstances.

#### Sample Request
<a name="API_RemoveTagsFromOnPremisesInstances_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: CodeDeploy_20141006.RemoveTagsFromOnPremisesInstances
X-Amz-Date: 20160707T025157Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "instanceNames": [
        "i-b2f7jf0d00EXAMPLE",
        "i-u3d8xa3m00EXAMPLE"
    ],
    "tags": [
        {
            "Key": "Name",
            "Value": "Project-765"
        }
    ]
}
```

#### Sample Response
<a name="API_RemoveTagsFromOnPremisesInstances_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 4ccc9cf0-88c9-11e5-8ce3-2704437d0309
Content-Type: application/x-amz-json-1.1
Content-Length: 0
```

## See Also
<a name="API_RemoveTagsFromOnPremisesInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

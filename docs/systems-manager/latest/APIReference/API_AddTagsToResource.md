---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AddTagsToResource.html
---

# AddTagsToResource
<a name="API_AddTagsToResource"></a>

Adds or overwrites one or more tags for the specified resource. *Tags* are metadata that you can assign to your automations, documents, managed nodes, maintenance windows, Parameter Store parameters, and patch baselines. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. For example, you could define a set of tags for your account's managed nodes that helps you track each node's owner and stack level. For example:
+  `Key=Owner,Value=DbAdmin`
+  `Key=Owner,Value=SysAdmin`
+  `Key=Owner,Value=Dev`
+  `Key=Stack,Value=Production`
+  `Key=Stack,Value=Pre-Production`
+  `Key=Stack,Value=Test`

Most resources can have a maximum of 50 tags. Automations can have a maximum of 5 tags.

We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add. Tags don't have any semantic meaning to and are interpreted strictly as a string of characters.

For more information about using tags with Amazon Elastic Compute Cloud (Amazon EC2) instances, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

## Request Syntax
<a name="API_AddTagsToResource_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_AddTagsToResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceId](#API_AddTagsToResource_RequestSyntax) **   <a name="systemsmanager-AddTagsToResource-request-ResourceId"></a>
The resource ID you want to tag.
Use the ID of the resource. Here are some examples:
 `MaintenanceWindow`: `mw-012345abcde`
 `PatchBaseline`: `pb-012345abcde`
 `Automation`: `example-c160-4567-8519-012345abcde`
 `OpsMetadata` object: `ResourceID` for tagging is created from the Amazon Resource Name (ARN) for the object. Specifically, `ResourceID` is created from the strings that come after the word `opsmetadata` in the ARN. For example, an OpsMetadata object with an ARN of `arn:aws:ssm:us-east-2:1234567890:opsmetadata/aws/ssm/MyGroup/appmanager` has a `ResourceID` of either `aws/ssm/MyGroup/appmanager` or `/aws/ssm/MyGroup/appmanager`.
For the `Document` and `Parameter` values, use the name of the resource. If you're tagging a shared document, you must use the full ARN of the document.
 `ManagedInstance`: `mi-012345abcde`
The `ManagedInstance` type for this API operation is only for on-premises managed nodes. You must specify the name of the managed node in the following format: `mi-ID_number `. For example, `mi-1a2b3c4d5e6f`.
Type: String
Required: Yes

 ** [ResourceType](#API_AddTagsToResource_RequestSyntax) **   <a name="systemsmanager-AddTagsToResource-request-ResourceType"></a>
Specifies the type of resource you are tagging.
The `ManagedInstance` type for this API operation is for on-premises managed nodes. You must specify the name of the managed node in the following format: `mi-ID_number `. For example, `mi-1a2b3c4d5e6f`.
Type: String
Valid Values: `Document | ManagedInstance | MaintenanceWindow | Parameter | PatchBaseline | OpsItem | OpsMetadata | Automation | Association | CloudConnector`
Required: Yes

 ** [Tags](#API_AddTagsToResource_RequestSyntax) **   <a name="systemsmanager-AddTagsToResource-request-Tags"></a>
One or more tags. The value parameter is required.
Don't enter personally identifiable information in this field.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: Yes

## Response Elements
<a name="API_AddTagsToResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AddTagsToResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidResourceId **
The resource ID isn't valid. Verify that you entered the correct ID and try again.
HTTP Status Code: 400

 ** InvalidResourceType **
The resource type isn't valid. For example, if you are attempting to tag an EC2 instance, the instance must be a registered managed node.
HTTP Status Code: 400

 ** TooManyTagsError **
The `Targets` parameter includes too many tags. Remove one or more tags and try the command again.
HTTP Status Code: 400

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

## Examples
<a name="API_AddTagsToResource_Examples"></a>

### Example
<a name="API_AddTagsToResource_Example_1"></a>

This example illustrates one usage of AddTagsToResource.

#### Sample Request
<a name="API_AddTagsToResource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.AddTagsToResource
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240220T232503Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240220/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 122

{
    "ResourceType": "PatchBaseline",
    "ResourceId": "pb-0c10e65780EXAMPLE",
    "Tags": [
        {
            "Key": "Stack",
            "Value": "Production"
        }
    ]
}
```

#### Sample Response
<a name="API_AddTagsToResource_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_AddTagsToResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/AddTagsToResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/AddTagsToResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AddTagsToResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/AddTagsToResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AddTagsToResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/AddTagsToResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/AddTagsToResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/AddTagsToResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/AddTagsToResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AddTagsToResource)

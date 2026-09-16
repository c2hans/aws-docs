---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RemoveTagsFromResource.html
---

# RemoveTagsFromResource
<a name="API_RemoveTagsFromResource"></a>

Removes tag keys from the specified resource.

## Request Syntax
<a name="API_RemoveTagsFromResource_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_RemoveTagsFromResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceId](#API_RemoveTagsFromResource_RequestSyntax) **   <a name="systemsmanager-RemoveTagsFromResource-request-ResourceId"></a>
The ID of the resource from which you want to remove tags. For example:
ManagedInstance: mi-012345abcde
MaintenanceWindow: mw-012345abcde
 `Automation`: `example-c160-4567-8519-012345abcde`
PatchBaseline: pb-012345abcde
OpsMetadata object: `ResourceID` for tagging is created from the Amazon Resource Name (ARN) for the object. Specifically, `ResourceID` is created from the strings that come after the word `opsmetadata` in the ARN. For example, an OpsMetadata object with an ARN of `arn:aws:ssm:us-east-2:1234567890:opsmetadata/aws/ssm/MyGroup/appmanager` has a `ResourceID` of either `aws/ssm/MyGroup/appmanager` or `/aws/ssm/MyGroup/appmanager`.
For the Document and Parameter values, use the name of the resource.
The `ManagedInstance` type for this API operation is only for on-premises managed nodes. Specify the name of the managed node in the following format: mi-ID\_number. For example, mi-1a2b3c4d5e6f.
Type: String
Required: Yes

 ** [ResourceType](#API_RemoveTagsFromResource_RequestSyntax) **   <a name="systemsmanager-RemoveTagsFromResource-request-ResourceType"></a>
The type of resource from which you want to remove a tag.
The `ManagedInstance` type for this API operation is only for on-premises managed nodes. Specify the name of the managed node in the following format: `mi-ID_number `. For example, `mi-1a2b3c4d5e6f`.
Type: String
Valid Values: `Document | ManagedInstance | MaintenanceWindow | Parameter | PatchBaseline | OpsItem | OpsMetadata | Automation | Association | CloudConnector`
Required: Yes

 ** [TagKeys](#API_RemoveTagsFromResource_RequestSyntax) **   <a name="systemsmanager-RemoveTagsFromResource-request-TagKeys"></a>
Tag keys that you want to remove from the specified resource.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Elements
<a name="API_RemoveTagsFromResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveTagsFromResource_Errors"></a>

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

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

## Examples
<a name="API_RemoveTagsFromResource_Examples"></a>

### Example
<a name="API_RemoveTagsFromResource_Example_1"></a>

This example illustrates one usage of RemoveTagsFromResource.

#### Sample Request
<a name="API_RemoveTagsFromResource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.RemoveTagsFromResource
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240221T004031Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240221/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 99

{
    "ResourceType": "PatchBaseline",
    "ResourceId": "pb-0c10e65780EXAMPLE",
    "TagKeys": [
        "Environment"
    ]
}
```

#### Sample Response
<a name="API_RemoveTagsFromResource_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_RemoveTagsFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/RemoveTagsFromResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/RemoveTagsFromResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/RemoveTagsFromResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/RemoveTagsFromResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/RemoveTagsFromResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/RemoveTagsFromResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/RemoveTagsFromResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/RemoveTagsFromResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/RemoveTagsFromResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/RemoveTagsFromResource)

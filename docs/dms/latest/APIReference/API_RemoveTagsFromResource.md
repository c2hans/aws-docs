---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_RemoveTagsFromResource.html
---

# RemoveTagsFromResource
<a name="API_RemoveTagsFromResource"></a>

Removes metadata tags from an AWS DMS resource, including replication instance, endpoint, subnet group, and migration task. For more information, see [`Tag`](https://docs.aws.amazon.com/dms/latest/APIReference/API_Tag.html) data type description.

## Request Syntax
<a name="API_RemoveTagsFromResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_RemoveTagsFromResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_RemoveTagsFromResource_RequestSyntax) **   <a name="DMS-RemoveTagsFromResource-request-ResourceArn"></a>
An AWS DMS resource from which you want to remove tag(s). The value for this parameter is an Amazon Resource Name (ARN).
Type: String
Required: Yes

 ** [TagKeys](#API_RemoveTagsFromResource_RequestSyntax) **   <a name="DMS-RemoveTagsFromResource-request-TagKeys"></a>
The tag key (name) of the tag to be removed.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_RemoveTagsFromResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveTagsFromResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

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
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256
Credential=<Credential>,
SignedHeaders=contenttype;date;host;user-
agent;x-amz-date;x-amz-target;x-amzn-
requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.RemoveTagsFromResource
{
   "ResourceArn":"arn:aws:dms:us-east-
1:123456789012:rep:PWEBBEUNOLU7VEB2OHTEH4I4GQ",
   "TagKeys":[
      "CostCenter"
   ]
}
```

#### Sample Response
<a name="API_RemoveTagsFromResource_Example_1_Response"></a>

```
Empty
```

## See Also
<a name="API_RemoveTagsFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/RemoveTagsFromResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/RemoveTagsFromResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/RemoveTagsFromResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/RemoveTagsFromResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/RemoveTagsFromResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/RemoveTagsFromResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/RemoveTagsFromResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/RemoveTagsFromResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/RemoveTagsFromResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/RemoveTagsFromResource)

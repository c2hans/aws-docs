---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_AddTagsToResource.html
---

# AddTagsToResource
<a name="API_AddTagsToResource"></a>

Adds metadata tags to an AWS DMS resource, including replication instance, endpoint, subnet group, and migration task. These tags can also be used with cost allocation reporting to track cost associated with DMS resources, or used in a Condition statement in an IAM policy for DMS. For more information, see [`Tag`](https://docs.aws.amazon.com/dms/latest/APIReference/API_Tag.html) data type description.

## Request Syntax
<a name="API_AddTagsToResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_AddTagsToResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_AddTagsToResource_RequestSyntax) **   <a name="DMS-AddTagsToResource-request-ResourceArn"></a>
Identifies the AWS DMS resource to which tags should be added. The value for this parameter is an Amazon Resource Name (ARN).
For AWS DMS, you can tag a replication instance, an endpoint, or a replication task.
Type: String
Required: Yes

 ** [Tags](#API_AddTagsToResource_RequestSyntax) **   <a name="DMS-AddTagsToResource-request-Tags"></a>
One or more tags to be assigned to the resource.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

## Response Elements
<a name="API_AddTagsToResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AddTagsToResource_Errors"></a>

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
<a name="API_AddTagsToResource_Examples"></a>

### Example
<a name="API_AddTagsToResource_Example_1"></a>

This example illustrates one usage of AddTagsToResource.

#### Sample Request
<a name="API_AddTagsToResource_Example_1_Request"></a>

```
      POST / HTTP/1.1
      Host: dms.<region>.<domain>
       x-amz-Date: <Date>
        Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
         User-Agent: <UserAgentString>
          Content-Type: application/x-amz-json-1.1
          Content-Length: <PayloadSizeBytes>
           Connection: Keep-Alive
           X-Amz-Target: AmazonDMSv20160101.AddTagsToResource
{
   "ResourceArn":"arn:aws:dms:us-east-
           1:123456789012:rep:PWEBBEUNOLU7VEB2OHTEH4I4GQ",
   "Tags":[
      {
         "Key":"CostCenter",
         "Value":"1234"
      }
   ]
}
```

#### Sample Response
<a name="API_AddTagsToResource_Example_1_Response"></a>

```
      Empty
```

## See Also
<a name="API_AddTagsToResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/AddTagsToResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/AddTagsToResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/AddTagsToResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/AddTagsToResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/AddTagsToResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/AddTagsToResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/AddTagsToResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/AddTagsToResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/AddTagsToResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/AddTagsToResource)

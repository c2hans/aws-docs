---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketAccessKeys.html
---

# GetBucketAccessKeys
<a name="API_GetBucketAccessKeys"></a>

Returns the existing access key IDs for the specified Amazon Lightsail bucket.

**Important**
This action does not return the secret access key value of an access key. You can get a secret access key only when you create it from the response of the [CreateBucketAccessKey](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateBucketAccessKey.html) action. If you lose the secret access key, you must create a new access key.

## Request Syntax
<a name="API_GetBucketAccessKeys_RequestSyntax"></a>

```
{
   "bucketName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetBucketAccessKeys_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bucketName](#API_GetBucketAccessKeys_RequestSyntax) **   <a name="Lightsail-GetBucketAccessKeys-request-bucketName"></a>
The name of the bucket for which to return access keys.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 54.
Pattern: `^[a-z0-9][a-z0-9-]{1,52}[a-z0-9]$`
Required: Yes

## Response Syntax
<a name="API_GetBucketAccessKeys_ResponseSyntax"></a>

```
{
   "accessKeys": [
      {
         "accessKeyId": "string",
         "createdAt": number,
         "lastUsed": {
            "lastUsedDate": number,
            "region": "string",
            "serviceName": "string"
         },
         "secretAccessKey": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetBucketAccessKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessKeys](#API_GetBucketAccessKeys_ResponseSyntax) **   <a name="Lightsail-GetBucketAccessKeys-response-accessKeys"></a>
An object that describes the access keys for the specified bucket.
Type: Array of [AccessKey](API_AccessKey.md) objects

## Errors
<a name="API_GetBucketAccessKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## Examples
<a name="API_GetBucketAccessKeys_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Get bucket access keys
<a name="API_GetBucketAccessKeys_Example_1"></a>

The following example returns the access keys for the bucket named `amzn-s3-demo-bucket`. The example response shows that the bucket has one access key (i.e., `AKIAZEXAMPLE12345PKWV`).

#### Sample Request
<a name="API_GetBucketAccessKeys_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: lightsail.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: Lightsail_20161128.GetBucketAccessKeys
Content-Type: application/x-amz-json-1.1
User-Agent: AGENT
X-Amz-Date: 20210616T143306Z
Authorization: AUTHPARAMS
Content-Length: 49

{"bucketName": "amzn-s3-demo-bucket"}
```

#### Sample Response
<a name="API_GetBucketAccessKeys_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 16 Jun 2021 14:33:07 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 99
x-amzn-RequestId: faebc873-b9cd-4dd1-bd6d-caac46bd5a19
Connection: keep-alive

{
    "accessKeys": [
        {
            "accessKeyId": "AKIAZEXAMPLE12345PKWV",
            "createdAt": 1.619209369E9,
            "status": "Active"
        }
    ]
}
```

## See Also
<a name="API_GetBucketAccessKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetBucketAccessKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetBucketAccessKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetBucketAccessKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetBucketAccessKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetBucketAccessKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetBucketAccessKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetBucketAccessKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetBucketAccessKeys)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetBucketAccessKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetBucketAccessKeys)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

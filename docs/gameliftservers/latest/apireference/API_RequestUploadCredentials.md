---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RequestUploadCredentials.html
---

# RequestUploadCredentials
<a name="API_RequestUploadCredentials"></a>

 **This API works with the following fleet types:** EC2

Retrieves a fresh set of credentials for use when uploading a new set of game build files to Amazon GameLift Servers's Amazon S3. This is done as part of the build creation process; see [CreateBuild](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateBuild.html).

To request new credentials, specify the build ID as returned with an initial `CreateBuild` request. If successful, a new set of credentials are returned, along with the S3 storage location associated with the build ID.

 **Learn more**

 [ Create a Build with Files in S3](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build)

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_RequestUploadCredentials_RequestSyntax"></a>

```
{
   "BuildId": "{{string}}"
}
```

## Request Parameters
<a name="API_RequestUploadCredentials_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BuildId](#API_RequestUploadCredentials_RequestSyntax) **   <a name="gameliftservers-RequestUploadCredentials-request-BuildId"></a>
A unique identifier for the build to get credentials for. You can use either the build ID or ARN value.
Type: String
Pattern: `^build-\S+|^arn:.*:build\/build-\S+`
Required: Yes

## Response Syntax
<a name="API_RequestUploadCredentials_ResponseSyntax"></a>

```
{
   "StorageLocation": {
      "Bucket": "string",
      "Key": "string",
      "ObjectVersion": "string",
      "RoleArn": "string"
   },
   "UploadCredentials": {
      "AccessKeyId": "string",
      "SecretAccessKey": "string",
      "SessionToken": "string"
   }
}
```

## Response Elements
<a name="API_RequestUploadCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StorageLocation](#API_RequestUploadCredentials_ResponseSyntax) **   <a name="gameliftservers-RequestUploadCredentials-response-StorageLocation"></a>
Amazon S3 path and key, identifying where the game build files are stored.
Type: [S3Location](API_S3Location.md) object

 ** [UploadCredentials](#API_RequestUploadCredentials_ResponseSyntax) **   <a name="gameliftservers-RequestUploadCredentials-response-UploadCredentials"></a>
 AWS credentials required when uploading a game build to the storage location. These credentials have a limited lifespan and are valid only for the build they were issued for.
Type: [AwsCredentials](API_AwsCredentials.md) object

## Errors
<a name="API_RequestUploadCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_RequestUploadCredentials_Examples"></a>

### Refresh access credentials for uploading a build
<a name="API_RequestUploadCredentials_Example_1"></a>

This example obtains new, valid access credentials for uploading a build file to a Amazon GameLift Servers Amazon S3 location. Credentials have a limited lift span. The build ID required for this operation is returned in response to the original `CreateBuild` request.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_RequestUploadCredentials_Example_1_Request"></a>

```
{
    "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
}
```

#### Sample Response
<a name="API_RequestUploadCredentials_Example_1_Response"></a>

```
{
    "StorageLocation": {
        "Bucket": "gamelift-builds-us-west-2",
        "Key": "123456789012/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
    },
    "UploadCredentials": {
        "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        "SessionToken": "AgoGb3JpZ2luENz...EXAMPLETOKEN=="
    }
}
```

## See Also
<a name="API_RequestUploadCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/RequestUploadCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/RequestUploadCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/RequestUploadCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/RequestUploadCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/RequestUploadCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/RequestUploadCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/RequestUploadCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/RequestUploadCredentials)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/RequestUploadCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/RequestUploadCredentials)

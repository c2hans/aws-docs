---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeBuild.html
---

# DescribeBuild
<a name="API_DescribeBuild"></a>

 **This API works with the following fleet types:** EC2

Retrieves properties for a custom game build. To request a build resource, specify a build ID. If successful, an object containing the build properties is returned.

 **Learn more**

 [ Upload a Custom Server Build](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html)

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_DescribeBuild_RequestSyntax"></a>

```
{
   "BuildId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBuild_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BuildId](#API_DescribeBuild_RequestSyntax) **   <a name="gameliftservers-DescribeBuild-request-BuildId"></a>
A unique identifier for the build to retrieve properties for. You can use either the build ID or ARN value.
Type: String
Pattern: `^build-\S+|^arn:.*:build\/build-\S+`
Required: Yes

## Response Syntax
<a name="API_DescribeBuild_ResponseSyntax"></a>

```
{
   "Build": {
      "BuildArn": "string",
      "BuildId": "string",
      "CreationTime": number,
      "Name": "string",
      "OperatingSystem": "string",
      "ServerSdkVersion": "string",
      "SizeOnDisk": number,
      "Status": "string",
      "Version": "string"
   }
}
```

## Response Elements
<a name="API_DescribeBuild_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Build](#API_DescribeBuild_ResponseSyntax) **   <a name="gameliftservers-DescribeBuild-response-Build"></a>
Set of properties describing the requested build.
Type: [Build](API_Build.md) object

## Errors
<a name="API_DescribeBuild_Errors"></a>

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
<a name="API_DescribeBuild_Examples"></a>

### View a build resource
<a name="API_DescribeBuild_Example_1"></a>

This example retrieves the information, including current status, about a specific build.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeBuild_Example_1_Request"></a>

```
{
    "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
}
```

#### Sample Response
<a name="API_DescribeBuild_Example_1_Response"></a>

```
{
    "Build": {
        "BuildArn": "arn:aws:gamelift:us-west-2::build/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "CreationTime": 1496708916.18,
        "Name": "My_Game_Server_Build_One",
        "OperatingSystem": "AMAZON_LINUX_2023",
        "SizeOnDisk": 1304924,
        "Status": "READY",
        "Version": "12345.678"
    }
}
```

## See Also
<a name="API_DescribeBuild_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeBuild)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeBuild)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeBuild)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeBuild)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeBuild)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeBuild)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeBuild)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeBuild)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeBuild)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeBuild)

---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeProject.html
---

# DescribeProject
<a name="API_DescribeProject"></a>

Retrieves information about a project.

## Request Syntax
<a name="API_DescribeProject_RequestSyntax"></a>

```
GET /projects/{{projectId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [projectId](#API_DescribeProject_RequestSyntax) **   <a name="iotsitewise-DescribeProject-request-uri-projectId"></a>
The ID of the project.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_DescribeProject_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeProject_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "portalId": "string",
   "projectArn": "string",
   "projectCreationDate": number,
   "projectDescription": "string",
   "projectId": "string",
   "projectLastUpdateDate": number,
   "projectName": "string"
}
```

## Response Elements
<a name="API_DescribeProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [portalId](#API_DescribeProject_ResponseSyntax) **   <a name="iotsitewise-DescribeProject-response-portalId"></a>
The ID of the portal that the project is in.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [projectArn](#API_DescribeProject_ResponseSyntax) **   <a name="iotsitewise-DescribeProject-response-projectArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the project, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:project/${ProjectId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [projectCreationDate](#API_DescribeProject_ResponseSyntax) **   <a name="iotsitewise-DescribeProject-response-projectCreationDate"></a>
The date the project was created, in Unix epoch time.
Type: Timestamp

 ** [projectDescription](#API_DescribeProject_ResponseSyntax) **   <a name="iotsitewise-DescribeProject-response-projectDescription"></a>
The project's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [projectId](#API_DescribeProject_ResponseSyntax) **   <a name="iotsitewise-DescribeProject-response-projectId"></a>
The ID of the project.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [projectLastUpdateDate](#API_DescribeProject_ResponseSyntax) **   <a name="iotsitewise-DescribeProject-response-projectLastUpdateDate"></a>
The date the project was last updated, in Unix epoch time.
Type: Timestamp

 ** [projectName](#API_DescribeProject_ResponseSyntax) **   <a name="iotsitewise-DescribeProject-response-projectName"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

## Errors
<a name="API_DescribeProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeProject)

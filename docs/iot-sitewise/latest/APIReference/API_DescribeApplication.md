---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeApplication.html
---

# DescribeApplication
<a name="API_DescribeApplication"></a>

Retrieves Application details based on the ID

## Request Syntax
<a name="API_DescribeApplication_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/applications/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_DescribeApplication_RequestSyntax) **   <a name="iotsitewise-DescribeApplication-request-uri-id"></a>
ID of the Application
Length Constraints: Fixed length of 36.
Pattern: `[a-z0-9-]{36}`
Required: Yes

 ** [workspaceName](#API_DescribeApplication_RequestSyntax) **   <a name="iotsitewise-DescribeApplication-request-uri-workspaceName"></a>
Name of the workspace to associate with the underlying Application
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_DescribeApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": number,
   "description": "string",
   "dnsSubdomain": "string",
   "id": "string",
   "idcApplicationArn": "string",
   "name": "string",
   "status": "string",
   "updatedAt": number,
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_DescribeApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DescribeApplication_ResponseSyntax) **   <a name="iotsitewise-DescribeApplication-response-arn"></a>
ARN of the application
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [createdAt](#API_DescribeApplication_ResponseSyntax) **   <a name="iotsitewise-DescribeApplication-response-createdAt"></a>
Timestamp when the application was created
Type: Timestamp

 ** [description](#API_DescribeApplication_ResponseSyntax) **   <a name="iotsitewise-DescribeApplication-response-description"></a>
Description of the application
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9_-]+`

 ** [dnsSubdomain](#API_DescribeApplication_ResponseSyntax) **   <a name="iotsitewise-DescribeApplication-response-dnsSubdomain"></a>
DNS subdomain for the application
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`

 ** [id](#API_DescribeApplication_ResponseSyntax) **   <a name="iotsitewise-DescribeApplication-response-id"></a>
Unique identifier of the application
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-z0-9-]{36}`

 ** [idcApplicationArn](#API_DescribeApplication_ResponseSyntax) **   <a name="iotsitewise-DescribeApplication-response-idcApplicationArn"></a>
Identity Center Application ARN associated with this application
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [name](#API_DescribeApplication_ResponseSyntax) **   <a name="iotsitewise-DescribeApplication-response-name"></a>
Name of the application
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9](?:[A-Za-z0-9 ._()\-]*[A-Za-z0-9._()\-])?`

 ** [status](#API_DescribeApplication_ResponseSyntax) **   <a name="iotsitewise-DescribeApplication-response-status"></a>
Current status of the application
Type: String
Valid Values: `CREATING | ACTIVE | DELETING`

 ** [updatedAt](#API_DescribeApplication_ResponseSyntax) **   <a name="iotsitewise-DescribeApplication-response-updatedAt"></a>
Timestamp when the application was last updated
Type: Timestamp

 ** [workspaceName](#API_DescribeApplication_ResponseSyntax) **   <a name="iotsitewise-DescribeApplication-response-workspaceName"></a>
Name of the workspace this application belongs to
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_DescribeApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

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
<a name="API_DescribeApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeApplication)

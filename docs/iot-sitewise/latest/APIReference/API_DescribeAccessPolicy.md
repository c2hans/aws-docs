---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAccessPolicy.html
---

# DescribeAccessPolicy
<a name="API_DescribeAccessPolicy"></a>

Describes an access policy, which specifies an identity's access to an AWS IoT SiteWise Monitor portal or project.

## Request Syntax
<a name="API_DescribeAccessPolicy_RequestSyntax"></a>

```
GET /access-policies/{{accessPolicyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAccessPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessPolicyId](#API_DescribeAccessPolicy_RequestSyntax) **   <a name="iotsitewise-DescribeAccessPolicy-request-uri-accessPolicyId"></a>
The ID of the access policy.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_DescribeAccessPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAccessPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessPolicyArn": "string",
   "accessPolicyCreationDate": number,
   "accessPolicyId": "string",
   "accessPolicyIdentity": {
      "group": {
         "id": "string"
      },
      "iamRole": {
         "arn": "string"
      },
      "iamUser": {
         "arn": "string"
      },
      "user": {
         "id": "string"
      }
   },
   "accessPolicyLastUpdateDate": number,
   "accessPolicyPermission": "string",
   "accessPolicyResource": {
      "portal": {
         "id": "string"
      },
      "project": {
         "id": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeAccessPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessPolicyArn](#API_DescribeAccessPolicy_ResponseSyntax) **   <a name="iotsitewise-DescribeAccessPolicy-response-accessPolicyArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the access policy, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:access-policy/${AccessPolicyId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [accessPolicyCreationDate](#API_DescribeAccessPolicy_ResponseSyntax) **   <a name="iotsitewise-DescribeAccessPolicy-response-accessPolicyCreationDate"></a>
The date the access policy was created, in Unix epoch time.
Type: Timestamp

 ** [accessPolicyId](#API_DescribeAccessPolicy_ResponseSyntax) **   <a name="iotsitewise-DescribeAccessPolicy-response-accessPolicyId"></a>
The ID of the access policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [accessPolicyIdentity](#API_DescribeAccessPolicy_ResponseSyntax) **   <a name="iotsitewise-DescribeAccessPolicy-response-accessPolicyIdentity"></a>
The identity (IAM Identity Center user, IAM Identity Center group, or IAM user) to which this access policy applies.
Type: [Identity](API_Identity.md) object

 ** [accessPolicyLastUpdateDate](#API_DescribeAccessPolicy_ResponseSyntax) **   <a name="iotsitewise-DescribeAccessPolicy-response-accessPolicyLastUpdateDate"></a>
The date the access policy was last updated, in Unix epoch time.
Type: Timestamp

 ** [accessPolicyPermission](#API_DescribeAccessPolicy_ResponseSyntax) **   <a name="iotsitewise-DescribeAccessPolicy-response-accessPolicyPermission"></a>
The access policy permission. Note that a project `ADMINISTRATOR` is also known as a project owner.
Type: String
Valid Values: `ADMINISTRATOR | VIEWER`

 ** [accessPolicyResource](#API_DescribeAccessPolicy_ResponseSyntax) **   <a name="iotsitewise-DescribeAccessPolicy-response-accessPolicyResource"></a>
The AWS IoT SiteWise Monitor resource (portal or project) to which this access policy provides access.
Type: [Resource](API_Resource.md) object

## Errors
<a name="API_DescribeAccessPolicy_Errors"></a>

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
<a name="API_DescribeAccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeAccessPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeAccessPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeAccessPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeAccessPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeAccessPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeAccessPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeAccessPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeAccessPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeAccessPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeAccessPolicy)

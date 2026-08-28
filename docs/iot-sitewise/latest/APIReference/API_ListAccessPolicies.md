---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAccessPolicies.html
---

# ListAccessPolicies
<a name="API_ListAccessPolicies"></a>

Retrieves a paginated list of access policies for an identity (an IAM Identity Center user, an IAM Identity Center group, or an IAM user) or an AWS IoT SiteWise Monitor resource (a portal or project).

## Request Syntax
<a name="API_ListAccessPolicies_RequestSyntax"></a>

```
GET /access-policies?iamArn={{iamArn}}&identityId={{identityId}}&identityType={{identityType}}&maxResults={{maxResults}}&nextToken={{nextToken}}&resourceId={{resourceId}}&resourceType={{resourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAccessPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [iamArn](#API_ListAccessPolicies_RequestSyntax) **   <a name="iotsitewise-ListAccessPolicies-request-uri-iamArn"></a>
The ARN of the IAM user. For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*. This parameter is required if you specify `IAM` for `identityType`.
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.\+=,@]+$`

 ** [identityId](#API_ListAccessPolicies_RequestSyntax) **   <a name="iotsitewise-ListAccessPolicies-request-uri-identityId"></a>
The ID of the identity. This parameter is required if you specify `USER` or `GROUP` for `identityType`.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`

 ** [identityType](#API_ListAccessPolicies_RequestSyntax) **   <a name="iotsitewise-ListAccessPolicies-request-uri-identityType"></a>
The type of identity (IAM Identity Center user, IAM Identity Center group, or IAM user). This parameter is required if you specify `identityId`.
Valid Values: `USER | GROUP | IAM`

 ** [maxResults](#API_ListAccessPolicies_RequestSyntax) **   <a name="iotsitewise-ListAccessPolicies-request-uri-maxResults"></a>
The maximum number of results to return for each paginated request.
Default: 50
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListAccessPolicies_RequestSyntax) **   <a name="iotsitewise-ListAccessPolicies-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [resourceId](#API_ListAccessPolicies_RequestSyntax) **   <a name="iotsitewise-ListAccessPolicies-request-uri-resourceId"></a>
The ID of the resource. This parameter is required if you specify `resourceType`.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [resourceType](#API_ListAccessPolicies_RequestSyntax) **   <a name="iotsitewise-ListAccessPolicies-request-uri-resourceType"></a>
The type of resource (portal or project). This parameter is required if you specify `resourceId`.
Valid Values: `PORTAL | PROJECT`

## Request Body
<a name="API_ListAccessPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAccessPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessPolicySummaries": [
      {
         "creationDate": number,
         "id": "string",
         "identity": {
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
         "lastUpdateDate": number,
         "permission": "string",
         "resource": {
            "portal": {
               "id": "string"
            },
            "project": {
               "id": "string"
            }
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAccessPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessPolicySummaries](#API_ListAccessPolicies_ResponseSyntax) **   <a name="iotsitewise-ListAccessPolicies-response-accessPolicySummaries"></a>
A list that summarizes each access policy.
Type: Array of [AccessPolicySummary](API_AccessPolicySummary.md) objects

 ** [nextToken](#API_ListAccessPolicies_ResponseSyntax) **   <a name="iotsitewise-ListAccessPolicies-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_ListAccessPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_ListAccessPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListAccessPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListAccessPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListAccessPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListAccessPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListAccessPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListAccessPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListAccessPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListAccessPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListAccessPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListAccessPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

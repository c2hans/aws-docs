---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListDeployments.html
---

# ListDeployments
<a name="API_ListDeployments"></a>

Retrieves a paginated list of deployments.

## Request Syntax
<a name="API_ListDeployments_RequestSyntax"></a>

```
GET /greengrass/v2/deployments?historyFilter={{historyFilter}}&maxResults={{maxResults}}&nextToken={{nextToken}}&parentTargetArn={{parentTargetArn}}&targetArn={{targetArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDeployments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [historyFilter](#API_ListDeployments_RequestSyntax) **   <a name="greengrassv2-ListDeployments-request-uri-historyFilter"></a>
The filter for the list of deployments. Choose one of the following options:
+  `ALL` – The list includes all deployments.
+  `LATEST_ONLY` – The list includes only the latest revision of each deployment.
Default: `LATEST_ONLY`
Valid Values: `ALL | LATEST_ONLY`

 ** [maxResults](#API_ListDeployments_RequestSyntax) **   <a name="greengrassv2-ListDeployments-request-uri-maxResults"></a>
The maximum number of results to be returned per paginated request.
Default: `50`
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListDeployments_RequestSyntax) **   <a name="greengrassv2-ListDeployments-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.

 ** [parentTargetArn](#API_ListDeployments_RequestSyntax) **   <a name="greengrassv2-ListDeployments-request-uri-parentTargetArn"></a>
The parent deployment's target [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) within a subdeployment.
Pattern: `arn:[^:]*:iot:[^:]*:[0-9]+:(thing|thinggroup)/.+`

 ** [targetArn](#API_ListDeployments_RequestSyntax) **   <a name="greengrassv2-ListDeployments-request-uri-targetArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the target AWS IoT thing or thing group.
Pattern: `arn:[^:]*:iot:[^:]*:[0-9]+:(thing|thinggroup)/.+`

## Request Body
<a name="API_ListDeployments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDeployments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deployments": [
      {
         "creationTimestamp": number,
         "deploymentId": "string",
         "deploymentName": "string",
         "deploymentStatus": "string",
         "isLatestForTarget": boolean,
         "parentTargetArn": "string",
         "revisionId": "string",
         "targetArn": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deployments](#API_ListDeployments_ResponseSyntax) **   <a name="greengrassv2-ListDeployments-response-deployments"></a>
A list that summarizes each deployment.
Type: Array of [Deployment](API_Deployment.md) objects

 ** [nextToken](#API_ListDeployments_ResponseSyntax) **   <a name="greengrassv2-ListDeployments-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String

## Errors
<a name="API_ListDeployments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
HTTP Status Code: 403

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

 ** ThrottlingException **
Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.
 ** quotaCode **
The code for the quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
 ** serviceCode **
The code for the service in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** fields **
The list of fields that failed to validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_ListDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/ListDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/ListDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ListDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/ListDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ListDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/ListDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/ListDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/ListDeployments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ListDeployments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

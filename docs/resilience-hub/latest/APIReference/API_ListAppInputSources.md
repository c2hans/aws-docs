---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppInputSources.html
---

# ListAppInputSources
<a name="API_ListAppInputSources"></a>

Lists all the input sources of the AWS Resilience Hub application. For more information about the input sources supported by AWS Resilience Hub, see [Discover the structure and describe your Resilience Hub application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure.html).

## Request Syntax
<a name="API_ListAppInputSources_RequestSyntax"></a>

```
POST /list-app-input-sources HTTP/1.1
Content-type: application/json

{
   "appArn": "{{string}}",
   "appVersion": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAppInputSources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAppInputSources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appArn](#API_ListAppInputSources_RequestSyntax) **   <a name="resiliencehub-ListAppInputSources-request-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [appVersion](#API_ListAppInputSources_RequestSyntax) **   <a name="resiliencehub-ListAppInputSources-request-appVersion"></a>
 AWS Resilience Hub application version.
Type: String
Pattern: `\S{1,50}`
Required: Yes

 ** [maxResults](#API_ListAppInputSources_RequestSyntax) **   <a name="resiliencehub-ListAppInputSources-request-maxResults"></a>
Maximum number of input sources to be displayed per AWS Resilience Hub application.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListAppInputSources_RequestSyntax) **   <a name="resiliencehub-ListAppInputSources-request-nextToken"></a>
Null, or the token from a previous call to get the next set of results.
Type: String
Pattern: `\S{1,2000}`
Required: No

## Response Syntax
<a name="API_ListAppInputSources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appInputSources": [
      {
         "eksSourceClusterNamespace": {
            "eksClusterArn": "string",
            "namespace": "string"
         },
         "importType": "string",
         "resourceCount": number,
         "sourceArn": "string",
         "sourceName": "string",
         "terraformSource": {
            "s3StateFileUrl": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAppInputSources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appInputSources](#API_ListAppInputSources_ResponseSyntax) **   <a name="resiliencehub-ListAppInputSources-response-appInputSources"></a>
The list of AWS Resilience Hub application input sources.
Type: Array of [AppInputSource](API_AppInputSource.md) objects

 ** [nextToken](#API_ListAppInputSources_ResponseSyntax) **   <a name="resiliencehub-ListAppInputSources-response-nextToken"></a>
Token for the next set of results, or null if there are no more results.
Type: String
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListAppInputSources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Resilience Hub service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This exception occurs when the specified resource could not be found.
 ** resourceId **
The identifier of the resource that the exception applies to.
 ** resourceType **
The type of the resource that the exception applies to.
HTTP Status Code: 404

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListAppInputSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/ListAppInputSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/ListAppInputSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ListAppInputSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/ListAppInputSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ListAppInputSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/ListAppInputSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/ListAppInputSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/ListAppInputSources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/ListAppInputSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ListAppInputSources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

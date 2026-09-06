---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppComponentCompliances.html
---

# ListAppComponentCompliances
<a name="API_ListAppComponentCompliances"></a>

Lists the compliances for an AWS Resilience Hub AppComponent.

## Request Syntax
<a name="API_ListAppComponentCompliances_RequestSyntax"></a>

```
POST /list-app-component-compliances HTTP/1.1
Content-type: application/json

{
   "assessmentArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAppComponentCompliances_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAppComponentCompliances_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assessmentArn](#API_ListAppComponentCompliances_RequestSyntax) **   <a name="resiliencehub-ListAppComponentCompliances-request-assessmentArn"></a>
Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app-assessment/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [maxResults](#API_ListAppComponentCompliances_RequestSyntax) **   <a name="resiliencehub-ListAppComponentCompliances-request-maxResults"></a>
Maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListAppComponentCompliances_RequestSyntax) **   <a name="resiliencehub-ListAppComponentCompliances-request-nextToken"></a>
Null, or the token from a previous call to get the next set of results.
Type: String
Pattern: `\S{1,2000}`
Required: No

## Response Syntax
<a name="API_ListAppComponentCompliances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "componentCompliances": [
      {
         "appComponentName": "string",
         "compliance": {
            "string" : {
               "achievableRpoInSecs": number,
               "achievableRtoInSecs": number,
               "complianceStatus": "string",
               "currentRpoInSecs": number,
               "currentRtoInSecs": number,
               "message": "string",
               "rpoDescription": "string",
               "rpoReferenceId": "string",
               "rtoDescription": "string",
               "rtoReferenceId": "string"
            }
         },
         "cost": {
            "amount": number,
            "currency": "string",
            "frequency": "string"
         },
         "message": "string",
         "resiliencyScore": {
            "componentScore": {
               "string" : {
                  "excludedCount": number,
                  "outstandingCount": number,
                  "possibleScore": number,
                  "score": number
               }
            },
            "disruptionScore": {
               "string" : number
            },
            "score": number
         },
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAppComponentCompliances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [componentCompliances](#API_ListAppComponentCompliances_ResponseSyntax) **   <a name="resiliencehub-ListAppComponentCompliances-response-componentCompliances"></a>
The compliances for an AWS Resilience Hub AppComponent, returned as an object. This object contains the names of the AppComponents, compliances, costs, resiliency scores, outage scores, and more.
Type: Array of [AppComponentCompliance](API_AppComponentCompliance.md) objects

 ** [nextToken](#API_ListAppComponentCompliances_ResponseSyntax) **   <a name="resiliencehub-ListAppComponentCompliances-response-nextToken"></a>
Token for the next set of results, or null if there are no more results.
Type: String
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListAppComponentCompliances_Errors"></a>

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
<a name="API_ListAppComponentCompliances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/ListAppComponentCompliances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/ListAppComponentCompliances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ListAppComponentCompliances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/ListAppComponentCompliances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ListAppComponentCompliances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/ListAppComponentCompliances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/ListAppComponentCompliances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/ListAppComponentCompliances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/ListAppComponentCompliances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ListAppComponentCompliances)

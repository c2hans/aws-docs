---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListSopRecommendations.html
---

# ListSopRecommendations
<a name="API_ListSopRecommendations"></a>

Lists the standard operating procedure (SOP) recommendations for the AWS Resilience Hub applications.

## Request Syntax
<a name="API_ListSopRecommendations_RequestSyntax"></a>

```
POST /list-sop-recommendations HTTP/1.1
Content-type: application/json

{
   "assessmentArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSopRecommendations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSopRecommendations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assessmentArn](#API_ListSopRecommendations_RequestSyntax) **   <a name="resiliencehub-ListSopRecommendations-request-assessmentArn"></a>
Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app-assessment/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [maxResults](#API_ListSopRecommendations_RequestSyntax) **   <a name="resiliencehub-ListSopRecommendations-request-maxResults"></a>
Maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListSopRecommendations_RequestSyntax) **   <a name="resiliencehub-ListSopRecommendations-request-nextToken"></a>
Null, or the token from a previous call to get the next set of results.
Type: String
Pattern: `\S{1,2000}`
Required: No

## Response Syntax
<a name="API_ListSopRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "sopRecommendations": [
      {
         "appComponentName": "string",
         "description": "string",
         "items": [
            {
               "alreadyImplemented": boolean,
               "discoveredAlarm": {
                  "alarmArn": "string",
                  "source": "string"
               },
               "excluded": boolean,
               "excludeReason": "string",
               "latestDiscoveredExperiment": {
                  "experimentArn": "string",
                  "experimentTemplateId": "string"
               },
               "resourceId": "string",
               "targetAccountId": "string",
               "targetRegion": "string"
            }
         ],
         "name": "string",
         "prerequisite": "string",
         "recommendationId": "string",
         "recommendationStatus": "string",
         "referenceId": "string",
         "serviceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSopRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSopRecommendations_ResponseSyntax) **   <a name="resiliencehub-ListSopRecommendations-response-nextToken"></a>
Token for the next set of results, or null if there are no more results.
Type: String
Pattern: `\S{1,2000}`

 ** [sopRecommendations](#API_ListSopRecommendations_ResponseSyntax) **   <a name="resiliencehub-ListSopRecommendations-response-sopRecommendations"></a>
The standard operating procedure (SOP) recommendations for the AWS Resilience Hub applications.
Type: Array of [SopRecommendation](API_SopRecommendation.md) objects

## Errors
<a name="API_ListSopRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

 ** ConflictException **
This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
 ** resourceId **
The identifier of the resource that the exception applies to.
 ** resourceType **
The type of the resource that the exception applies to.
HTTP Status Code: 409

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
<a name="API_ListSopRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/ListSopRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/ListSopRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ListSopRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/ListSopRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ListSopRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/ListSopRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/ListSopRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/ListSopRecommendations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/ListSopRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ListSopRecommendations)

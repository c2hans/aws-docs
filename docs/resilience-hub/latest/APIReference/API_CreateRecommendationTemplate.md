---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateRecommendationTemplate.html
---

# CreateRecommendationTemplate
<a name="API_CreateRecommendationTemplate"></a>

Creates a new recommendation template for the AWS Resilience Hub application.

## Request Syntax
<a name="API_CreateRecommendationTemplate_RequestSyntax"></a>

```
POST /create-recommendation-template HTTP/1.1
Content-type: application/json

{
   "assessmentArn": "{{string}}",
   "bucketName": "{{string}}",
   "clientToken": "{{string}}",
   "format": "{{string}}",
   "name": "{{string}}",
   "recommendationIds": [ "{{string}}" ],
   "recommendationTypes": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRecommendationTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRecommendationTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assessmentArn](#API_CreateRecommendationTemplate_RequestSyntax) **   <a name="resiliencehub-CreateRecommendationTemplate-request-assessmentArn"></a>
Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app-assessment/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [bucketName](#API_CreateRecommendationTemplate_RequestSyntax) **   <a name="resiliencehub-CreateRecommendationTemplate-request-bucketName"></a>
The name of the Amazon S3 bucket that will contain the recommendation template.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** [clientToken](#API_CreateRecommendationTemplate_RequestSyntax) **   <a name="resiliencehub-CreateRecommendationTemplate-request-clientToken"></a>
Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [format](#API_CreateRecommendationTemplate_RequestSyntax) **   <a name="resiliencehub-CreateRecommendationTemplate-request-format"></a>
The format for the recommendation template.
CfnJson
The template is CloudFormation JSON.
CfnYaml
The template is CloudFormation YAML.
Type: String
Valid Values: `CfnYaml | CfnJson`
Required: No

 ** [name](#API_CreateRecommendationTemplate_RequestSyntax) **   <a name="resiliencehub-CreateRecommendationTemplate-request-name"></a>
The name for the recommendation template.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** [recommendationIds](#API_CreateRecommendationTemplate_RequestSyntax) **   <a name="resiliencehub-CreateRecommendationTemplate-request-recommendationIds"></a>
Identifiers for the recommendations used to create a recommendation template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: No

 ** [recommendationTypes](#API_CreateRecommendationTemplate_RequestSyntax) **   <a name="resiliencehub-CreateRecommendationTemplate-request-recommendationTypes"></a>
An array of strings that specify the recommendation template type or types.
Alarm
The template is an [AlarmRecommendation](API_AlarmRecommendation.md) template.
Sop
The template is a [SopRecommendation](API_SopRecommendation.md) template.
Test
The template is a [TestRecommendation](API_TestRecommendation.md) template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `Alarm | Sop | Test`
Required: No

 ** [tags](#API_CreateRecommendationTemplate_RequestSyntax) **   <a name="resiliencehub-CreateRecommendationTemplate-request-tags"></a>
Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

## Response Syntax
<a name="API_CreateRecommendationTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "recommendationTemplate": {
      "appArn": "string",
      "assessmentArn": "string",
      "endTime": number,
      "format": "string",
      "message": "string",
      "name": "string",
      "needsReplacements": boolean,
      "recommendationIds": [ "string" ],
      "recommendationTemplateArn": "string",
      "recommendationTypes": [ "string" ],
      "startTime": number,
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "templatesLocation": {
         "bucket": "string",
         "prefix": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateRecommendationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recommendationTemplate](#API_CreateRecommendationTemplate_ResponseSyntax) **   <a name="resiliencehub-CreateRecommendationTemplate-response-recommendationTemplate"></a>
The newly created recommendation template, returned as an object. This object includes the template's name, format, status, tags, Amazon S3 bucket location, and more.
Type: [RecommendationTemplate](API_RecommendationTemplate.md) object

## Errors
<a name="API_CreateRecommendationTemplate_Errors"></a>

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

 ** ServiceQuotaExceededException **
This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateRecommendationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/CreateRecommendationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/CreateRecommendationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/CreateRecommendationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/CreateRecommendationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/CreateRecommendationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/CreateRecommendationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/CreateRecommendationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/CreateRecommendationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/CreateRecommendationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/CreateRecommendationTemplate)

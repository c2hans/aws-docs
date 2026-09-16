---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_BatchUpdateRecommendationStatus.html
---

# BatchUpdateRecommendationStatus
<a name="API_BatchUpdateRecommendationStatus"></a>

Enables you to include or exclude one or more operational recommendations.

## Request Syntax
<a name="API_BatchUpdateRecommendationStatus_RequestSyntax"></a>

```
POST /batch-update-recommendation-status HTTP/1.1
Content-type: application/json

{
   "appArn": "{{string}}",
   "requestEntries": [
      {
         "appComponentId": "{{string}}",
         "entryId": "{{string}}",
         "excluded": {{boolean}},
         "excludeReason": "{{string}}",
         "item": {
            "resourceId": "{{string}}",
            "targetAccountId": "{{string}}",
            "targetRegion": "{{string}}"
         },
         "referenceId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateRecommendationStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchUpdateRecommendationStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appArn](#API_BatchUpdateRecommendationStatus_RequestSyntax) **   <a name="resiliencehub-BatchUpdateRecommendationStatus-request-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [requestEntries](#API_BatchUpdateRecommendationStatus_RequestSyntax) **   <a name="resiliencehub-BatchUpdateRecommendationStatus-request-requestEntries"></a>
Defines the list of operational recommendations that need to be included or excluded.
Type: Array of [UpdateRecommendationStatusRequestEntry](API_UpdateRecommendationStatusRequestEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateRecommendationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appArn": "string",
   "failedEntries": [
      {
         "entryId": "string",
         "errorMessage": "string"
      }
   ],
   "successfulEntries": [
      {
         "appComponentId": "string",
         "entryId": "string",
         "excluded": boolean,
         "excludeReason": "string",
         "item": {
            "resourceId": "string",
            "targetAccountId": "string",
            "targetRegion": "string"
         },
         "referenceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateRecommendationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_BatchUpdateRecommendationStatus_ResponseSyntax) **   <a name="resiliencehub-BatchUpdateRecommendationStatus-response-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [failedEntries](#API_BatchUpdateRecommendationStatus_ResponseSyntax) **   <a name="resiliencehub-BatchUpdateRecommendationStatus-response-failedEntries"></a>
A list of items with error details about each item, which could not be included or excluded.
Type: Array of [BatchUpdateRecommendationStatusFailedEntry](API_BatchUpdateRecommendationStatusFailedEntry.md) objects

 ** [successfulEntries](#API_BatchUpdateRecommendationStatus_ResponseSyntax) **   <a name="resiliencehub-BatchUpdateRecommendationStatus-response-successfulEntries"></a>
A list of items that were included or excluded.
Type: Array of [BatchUpdateRecommendationStatusSuccessfulEntry](API_BatchUpdateRecommendationStatusSuccessfulEntry.md) objects

## Errors
<a name="API_BatchUpdateRecommendationStatus_Errors"></a>

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

## Examples
<a name="API_BatchUpdateRecommendationStatus_Examples"></a>

### Sample request
<a name="API_BatchUpdateRecommendationStatus_Example_1"></a>

This example illustrates one usage of BatchUpdateRecommendationStatus.

```
{
  "appArn": "APP_ARN",
  "requestEntries": [
    {
      "entryId": "entry_num_1",
      "referenceId": "s3:alarm:health_4xx_errors_count:2020-04-01",
      "item": {
        "resourceId": "a-resource-id",
        "targetAccountId": "123456789012",
        "targetRegion": "us-west-2"
      },
      "excluded": true,
      "excludeReason": "AlreadyImplemented"
    },
    {
      "entryId": "entry_num_2",
      "referenceId": "s3:alarm:health_total_request_latency:2020-04-01",
      "item": {
        "resourceId": "a-resource-id",
        "targetAccountId": "123456789012",
        "targetRegion": "us-west-2"
      },
      "excluded": true
    }
  ]
}
```

### Sample response
<a name="API_BatchUpdateRecommendationStatus_Example_2"></a>

This example illustrates one usage of BatchUpdateRecommendationStatus.

```
{
  "appArn": "APP_ARN",
  "successfulEntries": [
    {
      "entryId": "entry_num_2",
      "referenceId": "s3:alarm:health_total_request_latency:2020-04-01",
      "item": {
        "resourceId": "a-resource-id",
        "targetAccountId": "123456789012",
        "targetRegion": "us-west-2"
      },
      "excluded": true
    },
    {
      "entryId": "entry_num_1",
      "referenceId": "s3:alarm:health_4xx_errors_count:2020-04-01",
      "item": {
        "resourceId": "a-resource-id",
        "targetAccountId": "123456789012",
        "targetRegion": "us-west-2"
      },
      "excluded": true,
      "excludeReason": "AlreadyImplemented"
    }
  ],
  "failedEntries": []
}
```

## See Also
<a name="API_BatchUpdateRecommendationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/BatchUpdateRecommendationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/BatchUpdateRecommendationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/BatchUpdateRecommendationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/BatchUpdateRecommendationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/BatchUpdateRecommendationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/BatchUpdateRecommendationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/BatchUpdateRecommendationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/BatchUpdateRecommendationStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/BatchUpdateRecommendationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/BatchUpdateRecommendationStatus)

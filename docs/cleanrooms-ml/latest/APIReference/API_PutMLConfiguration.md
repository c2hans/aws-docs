---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_PutMLConfiguration.html
---

# PutMLConfiguration
<a name="API_PutMLConfiguration"></a>

Assigns information about an ML configuration.

## Request Syntax
<a name="API_PutMLConfiguration_RequestSyntax"></a>

```
PUT /memberships/{{membershipIdentifier}}/ml-configurations HTTP/1.1
Content-type: application/json

{
   "defaultOutputLocation": {
      "destination": {
         "s3Destination": {
            "s3Uri": "{{string}}"
         }
      },
      "roleArn": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_PutMLConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_PutMLConfiguration_RequestSyntax) **   <a name="API-PutMLConfiguration-request-uri-membershipIdentifier"></a>
The membership ID of the member that is being configured.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_PutMLConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [defaultOutputLocation](#API_PutMLConfiguration_RequestSyntax) **   <a name="API-PutMLConfiguration-request-defaultOutputLocation"></a>
The default Amazon S3 location where ML output is stored for the specified member.
Type: [MLOutputConfiguration](API_MLOutputConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_PutMLConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutMLConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutMLConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_PutMLConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/PutMLConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/PutMLConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/PutMLConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/PutMLConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/PutMLConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/PutMLConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/PutMLConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/PutMLConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/PutMLConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/PutMLConfiguration)

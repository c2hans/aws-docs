---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DeleteQueuedSavingsPlan.html
---

# DeleteQueuedSavingsPlan
<a name="API_DeleteQueuedSavingsPlan"></a>

Deletes the queued purchase for the specified Savings Plan.

## Request Syntax
<a name="API_DeleteQueuedSavingsPlan_RequestSyntax"></a>

```
POST /DeleteQueuedSavingsPlan HTTP/1.1
Content-type: application/json

{
   "savingsPlanId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteQueuedSavingsPlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteQueuedSavingsPlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [savingsPlanId](#API_DeleteQueuedSavingsPlan_RequestSyntax) **   <a name="savingsplans-DeleteQueuedSavingsPlan-request-savingsPlanId"></a>
The ID of the Savings Plan.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteQueuedSavingsPlan_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteQueuedSavingsPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteQueuedSavingsPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
A service quota has been exceeded.
HTTP Status Code: 402

 ** ValidationException **
One of the input parameters is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteQueuedSavingsPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/savingsplans-2019-06-28/DeleteQueuedSavingsPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/savingsplans-2019-06-28/DeleteQueuedSavingsPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/DeleteQueuedSavingsPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/savingsplans-2019-06-28/DeleteQueuedSavingsPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/DeleteQueuedSavingsPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/savingsplans-2019-06-28/DeleteQueuedSavingsPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/savingsplans-2019-06-28/DeleteQueuedSavingsPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/savingsplans-2019-06-28/DeleteQueuedSavingsPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/savingsplans-2019-06-28/DeleteQueuedSavingsPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/DeleteQueuedSavingsPlan)

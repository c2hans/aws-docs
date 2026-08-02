---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListOfferingPromotions.html
---

# ListOfferingPromotions
<a name="API_ListOfferingPromotions"></a>

Returns a list of offering promotions. Each offering promotion record contains the ID and description of the promotion. The API returns a `NotEligible` error if the caller is not permitted to invoke the operation. Contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you must be able to invoke this operation.

## Request Syntax
<a name="API_ListOfferingPromotions_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListOfferingPromotions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListOfferingPromotions_RequestSyntax) **   <a name="devicefarm-ListOfferingPromotions-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListOfferingPromotions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "offeringPromotions": [
      {
         "description": "string",
         "id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOfferingPromotions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListOfferingPromotions_ResponseSyntax) **   <a name="devicefarm-ListOfferingPromotions-response-nextToken"></a>
An identifier to be used in the next call to this operation, to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [offeringPromotions](#API_ListOfferingPromotions_ResponseSyntax) **   <a name="devicefarm-ListOfferingPromotions-response-offeringPromotions"></a>
Information about the offering promotions.
Type: Array of [OfferingPromotion](API_OfferingPromotion.md) objects

## Errors
<a name="API_ListOfferingPromotions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotEligibleException **
Exception gets thrown when a user is not eligible to perform the specified transaction.
 ** message **
The HTTP response code of a Not Eligible exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListOfferingPromotions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListOfferingPromotions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListOfferingPromotions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListOfferingPromotions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListOfferingPromotions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListOfferingPromotions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListOfferingPromotions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListOfferingPromotions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListOfferingPromotions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListOfferingPromotions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListOfferingPromotions)

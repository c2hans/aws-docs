---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_RenewOffering.html
---

# RenewOffering
<a name="API_RenewOffering"></a>

Explicitly sets the quantity of devices to renew for an offering, starting from the `effectiveDate` of the next period. The API returns a `NotEligible` error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com).

## Request Syntax
<a name="API_RenewOffering_RequestSyntax"></a>

```
{
   "offeringId": "{{string}}",
   "quantity": {{number}}
}
```

## Request Parameters
<a name="API_RenewOffering_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [offeringId](#API_RenewOffering_RequestSyntax) **   <a name="devicefarm-RenewOffering-request-offeringId"></a>
The ID of a request to renew an offering.
Type: String
Length Constraints: Minimum length of 32.
Required: Yes

 ** [quantity](#API_RenewOffering_RequestSyntax) **   <a name="devicefarm-RenewOffering-request-quantity"></a>
The quantity requested in an offering renewal.
Type: Integer
Required: Yes

## Response Syntax
<a name="API_RenewOffering_ResponseSyntax"></a>

```
{
   "offeringTransaction": {
      "cost": {
         "amount": number,
         "currencyCode": "string"
      },
      "createdOn": number,
      "offeringPromotionId": "string",
      "offeringStatus": {
         "effectiveOn": number,
         "offering": {
            "description": "string",
            "id": "string",
            "platform": "string",
            "recurringCharges": [
               {
                  "cost": {
                     "amount": number,
                     "currencyCode": "string"
                  },
                  "frequency": "string"
               }
            ],
            "type": "string"
         },
         "quantity": number,
         "type": "string"
      },
      "transactionId": "string"
   }
}
```

## Response Elements
<a name="API_RenewOffering_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [offeringTransaction](#API_RenewOffering_ResponseSyntax) **   <a name="devicefarm-RenewOffering-response-offeringTransaction"></a>
Represents the status of the offering transaction for the renewal.
Type: [OfferingTransaction](API_OfferingTransaction.md) object

## Errors
<a name="API_RenewOffering_Errors"></a>

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

## Examples
<a name="API_RenewOffering_Examples"></a>

### Example
<a name="API_RenewOffering_Example_1"></a>

The following example renews the offering for one unmetered iOS device.

#### Sample Request
<a name="API_RenewOffering_Example_1_Request"></a>

```
{
    "transactions": [
        "renew": {
            "offeringId": "offering-id-ios",
            "quantity": 1,
        }
    ]
}
```

#### Sample Response
<a name="API_RenewOffering_Example_1_Response"></a>

```
{
    "offeringTransaction": {
        "createdOn": 1458596930.431,
        "offeringStatus": {
            "effectiveOn": 1459468800.0,
            "type": "RECURRING",
            "offering": {
                "platform": "IOS",
                "type": "RECURRING",
                "id": "offering-id-ios",
                "description": "iOS Unmetered Device Slot"
            },
            "quantity": 1
        },
        "cost": {
            "amount": 250.0,
            "currencyCode": "USD"
        },
        "transactionId": "transaction-id"
    }
}
```

## See Also
<a name="API_RenewOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/RenewOffering)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/RenewOffering)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/RenewOffering)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/RenewOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/RenewOffering)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/RenewOffering)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/RenewOffering)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/RenewOffering)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/RenewOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/RenewOffering)

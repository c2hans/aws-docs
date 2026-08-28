---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListOfferingTransactions.html
---

# ListOfferingTransactions
<a name="API_ListOfferingTransactions"></a>

Returns a list of all historical purchases, renewals, and system renewal transactions for an AWS account. The list is paginated and ordered by a descending timestamp (most recent transactions are first). The API returns a `NotEligible` error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com).

## Request Syntax
<a name="API_ListOfferingTransactions_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListOfferingTransactions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListOfferingTransactions_RequestSyntax) **   <a name="devicefarm-ListOfferingTransactions-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListOfferingTransactions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "offeringTransactions": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListOfferingTransactions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListOfferingTransactions_ResponseSyntax) **   <a name="devicefarm-ListOfferingTransactions-response-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [offeringTransactions](#API_ListOfferingTransactions_ResponseSyntax) **   <a name="devicefarm-ListOfferingTransactions-response-offeringTransactions"></a>
The audit log of subscriptions you have purchased and modified through AWS Device Farm.
Type: Array of [OfferingTransaction](API_OfferingTransaction.md) objects

## Errors
<a name="API_ListOfferingTransactions_Errors"></a>

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
<a name="API_ListOfferingTransactions_Examples"></a>

### Example
<a name="API_ListOfferingTransactions_Example_1"></a>

The following example response contains all the transactions that the customer has made.

#### Sample Response
<a name="API_ListOfferingTransactions_Example_1_Response"></a>

```
{
    "offeringTransactions": [
        {
            "createdOn": 1458596241.001,
            "offeringStatus": {
                "effectiveOn": 1458596240.974,
                "type": "PURCHASE",
                "offering": {
                    "platform": "IOS",
                    "type": "RECURRING",
                    "id": "offering-id-ios",
                    "description": "iOS Unmetered Device Slot"
                },
                "quantity": 1
            },
            "cost": {
                "amount": 80.65,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458587590.308,
            "offeringStatus": {
                "effectiveOn": 1458587590.24,
                "type": "PURCHASE",
                "offering": {
                    "platform": "IOS",
                    "type": "RECURRING",
                    "id": "offering-id-ios",
                    "description": "iOS Unmetered Device Slot"
                },
                "quantity": 1
            },
            "cost": {
                "amount": 80.65,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458541943.395,
            "offeringStatus": {
                "effectiveOn": 1458541943.34,
                "type": "PURCHASE",
                "offering": {
                    "platform": "ANDROID",
                    "type": "RECURRING",
                    "id": "offering-id-android",
                    "description": "Android Unmetered Device Slot"
                },
                "quantity": 10
            },
            "cost": {
                "amount": 806.45,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458584276.849,
            "offeringStatus": {
                "effectiveOn": 1458584276.811,
                "type": "PURCHASE",
                "offering": {
                    "platform": "ANDROID",
                    "type": "RECURRING",
                    "id": "offering-id-android",
                    "description": "Android Unmetered Device Slot"
                },
                "quantity": 2
            },
            "cost": {
                "amount": 161.29,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458592981.171,
            "offeringStatus": {
                "effectiveOn": 1458592981.137,
                "type": "PURCHASE",
                "offering": {
                    "platform": "IOS",
                    "type": "RECURRING",
                    "id": "offering-id-ios",
                    "description": "iOS Unmetered Device Slot"
                },
                "quantity": 1
            },
            "cost": {
                "amount": 80.65,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458591927.511,
            "offeringStatus": {
                "effectiveOn": 1458591927.468,
                "type": "PURCHASE",
                "offering": {
                    "platform": "IOS",
                    "type": "RECURRING",
                    "id": "offering-id-ios",
                    "description": "iOS Unmetered Device Slot"
                },
                "quantity": 1
            },
            "cost": {
                "amount": 80.65,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458581880.117,
            "offeringStatus": {
                "effectiveOn": 1459468800.0,
                "type": "RENEW",
                "offering": {
                    "platform": "IOS",
                    "type": "RECURRING",
                    "id": "offering-id-ios",
                    "description": "iOS Unmetered Device Slot"
                },
                "quantity": 0
            },
            "cost": {
                "amount": 0.0,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458587390.031,
            "offeringStatus": {
                "effectiveOn": 1458587390.008,
                "type": "PURCHASE",
                "offering": {
                    "platform": "ANDROID",
                    "type": "RECURRING",
                    "id": "offering-id-android",
                    "description": "Android Unmetered Device Slot"
                },
                "quantity": 1
            },
            "cost": {
                "amount": 80.65,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458591927.99,
            "offeringStatus": {
                "effectiveOn": 1459468800.0,
                "type": "RENEW",
                "offering": {
                    "platform": "ANDROID",
                    "type": "RECURRING",
                    "id": "offering-id-android",
                    "description": "Android Unmetered Device Slot"
                },
                "quantity": 3
            },
            "cost": {
                "amount": 750.0,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458581580.426,
            "offeringStatus": {
                "effectiveOn": 1458581580.377,
                "type": "PURCHASE",
                "offering": {
                    "platform": "ANDROID",
                    "type": "RECURRING",
                    "id": "offering-id-android",
                    "description": "Android Unmetered Device Slot"
                },
                "quantity": 1
            },
            "cost": {
                "amount": 80.65,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458582235.794,
            "offeringStatus": {
                "effectiveOn": 1459468800.0,
                "type": "RENEW",
                "offering": {
                    "platform": "ANDROID",
                    "type": "RECURRING",
                    "id": "offering-id-android",
                    "description": "Android Unmetered Device Slot"
                },
                "quantity": 1
            },
            "cost": {
                "amount": 250.0,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458581580.429,
            "offeringStatus": {
                "effectiveOn": 1458581580.372,
                "type": "PURCHASE",
                "offering": {
                    "platform": "IOS",
                    "type": "RECURRING",
                    "id": "offering-id-ios",
                    "description": "iOS Unmetered Device Slot"
                },
                "quantity": 1
            },
            "cost": {
                "amount": 80.65,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458593014.881,
            "offeringStatus": {
                "effectiveOn": 1458593014.856,
                "type": "PURCHASE",
                "offering": {
                    "platform": "IOS",
                    "type": "RECURRING",
                    "id": "offering-id-ios",
                    "description": "iOS Unmetered Device Slot"
                },
                "quantity": 2
            },
            "cost": {
                "amount": 161.29,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458581880.415,
            "offeringStatus": {
                "effectiveOn": 1459468800.0,
                "type": "RENEW",
                "offering": {
                    "platform": "ANDROID",
                    "type": "RECURRING",
                    "id": "offering-id-android",
                    "description": "Android Unmetered Device Slot"
                },
                "quantity": 0
            },
            "cost": {
                "amount": 0.0,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458591927.662,
            "offeringStatus": {
                "effectiveOn": 1458591927.491,
                "type": "PURCHASE",
                "offering": {
                    "platform": "ANDROID",
                    "type": "RECURRING",
                    "id": "offering-id-android",
                    "description": "Android Unmetered Device Slot"
                },
                "quantity": 1
            },
            "cost": {
                "amount": 80.65,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458582235.834,
            "offeringStatus": {
                "effectiveOn": 1459468800.0,
                "type": "RENEW",
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
        },
        {
            "createdOn": 1458583642.184,
            "offeringStatus": {
                "effectiveOn": 1459468800.0,
                "type": "RENEW",
                "offering": {
                    "platform": "IOS",
                    "type": "RECURRING",
                    "id": "offering-id-ios",
                    "description": "iOS Unmetered Device Slot"
                },
                "quantity": 0
            },
            "cost": {
                "amount": 0.0,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        },
        {
            "createdOn": 1458581880.007,
            "offeringStatus": {
                "effectiveOn": 1458581879.937,
                "type": "PURCHASE",
                "offering": {
                    "platform": "ANDROID",
                    "type": "RECURRING",
                    "id": "offering-id-android",
                    "description": "Android Unmetered Device Slot"
                },
                "quantity": 1
            },
            "cost": {
                "amount": 80.65,
                "currencyCode": "USD"
            },
            "transactionId": "transaction-id"
        }
    ]
}
```

## See Also
<a name="API_ListOfferingTransactions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListOfferingTransactions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListOfferingTransactions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListOfferingTransactions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListOfferingTransactions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListOfferingTransactions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListOfferingTransactions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListOfferingTransactions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListOfferingTransactions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListOfferingTransactions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListOfferingTransactions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

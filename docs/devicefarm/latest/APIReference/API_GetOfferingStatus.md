---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetOfferingStatus.html
---

# GetOfferingStatus
<a name="API_GetOfferingStatus"></a>

Gets the current status and future status of all offerings purchased by an AWS account. The response indicates how many offerings are currently available and the offerings that will be available in the next period. The API returns a `NotEligible` error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com).

## Request Syntax
<a name="API_GetOfferingStatus_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetOfferingStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_GetOfferingStatus_RequestSyntax) **   <a name="devicefarm-GetOfferingStatus-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_GetOfferingStatus_ResponseSyntax"></a>

```
{
   "current": {
      "string" : {
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
      }
   },
   "nextPeriod": {
      "string" : {
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
      }
   },
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetOfferingStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [current](#API_GetOfferingStatus_ResponseSyntax) **   <a name="devicefarm-GetOfferingStatus-response-current"></a>
When specified, gets the offering status for the current period.
Type: String to [OfferingStatus](API_OfferingStatus.md) object map
Key Length Constraints: Minimum length of 32.

 ** [nextPeriod](#API_GetOfferingStatus_ResponseSyntax) **   <a name="devicefarm-GetOfferingStatus-response-nextPeriod"></a>
When specified, gets the offering status for the next period.
Type: String to [OfferingStatus](API_OfferingStatus.md) object map
Key Length Constraints: Minimum length of 32.

 ** [nextToken](#API_GetOfferingStatus_ResponseSyntax) **   <a name="devicefarm-GetOfferingStatus-response-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

## Errors
<a name="API_GetOfferingStatus_Errors"></a>

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
<a name="API_GetOfferingStatus_Examples"></a>

### Example
<a name="API_GetOfferingStatus_Example_1"></a>

The following example checks the current and renewal status.

#### Sample Response
<a name="API_GetOfferingStatus_Example_1_Response"></a>

```
{
    "current": {
        "offering-id-ios": {
            "offering": {
                "platform": "IOS",
                "type": "RECURRING",
                "id": "offering-id-ios",
                "description": "iOS Unmetered Device Slot"
            },
            "quantity": 1
        }
    },
    "nextPeriod": {
        "offering-id-ios": {
              "effectiveOn": 1459468800.0,
              "offering": {
                  "platform": "IOS",
                  "type": "RECURRING",
                  "id": "offering-id-ios",
                  "description": "iOS Unmetered Device Slot"
              },
              "quantity": 1
          }
    }
}
```

## See Also
<a name="API_GetOfferingStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/GetOfferingStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/GetOfferingStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/GetOfferingStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/GetOfferingStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/GetOfferingStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/GetOfferingStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/GetOfferingStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/GetOfferingStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/GetOfferingStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/GetOfferingStatus)

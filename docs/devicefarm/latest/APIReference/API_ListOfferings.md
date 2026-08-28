---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListOfferings.html
---

# ListOfferings
<a name="API_ListOfferings"></a>

Returns a list of products or offerings that the user can manage through the API. Each offering record indicates the recurring price per unit and the frequency for that offering. The API returns a `NotEligible` error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com).

## Request Syntax
<a name="API_ListOfferings_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListOfferings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListOfferings_RequestSyntax) **   <a name="devicefarm-ListOfferings-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListOfferings_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "offerings": [
      {
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
      }
   ]
}
```

## Response Elements
<a name="API_ListOfferings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListOfferings_ResponseSyntax) **   <a name="devicefarm-ListOfferings-response-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [offerings](#API_ListOfferings_ResponseSyntax) **   <a name="devicefarm-ListOfferings-response-offerings"></a>
A value that represents the list offering results.
Type: Array of [Offering](API_Offering.md) objects

## Errors
<a name="API_ListOfferings_Errors"></a>

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
<a name="API_ListOfferings_Examples"></a>

### Example
<a name="API_ListOfferings_Example_1"></a>

The following example response shows a list of device offerings for the user's account.

#### Sample Response
<a name="API_ListOfferings_Example_1_Response"></a>

```
{
    "offerings": [
        {
           "recurringCharges": [
               {
                   "cost": {
                       "amount": 250.0,
                       "currencyCode": "USD"
                   },
                   "frequency": "MONTHLY"
               }
           ],
           "platform": "IOS",
           "type": "RECURRING",
           "id": "offering-id-ios",
           "description": "iOS Unmetered Device Slot"
       },
       {
           "recurringCharges": [
               {
                   "cost": {
                       "amount": 250.0,
                       "currencyCode": "USD"
                   },
                  "frequency": "MONTHLY"
                }
            ],
           "platform": "ANDROID",
           "type": "RECURRING",
           "id": "offering-id-android",
           "description": "Android Unmetered Device Slot"
        }
    ]
}
```

## See Also
<a name="API_ListOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListOfferings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListOfferings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCostEstimate.html
---

# GetCostEstimate
<a name="API_GetCostEstimate"></a>

Retrieves information about the cost estimate for a specified resource. A cost estimate will not generate for a resource that has been deleted.

## Request Syntax
<a name="API_GetCostEstimate_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "resourceName": "{{string}}",
   "startTime": {{number}}
}
```

## Request Parameters
<a name="API_GetCostEstimate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_GetCostEstimate_RequestSyntax) **   <a name="Lightsail-GetCostEstimate-request-endTime"></a>
The cost estimate end time.
Constraints:
+ Specified in Coordinated Universal Time (UTC).
+ Specified in the Unix time format.

  For example, if you want to use an end time of October 1, 2018, at 9 PM UTC, specify `1538427600` as the end time.
You can convert a human-friendly time to Unix time format using a converter like [Epoch converter](https://www.epochconverter.com/).
Type: Timestamp
Required: Yes

 ** [resourceName](#API_GetCostEstimate_RequestSyntax) **   <a name="Lightsail-GetCostEstimate-request-resourceName"></a>
The resource name.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [startTime](#API_GetCostEstimate_RequestSyntax) **   <a name="Lightsail-GetCostEstimate-request-startTime"></a>
The cost estimate start time.
Constraints:
+ Specified in Coordinated Universal Time (UTC).
+ Specified in the Unix time format.

  For example, if you want to use a start time of October 1, 2018, at 8 PM UTC, specify `1538424000` as the start time.
You can convert a human-friendly time to Unix time format using a converter like [Epoch converter](https://www.epochconverter.com/).
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_GetCostEstimate_ResponseSyntax"></a>

```
{
   "resourcesBudgetEstimate": [
      {
         "costEstimates": [
            {
               "resultsByTime": [
                  {
                     "currency": "string",
                     "pricingUnit": "string",
                     "timePeriod": {
                        "end": number,
                        "start": number
                     },
                     "unit": number,
                     "usageCost": number
                  }
               ],
               "usageType": "string"
            }
         ],
         "endTime": number,
         "resourceName": "string",
         "resourceType": "string",
         "startTime": number
      }
   ]
}
```

## Response Elements
<a name="API_GetCostEstimate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourcesBudgetEstimate](#API_GetCostEstimate_ResponseSyntax) **   <a name="Lightsail-GetCostEstimate-response-resourcesBudgetEstimate"></a>
Returns the estimate's forecasted cost or usage.
Type: Array of [ResourceBudgetEstimate](API_ResourceBudgetEstimate.md) objects

## Errors
<a name="API_GetCostEstimate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetCostEstimate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetCostEstimate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetCostEstimate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetCostEstimate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetCostEstimate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetCostEstimate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetCostEstimate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetCostEstimate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetCostEstimate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetCostEstimate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetCostEstimate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

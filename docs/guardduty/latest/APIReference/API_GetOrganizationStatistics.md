---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetOrganizationStatistics.html
---

# GetOrganizationStatistics
<a name="API_GetOrganizationStatistics"></a>

Retrieves how many active member accounts have each feature enabled within GuardDuty. Only a delegated GuardDuty administrator of an organization can run this API.

When you create a new organization, it might take up to 24 hours to generate the statistics for the entire organization.

## Request Syntax
<a name="API_GetOrganizationStatistics_RequestSyntax"></a>

```
GET /organization/statistics HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOrganizationStatistics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetOrganizationStatistics_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOrganizationStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "organizationDetails": {
      "organizationStatistics": {
         "activeAccountsCount": number,
         "countByFeature": [
            {
               "additionalConfiguration": [
                  {
                     "enabledAccountsCount": number,
                     "name": "string"
                  }
               ],
               "enabledAccountsCount": number,
               "name": "string"
            }
         ],
         "enabledAccountsCount": number,
         "memberAccountsCount": number,
         "totalAccountsCount": number
      },
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_GetOrganizationStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [organizationDetails](#API_GetOrganizationStatistics_ResponseSyntax) **   <a name="guardduty-GetOrganizationStatistics-response-organizationDetails"></a>
Information about the statistics report for your organization.
Type: [OrganizationDetails](API_OrganizationDetails.md) object

## Errors
<a name="API_GetOrganizationStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_GetOrganizationStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetOrganizationStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetOrganizationStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetOrganizationStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetOrganizationStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetOrganizationStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetOrganizationStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetOrganizationStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetOrganizationStatistics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetOrganizationStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetOrganizationStatistics)
